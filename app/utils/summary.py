import subprocess
import json
from openai import OpenAI
import os
from app.core.config import settings
def get_metadata(path: str):
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration:stream=width,height,codec_name",
        "-of", "json",
        path
    ]
    out = subprocess.check_output(cmd).decode()
    return json.loads(out)



client = OpenAI(api_key=settings.OPENAI_API_KEY)

def summarize_video(video_path: str) -> str:
    metadata = get_metadata(video_path)

    prompt = f"""
    Voici les métadonnées d'une vidéo :

    {metadata}

    Fais un résumé très court du contenu probable de cette vidéo.
    Ne parle que d'hypothèses en te basant sur la durée et les caractéristiques techniques.
    """

    completion = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return completion.choices[0].message.content
