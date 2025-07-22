import os
from datetime import datetime

import srt
from rich.progress import track
from rich import print as rprint

from utils.gemini_translate import geminiTranslate
from file_paths import TRANSLATE, TMP_PARTS


def appendTranslate(index: int, content, fileName):
    subs = list(srt.parse(content))
    with open(f"{TRANSLATE}/{fileName}.srt", "a") as f:
        f.write(srt.compose(subs, start_index=index))
    index += len(subs)
    return index


def translateFiles():
    paths = os.listdir(TMP_PARTS)
    os.makedirs(TRANSLATE, exist_ok=True)
    fileName = datetime.now().strftime("%B_%H-%M-%S")
    with open(f"{TRANSLATE}/{fileName}.srt", "w"):
        pass
    rprint(f"[bold cyan]Video Parts:[/bold cyan] {len(paths)}")
    rprint("[bold green]Translation started for all parts...[/bold green]")
    rprint(
        f"[bold yellow]All translated parts will be saved at:[/bold yellow] [italic]{os.path.join(os.path.dirname(os.path.abspath(__file__)), TRANSLATE, fileName + '.srt')}[/italic]"
    )
    index = 1
    for i in track(range(0, len(paths))):
        rprint(f"[bold yellow]Translate[/bold yellow]: {TMP_PARTS}/{i}.srt ...")
        content = geminiTranslate(f"{TMP_PARTS}/{i}.srt")
        index = appendTranslate(index, content, fileName)


if __name__ == "__main__":
    translateFiles()
