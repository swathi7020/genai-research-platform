from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(
    text: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200
) -> list[str]:
    """
    Split extracted document text into overlapping chunks.

    Args:
        text: Full extracted document text.
        chunk_size: Maximum size of each chunk.
        chunk_overlap: Number of overlapping characters.

    Returns:
        A list of text chunks.
    """

    if not text or not text.strip():
        raise ValueError("Text cannot be empty.")

    if chunk_overlap >= chunk_size:
        raise ValueError(
            "chunk_overlap must be smaller than chunk_size."
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    chunks = splitter.split_text(text)

    if not chunks:
        raise ValueError("No chunks were created.")

    return chunks