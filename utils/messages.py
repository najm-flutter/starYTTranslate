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
    console.log(template(ERROR_TITLE, f"[bold red]{mes}[/bold red]"))


def SuccessMessage(mes):
    console.log(template(ERROR_TITLE, f"[bold greeb]{mes}[/bold green]"))


def startTaskMessage(n, description=""):
    rprint(f"task {n} start: {description}")


def completeTaskMessage(n, description=""):
    rprint(f"task {n} complete: {description}")
