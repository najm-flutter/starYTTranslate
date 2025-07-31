import re
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.gemini_translate import gemini_translate
from services.sub_extract import subs_extract
from utils.messages import error_message
from utils.srt_tools import split_srt_file, start_end_srt_file
from services.time_handler import time_handel


def get_vd_url() -> str:
    url_pattern = r"^(?:http|https)://"
    while True:
        vdUrl = input("\nEnter the YouTube video URL: ").strip()
        if re.match(url_pattern, vdUrl):
            return vdUrl
        else:
            error_message(f"The URL '{vdUrl}' is incorrect. Please try again.")


def enter_time():
    val = (
        input(
            "Do you want to specify a start and end time for translation? Enter 'y' for yes or 'n' to translate the entire video: "
        )
        .strip()
        .lower()
    )
    if "y" in val:
        return True
    return False


def handle():
    try:
        vdUrl = get_vd_url()
        vd_title = subs_extract(vdUrl)
        if enter_time():
            star, end = time_handel()
            start_end_srt_file(star, end)
        split_srt_file()
        gemini_translate(vd_title)
    except ValueError as e:
        error_message(e)
