from pathlib import Path

from pypdf import PdfReader


def load_pdf(file_path: str) -> str:
    """
    Extract text from a PDF file.

    Args:
        file_path: Path to the PDF file.

    Returns:
        Extracted text from all pages.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {file_path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError("The provided file must be a PDF.")

    reader = PdfReader(str(path))

    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if text:
            pages.append(
                f"\n--- Page {page_number} ---\n{text}"
            )

    if not pages:
        raise ValueError(
            "No text could be extracted from the PDF. "
            "The PDF may be scanned or image-based."
        )

    return "\n".join(pages)