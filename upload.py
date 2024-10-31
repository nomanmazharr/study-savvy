import streamlit as st
from PyPDF2 import PdfReader
from docx import Document

def upload_and_read_file():
    uploaded_file = st.file_uploader("Upload a document with specific content for study planning (e.g., topics or descriptions)", type=["txt", "pdf", "docx"])
    file_content = ""
    
    if uploaded_file is not None:
        # Determine the file type and read accordingly
        file_extension = uploaded_file.name.split(".")[-1].lower()
        
        if file_extension == "txt":
            file_content = uploaded_file.read().decode("utf-8")
        elif file_extension == "pdf":
            pdf_reader = PdfReader(uploaded_file)
            file_content = ""
            for page in pdf_reader.pages:
                file_content += page.extract_text() or ""
        elif file_extension == "docx":
            doc = Document(uploaded_file)
            file_content = "\n".join([para.text for para in doc.paragraphs])

            if not file_content:
                st.write('No text found in the file. Please check the file')
        # Display extracted content
        st.write("Content extracted from uploaded file:")
        st.write(file_content)
    
    return file_content
