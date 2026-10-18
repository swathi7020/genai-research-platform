from pathlib import Path
import sys

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from app.rag.loader import load_pdf


PDF_PATH = PROJECT_ROOT / "data" / "research_paper.pdf"


def main():
    text = load_pdf(str(PDF_PATH))

    print("\n" + "=" * 60)
    print("PDF LOADING SUCCESSFUL")
    print("=" * 60)

    print(f"\nExtracted characters: {len(text)}")

    print("\nFirst 2000 characters:")
    print("-" * 60)
    print(text[:2000])


if __name__ == "__main__":
    main()
