import sys
import os

from rich import print as rprint

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.ai_modle import testConnected
from utils.messages import errorMessage, SuccessMessage

API_KEY_FILE = "api_key.txt"

def add_api_key():
    rprint("""
This page allows you to add your API key.
Enter your [bold green]Gemini API key[/bold green] below, or press Enter to [bold red]exit[/bold red].
""")
    while True:
        api_key = input("Enter your Gemini API key: ").strip()
        if not api_key:
            return
        rprint("[bold yellow]Validating[/bold yellow] API key...")
        if testConnected(api_key):
            with open(API_KEY_FILE, "w") as f:
                f.write(api_key)
            SuccessMessage("API key saved successfully to api_key.txt")
            return
        else:
            errorMessage("Invalid API key or connection error. try again ")