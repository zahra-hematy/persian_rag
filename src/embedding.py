from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    """
    Generates dense vector embeddings from text using
    a SentenceTransformer model.
    """

    def __init__(self, model_name="intfloat/multilingual-e5-small"):
        # Default multilingual model suitable for Persian retrieval
        self.model = SentenceTransformer(model_name)

    def encode(self, texts):
        """
        Converts one or more texts into vector embeddings.
        """

        if isinstance(texts, str):
            texts = [texts]

        vectors = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return vectors