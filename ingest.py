"""
ingest.py — The Unofficial Guide

Reads local Instructor-rating documents.
Each complete "--- Review N ---" record becomes one chunk.
"""

import os
import random

from config import DOCS_PATH, REVIEW_PATTERN


def load_documents():
    """Load every local .txt source document."""
    if not os.path.isdir(DOCS_PATH):
        raise FileNotFoundError(f"Documents folder not found: {DOCS_PATH}")

    filenames = sorted(
        filename
        for filename in os.listdir(DOCS_PATH)
        if filename.endswith(".txt")
    )

    if not filenames:
        raise FileNotFoundError(f"No .txt files found in: {DOCS_PATH}")

    documents = []

    for filename in filenames:
        file_path = os.path.join(DOCS_PATH, filename)

        with open(file_path, encoding="utf-8") as file:
            text = file.read()

        documents.append({
            "source": filename,
            "text": text.replace("\r\n", "\n").replace("\r", "\n"),
        })

    print(f"Loaded {len(documents)} source document(s): {filenames}")
    return documents



def chunk_document(text, source):
    """
    Turn one document into one chunk per complete review record.

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
      - "text"     : instructor + the chunk text (str)
      - "instructor" : instructor name, e.g. "anahit asadyan" (str)
      - "position": review_number, also position of the review in document
      - "chunk_id" : a unique identifier, e.g.
                     "anahit_asadyan_review_1" (str)
    """
    matches = list(REVIEW_PATTERN.finditer(text))

    if not matches:
        raise ValueError(
            f"No review markers found in {source}. "
            'Expected a line like "--- Review 1 ---".'
        )

    source_stem = os.path.splitext(source)[0]
    instructor = source_stem.replace("_", " ").title()
    chunks = []

    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        review_text = text[match.start():end].strip()
        review_number = int(match.group(1))

        if review_text:
            chunks.append({
                "text": f"Instructor: {instructor}\n{review_text}",
                "source": source,
                "position": review_number,
                "chunk_id": f"{source_stem}_review_{review_number}",
            })

    return chunks


if __name__ == "__main__":
    documents = load_documents()
    chunks = []

    for document in documents:
        chunks.extend(chunk_document(document["text"], document["source"]))

    print(f"\nLoaded source documents: {len(documents)}")
    print(f"Created review chunks: {len(chunks)}")
    print(f"Expected 12 documents: {'PASS' if len(documents) == 12 else 'CHECK'}")
    print(f"Expected 141 review chunks: {'PASS' if len(chunks) == 141 else 'CHECK'}")

    sample_chunks = random.sample(chunks, k=min(5, len(chunks)))

    print("\n=== FIVE REVIEW-CHUNK SAMPLES ===")

    for sample_number, chunk in enumerate(sample_chunks, start=1):
        print("\n" + "=" * 72)
        print(
            f"Sample {sample_number} | "
            f"source: {chunk['source']} | "
            f"position: {chunk['position']} | "
            f"id: {chunk['chunk_id']}"
        )
        print("-" * 72)
        print(chunk["text"])
        
        
    print("\n=== EDGE-CASE CHUNK CHECKS ===")

    edge_indices = [0, 1, len(chunks) - 1]

    for index in edge_indices:
        chunk = chunks[index]

        print("\n" + "=" * 72)
        print(
            f"Corpus index: {index} | "
            f"source: {chunk['source']} | "
            f"position: {chunk['position']} | "
            f"id: {chunk['chunk_id']}"
        )
        print("-" * 72)
        print(chunk["text"])