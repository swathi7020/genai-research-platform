from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from app.rag.loader import load_pdf
from app.rag.chunker import split_text


PDF_PATH = PROJECT_ROOT / "data" / "research_paper.pdf"


def main():
    text = load_pdf(str(PDF_PATH))

    chunks = split_text(text)

    print("\n" + "=" * 60)
    print("TEXT CHUNKING SUCCESSFUL")
    print("=" * 60)

    print(f"\nTotal characters: {len(text)}")
    print(f"Total chunks: {len(chunks)}")

    print("\nFirst 3 chunks:")
    print("-" * 60)

    for i, chunk in enumerate(chunks[:3], start=1):
        print(f"\nCHUNK {i}")
        print("-" * 40)
        print(chunk[:500])


if __name__ == "__main__":
    main()