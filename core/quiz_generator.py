from core.llm_client import llm_quiz

def generate_multiple_choice_quiz(summary, num_questions, difficulty):
    prompt = f"""
Anda adalah sistem pembuat soal akademik yang ahli dalam menganalisis konten dan membuat pertanyaan berkualitas tinggi.

TUGAS UTAMA:
Buat tepat {num_questions} soal pilihan ganda dengan tingkat kesulitan {difficulty} berdasarkan ringkasan yang diberikan.

PEDOMAN PEMBUATAN SOAL:

1. Sumber Informasi:
   - Gunakan HANYA informasi dari ringkasan yang disediakan
   - DILARANG keras menambahkan pengetahuan eksternal
   - Pastikan setiap soal dapat dijawab langsung dari ringkasan

2. Kualitas Soal:
   - Buat pertanyaan yang menguji pemahaman sesuai tingkat kesulitan yang diberikan adalah "{difficulty}"
   - Pastikan setiap soal memiliki SATU jawaban yang jelas benar
   - Buat pengecoh (distractor) yang masuk akal namun salah
   - Hindari pertanyaan yang terlalu mudah ditebak

3. Format dan Bahasa:
   - Gunakan bahasa yang sama dengan ringkasan
   - Pastikan pertanyaan jelas dan tidak ambigu
   - Setiap soal harus memiliki tepat 4 opsi jawaban (A, B, C, D)

FORMAT OUTPUT WAJIB:
Berikan output dalam format JSON yang valid dan lengkap berikut ini:

{{
  "quiz": [
    {{
      "number": 1,
      "question": "Teks pertanyaan",
      "options": {{
        "A": "Pilihan A",
        "B": "Pilihan B",
        "C": "Pilihan C",
        "D": "Pilihan D"
      }},
      "answer": "A) Pilihan A"
    }}
  ]
}}

RINGKASAN MATERI:
{summary}

INSTRUKSI AKHIR:
- Output HARUS berupa JSON valid tanpa teks tambahan
- Periksa kembali struktur JSON sebelum memberikan respons
- Pastikan semua {num_questions} soal telah dibuat dengan lengkap
"""
    return llm_quiz(prompt)

def generate_essay_quiz(summary, num_questions, difficulty):
    prompt = f"""
Anda adalah ahli evaluasi pendidikan.

Buat {num_questions} soal ESAI tingkat {difficulty}
berdasarkan ringkasan berikut.
Soal HARUS 100% berasal dari ringkasan.

Ringkasan:
{summary}

ATURAN:
- Pertanyaan bersifat terbuka
- Menguji pemahaman, analisis, atau sintesis
- Sertakan jawaban ideal singkat

FORMAT OUTPUT (JSON VALID SAJA):
{{
  "quiz": [
    {{
      "number": 1,
      "question": "Pertanyaan esai",
      "answer_key": "Jawaban ideal singkat"
    }}
  ]
}}
"""
    return llm_quiz(prompt)