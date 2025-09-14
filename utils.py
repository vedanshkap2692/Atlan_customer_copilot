import json
import logging
from collections import Counter, defaultdict
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from wordcloud import WordCloud
import pandas as pd
from classification import optimized_agent

# Helper: normalize a record to a consistent prediction dict
def _extract_prediction(item):
    """
    Returns dict with keys: topics (list), sentiment (str), priority (str)
    Works whether item has a nested "prediction" dict or flat top-level keys.
    """
    if isinstance(item, dict) and "prediction" in item and isinstance(item["prediction"], dict):
        pred = item["prediction"]
        topics = pred.get("topics") or []
        sentiment = pred.get("sentiment") or ""
        priority = pred.get("priority") or ""
    else:
        # flat structure (e.g., from df.to_dict("records"))
        topics = item.get("topics") or []
        sentiment = item.get("sentiment") or ""
        priority = item.get("priority") or ""
    # Ensure types
    if not isinstance(topics, (list, tuple)):
        topics = [topics] if topics else []
    return {"topics": list(topics), "sentiment": sentiment, "priority": priority}


def bulk_classify_tickets(json_path, optimized_agent):
    """
    Loads tickets from ground_truth.json, classifies each using optimized_agent,
    and returns a list of dicts: [{id, subject, body, classification, prediction}]
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[logging.StreamHandler()]
    )
    logger = logging.getLogger("BulkClassifier")

    with open(json_path, "r") as f:
        data = json.load(f)

    results = []
    for item in data:
        if not all(k in item for k in ("id", "subject", "body", "classification")):
            logger.warning(f"Skipping incomplete record: {item}")
            continue

        id = item["id"]
        subject = item["subject"]
        body = item["body"]
        gt_class = item["classification"]

        try:
            pred = optimized_agent(id=id, subject=subject, body=body).parsed_document
            logger.info(f"Ticket {id} classified: {pred}")
            results.append({
                "id": id,
                "subject": subject,
                "body": body,
                "ground_truth": gt_class,
                "prediction": {
                    "topics": getattr(pred, "topics", []),
                    "sentiment": getattr(pred, "sentiment", ""),
                    "priority": getattr(pred, "priority", "")
                }
            })
        except Exception as e:
            logger.error(f"Error processing record ID {id}: {e}")

    logger.info(f"Bulk classification complete. Total processed: {len(results)}")
    return results


def classify_first_ticket(json_path, optimized_agent):
    """
    Loads the first ticket from ground_truth.json and classifies it.
    Returns the result dict.
    """
    with open(json_path, "r") as f:
        data = json.load(f)

    for item in data:
        if all(k in item for k in ("id", "subject", "body", "classification")):
            id = item["id"]
            subject = item["subject"]
            body = item["body"]
            gt_class = item["classification"]
            try:
                pred = optimized_agent(id=id, subject=subject, body=body).parsed_document
                return {
                    "id": id,
                    "subject": subject,
                    "body": body,
                    "ground_truth": gt_class,
                    "prediction": {
                        "topics": getattr(pred, "topics", []),
                        "sentiment": getattr(pred, "sentiment", ""),
                        "priority": getattr(pred, "priority", "")
                    }
                }
            except Exception as e:
                print(f"Error processing record ID {id}: {e}")
            break
    return None


def get_prediction_distributions(results):
    """
    Given bulk classification results (either nested 'prediction' or flat),
    returns Counter dicts for topics, sentiment, and priority.
    """
    topic_counter = Counter()
    sentiment_counter = Counter()
    priority_counter = Counter()

    for item in results:
        pred = _extract_prediction(item)
        for topic in pred["topics"]:
            if topic:
                topic_counter[topic] += 1
        sentiment = pred["sentiment"]
        if sentiment:
            sentiment_counter[sentiment] += 1
        priority = pred["priority"]
        if priority:
            priority_counter[priority] += 1

    return {"topics": topic_counter, "sentiment": sentiment_counter, "priority": priority_counter}


def plot_prediction_distributions(results, title_prefix="Bulk Tickets"):
    """
    Plots bar and pie charts for topics, sentiment, and priority distributions (bulk).
    Handles empty cases gracefully.
    """
    dist = get_prediction_distributions(results)

    fig, axes = plt.subplots(1, 3, figsize=(16, 7))

    # Topics Bar
    if dist["topics"]:
        keys = list(dist["topics"].keys())
        vals = [dist["topics"][k] for k in keys]
        sns.barplot(x=keys, y=vals, palette="viridis", ax=axes[0])
        axes[0].set_title(f"{title_prefix} Topics Distribution")
        axes[0].tick_params(axis="x", rotation=45)
    else:
        axes[0].text(0.5, 0.5, "No Topics", ha="center", va="center")
        axes[0].set_axis_off()

    # Sentiment Pie
    if dist["sentiment"]:
        labels = list(dist["sentiment"].keys())
        sizes = [dist["sentiment"][k] for k in labels]
        axes[1].pie(sizes, labels=labels, autopct='%1.1f%%', colors=sns.color_palette("pastel"))
        axes[1].set_title(f"{title_prefix} Sentiment Distribution")
    else:
        axes[1].text(0.5, 0.5, "No Sentiment", ha="center", va="center")
        axes[1].set_axis_off()

    # Priority Bar
    if dist["priority"]:
        keys = list(dist["priority"].keys())
        vals = [dist["priority"][k] for k in keys]
        sns.barplot(x=keys, y=vals, palette="mako", ax=axes[2])
        axes[2].set_title(f"{title_prefix} Priority Distribution")
    else:
        axes[2].text(0.5, 0.5, "No Priority", ha="center", va="center")
        axes[2].set_axis_off()

    plt.tight_layout()
    st.pyplot(fig)


# --- New analytics helpers ---

def get_summary_metrics(results):
    """Returns total tickets and unique counts for summary display."""
    total = len(results)
    dist = get_prediction_distributions(results)
    return {
        "total": total,
        "unique_topics": len(dist["topics"]),
        "unique_sentiments": len(dist["sentiment"]),
        "unique_priorities": len(dist["priority"])
    }


def plot_stacked_priority_topics(results):
    """Stacked bar chart of topics vs priority."""
    data = defaultdict(lambda: Counter())
    for item in results:
        pred = _extract_prediction(item)
        topics = pred.get("topics", [])
        priority = pred.get("priority", "Unknown") or "Unknown"
        for t in topics:
            data[t][priority] += 1

    if not data:
        st.warning("No data available for stacked chart.")
        return

    df = pd.DataFrame(data).fillna(0)
    # transpose so topics are on x-axis and priorities are stacked bars
    df.T.plot(kind="bar", stacked=True, figsize=(12, 6), colormap="viridis")
    plt.title("Topics vs Priority (Stacked)")
    plt.ylabel("Count")
    st.pyplot(plt.gcf())


def plot_heatmap_topics_sentiment(results):
    """Heatmap of topics vs sentiment counts."""
    data = defaultdict(lambda: Counter())
    for item in results:
        pred = _extract_prediction(item)
        topics = pred.get("topics", [])
        sentiment = pred.get("sentiment", "Unknown") or "Unknown"
        for t in topics:
            data[t][sentiment] += 1

    if not data:
        st.warning("No data available for heatmap.")
        return

    df = pd.DataFrame(data).fillna(0).astype(int)
    plt.figure(figsize=(10, 6))
    sns.heatmap(df, annot=True, fmt="d", cmap="coolwarm")
    plt.title("Topics vs Sentiment Heatmap")
    st.pyplot(plt.gcf())


def generate_wordcloud(results):
    topic_counter = get_prediction_distributions(results)["topics"]
    if not topic_counter:
        st.warning("No topics available for wordcloud.")
        return

    # --- NEW: normalize counts to soften big differences ---
    max_count = max(topic_counter.values())
    normalized = {k: v / max_count for k, v in topic_counter.items()}

    wc = WordCloud(
        width=900,
        height=450,
        background_color="white",
        colormap="viridis",
        prefer_horizontal=1.0,   # all words horizontal
        max_font_size=120,       # cap largest font
        min_font_size=20
    ).generate_from_frequencies(normalized)

    plt.figure(figsize=(12, 6))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title("Topic WordCloud", fontsize=18)
    st.pyplot(plt.gcf())
