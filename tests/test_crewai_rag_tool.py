import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


from app.rag.pipeline import RAGPipeline
from app.tools.crewai_rag_search import RAGSearchTool


PDF_PATH = PROJECT_ROOT / "data" / "research_paper.pdf"


def main():

    print("\n" + "=" * 60)
    print("TESTING CREWAI RAG TOOL")
    print("=" * 60)

    print("\nLoading RAG pipeline...")

    rag_pipeline = RAGPipeline(
        pdf_path=str(PDF_PATH)
    )

    print("\nCreating CrewAI RAG tool...")

    tool = RAGSearchTool(
        rag_pipeline=rag_pipeline
    )

    print(f"\nTool name: {tool.name}")

    print("\nTool description:")
    print(tool.description)

    query = (
        "How does the social brain develop "
        "during childhood?"
    )

    print("\nRunning document search...")

    result = tool.run(query)

    print("\n" + "=" * 60)
    print("DOCUMENT SEARCH RESULTS")
    print("=" * 60)

    print(result[:4000])

    print("\n" + "=" * 60)
    print("CREWAI RAG TOOL TEST SUCCESSFUL")
    print("=" * 60)


if __name__ == "__main__":
    main()