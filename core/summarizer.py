from config.settings import SUMMARIZE_PATH
from core.gemini_client import gemini_client
from core.llm_client import call_llm

def summarize():
    prompt = f"""
Peran:
Anda adalah seorang ahli analisis materi akademik multimodal. Tugas Anda adalah meringkas dokumen PDF yang terdiri dari teks komprehensif dan elemen visual (gambar, diagram, grafik, atau tabel).

Instruksi Khusus:
1. Analisis Teks & Visual: Baca seluruh teks dan amati setiap gambar/elemen visual. Jangan abaikan informasi yang hanya tersaji dalam bentuk grafik atau diagram.
2. Sintesis Informasi: Hubungkan penjelasan tekstual dengan data yang ada pada gambar untuk mendapatkan pemahaman yang utuh.
3. Identifikasi Konsep: Temukan teori utama, temuan kunci, serta tren data yang ditampilkan secara visual.
4. Organisasi Hierarkis: Susun informasi secara logis menggunakan poin-poin yang terstruktur.
5. Bahasa: Gunakan bahasa Indonesia akademik yang formal, presisi, namun tetap mengalir.

Panduan Penulisan Poin:
* Poin Utama (•): Berisi konsep besar atau temuan utama.
* Sub-poin (◦): Berisi detail pendukung, penjelasan istilah, atau interpretasi data dari gambar/tabel yang relevan dengan poin utama tersebut.

Format Output:
* Judul Ringkasan: (Tuliskan judul materi)
* Ringkasan Eksekutif: (1-2 kalimat gambaran umum materi)
* Poin-Poin Utama: (Daftar poin dan sub-poin)
* Catatan Visual Penting: (Opsional: Jika ada diagram/grafik kunci, jelaskan maknanya secara singkat di bagian ini).

Kriteria Kualitas:
* Integrasi: Berhasil menggabungkan narasi teks dengan data visual.
* Akurasi & Kelengkapan: Tidak ada informasi krusial yang terlewat.
* Kejelasan: Terminologi akademik digunakan dengan tepat dan mudah dipahami.
"""
    result = gemini_client(prompt)
    with open(SUMMARIZE_PATH, "w") as f:
        f.write(f"{result}\n")

    return gemini_client(result)
