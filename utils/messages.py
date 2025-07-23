from rich.console import Console
from rich.panel import Panel
from rich import print as rprint


ERROR_TITLE = "⛔ ERROR"
SUCCESS_TITLE = "✅ SUCCESS"
console = Console()


def template(title, description) -> Panel:
    return Panel.fit(
        f"\n{description}\n",
        title=title,
        border_style="bright_blue",
    )


def error_message(mes):
    rprint(template(ERROR_TITLE, f"[bold red]{mes}[/bold red]"))


def success_message(mes):
    rprint(template(SUCCESS_TITLE, f"[bold green]{mes}[/bold green]"))
