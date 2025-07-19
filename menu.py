from utils.welcome import welcome_message
from handlers import sub_translate


def run_menu():
    welcome_message()
    sub_translate.handle()
