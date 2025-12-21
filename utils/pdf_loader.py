import os
import pdfplumber

from config.settings import EXTRACT_PDF_PATH

os.makedirs("data/pdf", exist_ok=True)

def extract_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    with open(EXTRACT_PDF_PATH, "w") as f:
        f.write(f"{text}\n")

    return text
