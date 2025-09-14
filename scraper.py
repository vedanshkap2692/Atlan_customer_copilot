import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import logging

# --- Setup Logging ---
logging.basicConfig(
    level=logging.INFO,  # change to DEBUG for more details
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


class WebToMarkdownScraper:
    def __init__(self, base_url, output_dir, max_depth=5):
        self.base_url = base_url
        self.visited = set()
        self.output_dir = output_dir
        self.max_depth = max_depth
        os.makedirs(output_dir, exist_ok=True)

    def is_same_domain(self, url):
        return urlparse(url).netloc == urlparse(self.base_url).netloc

    def scrape(self, url=None, depth=0):
        if url is None:
            url = self.base_url
        if depth > self.max_depth:
            logger.debug(f"Skipping {url} (depth {depth} > max_depth {self.max_depth})")
            return
        if url in self.visited:
            logger.debug(f"Already visited: {url}")
            return
        self.visited.add(url)

        try:
            logger.info(f"Fetching: {url}")
            res = requests.get(url, timeout=10)
            res.raise_for_status()
        except Exception as e:
            logger.error(f"❌ Failed to fetch {url}: {e}")
            return

        soup = BeautifulSoup(res.text, "html.parser")
        md_content = self._extract_markdown(soup, url)

        # Save structured markdown page-wise
        filename = self._url_to_filename(url)
        filepath = os.path.join(self.output_dir, filename)
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(md_content)
            logger.info(f"✅ Saved {filepath}")
        except Exception as e:
            logger.error(f"❌ Failed to save {filepath}: {e}")

        # Recurse into links (only within same domain)
        for link in soup.find_all("a", href=True):
            abs_url = urljoin(url, link['href'])
            if self.is_same_domain(abs_url):
                self.scrape(abs_url, depth + 1)
            else:
                logger.debug(f"Skipping external link: {abs_url}")

    def _extract_markdown(self, soup, url):
        """
        Extracts structured markdown from a page with headings and citations.
        """
        md_lines = []
        current_heading = None
        buffer = []

        for el in soup.find_all(["h1", "h2", "h3", "h4", "h5", "p", "li", "pre", "code"]):
            if el.name.startswith("h"):  # heading found
                if current_heading:
                    md_lines.append(f"{current_heading}\n(source: {url})\n")
                    md_lines.extend(buffer)
                    md_lines.append("\n")
                    buffer = []

                level = int(el.name[1])
                heading_text = el.get_text(strip=True)
                if level <= 5:
                    current_heading = "#" * level + " " + heading_text
                else:
                    current_heading = "##### " + heading_text
            else:
                text = el.get_text(strip=True)
                if text:
                    buffer.append(text + "\n")

        if current_heading:
            md_lines.append(f"{current_heading}\n(source: {url})\n")
            md_lines.extend(buffer)

        return "\n".join(md_lines)

    def _url_to_filename(self, url):
        """
        Convert URL path into a filesystem-safe filename.
        """
        parsed = urlparse(url)
        domain = parsed.netloc.replace(".", "_")
        path = parsed.path.strip("/")
        if not path:
            path = "index"
        return domain + "_" + path.replace("/", "_") + ".md"


if __name__ == "__main__":
    output_dir = "/Users/vedansh.kapoor/atlan_copilot/knowledge_base"
    urls = [
        "https://docs.atlan.com/",   # first URL
        "https://developer.atlan.com/"      # second URL (example)
    ]

    for url in urls:
        logger.info(f"🚀 Starting scrape for {url}")
        scraper = WebToMarkdownScraper(
            base_url=url,
            output_dir=output_dir,
            max_depth=5
        )
        scraper.scrape()

    logger.info(f"🎉 Scraping complete. Markdown files saved in '{output_dir}'")
