import re
from rich import print as rprint
from core.services.subs_translate_service import sub_translate


def get_vdUrl() -> str:
    vdUrl = input("Enter enter the YouTube video URL--> ").strip()
    while True:
        if re.search(r"(?:https|http)://", vdUrl):
            return vdUrl
        else:
            rprint("⛔[bold red]Error enter valid[/bold red]")
            vdUrl = input("Enter correct the YouTube video URL--> ").strip()


def handle():
    vdUrl = get_vdUrl()
    sub_translate(vdUrl)
