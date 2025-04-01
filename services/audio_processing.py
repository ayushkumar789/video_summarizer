import whisper

def extract_audio(video_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    transcript = result["text"]
    return transcript, None
