from app.rag.pipeline import RAGPipeline
from app.tools.web_search import WebSearchTool


class ResearchEngine:

    def __init__(self, pdf_path: str):

        print("Initializing Research Engine...")

        self.rag = RAGPipeline(
            pdf_path=pdf_path
        )

        self.web_search = WebSearchTool()

        print("Research Engine initialized successfully.")

    def research(
        self,
        question: str,
        top_k: int = 3,
        web_results: int = 3
    ):

        if not question or not question.strip():
            raise ValueError(
                "Research question cannot be empty."
            )

        # ------------------------------------------------
        # 1. Search uploaded research documents
        # ------------------------------------------------

        document_results = self.rag.retrieve(
            query=question,
            top_k=top_k
        )

        document_context = "\n\n".join(
            result["document"]
            for result in document_results
        )

        # ------------------------------------------------
        # 2. Search the web
        # ------------------------------------------------

        web_results_data = self.web_search.search(
            query=question,
            max_results=web_results
        )

        web_context = "\n\n".join(
            (
                f"Title: {result['title']}\n"
                f"URL: {result['url']}\n"
                f"Content: {result['content']}"
            )
            for result in web_results_data
        )

        # ------------------------------------------------
        # 3. Combine both sources
        # ------------------------------------------------

        combined_context = f"""
DOCUMENT SOURCES
================

{document_context}


WEB SOURCES
===========

{web_context}
"""

        # ------------------------------------------------
        # 4. Generate final answer
        # ------------------------------------------------

        answer = self.rag.llm.generate_answer(
            question=question,
            context=combined_context
        )

        # ------------------------------------------------
        # 5. Return answer + sources
        # ------------------------------------------------

        return {
            "question": question,
            "answer": answer,
            "document_sources": document_results,
            "web_sources": web_results_data
        }