# Atlan Customer Support Copilot

## 🧠 Project Overview

This repository contains a modular, production-ready AI helpdesk demo for Atlan’s customer support team.  
It leverages DSPy for declarative LLM orchestration, FAISS for fast semantic retrieval, and Streamlit for a modern, interactive UI.  
The system automates ticket classification, triage, and intelligent response generation using a Retrieval-Augmented Generation (RAG) pipeline.

---

## ⚡️ Installation & Local Setup

### 1. **Clone the Repository**
```bash
git clone https://github.com/vedanshkap2692/Atlan_customer_copilot.git
cd Atlan_customer_copilot
```

### 2. **Create and Activate a Virtual Environment**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. **Install Python Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Set Up Environment Variables**
Create a `.env` file in the project root:
```
OPENROUTER_API_KEY=your_openrouter_api_key
```

### 5. **Prepare the Knowledge Base**
- Scrape Atlan documentation and developer hub using `scraper.py` (or use provided markdown files).
- Build the FAISS vector index:
  ```bash
  python faiss_index.py
  ```

### 6. **Run the Streamlit App**
```bash
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🏗️ Technical Approach & Architecture

### **Pipeline Breakdown**

- **Classification Module (`classification.py`):**
  - DSPy `Signature` defines a strict schema for ticket classification (topics, sentiment, priority).
  - DSPy `LabeledFewShot` optimizer compiles a robust agent from curated examples, ensuring high accuracy and schema adherence.
  - The agent is callable for both bulk and single ticket flows.

- **RAG Module (`rag_agent.py`):**
  - Loads a FAISS vector index and chunk metadata for semantic retrieval.
  - DSPy `ChainOfThought` generates answers, with context retrieved from the knowledge base.
  - All answers cite proper HTTPS documentation links, not just markdown filenames.

- **Knowledge Base (`scraper.py`, `faiss_index.py`):**
  - Scrapes Atlan docs and developer hub, converts HTML to structured markdown with citations.
  - Chunks markdown files and embeds them using SentenceTransformer.
  - Stores embeddings and metadata in FAISS for fast, production-grade retrieval.

- **Streamlit UI (`app.py`):**
  - Sidebar navigation for bulk dashboard and interactive agent.
  - Bulk classification streams ticket-by-ticket results, supports multi-filtering (topics, sentiment, priority), and visualizes analytics.
  - Interactive agent collects subject/body, runs classification, and generates RAG answers with source citations.

---

### **DSPy: Why and How**

- **Declarative LLM Orchestration:**  
  DSPy lets you define input/output schemas and reasoning steps as Python classes, eliminating manual prompt engineering and output parsing.

- **Few-Shot Optimization:**  
  Instead of hand-tuning prompts, you use DSPy’s optimizer to train your agent on labeled examples. This dramatically improves classification accuracy and consistency.

- **Chain-of-Thought Reasoning:**  
  For RAG, DSPy’s `ChainOfThought` module enables stepwise answer generation, making it easy to combine retrieved context with LLM reasoning.

- **Streaming (Optional):**  
  DSPy supports streaming LLM outputs for a responsive UI, though the current implementation returns the full answer for simplicity.

- **Unified API:**  
  All LLM calls, retrieval, and output parsing are handled by DSPy modules, making the codebase maintainable and extensible.

---

## 🧑‍💻 Engineering Decisions & Trade-offs

- **Modularity:**  
  Each pipeline component (classification, RAG, retrieval, embedding) is a standalone Python module, making it easy to test, extend, or swap out models.

- **Strict Schema Enforcement:**  
  Classification strictly follows Atlan’s support taxonomy, enforced via DSPy signatures and curated few-shot examples.

- **Efficient Retrieval:**  
  FAISS is used for vector search, enabling sub-second retrieval of relevant documentation chunks even at scale.

- **Source Attribution:**  
  RAG answers always cite HTTPS documentation links, ensuring transparency and trustworthiness.

- **UI/UX:**  
  Streamlit provides a fast, interactive dashboard with ticket-by-ticket streaming, multi-filtering, and analytics.

- **Scalability:**  
  The pipeline is designed to handle thousands of tickets and large knowledge bases with minimal latency.

---

## 📊 Features

- **Bulk Ticket Classification:**  
  - Streams results ticket-by-ticket.
  - Multi-filter by topics, sentiment, priority.
  - Analytics: distributions, stacked bar, heatmap, wordcloud.

- **Interactive AI Agent:**  
  - Submit new tickets (subject + body).
  - Shows internal analysis (classification).
  - Generates direct answers for relevant topics using RAG.
  - Cites official documentation sources.
  - Confirmation message for ticket routing.

- **Knowledge Base Scraper:**  
  - Scrapes Atlan docs and developer hub to markdown.
  - Builds FAISS index for fast retrieval.

---

## 📝 Evaluation & Annotation Methodology

- **Manual Annotation:**  
  All sample tickets in `ground_truth.json` were manually annotated for topics, sentiment, and priority to create a robust ground truth for evaluation.
- **LLM as Judge:**  
  Used an LLM to assist in evaluating classification accuracy, ensuring objective and consistent scoring.

### **Classification Accuracy Results**
- **Topics accuracy (partial credit):** 49 / 56 (87.50%)
- **Sentiment accuracy:** 27 / 30 (90.00%)
- **Priority accuracy:** 28 / 30 (93.33%)

This rigorous evaluation demonstrates the reliability and precision of the DSPy-powered classification pipeline.

---

## 📝 Usage

1. **Bulk Dashboard:**  
   - Go to "Bulk Classification" in the sidebar.
   - Click "Start Bulk Classification" to process all tickets.
   - Use filters to shortlist tickets by topic, sentiment, or priority.
   - View analytics and distributions.

2. **Interactive Agent:**  
   - Go to "Interactive Agent" in the sidebar.
   - Enter ticket subject and body.
   - View classification and AI-generated response.
   - See cited sources and confirmation message.

---

## 🏁 Deployment

- Deploy for free on [Streamlit Community Cloud](https://streamlit.io/cloud).
- Or use Vercel, Railway, or any cloud platform supporting Python and Streamlit.

---

## 📚 References

- [DSPy Documentation](https://github.com/stanfordnlp/dspy)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Sentence Transformers](https://www.sbert.net/)

---

## 🙏 Acknowledgements

Special thanks to Atlan, OpenRouter, and the DSPy team for enabling rapid prototyping of AI-powered support tools.

---

## 🏗️ System Design Diagram

Below is a high-level architecture diagram of the Atlan Customer Support Copilot pipeline:

```mermaid
graph TD
    A[User] -->|Bulk Tickets| B[Streamlit UI]
    A -->|New Ticket| B
    B -->|Classify| C[Classification Agent (DSPy)]
    B -->|RAG Query| D[RAG Agent (DSPy + FAISS)]
    D -->|Retrieve| E[FAISS Vector DB]
    D -->|Embed| F[SentenceTransformer]
    D -->|Docs| G[Markdown Knowledge Base]
    C -->|Results| B
    D -->|Response + Sources| B
```

---

**For questions or contributions, open an issue or pull request on GitHub!**
