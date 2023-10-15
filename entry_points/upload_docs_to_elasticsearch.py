from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from question_answering.document_store import DocumentStore


if __name__ == "__main__":
    # index: document or label; Public IPv4 address
    doc = DocumentStore("document", "34.246.184.150")
    # Uncomment the next line: To remove the documents and in the index (document)
    # doc.remove_document_store()
    doc.create_document_store_from_scratch(upload_embeddings=True)
