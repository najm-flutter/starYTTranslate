import yt_dlp
import os
import shutil


def subs_extract(vdUrl):
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
            raise ValueError()
