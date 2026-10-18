from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from app.rag.pipeline import RAGPipeline


PDF_PATH = PROJECT_ROOT / "data" / "research_paper.pdf"


def main():

    print("\n" + "=" * 60)
    print("INITIALIZING RAG PIPELINE")
    print("=" * 60)

    rag = RAGPipeline(
        pdf_path=str(PDF_PATH)
    )

    query = "How does the social brain develop during childhood?"

    print("\n")
    print("=" * 60)
    print("QUERY")
    print("=" * 60)

    print(query)

    results = rag.retrieve(
        query=query,
        top_k=3
    )

    print("\n")
    print("=" * 60)
    print("RETRIEVED DOCUMENT CHUNKS")
    print("=" * 60)

    for i, result in enumerate(results, start=1):

        print(f"\nRESULT {i}")

        print(
            f"Distance: {result['distance']:.4f}"
        )

        print("-" * 50)

        print(
            result["document"][:700]
        )


if __name__ == "__main__":
    main()