from google import genai
from google.genai import types
import srt

import re
import os

from utils.messages import errorMessage
from utils.ai_modle import api_key, PROMPT, MODLE


client = genai.Client(
    api_key=api_key(),
)


generate_content_config = types.GenerateContentConfig(
    system_instruction=[
        types.Part.from_text(text=PROMPT),
    ],
    # thinking_config=types.ThinkingConfig(
    #     thinking_budget=-1,
    # ),
    media_resolution="MEDIA_RESOLUTION_MEDIUM",
    tools=[
        types.Tool(googleSearch=types.GoogleSearch()),
    ],
    response_mime_type="text/plain",
)


def contentGenerate(content, length):
    print(length, "???????")
    return [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=f"""{content}""")],
        )
    ]


def getFilesPath():
    listPaths = os.listdir("tmp/parts/")
    return listPaths


def textToSrt(content):
    try:
        subs = list(srt.parse(content))
    except srt.SRTParseError:
        return None
    else:
        return subs


def validateOfTranslate(content, subtitles, index, max):
    srtText = re.sub(r"```.*", "", content)
    print(srtText)
    if subs := textToSrt(srtText):
        if index == max - 1:
            return srt.compose(subs)
        print(len(subs), len(subtitles))
        if len(subs) == len(subtitles):
            print("done3")
            for i in range(len(subs)):
                first: srt.Subtitle = subs[i]
                second: srt.Subtitle = subtitles[i]
                print("start:", first.start, "end:", first.end)
                print("start:", second.start, "end:", second.end)

                if first.start != second.start or first.end != second.end:
                    print("error2")
                    break
            else:
                return srt.compose(subs)


def geminiTranslate(filePath, max=5):
    with open(filePath) as file:
        subtitles = list(srt.parse(file.read()))
        for i in range(max):
            try:
                response = client.models.generate_content(
                    model=MODLE,
                    contents=contentGenerate(
                        content=srt.compose(subtitles),
                        length=len(subtitles),
                    ),
                    config=generate_content_config,
                )
                print("done")
            except Exception as e:
                errorMessage(f"API ERROR MESSAGE : {e}")

            else:
                if subs := validateOfTranslate(
                    response.text if response.text else " ", subtitles, i, max
                ):
                    return subs
        else:
            errorMessage("we can't translate this part")
            return " "
