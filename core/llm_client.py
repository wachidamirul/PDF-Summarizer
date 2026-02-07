from google import genai
from google.genai import types
import pathlib

from config.settings import PDF_PATH, GEMINI_KEY, GEMINI_MODEL

client = genai.Client(api_key=GEMINI_KEY)
filepath = pathlib.Path(PDF_PATH)

def llm_summarize(prompt):
    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=[
                types.Part.from_bytes(
                    data=filepath.read_bytes(),
                    mime_type='application/pdf',
                ),
                prompt])
        return response.text
    except Exception as e:
        return f"Terjadi kesalahan: {e}"

def llm_quiz(prompt):
    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Terjadi kesalahan: {e}"