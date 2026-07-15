import fitz


class PDFLoader:

    def load(self, file_path):

        doc = fitz.open(file_path)
        pages = []

        for page_number, page in enumerate(doc):
            text = page.get_text()
            pages.append(
                {
                    "text": text,
                    "metadata":
                    {
                        "source": file_path,
                        "page": page_number + 1
                    }
                }
            )

        return pages