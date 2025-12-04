from openai import OpenAI
client = OpenAI()

def transcribe_audio(audio_path: str) -> str:
    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcript.text
# def transcribe_audio(file_path: str) -> str:
#     """
#     Transcrit un fichier audio en texte avec Whisper.
#     """
#     result = model.transcribe(file_path)
#     return result.get("text", "")


# model = whisper.load_model("base")

# def transcribe_audio(audio_path):
#     result = model.transcribe(audio_path)
#     return result["text"]
