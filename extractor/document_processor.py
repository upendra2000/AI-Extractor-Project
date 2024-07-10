import csv
from docx import Document
from pypdf import PdfReader
import io

class DocumentProcessor:
    @staticmethod
    def read_docx(file_content: bytes) -> str:
        doc = Document(io.BytesIO(file_content))
        return " ".join([paragraph.text for paragraph in doc.paragraphs])

    @staticmethod
    def read_pdf(file_content: bytes) -> str:
        reader = PdfReader(io.BytesIO(file_content))
        return " ".join([page.extract_text() for page in reader.pages])

    @staticmethod
    def read_csv(file_content: bytes) -> list:
        decoded_content = file_content.decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_content)
        return list(reader)
