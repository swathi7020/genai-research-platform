from pathlib import Path

from crewai import Agent

from app.rag.pipeline import RAGPipeline
from app.tools.crewai_rag_search import RAGSearchTool


def create_document_analyst_agent(pdf_path: str):

    document_pdf_path = Path(pdf_path)

    if not document_pdf_path.exists():
        raise FileNotFoundError(
            f"Research document not found: {pdf_path}"
        )

    rag_pipeline = RAGPipeline(
        pdf_path=str(document_pdf_path)
    )

    rag_search_tool = RAGSearchTool(
        rag_pipeline=rag_pipeline
    )

    document_agent = Agent(
        role="Document Analyst",

        goal=(
            "Analyze information retrieved from the provided "
            "research document and identify relevant evidence, "
            "findings, methods, and conclusions."
        ),

        backstory=(
            "You are a scientific document analyst experienced "
            "in reviewing research papers. You carefully examine "
            "retrieved document evidence and never invent "
            "information that is not present in the document."
        ),

        tools=[
            rag_search_tool
        ],

        verbose=True,

        allow_delegation=False
    )

    return document_agent