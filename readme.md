# 📄 AI Perangkum PDF & Pembuat Kuis

Aplikasi berbasis Python yang menggunakan kecerdasan buatan (AI) untuk merangkum dokumen PDF secara otomatis dan menghasilkan kuis (pilihan ganda atau esai) untuk menguji pemahaman materi. Proyek ini mengintegrasikan Google Gemini untuk pemrosesan teks tingkat lanjut.

## 🌟 Fitur Utama

- **Peringkasan PDF Cerdas**: Menggunakan Google Gemini 3 Flash untuk mengekstrak poin-poin penting dari dokumen PDF, termasuk analisis terhadap elemen visual seperti grafik dan tabel.
- **Generator Kuis Otomatis**: Membuat soal kuis berdasarkan hasil ringkasan materi menggunakan model Ollama.
- **Kustomisasi Kuis**: 
  - **Tipe Soal**: Pilih antara Pilihan Ganda (dengan kunci jawaban) atau Esai.
  - **Tingkat Kesulitan**: Mudah, Sedang, atau Sulit.
  - **Jumlah Soal**: Atur jumlah soal yang ingin dihasilkan (5 - 20 soal).
- **Antarmuka Streamlit**: UI yang bersih dan interaktif untuk pengalaman pengguna yang intuitif.
- **Logging Aktivitas**: Mencatat setiap proses yang berjalan untuk memudahkan debugging dan pemantauan.

## 🏗️ Struktur Proyek

```text
PDF-Summarizer/
├── config/             # Konfigurasi aplikasi & model (Gemini & Ollama)
├── core/               # Logika utama (LLM clients, summarizer, quiz generator)
├── ui/                 # Implementasi antarmuka Streamlit
├── utils/              # Helper functions (logging, JSON parsing)
├── main.py             # Entry point utama aplikasi
├── requirements.txt    # Daftar dependensi library
└── readme.md           # Dokumentasi proyek
```

## ⚙️ Persiapan & Instalasi

### 1. Prasyarat
- Python 3.10 atau lebih tinggi.
- API Key dari [Google AI Studio](https://aistudio.google.com/) untuk layanan Gemini.

### 2. Instalasi Dependensi
Clone repository ini dan instal library yang dibutuhkan:
```bash
git clone https://github.com/wachidamirul/PDF-Summarizer.git
cd PDF-Summarizer

pip install -r requirements.txt
```

### 3. Konfigurasi Environment
Buat file `.env` di direktori root proyek dan masukkan API Key Gemini Anda:
```env
GEMINI_API_KEY=isi_dengan_api_key_gemini_anda
```

### 4. Menjalankan Aplikasi
Jalankan perintah berikut untuk memulai aplikasi:
```bash
streamlit run main.py
```

## 📖 Cara Penggunaan

1. **Unggah PDF**: Pilih dan unggah file PDF yang ingin dipelajari melalui area upload.
2. **Atur Parameter**: 
   - Pilih tipe kuis (Pilihan Ganda atau Esai).
   - Tentukan tingkat kesulitan materi.
   - Geser slider untuk menentukan jumlah soal.
3. **Proses**: Klik tombol **🚀 Proses**. Aplikasi akan:
   - Membaca dan merangkum isi PDF menggunakan Gemini.
   - Menghasilkan kuis berdasarkan ringkasan tersebut menggunakan Gemini.
4. **Pelajari & Kerjakan**: Baca ringkasan eksekutif dan kerjakan kuis yang muncul di layar.
5. **Reset**: Gunakan tombol **🔄 Buat soal lagi** jika ingin memproses dokumen baru.

---
*Proyek ini dikembangkan untuk memenuhi tugas mata kuliah Pemrograman Python.*
