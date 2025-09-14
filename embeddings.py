from sentence_transformers import SentenceTransformer

def load_embedder(model_name="BAAI/bge-large-en-v1.5"):
    return SentenceTransformer(model_name)

def create_embeddings(texts, embedder):
    """
    Given a list of texts and a loaded embedder, returns numpy embeddings.
    """
    return embedder.encode(texts, convert_to_numpy=True)