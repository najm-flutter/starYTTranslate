import re
from services.subs_translate_service import sub_translate
from utils.mesaages import errorMessage


def get_vdUrl() -> str:
    url_pattern = r"^(?:http|https)://"
    while True:
        vdUrl = input("Enter the YouTube video URL: ").strip()
        if re.match(url_pattern, vdUrl):
            return vdUrl
        else:
            errorMessage(f"The URL '{vdUrl}' is incorrect. Please try again.")


def handle():
    vdUrl = get_vdUrl()
    sub_translate(vdUrl)
