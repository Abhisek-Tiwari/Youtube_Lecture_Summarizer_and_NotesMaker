
# 🎙️ YouTube Lecture Summarizer & Study Notes Generator 📄

**An AI-powered web app that turns YouTube lectures into clean, structured study notes — powered by Whisper, BART Summarizer, FastAPI backend, and Streamlit frontend.**

---

## 🚀 Features

✅ Convert YouTube lectures to text using OpenAI Whisper  
✅ Summarize lecture content with BART Transformer  
✅ Automatically format clean, structured study notes  
✅ Download notes as a text file  
✅ FastAPI backend handling all heavy lifting  
✅ Streamlit frontend for a smooth user experience  

---

## 📊 Tech Stack

- **Python 3.10+**
- **OpenAI Whisper** (audio transcription)
- **Hugging Face Transformers** (BART for summarization)
- **FastAPI** (API backend)
- **Streamlit** (frontend)
- **yt-dlp** (audio download from YouTube)

---

## 📐 Project Structure

```
project_root/
├── backend/
│   ├── main.py
│   └── utils/
│       ├── audio_utils.py
│       ├── transcription.py
│       ├── summarizer.py
│       └── notes.py
│
├── frontend/
│   └── app.py
│
├── models/
│   └── bart-large-cnn/
│
├── lecture_audio/
└── README.md
```

---

## ⚙️ Installation & Running Locally

1️⃣ Clone the repo  
```bash
git clone https://github.com/Abhisek-Tiwari/youtube-summarizer.git
cd youtube-summarizer
```

2️⃣ Install the requirements
```bash
pip install -r requirements.txt
```


3️⃣ Install backend dependencies  
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

4️⃣ Install frontend dependencies  
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

---

## 📦 API Endpoints

| Method | Endpoint      | Description                  |
|:--------|:----------------|:--------------------------------|
| `POST` | `/transcribe/` | Transcribe audio from YouTube |
| `POST` | `/summarize/`  | Summarize text content        |
| `GET`  | `/ping`        | Check API health              |

---

## 🎨 Screenshots

> 📸 *[Add a few screenshots of your frontend here]*

---

## 📑 Future Improvements

- Add multi-language summarization support  
- Support uploading local audio/video files  
- Deploy on Render/Hugging Face Spaces/Docker  
- Add authentication for premium users  

---

## 🤝 Contributing

Contributions are welcome!  
- Fork the repo  
- Create a new branch  
- Make changes  
- Submit a pull request  

---

## 📬 Connect with Me

- **GitHub:** [Abhisek-Tiwari](https://github.com/Abhisek-Tiwari)
- **LinkedIn:** [abhisek-tiwari-a06315262](https://www.linkedin.com/in/abhisek-tiwari-a06315262/)

---

⭐️ If you like this project, don't forget to leave a star!
