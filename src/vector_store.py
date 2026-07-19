import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension):

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.documents = []
    def add(self, vectors, documents):

        vectors = np.array(
            vectors
        ).astype("float32")

        self.index.add(
            vectors
        )

        self.documents.extend(
            documents
        )

    def search(self, query_vector, k=3):

        query_vector = np.array(
            [query_vector]
        ).astype("float32")

        distances, indices = self.index.search(
            query_vector,
            k
        )

        results = []
        for idx in indices[0]:

            results.append(
                self.documents[idx]
            )
        return results