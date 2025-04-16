import yt_dlp

def extract_audio(url, output_path = "resources/downloaded_audio"):
    """
        Takes a url and extracts audio from it
        :param url : url of YouTube video
        :param output_path : path where the downloaded audio will be saved
        :return : Path of the downloaded audio file
    """

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return output_path