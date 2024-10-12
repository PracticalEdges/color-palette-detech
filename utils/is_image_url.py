import requests

def is_image_url(url: str) -> bool:
    try:
        request = requests.head(url, allow_redirects=True)
        content_type = request.headers["content-type"]
        if content_type and content_type.startswith("image"):
            return True
        return False
    except Exception as e:
        print(f"Error checking the url: {e}")