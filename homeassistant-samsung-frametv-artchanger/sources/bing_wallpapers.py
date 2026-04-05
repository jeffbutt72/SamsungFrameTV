import requests
from io import BytesIO

def get_image_url():
    return "https://bing.biturl.top/?resolution=UHD&mkt=en-CA"

def get_image(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return BytesIO(r.content), "JPEG"
    except Exception as e:
        print(f"Error: {e}")
        return None, None