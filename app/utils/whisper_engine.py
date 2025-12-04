from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def transcribe_audio(audio_path: str) -> str:
    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    context =f" A partir de tes connaissances et de tes sources, dit moi si la vidéo ci dessous est réel ou si c'est une fausse information : {transcript.text}"
    return context
