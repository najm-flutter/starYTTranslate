import sys
import os

from rich import print as rprint

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.ai_modle import test_connected
from utils.messages import error_message, success_message
from file_paths import API_KEY


def handel():
    rprint("""
This page allows you to add your API key.
Enter your [bold green]Gemini API key[/bold green] below, or press Enter to [bold red]exit[/bold red].
""")
    while True:
        api_key = input("Enter your Gemini API key: ").strip()
        if not api_key:
            return
        rprint("[bold yellow]Validating[/bold yellow] API key...")
        if test_connected(api_key):
            with open(API_KEY, "w") as f:
                f.write(api_key)
            success_message("API key saved successfully to api_key.txt")
            return
        else:
            error_message("Invalid API key or connection error. try again ")
