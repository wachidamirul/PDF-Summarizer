from utils.pdf_loader import extract_text
from utils.text_cleaner import clean_text

if __name__ == '__main__':
    text = clean_text(extract_text("data/pdf/temp.pdf"))


    print(f"{text}")
