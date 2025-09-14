import os
import logging
import faiss
import pickle
from glob import glob
from langchain.text_splitter import MarkdownHeaderTextSplitter
from embeddings import load_embedder, create_embeddings

VECTOR_DB_DIR = "vector_database"
METADATA_PATH = os.path.join(VECTOR_DB_DIR, "metadata_store.pkl")
FAISS_INDEX_PATH = os.path.join(VECTOR_DB_DIR, "faiss.index")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("FaissIndexer")

def get_markdown_files(knowledge_base_dir):
    md_files = glob(os.path.join(knowledge_base_dir, "*.md"))
    logger.info(f"Found {len(md_files)} markdown files in {knowledge_base_dir}")
    return md_files

def chunk_markdown_files(md_file_paths):
    headers_to_split_on = [("#", "Header1"), ("##", "Header2"), ("###", "Header3")]
    splitter = MarkdownHeaderTextSplitter(headers_to_split_on, strip_headers=False)
    all_chunks = []
    for path in md_file_paths:
        logger.info(f"Reading {path}")
        with open(path, "r", encoding="utf-8") as f:
            md_content = f.read()
        chunks = splitter.split_text(md_content)
        for ch in chunks:
            ch.metadata["source"] = os.path.basename(path)
        all_chunks.extend(chunks)
    logger.info(f"Total chunks after splitting: {len(all_chunks)}")
    return all_chunks

def prepare_texts_for_embedding(chunks):
    texts_to_embed = []
    for idx, chunk in enumerate(chunks):
        headers = [chunk.metadata[h] for h in ["Header1", "Header2", "Header3"] if h in chunk.metadata]
        header_text = " | ".join(headers)
        source_text = chunk.metadata.get("source", "")
        embed_text = f"{header_text} | {source_text} | {chunk.page_content}"
        texts_to_embed.append(embed_text)
        logger.debug(f"Chunk {idx} prepared (len={len(embed_text)})")
    return texts_to_embed

def build_and_store_faiss_index(knowledge_base_dir, embed_model_name="BAAI/bge-large-en-v1.5"):
    os.makedirs(VECTOR_DB_DIR, exist_ok=True)
    md_file_paths = get_markdown_files(knowledge_base_dir)
    chunks = chunk_markdown_files(md_file_paths)
    texts = prepare_texts_for_embedding(chunks)
    embedder = load_embedder(embed_model_name)
    logger.info(f"Creating embeddings for {len(texts)} chunks...")
    embeddings = create_embeddings(texts, embedder)
    embedding_dim = embeddings.shape[1]
    faiss_index = faiss.IndexFlatL2(embedding_dim)
    faiss_index.add(embeddings)
    logger.info(f"FAISS index created with dimension {embedding_dim} and populated with {embeddings.shape[0]} embeddings.")

    # Save FAISS index and metadata
    faiss.write_index(faiss_index, FAISS_INDEX_PATH)
    with open(METADATA_PATH, "wb") as f:
        pickle.dump(chunks, f)
    logger.info(f"FAISS index saved to {FAISS_INDEX_PATH}")
    logger.info(f"Metadata store saved to {METADATA_PATH}")

    return FAISS_INDEX_PATH, METADATA_PATH

def load_faiss_index_and_metadata():
    faiss_index = faiss.read_index(FAISS_INDEX_PATH)
    with open(METADATA_PATH, "rb") as f:
        metadata_store = pickle.load(f)
    logger.info("Loaded FAISS index and metadata from disk.")
    return faiss_index, metadata_store

# Example usage:
build_and_store_faiss_index("knowledge_base")
faiss_index, metadata_store = load_faiss_index_and_metadata()