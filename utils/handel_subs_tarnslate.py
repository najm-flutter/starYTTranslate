import os
from utils.gemini_translate import geminiTranslate
import datetime
from rich.progress import track
import srt


def getSrtFiles():
    return


def tranlateFiles():
    content = ""
    paths = os.listdir("tmp/parts")

    for i in track(range(0, len(paths))):
        print(f"tmp/parts/{i}.srt")
        content += geminiTranslate(f"tmp/parts/{i}.srt")
    os.makedirs("translate", exist_ok=True)
    subs = list(srt.parse(content))
    for i in range(0, len(subs)):
        subs[i].index = i + 1
    with open(
        f"translate/{datetime.datetime.now().strftime('%B_%H-%M-%S')}.srt", "w"
    ) as file:
        file.write(srt.compose(subs))


if __name__ == "__main__":
    tranlateFiles()
