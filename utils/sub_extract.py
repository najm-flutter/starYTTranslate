import yt_dlp
import os
import shutil
from utils.mesaages import errorMessage, startTaskMessage, completeTaskMessage
from time import sleep


def subs_extract(vdUrl):
    startTaskMessage(1)
    sleep(3)
    ydl_opts = {
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitlesformat": "srt",
        "skip_download": True,
        "outtmpl": "tmp/file",
        "quiet": True,
        "no_warnings": True,
    }
    if os.path.exists("tmp/"):
        shutil.rmtree("tmp/")
    os.mkdir("tmp/")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([vdUrl])
        except yt_dlp.DownloadError:
            errorMessage(f"we cant downaload transcript for this video : {vdUrl}")
            raise ValueError()
        else:
            completeTaskMessage(1)
