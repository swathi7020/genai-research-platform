import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension: int):
        self.dimension = dimension

        self.index = faiss.IndexFlatL2(dimension)

        self.documents = []

    def add_documents(self, embeddings, documents):

        if len(embeddings) != len(documents):
            raise ValueError(
                "Number of embeddings must match number of documents."
            )

        vectors = np.array(
            embeddings,
            dtype="float32"
        )

        self.index.add(vectors)

        self.documents.extend(documents)

    def search(self, query_embedding, top_k: int = 5):

        if self.index.ntotal == 0:
            raise ValueError("Vector store is empty.")

        query_vector = np.array(
            [query_embedding],
            dtype="float32"
        )

        distances, indices = self.index.search(
            query_vector,
            top_k
        )

        results = []

        for distance, index in zip(
            distances[0],
            indices[0]
        ):

            if index == -1:
                continue

            results.append({
                "document": self.documents[index],
                "distance": float(distance)
            })

        return results