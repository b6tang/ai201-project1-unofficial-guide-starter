"""
retriever.py — The Unofficial Guide

Opens the persistent ChromaDB collection for PCC MATH 005A review chunks
and will provide semantic retrieval for user questions.
"""
import chromadb
from chromadb.utils import embedding_functions
from config import CHROMA_COLLECTION, CHROMA_PATH, EMBEDDING_MODEL, N_RESULTS
import re



# ChromaDB uses this embedding function automatically when documents are
# added or queried. The model downloads on first use, then reuses its local
# cache in later runs.
_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBEDDING_MODEL
)

# This opens the persistent ChromaDB database stored at CHROMA_PATH.
# It reuses existing stored chunks instead of re-embedding them on import.
_client = chromadb.PersistentClient(path=CHROMA_PATH)
_collection = _client.get_or_create_collection(
    name=CHROMA_COLLECTION,
    embedding_function=_ef,
    metadata={"hnsw:space": "cosine"},
)



def get_collection():
    """Return the ChromaDB collection. Used by app.py during ingestion."""
    return _collection


def embed_and_store(chunks):
    """
    Embed M3 review chunks and store them in the persistent ChromaDB collection.

    ChromaDB automatically converts each chunk's text into an embedding with
    all-MiniLM-L6-v2 through the collection's embedding function.

    Args:
        chunks (list[dict]):
            Review chunks returned by ingest.py. Each chunk must contain:
            - "text" (str): complete review text, including professor context;
            - "source" (str): source document filename;
            - "position" (int): review position within that source document;
            - "chunk_id" (str): unique ID for the review chunk.

    Returns:
        None.

    Side effects:
        Adds each chunk's text, source metadata, review position metadata,
        and unique ID to the persistent ChromaDB collection.
    """
    if not chunks:
        raise ValueError("No chunks were provided for embedding.")
    
    _collection.add(
        documents=[chunk["text"] for chunk in chunks],
        metadatas=[
            {
                "source": chunk["source"],
                "position": chunk["position"],
            }
            for chunk in chunks
        ],
        ids=[chunk["chunk_id"] for chunk in chunks],
    )

    print(f"Stored {_collection.count()} total chunks in the vector database.")



def retrieve(query, top_k=N_RESULTS):
    """
    Retrieve the most semantically relevant stored review chunks for one user query.

    Inputs:
        query (str):
            A non-empty natural-language question about the collected MATH 005A instructor reviews.
        top_k (int):
            Maximum number of nearest chunks to return. Defaults to 5.

    Returns:
        list[dict]:
            Up to top_k retrieved chunks, ordered from lowest distance to highest distance. Each dictionary contains:
            - "text" (str): complete retrieved review text;
            - source (str): source document filename; 
            - position(int): review-position within that source document;
            - "distance" (float): Chroma distance score, where lower means the chunk is more semantically similar to the query.

    Side effects:
        None. When implemented, this function reads from the persistent
        ChromaDB collection but does not modify it.
    """
    if _collection.count() == 0:
        return []

    results = _collection.query(
        query_texts=[query],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )

    return [
        {
            "chunk_id": chunk_id,
            "text": text,
            "source": metadata["source"],
            "position": metadata["position"],
            "distance": float(distance),
        }
        for chunk_id, text, metadata, distance in zip(
            results["ids"][0],
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0],
        )
    ]