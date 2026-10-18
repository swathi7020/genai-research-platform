from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"


class EmbeddingModel:
    def __init__(self, model_name: str = MODEL_NAME):
        self.model = SentenceTransformer(model_name)

    def embed_text(self, text: str):
        if not text or not text.strip():
            raise ValueError("Text cannot be empty.")

        return self.model.encode(text)

    def embed_documents(self, texts: list[str]):
        if not texts:
            raise ValueError("Text list cannot be empty.")

        return self.model.encode(
            texts,
            show_progress_bar=True
        )