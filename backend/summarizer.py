from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

model_path = "../models/bart-large-cnn"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

def get_summary(transcribed_text):
    """
    Summarizes the transcribed text
    :param transcribed_text: Transcribed text from the downloaded audio file
    :return: Summarized text
    """
    summary = summarizer(transcribed_text, max_length=200, min_length=50, do_sample=False)
    summary_text = summary[0]['summary_text']

    return summary_text