class Retriever:

    def __init__(
        self,
        embedding_model,
        vector_store
    ):

        self.embedding_model = embedding_model
        self.vector_store = vector_store

    def retrieve(
        self,
        question,
        k=3,
        threshold=0.7
    ):

        query_vector = self.embedding_model.encode(
            question
        )

        results, scores = self.vector_store.search(
            query_vector[0],
            k
        )

        if scores[0] < threshold:
            return {
                "answer":
                "اطلاعات کافی در اسناد موجود نیست."
            }

        return results