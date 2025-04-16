import streamlit as st
import requests

backend_url = "http://localhost:8000"

st.title("🎙️ YouTube Lecture Summarizer 📄")
url = st.text_input("Enter YouTube Video URL:")

if st.button("Generate Study Notes"):
    if url:
        with st.spinner("Processing..."):
            # 1️⃣ Transcribe
            res = requests.post(f"{backend_url}/transcribe/", json={"url": url})
            transcription = res.json()["transcription"]

            # 2️⃣ Summarize
            res = requests.post(f"{backend_url}/summarize/", data={"text": transcription})
            notes = res.json()["notes"]

            st.subheader("📖 Summary Notes:")
            st.text_area("", notes, height=300)

            # Download notes
            st.download_button("📥 Download Notes", notes, file_name="lecture_notes.txt")
        st.success("Done!")
    else:
        st.warning("Please enter a valid URL.")