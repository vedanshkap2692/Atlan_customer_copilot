import logging
import faiss
import pickle
import dspy
from embeddings import load_embedder

import os
from dotenv import load_dotenv
load_dotenv()

VECTOR_DB_DIR = "vector_database"
FAISS_INDEX_PATH = f"{VECTOR_DB_DIR}/faiss.index"
METADATA_PATH = f"{VECTOR_DB_DIR}/metadata_store.pkl"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("MarkdownRAG")

class GenerateAnswer(dspy.Signature):
    """citing the https links mentioned in the sources and make sure you cite them correctly, this is very crucial, no answer should be without a https source, you will get negative points if you wont cite proper https links"""
    context = dspy.InputField(desc="Relevant markdown context extracted from chunks")
    question = dspy.InputField(desc="User question")
    answer = dspy.OutputField(desc="Concise, accurate answer citing sources, you will not cite .md files, you will cite the https links mentioned in the sources and make sure you cite them correctly.")

class MarkdownRAG(dspy.Module):
    def __init__(self, faiss_index, metadata_store, embed_model, k=3):
        super().__init__()
        self.faiss_index = faiss_index
        self.metadata_store = metadata_store
        self.embed_model = embed_model
        self.k = k
        self.generate_answer = dspy.ChainOfThought(GenerateAnswer)
        logger.info("MarkdownRAG agent initialized.")

    def forward(self, question: str):
        logger.info(f"Received query: {question}")
        query_emb = self.embed_model.encode([question], convert_to_numpy=True)
        D, I = self.faiss_index.search(query_emb, self.k)
        retrieved_chunks = [self.metadata_store[i] for i in I[0]]
        logger.info(f"Retrieved {len(retrieved_chunks)} chunks for the query.")

        context_pieces = []
        sources = set()
        for chunk in retrieved_chunks:
            source = chunk.metadata.get("source", "")
            sources.add(source)
            context_pieces.append(f"{chunk.page_content}\n(Source: {source})")
        context = "\n---\n".join(context_pieces)

        result = self.generate_answer(context=context, question=question)
        logger.info("Generated answer for query.")
        return {
            "answer": result.answer,
            "sources": list(sources)
        }

# def setup_lm():
#     import dspy
#     import os
#     from dotenv import load_dotenv
#     load_dotenv()
#     OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
#     lm = dspy.LM("openrouter/meta-llama/llama-4-scout", api_key=OPENROUTER_API_KEY, cache=False, provider="groq")
#     dspy.configure(lm=lm)
#     return lm

def load_rag_agent(embed_model):
    #setup_lm()  # Ensure LM is configured before agent is used
    faiss_index = faiss.read_index(FAISS_INDEX_PATH)
    with open(METADATA_PATH, "rb") as f:
        metadata_store = pickle.load(f)
    logger.info("Loaded FAISS index and metadata for RAG agent.")
    return MarkdownRAG(faiss_index, metadata_store, embed_model)

# Example usage:
if __name__ == "__main__":
    from embeddings import load_embedder
    embed_model = load_embedder("BAAI/bge-large-en-v1.5")
    rag_agent = load_rag_agent(embed_model)
    query = "how do i set up snowflake in atlan"
    response = rag_agent(query)
    print("Answer:", response["answer"])
    print("Sources:", response["sources"])

# Example usage:
# if __name__ == "__main__":
#     from embeddings import load_embedder
#     embed_model = load_embedder("BAAI/bge-large-en-v1.5")
#     rag_agent = load_rag_agent(embed_model)
#     query = "how do i set up snowflake in atlan"
#     response = rag_agent(query)
#     print("Answer:", response["answer"])
#     print("Sources:", response["sources"])