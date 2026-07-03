"""
ingest.py — The Unofficial Guide

Reads local professor-review documents.
Each complete "--- Review N ---" record becomes one chunk.
"""

from pathlib import Path
import re


DOCUMENTS_DIR = Path(__file__).resolve().parent / "documents"
REVIEW_PATTERN = re.compile(r"(?m)^---\s*Review\s+(\d+)\s*---\s*$")


def load_documents():
    """Load every local .txt source document."""
    if not DOCUMENTS_DIR.is_dir():
        raise FileNotFoundError(f"Documents folder not found: {DOCUMENTS_DIR}")

    documents = []

    for path in sorted(DOCUMENTS_DIR.glob("*.txt")):
        text = path.read_text(encoding="utf-8")
        documents.append({
            "source": path.name,
            "text": text.replace("\r\n", "\n").replace("\r", "\n"),
        })

    return documents


def chunk_document(text, source):
    """
    Turn one professor document into one chunk per complete review record.

    Document headers and derived statistics before the first review marker
    are intentionally not included in any chunk.
    
    Strategy: one complete review record per chunk.
      - Each chunk starts at a line formatted as "--- Review N ---" and 
        ends immediately before the next review marker, or at the end of the document.
      - Each review stays intact because its course, rating, difficulty, grade, 
        and written explanation should remain connected.
      - overlap = 0 
      - Text before the first review marker is excluded, so document headers and 
        derived statistics before the first review marker are intentionally not included in any chunk.
      
    Returns a list of dicts, each with:
      - "text"     : professor name plus one complete review record (str)
      - "source"   : source filename, e.g. "anahit_asadyan.txt" (str)
      - "position" : review number within that source document (int)
      - "chunk_id" : stable identifier, e.g.
                     "anahit_asadyan_review_1" (str)
    """
    matches = list(REVIEW_PATTERN.finditer(text))
    professor_name = Path(source).stem.replace("_", " ").title()
    chunks = []

    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        review_number = int(match.group(1))
        review_text = text[match.start():end].strip()

        if review_text:
            chunks.append({
                "text": f"Professor: {professor_name}\n\n{review_text}",
                "source": source,
                "position": review_number,
                "chunk_id": f"{Path(source).stem}_review_{review_number}",
            })

    return chunks


if __name__ == "__main__":
    documents = load_documents()
    chunks = []

    for document in documents:
        chunks.extend(chunk_document(document["text"], document["source"]))

    print(f"Loaded source documents: {len(documents)}")
    print(f"Created review chunks: {len(chunks)}")
    print(f"Expected 12 documents: {'PASS' if len(documents) == 12 else 'CHECK'}")
    print(f"Expected 141 review chunks: {'PASS' if len(chunks) == 141 else 'CHECK'}")

    if chunks:
        sample_indices = [
            0,
            len(chunks) // 4,
            len(chunks) // 2,
            (len(chunks) * 3) // 4,
            len(chunks) - 1,
        ]

        print("\n=== FIVE REVIEW-CHUNK SAMPLES ===")

        for sample_number, index in enumerate(sample_indices, start=1):
            chunk = chunks[index]

            print("\n" + "=" * 72)
            print(
                f"Sample {sample_number} | "
                f"source: {chunk['source']} | "
                f"position: {chunk['position']} | "
                f"id: {chunk['chunk_id']}"
            )
            print("-" * 72)
            print(chunk["text"])