import streamlit as st

from config.settings import PDF_PATH
from core.quiz_generator import generate_quiz
from core.summarizer import summarize
from utils.activity_log import log_activity
from utils.json_validation import extract_json_block

def render_quiz_from_json(quiz_json_str, show_answer=True):
    try:
        if isinstance(quiz_json_str, dict):
            data = quiz_json_str
        else:
            data = extract_json_block(quiz_json_str)

        quiz_list = data.get("quiz", [])

        if not quiz_list:
            st.warning("⚠️ Kuis kosong")
            return

        for item in quiz_list:
            st.markdown(f"### {item['number']}) {item['question']}")

            for key in ["A", "B", "C", "D"]:
                st.markdown(f"**{key}.** {item['options'][key]}")

            if show_answer:
                st.info(f"✅ Kunci Jawaban: **{item['answer']}**")

            st.markdown("---")

    except Exception as e:
        st.error("❌ Gagal memproses kuis")
        st.code(quiz_json_str)
        st.exception(e)

def run_ui():
    st.title("📄 AI Perangkum PDF & Pembuat Kuis")

    # =======================
    # INIT SESSION STATE
    # =======================
    if "ui_state" not in st.session_state:
        st.session_state.ui_state = "idle"  # idle | processing | done

    if "summary" not in st.session_state:
        st.session_state.summary = None

    if "quiz" not in st.session_state:
        st.session_state.quiz = None

    if "error_message" not in st.session_state:
        st.session_state.error_message = None

    disable_input = st.session_state.ui_state != "idle"

    # =======================
    # INPUTS
    # =======================
    uploaded = st.file_uploader(
        "Upload PDF",
        type="pdf",
        disabled=disable_input
    )

    difficulty = st.selectbox(
        "Tingkat Kesulitan",
        ["Mudah", "Sedang", "Sulit"],
        disabled=disable_input
    )

    num_questions = st.slider(
        "Jumlah Soal",
        5, 20, 10,
        disabled=disable_input
    )

    # =======================
    # FILE HANDLING
    # =======================
    if uploaded:
        with open(PDF_PATH, "wb") as f:
            f.write(uploaded.read())

        # =======================
        # STATE: IDLE
        # =======================
        if st.session_state.ui_state == "idle":
            if st.session_state.error_message:
                st.warning(st.session_state.error_message)
                st.session_state.error_message = None  # reset setelah tampil

            if st.button("🚀 Proses"):
                st.session_state.ui_state = "processing"
                st.rerun()

        # =======================
        # STATE: PROCESSING
        # =======================
        if st.session_state.ui_state == "processing":
            progress = st.progress(10)
            try:
                with st.spinner("📄 Membaca dan meringkas PDF..."):
                    log_activity("PDF diproses")

                    st.session_state.summary = summarize()
                    progress.progress(50)

                    log_activity("Ringkasan berhasil dibuat")

                with st.spinner("📝 Membuat kuis..."):
                    st.session_state.quiz = generate_quiz(
                        st.session_state.summary,
                        num_questions,
                        difficulty
                    )
                    progress.progress(100)

                    log_activity("Kuis berhasil dibuat")

                st.session_state.ui_state = "done"
                log_activity("Proses selesai")

            except Exception as e:
                st.session_state.ui_state = "idle"
                st.session_state.error_message = "⏳ Limit API tercapai, silakan coba lagi nanti."
                log_activity(f"ERROR: {str(e)}")
                st.rerun()

        # =======================
        # STATE: DONE
        # =======================
        if st.session_state.ui_state == "done":
            st.success("✅ Proses selesai")

            st.subheader("📌 Ringkasan")
            st.write(st.session_state.summary)

            st.subheader("📝 Kuis")
            render_quiz_from_json(
                st.session_state.quiz,
                show_answer=True
            )


            if st.button("🔄 Buat soal lagi"):
                # RESET TOTAL
                st.session_state.ui_state = "idle"
                st.session_state.summary = None
                st.session_state.quiz = None

                log_activity("Reset untuk proses ulang")
                st.rerun()
