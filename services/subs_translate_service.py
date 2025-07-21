import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.handel_subs_tarnslate import tranlateFiles

from utils.sub_extract import subs_extract
from utils.messages import errorMessage, startTaskMessage, completeTaskMessage
from utils.split_srt import getPath, splitSrtFile


def sub_extract_handle(vdUrl):
    startTaskMessage(1)
    try:
        subs_extract(vdUrl)
    except ValueError:
        errorMessage(f"we cant downaload transcript for this video : {vdUrl}")
        raise ValueError("error")
    else:
        completeTaskMessage(1)


def sub_translate(vdUrl):
    sub_extract_handle(vdUrl)
    splitSrtFile(getPath())
    tranlateFiles()
