import whisper

model = whisper.load_model("base")


def text_from_audio(file_path):
    """
    Takes Audio file and transcribes it into text
    :param file_path: file path of audio file
    :return: transcribed text
    """
    result = model.transcribe(file_path)
    text = result['text']

    return text
