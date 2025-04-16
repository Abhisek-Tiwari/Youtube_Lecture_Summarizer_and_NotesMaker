from fastapi import FastAPI, UploadFile, Form
from audio_extractor import extract_audio
from audio_to_text_convertor import text_from_audio
from summarizer import get_summary
from notes_maker import format_notes
from pydantic import BaseModel
from fastapi.responses import JSONResponse
app = FastAPI()

class Video(BaseModel):
    url: str

@app.post("/transcribe")
def transcribe_audio(video: Video):
    path = extract_audio(video.url) + ".mp3"
    text = text_from_audio(path)

    return JSONResponse(content = {"transcription": text})

@app.post("/summarize")
def summarize_text(text: str = Form(...)):
    summary = get_summary(text)
    formated_notes = format_notes(summary)

    return JSONResponse(content = {"notes": formated_notes})