import sys
import os
import shutil

import yt_dlp

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from youtube_transcript_api import (
    YouTubeTranscriptApi,
    NoTranscriptFound,
    TranslationLanguageNotAvailable,
)
from youtube_transcript_api.formatters import SRTFormatter
from youtube_extractor import extract_video_id_from_url
from pytube import YouTube, exceptions

from utils.messages import error_message
from file_paths import TMP_PATH


def get_en_transcript(vdId):
    ytt_api = YouTubeTranscriptApi()
    try:
        transcript = ytt_api.fetch(vdId)
    except (TranslationLanguageNotAvailable, NoTranscriptFound):
        return None
    else:
        return transcript


def get_manually_transcript(vdId):
    try:
        ytt_api = YouTubeTranscriptApi.list(vdId)
        transcript = ytt_api.find_manually_created_transcript(
            ytt_api._translation_languages
        )
    except (TranslationLanguageNotAvailable, NoTranscriptFound):
        return None
    else:
        return transcript


def get_generated_transcript(vdId):
    try:
        ytt_api = YouTubeTranscriptApi.list(vdId)
        transcript = ytt_api.find_generated_transcript(ytt_api._translation_languages)
    except (TranslationLanguageNotAvailable, NoTranscriptFound):
        return None
    else:
        return transcript


def save_transcript(transcript):
    formatter = SRTFormatter()
    srt_formatted = formatter.format_transcript(transcript)
    with open(f"{TMP_PATH}/file.srt", "w", encoding="utf-8") as srt_file:
        srt_file.write(srt_formatted)


def subs_extract(vdUrl):
    if os.path.exists(TMP_PATH):
        shutil.rmtree(TMP_PATH)
    os.mkdir(TMP_PATH)
    vdId = extract_video_id_from_url(vdUrl)

    if not vdId:
        error_message("Invalid YouTube URL , try again")
        raise ValueError()
    title = None
    ydl_opts = {
        "quiet": True,
        "skip_download": True,  # Do not download the video
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(vdUrl, download=False)
            print("Title:", info["title"])
            title = info["title"]
    except exceptions.PytubeError:
        pass
    if transcript := get_en_transcript(vdId):
        save_transcript(transcript)
        return title
    if transcript := get_manually_transcript(vdId):
        save_transcript(transcript)
        return title
    if transcript := get_generated_transcript(vdId):
        save_transcript(transcript)
        return title
    raise ValueError("Can't Translate This video")
