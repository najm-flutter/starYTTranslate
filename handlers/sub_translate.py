import re
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.gemini_translate import gemini_translate
from services.sub_extract import subs_extract
from utils.messages import error_message
from utils.srt_tools import split_srt_file


def get_vd_url() -> str:
    url_pattern = r"^(?:http|https)://"
    while True:
        vdUrl = input("\nEnter the YouTube video URL: ").strip()
        if re.match(url_pattern, vdUrl):
            return vdUrl
        else:
            error_message(f"The URL '{vdUrl}' is incorrect. Please try again.")


def handle():
    try:
        vdUrl = get_vd_url()
        subs_extract(vdUrl)
        split_srt_file()
        gemini_translate()
    except ValueError as e:
        error_message(e)
