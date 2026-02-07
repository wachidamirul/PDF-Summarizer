import os
from dotenv import load_dotenv
load_dotenv()

GEMINI_MODEL = "gemini-3-flash-preview"
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

PDF_PATH = "data/pdf/temp.pdf"
LOG_PATH = "data/logs/activity.log"
SUMMARIZE_PATH = "data/pdf/temp.txt"
QUIZ_PATH = "data/quizzes/temp.txt"