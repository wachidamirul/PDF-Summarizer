from core.quiz_generator import generate_quiz
from core.summarizer import summarize
from utils.activity_log import log_activity
from utils.pdf_loader import extract_text
from utils.text_cleaner import clean_text

if __name__ == '__main__':
    text = clean_text(extract_text("data/pdf/temp.pdf"))
    pdf_summarize = summarize(text)
    log_activity("Ringkasan berhasil dibuat")

    quiz = generate_quiz(text,10,"mudah")
    log_activity("Kuis berhasil dibuat")

    print(f"{pdf_summarize}")
    print(f"--- KUIS")
    print(f"{quiz}")