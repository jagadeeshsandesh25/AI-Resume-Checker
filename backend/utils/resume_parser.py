import PyPDF2
from docx import Document
from io import BytesIO

def extract_text_from_pdf(file_stream):
    """Extract text from PDF file stream"""
    try:
        reader = PyPDF2.PdfReader(file_stream)
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
        return text.strip()
    except Exception as e:
        raise ValueError(f"Failed to parse PDF: {str(e)}")

def extract_text_from_docx(file_stream):
    """Extract text from .docx file stream"""
    try:
        doc = Document(file_stream)
        text = ""
        for para in doc.paragraphs:
            if para.text.strip():
                text += para.text + "\n"
        return text.strip()
    except Exception as e:
        raise ValueError(f"Failed to parse DOCX: {str(e)}")

def extract_text(file_stream, filename):
    """
    Auto-detect file type and extract text.
    Supports .pdf and .docx
    """
    filename = filename.lower()
    if filename.endswith('.pdf'):
        return extract_text_from_pdf(file_stream)
    elif filename.endswith('.docx'):
        return extract_text_from_docx(file_stream)
    else:
        raise ValueError("Unsupported file type. Please upload a PDF or DOCX file.")