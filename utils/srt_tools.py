import srt
import os

from file_paths import TMP_PATH, TMP_PARTS


def get_srt_path():
    for item in os.listdir(TMP_PATH):
        if os.path.isfile(f"{TMP_PATH}/{item}"):
            return f"{TMP_PATH}/{item}"


def read_srt_file(file_path):
    with open(file_path) as file:
        return list(srt.parse(file.read()))


def write_srt_file(file_path, subtitles: list[srt.Subtitle]):
    for i in range(len(subtitles)):
        if not subtitles[i].content:
            subtitles[i].content = "...nothing..."

    with open(file_path, "w") as file:
        file.write(srt.compose(subtitles))


def split_srt_file(lines_per_file=100):
    os.makedirs(TMP_PARTS, exist_ok=True)
    subs = read_srt_file(get_srt_path())

    for i in range(0, len(subs), lines_per_file):
        chunk = subs[i : i + lines_per_file]
        write_srt_file(f"{TMP_PARTS}/{i // lines_per_file}.srt", chunk)


def text_to_srt(content):
    try:
        subs = list(srt.parse(content))
    except srt.SRTParseError:
        return None
    else:
        return subs
