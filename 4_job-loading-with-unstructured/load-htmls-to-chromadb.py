import os
import configparser
from unstructured.ingest.file_processor import process_file
from chromadb import ChromaClient
from chromadb.config import Settings

def load_config(config_path):
    """Load configuration from config.ini file."""
    config = configparser.ConfigParser()
    config.read(config_path)
    return config

def get_pdf_files(directory):
    """Recursively get all PDF files in the specified directory."""
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

def process_pdfs_and_store(config):
    """Process PDFs and store their content in a local vector database."""
    # Load settings from config
    pdfs_root_directory = config['settings']['pdfs_root_directory']
    vector_db_path = config['settings']['vector_db_path']
    batch_size = int(config['settings'].get('batch_size', 10))

    # Initialize Chroma client for local persistent storage
    client = ChromaClient(Settings(persist_directory=vector_db_path))

    # Get all PDF files
    pdf_files = get_pdf_files(pdfs_root_directory)

    # Process files in batches and store in vector database
    for i in range(0, len(pdf_files), batch_size):
        batch_files = pdf_files[i:i + batch_size]
        for pdf_file in batch_files:
            print(f"Processing file: {pdf_file}")

            # Extract content from PDF
            extracted_content = process_file(pdf_file)

            # Store content in vector database
            if extracted_content:
                client.index_documents(extracted_content)
                print(f"Stored content from {pdf_file} in vector database.")

    # Persist the database to disk
    client.persist()

if __name__ == "__main__":
    # Load config
    config = load_config('config.ini')

    # Process PDFs and store in vector database
    process_pdfs_and_store(config)
