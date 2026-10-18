from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


from app.research.engine import ResearchEngine


PDF_PATH = PROJECT_ROOT / "data" / "research_paper.pdf"


def main():

    print("\n" + "=" * 60)
    print("TESTING RESEARCH ENGINE")
    print("=" * 60)

    engine = ResearchEngine(
        pdf_path=str(PDF_PATH)
    )

    question = (
        "What are the major findings about "
        "social brain development during childhood?"
    )

    print("\nQuestion:")
    print(question)

    result = engine.research(
        question=question,
        top_k=3,
        web_results=3
    )

    print("\n" + "=" * 60)
    print("FINAL RESEARCH ANSWER")
    print("=" * 60)

    print("\n")
    print(result["answer"])

    print("\n" + "=" * 60)
    print("DOCUMENT SOURCES")
    print("=" * 60)

    for i, source in enumerate(
        result["document_sources"],
        start=1
    ):

        print(f"\nDocument Source {i}")
        print(
            source["document"][:300]
        )

    print("\n" + "=" * 60)
    print("WEB SOURCES")
    print("=" * 60)

    for i, source in enumerate(
        result["web_sources"],
        start=1
    ):

        print(f"\nWeb Source {i}")
        print(f"Title: {source['title']}")
        print(f"URL: {source['url']}")


if __name__ == "__main__":
    main()