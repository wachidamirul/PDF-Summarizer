from core.summarizer import summarize
from utils.pdf_loader import extract_text
from utils.text_cleaner import clean_text

if __name__ == '__main__':
    text = clean_text(extract_text("data/pdf/temp.pdf"))

    pdf_summarize = summarize(text)

    print(f"{pdf_summarize}")
