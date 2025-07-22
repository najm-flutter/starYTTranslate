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


def errorMessage(mes):
    rprint(template(ERROR_TITLE, f"[bold red]{mes}[/bold red]"))


def SuccessMessage(mes):
    rprint(template(SUCCESS_TITLE, f"[bold green]{mes}[/bold green]"))


def startTaskMessage(n, description=""):
    rprint(f"\ntask {n} start: {description}\n")


def completeTaskMessage(n, description=""):
    rprint(f"\ntask {n} complete: {description}\n")
