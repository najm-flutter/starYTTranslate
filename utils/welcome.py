from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def welcome_message():
    title = Text("👋 Welcome to starTYTranslate!", style="bold magenta")

    description = (
        "[bold cyan]About this tool:[/bold cyan]\n"
        "✨ Developed by [bold yellow]najm-alden[/bold yellow]\n"
        "🎯 Purpose: Generate [bold green]SRT subtitle files[/bold green] "
        "from YouTube videos quickly and easily.\n"
    )

    instructions = "[bold]To begin, please enter the YouTube video URL below:[/bold]"

    panel = Panel.fit(
        f"{title}\n\n{description}\n{instructions}",
        title="🌟 starTYTranslate",
        border_style="bright_blue",
    )

    console.print(panel)

