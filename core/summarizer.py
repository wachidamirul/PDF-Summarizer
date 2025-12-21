from core.llm_client import call_llm

def summarize(text):
    prompt = f"""
Anda adalah seorang ahli dalam meringkas materi akademik. Tugas Anda adalah menganalisis materi yang diberikan dan membuat ringkasan dalam bentuk poin-poin utama yang terstruktur.

Instruksi:
1. Baca dan analisis seluruh materi yang diberikan dengan teliti
2. Identifikasi konsep-konsep kunci, teori utama, dan informasi penting
3. Organisasikan informasi menjadi poin-poin utama yang logis dan hierarkis
4. Gunakan bahasa akademik Indonesia yang formal, jelas, dan mudah dipahami
5. Pastikan setiap poin mencakup esensi dari bagian materi yang relevan

Format Output:
- Gunakan bullet points (•) untuk poin utama
- Gunakan sub-bullet points (◦) untuk detail pendukung jika diperlukan
- Maksimal 8-10 poin utama
- Setiap poin harus ringkas namun informatif (1-2 kalimat)
- Gunakan terminologi akademik yang tepat

Kriteria Kualitas:
- Akurasi: Ringkasan harus mencerminkan isi materi asli
- Kelengkapan: Mencakup semua aspek penting dari materi
- Kejelasan: Mudah dipahami dan logis
- Konsistensi: Gaya bahasa dan format yang seragam

Materi yang akan diringkas:
{text}
"""
    return call_llm(prompt)
