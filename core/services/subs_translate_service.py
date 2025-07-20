from rich.console import Console
from utils.sub_extract import subs_extract

def sub_translate(vdUrl):
    console = Console()
    with console.status("[bold green]Working on tasks..."):
        subs_extract(vdUrl)
