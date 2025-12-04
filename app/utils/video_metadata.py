import requests
from bs4 import BeautifulSoup

VIDEO_PLATFORMS = [
    "youtube.com",
    "youtu.be",
    "tiktok.com",
    "instagram.com",
    "facebook.com",
    "fb.watch",
    "twitter.com",
    "x.com",
    "vimeo.com"
]

def is_video_url(url: str) -> bool:
    return any(domain in url.lower() for domain in VIDEO_PLATFORMS)

def extract_video_metadata(url: str):
    try:
        if not is_video_url(url):
            return {"error": "Ce lien n'est pas reconnu comme une vidéo."}

        response = requests.get(url, timeout=10, headers={
            "User-Agent": "Mozilla/5.0"
        })
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")

        metadata = {}

        # Open Graph video data
        for tag in soup.find_all("meta"):
            prop = tag.get("property")
            if not prop:
                continue

            if prop.startswith("og:video"):
                metadata[prop] = tag.get("content")
            if prop in ["og:title", "og:description", "og:image", "og:site_name"]:
                metadata[prop] = tag.get("content")

        return metadata if metadata else {"error": "Aucune meta vidéo trouvée."}

    except Exception as e:
        return {"error": str(e)}
