# 🔬 GenAI Research Intelligence Platform

An AI-powered research and knowledge intelligence platform that combines **Retrieval-Augmented Generation (RAG), FAISS vector search, CrewAI multi-agent orchestration, Tavily web search, LLMs, FastAPI, and Streamlit** to analyze research documents and generate evidence-based research responses.

---

## 🚀 Project Overview

The GenAI Research Intelligence Platform allows users to:

- Upload research papers in PDF format
- Ask questions about uploaded documents
- Retrieve relevant document sections using semantic search
- Perform web research using Tavily
- Use multiple specialized AI agents through CrewAI
- Combine document evidence and web research
- Generate a synthesized research response using an LLM
- Access the system through a FastAPI backend
- Interact with the platform through a Streamlit frontend

The platform is designed as an end-to-end Generative AI application demonstrating how modern AI components can be combined into a production-oriented research workflow.

---

## ✨ Key Features

### 📄 Research Document Upload

Users can upload a PDF research paper directly through the Streamlit interface.

The uploaded document is processed dynamically rather than relying on a fixed document.

### 🧠 Retrieval-Augmented Generation

The platform uses a RAG pipeline:

```text
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embeddings
 ↓
FAISS Vector Search
 ↓
Relevant Context
 ↓
LLM