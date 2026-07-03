import gradio as gr

from ingest import load_documents, chunk_document
from retriever import embed_and_store, retrieve, get_collection
from generator import generate_response


def run_ingestion():
    """
    Load local PCC MATH 005A review documents, chunk them, and store them in ChromaDB only when the persistent collection is empty.
    """
    collection = get_collection()
    existing_count = collection.count()

    if existing_count > 0:
        print(
            f"Vector store already populated "
            f"({existing_count} review chunks). Skipping ingestion."
        )
        return

    print("Ingesting PCC MATH 005A review documents...")
    documents = load_documents()
    all_chunks = []

    for document in documents:
        chunks = chunk_document(
            document["text"],
            document["source"],
        )
        all_chunks.extend(chunks)

    if not all_chunks:
        print("No review chunks were produced. Check ingest.py.")
        return

    embed_and_store(all_chunks)
    print(f"Ingestion complete. {len(all_chunks)} review chunks stored.")


def chat(message, history):
    """
    Handle one Gradio chat message.

    `history` is required by Gradio's ChatInterface signature, but this required-only version does not use conversation history for retrieval.
    """
    question = message.strip()

    if not question:
        return "Please enter a question about a MATH 005A instructor."

    retrieved_chunks = retrieve(question)
    return generate_response(question, retrieved_chunks)

def handle_query(question):
    return chat(question, [])


with gr.Blocks() as demo:
    gr.Markdown("# The Unofficial Guide")
    gr.Markdown(
        "An unofficial guide to selected Pasadena City College MATH 005A "
        "instructors, based on past student reviews with written comments."
    )

    inp = gr.Textbox(label="Ask about a MATH 005A instructor")
    btn = gr.Button("Ask")
    answer = gr.Textbox(label="Answer", lines=12)

    btn.click(handle_query, inputs=inp, outputs=answer)
    inp.submit(handle_query, inputs=inp, outputs=answer)


if __name__ == "__main__":
    run_ingestion()
    demo.launch()

