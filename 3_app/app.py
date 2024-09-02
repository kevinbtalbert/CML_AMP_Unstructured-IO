import streamlit as st
from unstructured.partition.auto import partition
from sentence_transformers import SentenceTransformer
import chromadb

# Initialize Chroma vector database
client = chromadb.Client()
collection = client.get_or_create_collection(name="document_vectors")

# Load a pre-trained sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Streamlit app interface
st.title("Document Upload and Vector Storage App")

# File uploader accepting various document types
uploaded_files = st.file_uploader(
    "Upload your documents (PDF, DOCX, TXT, etc.)", 
    accept_multiple_files=True,
    type=["pdf", "docx", "txt"]
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Read file content
        file_content = uploaded_file.read()
        
        # Use unstructured.io to partition the document content
        try:
            partitioned_content = partition(file_content)
            st.write(f"Successfully partitioned {uploaded_file.name}")
        except Exception as e:
            st.error(f"Error processing {uploaded_file.name}: {e}")
            continue
        
        # Convert partitioned content into text
        document_text = " ".join([element.text for element in partitioned_content if element.text])

        # Generate vectors using sentence transformer
        document_vector = model.encode([document_text])

        # Store vectors in Chroma vector database
        collection.add(
            embeddings=document_vector,
            documents=[document_text],
            metadatas=[{"filename": uploaded_file.name}]
        )

        st.success(f"Document {uploaded_file.name} has been processed and stored in the vector database.")

st.write("Upload documents to see their vector representations stored in the Chroma vector database.")
