from handlers import add_api_key, sub_translate
from utils.welcome import welcome_message
from utils.ai_modle import is_api_key_stored
from rich import print as rprint

menu_text = (
    "\nPlease choose an option:\n"
    "1 - Translate a YouTube video\n"
    "2 - Add your Gemini API key\n"
    "3 - Exit\n"
    "Your choice: "
)


def run_menu():
    welcome_message()

    choice = input(menu_text)
    while choice not in "3":
        match choice:
            case "1":
                if is_api_key_stored():
                    sub_translate.handle()
                else:
                    rprint(
                        "\nGemini API key [bold red]not found[/bold red]. Please add your API key first.\n"
                    )
            case "2":
                add_api_key.handel()
            case _:
                rprint(
                    "\n[bold red]Invalid sel-ection[/bold red]. Please enter 1, 2, or 3.\n"
                )
        choice = input(menu_text)
