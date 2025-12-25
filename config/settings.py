import os
from dotenv import load_dotenv
load_dotenv()

OLLAMA_MODEL = "gemini-3-flash-preview:cloud"
# OLLAMA_MODEL = "mistral:7b"
# OLLAMA_MODEL = "deepseek-r1:7b"
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_TEMPERATURE = 0.3

GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

PDF_PATH = "data/pdf/temp.pdf"
LOG_PATH = "data/logs/activity.log"
SUMMARIZE_PATH = "data/pdf/temp.txt"
QUIZ_PATH = "data/quizzes/temp.txt"