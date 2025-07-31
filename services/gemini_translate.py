from datetime import datetime
import re
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from google import genai
from google.genai import types
from rich import print as rprint
from rich.progress import track
import srt

from utils.messages import error_message
from utils.ai_modle import api_key, prompt, MODLE
from file_paths import TMP_PARTS, TRANSLATE
from utils.srt_tools import text_to_srt


def client():
    return genai.Client(
        api_key=api_key(),
    )


def content_generate(content):
    return [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=content)],
        )
    ]


def translate_validator(content, subtitles, index, max):
    srtText = re.sub(r"```.*", "", content)
    if subs := text_to_srt(srtText):
        if index == max - 1:
            return srt.compose(subs)
        if len(subs) == len(subtitles):
            for i in range(len(subs)):
                first: srt.Subtitle = subs[i]
                second: srt.Subtitle = subtitles[i]
                if first.start != second.start or first.end != second.end:
                    break
            else:
                return srt.compose(subs)


def translate_part(filePath, max=4, vd_title=None):
    with open(filePath) as file:
        subtitles = list(srt.parse(file.read()))
        for i in range(max):
            try:
                response = client().models.generate_content(
                    model=MODLE,
                    contents=content_generate(
                        content=srt.compose(subtitles),
                    ),
                    config=types.GenerateContentConfig(
                        system_instruction=[
                            types.Part.from_text(text=prompt(vd_title=vd_title)),
                        ],
                        # thinking_config=types.ThinkingConfig(
                        #     thinking_budget=-1,
                        # ),
                        media_resolution="MEDIA_RESOLUTION_MEDIUM",
                        tools=[
                            types.Tool(googleSearch=types.GoogleSearch()),
                        ],
                        response_mime_type="text/plain",
                    ),
                )
            except Exception as e:
                error_message(f"API ERROR MESSAGE : {e}")

            else:
                if subs := translate_validator(
                    response.text if response.text else " ", subtitles, i, max
                ):
                    rprint(f"[bold green]Translated[/bold green]: {filePath}.")
                    return subs
        else:
            error_message("we can't translate this part")
            return " "


def append_translate(index: int, content, fileName):
    subs = list(srt.parse(content))

    with open(f"{TRANSLATE}/{fileName}.srt", "a") as f:
        f.write(srt.compose(subs, start_index=index))
    index += len(subs)
    return index


def gemini_translate(vd_title=None):
    print(vd_title)
    parts_paths = os.listdir(TMP_PARTS)
    os.makedirs(TRANSLATE, exist_ok=True)
    fileName = datetime.now().strftime("%B_%H-%M-%S")
    with open(f"{TRANSLATE}/{fileName}.srt", "w"):
        pass
    rprint(f"[bold cyan]Video Parts:[/bold cyan] {len(parts_paths)}")
    rprint("[bold green]Translation started for all parts...[/bold green]")
    rprint(
        f"[bold yellow]All translated parts will be saved at:[/bold yellow] [italic]{os.path.join(os.path.dirname(os.path.dirname(__file__)), TRANSLATE, fileName + '.srt')}[/italic]"
    )
    index = 1
    for i in track(range(0, len(parts_paths))):
        rprint(f"[bold yellow]Translate[/bold yellow]: {TMP_PARTS}/{i}.srt ...")
        content = translate_part(f"{TMP_PARTS}/{i}.srt", vd_title=vd_title)
        index = append_translate(index, content, fileName)
