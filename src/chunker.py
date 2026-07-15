class TextChunker:
    """
    Splits long documents into smaller chunks while preserving
    semantic boundaries and metadata information.
    """

    def __init__(self, chunk_size=500, overlap=100):

        # Maximum size of each chunk
        self.chunk_size = chunk_size

        # Number of characters shared between consecutive chunks
        # to preserve context between chunks
        self.overlap = overlap


        # Splitting priority:
        # Prefer larger semantic boundaries first
        # and fall back to smaller separators if needed
        self.separators = [
            "\n\n",   # Paragraph break
            "\n",     # Line break
            "؟",      # Persian question mark
            "!",      # Exclamation mark
            ".",      # Sentence ending
            " "       # Word boundary
        ]


    def find_split_position(self, text, start, end):
        """
        Finds the best position to split text.
        Searches backward from the chunk limit
        to avoid breaking sentences or words.
        """

        for separator in self.separators:

            position = text.rfind(
                separator,
                start,
                end
            )

            if position != -1:
                return position + len(separator)

        # If no separator is found, split at the maximum size
        return end



    def chunk(self, text, metadata=None):
        """
        Splits input text into chunks and attaches metadata.

        Returns:
            List of dictionaries containing:
            - chunk text
            - metadata
        """

        chunks = []
        start = 0
        chunk_id = 0

        while start < len(text):

            # Calculate chunk end position
            end = min(
                start + self.chunk_size,
                len(text)
            )

            # Try to split at meaningful boundaries
            if end < len(text):

                end = self.find_split_position(
                    text,
                    start,
                    end
                )

            chunk_text = text[start:end].strip()

            chunk = {

                "text": chunk_text,

                "metadata": {

                    "chunk_id": chunk_id,

                    # Character positions are useful
                    # for debugging and tracing chunks
                    "char_start": start,
                    "char_end": end
                }
            }

            # Add document-level metadata
            # such as file name and page number
            if metadata:
                chunk["metadata"].update(metadata)

            chunks.append(chunk)
            chunk_id += 1

            # Stop when reaching the end of document
            if end == len(text):
                break

            # Move backward to preserve context overlap
            start = end - self.overlap

        return chunks