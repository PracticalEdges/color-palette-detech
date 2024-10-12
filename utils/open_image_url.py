from PIL import Image
import requests
from io import BytesIO

def open_image_url(url: str) -> Image:
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img
    except Exception as e:
        print(f"Error opening the image: {e}")