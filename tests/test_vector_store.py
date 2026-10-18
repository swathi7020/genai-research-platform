from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from app.rag.loader import load_pdf
from app.rag.chunker import split_text
from app.rag.embeddings import EmbeddingModel
from app.rag.vector_store import VectorStore


PDF_PATH = PROJECT_ROOT / "data" / "research_paper.pdf"


def main():

    print("\nLoading PDF...")

    text = load_pdf(str(PDF_PATH))

    print("Splitting text...")

    chunks = split_text(text)

    print(f"Total chunks: {len(chunks)}")

    print("\nCreating embeddings...")

    embedding_model = EmbeddingModel()

    embeddings = embedding_model.embed_documents(chunks)

    print(f"Embedding shape: {embeddings.shape}")

    dimension = embeddings.shape[1]

    print("\nCreating vector store...")

    vector_store = VectorStore(
        dimension=dimension
    )

    vector_store.add_documents(
        embeddings,
        chunks
    )

    print(
        f"Vectors stored: {vector_store.index.ntotal}"
    )

    print("\nTesting semantic search...")

    query = "How does the brain develop during childhood?"

    query_embedding = embedding_model.embed_text(query)

    results = vector_store.search(
        query_embedding,
        top_k=3
    )

    print("\n" + "=" * 60)
    print("VECTOR SEARCH SUCCESSFUL")
    print("=" * 60)

    for i, result in enumerate(results, start=1):

        print(f"\nRESULT {i}")

        print(
            f"Distance: {result['distance']:.4f}"
        )

        print("-" * 40)

        print(
            result["document"][:500]
        )


if __name__ == "__main__":
    main()