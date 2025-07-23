from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter
from youtube_extractor import extract_video_id_from_url

import os
import shutil

from utils.messages import errorMessage
from file_paths import TMP_PATH


def subs_extract(vdUrl):
    if os.path.exists(TMP_PATH):
        shutil.rmtree(TMP_PATH)
    os.mkdir(TMP_PATH)
    video_id = extract_video_id_from_url(vdUrl)

    if not video_id:
        errorMessage("Invalid YouTube URL , try again")
        raise ValueError()

    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(video_id)
    transcript

    formatter = SRTFormatter()
    srt_formatted = formatter.format_transcript(transcript)
    with open(f"{TMP_PATH}/file.srt", "w", encoding="utf-8") as srt_file:
        srt_file.write(srt_formatted)