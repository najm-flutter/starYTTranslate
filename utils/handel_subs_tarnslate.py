import os
from utils.gemini_translate import geminiTranslate
import datetime
from rich.progress import track
import srt


def appendTranslate(index: int, content, fileName):
    subs = list(srt.parse(content))
    with open(f"translate/{fileName}.srt", "a") as f:
        f.write(srt.compose(subs, start_index=index))
    index += len(subs)
    return index


def translateFiles():
    paths = os.listdir("tmp/parts")
    os.makedirs("translate", exist_ok=True)
    fileName = datetime.datetime.now().strftime("%B_%H-%M-%S")
    with open(f"translate/{fileName}.srt", "w"):
        pass

    index = 1
    for i in track(range(0, len(paths))):
        print(f"tmp/parts/{i}.srt")
        content = geminiTranslate(f"tmp/parts/{i}.srt")
        index = appendTranslate(index, content, fileName)


if __name__ == "__main__":
    translateFiles()
