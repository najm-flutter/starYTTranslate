from utils.welcome import welcome_message
from handlers import sub_translate, add_api_key
from utils.ai_modle import isApiKeyAvailable
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
                if isApiKeyAvailable():
                    sub_translate.handle()
                else:
                    rprint(
                        "\nGemini API key [bold red]not found[/bold red]. Please add your API key first.\n"
                    )
            case "2":
                add_api_key.add_api_key()
                rprint(
                    "\nYour Gemini API key has been added [bold green]successfully[/bold green].\n"
                )
            case _:
                rprint(
                    "\n[bold red]Invalid sel-ection[/bold red]. Please enter 1, 2, or 3.\n"
                )
        choice = input(menu_text)


if __name__ == "__main__":
    run_menu()
