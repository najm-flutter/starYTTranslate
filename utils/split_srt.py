import srt
import os

PARTS_PATH = "tmp/parts"


def readSrtFile(file_path):
    with open(file_path) as file:
        return list(srt.parse(file.read()))


def writeSrtFile(file_path, subtitles):
    with open(file_path, "w") as file:
        file.write(srt.compose(subtitles))


def splitSrtFile(file_path, lines_per_file=150):
    os.makedirs(PARTS_PATH, exist_ok=True)
    subs = readSrtFile(file_path)

    for i in range(0, len(subs), lines_per_file):
        chunk = subs[i : i + lines_per_file]
        writeSrtFile(f"{PARTS_PATH}/{i // lines_per_file}.srt", chunk)
