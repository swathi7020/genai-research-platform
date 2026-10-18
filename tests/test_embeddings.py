from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from app.rag.loader import load_pdf
from app.rag.chunker import split_text
from app.rag.embeddings import EmbeddingModel


PDF_PATH = PROJECT_ROOT / "data" / "research_paper.pdf"


def main():
    print("\nLoading PDF...")

    text = load_pdf(str(PDF_PATH))

    print("Splitting text into chunks...")

    chunks = split_text(text)

    print(f"Total chunks: {len(chunks)}")

    print("\nLoading embedding model...")

    embedding_model = EmbeddingModel()

    print("Creating embeddings...")

    embeddings = embedding_model.embed_documents(chunks)

    print("\n" + "=" * 60)
    print("EMBEDDINGS SUCCESSFUL")
    print("=" * 60)

    print(f"\nNumber of chunks: {len(chunks)}")
    print(f"Embedding shape: {embeddings.shape}")

    print("\nFirst embedding:")
    print(embeddings[0][:10])


if __name__ == "__main__":
    main()