from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from app.rag.pipeline import RAGPipeline


PDF_PATH = PROJECT_ROOT / "data" / "research_paper.pdf"


def main():

    rag = RAGPipeline(
        pdf_path=str(PDF_PATH)
    )

    question = (
        "How does the social brain develop "
        "during childhood?"
    )

    result = rag.answer(
        query=question,
        top_k=3
    )

    print("\n" + "=" * 60)
    print("RAG ANSWER")
    print("=" * 60)

    print("\nQuestion:")
    print(result["question"])

    print("\nAnswer:")
    print(result["answer"])

    print("\n" + "=" * 60)
    print("SOURCES")
    print("=" * 60)

    for i, source in enumerate(
        result["sources"],
        start=1
    ):

        print(f"\nSource {i}")

        print(
            f"Distance: {source['distance']:.4f}"
        )

        print("-" * 50)

        print(
            source["document"][:300]
        )


if __name__ == "__main__":
    main()