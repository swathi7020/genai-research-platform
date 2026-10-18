from app.rag.loader import load_pdf
from app.rag.chunker import split_text
from app.rag.embeddings import EmbeddingModel
from app.rag.vector_store import VectorStore
from app.llm.client import LLMClient


class RAGPipeline:

    def __init__(self, pdf_path: str):

        self.pdf_path = pdf_path

        print("Loading document...")

        self.text = load_pdf(self.pdf_path)

        print("Splitting document...")

        self.chunks = split_text(self.text)

        print(f"Created {len(self.chunks)} chunks.")

        print("Loading embedding model...")

        self.embedding_model = EmbeddingModel()

        print("Creating document embeddings...")

        self.embeddings = self.embedding_model.embed_documents(
            self.chunks
        )

        dimension = self.embeddings.shape[1]

        print("Creating vector store...")

        self.vector_store = VectorStore(
            dimension=dimension
        )

        self.vector_store.add_documents(
            self.embeddings,
            self.chunks
        )

        print("Loading LLM client...")

        self.llm = LLMClient()

        print("RAG pipeline initialized successfully.")

    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ):

        if not query or not query.strip():
            raise ValueError("Query cannot be empty.")

        query_embedding = self.embedding_model.embed_text(
            query
        )

        results = self.vector_store.search(
            query_embedding,
            top_k=top_k
        )

        return results

    def answer(
        self,
        query: str,
        top_k: int = 5
    ):

        results = self.retrieve(
            query=query,
            top_k=top_k
        )

        context = "\n\n".join(
            result["document"]
            for result in results
        )

        answer = self.llm.generate_answer(
            question=query,
            context=context
        )

        return {
            "question": query,
            "answer": answer,
            "sources": results
        }