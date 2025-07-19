import io
import sys
import yt_dlp
import os
import shutil


def subs_extract(url):
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
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception:
            raise ValueError("e.msg")
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr
