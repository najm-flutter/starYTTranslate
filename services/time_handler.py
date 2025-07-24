from utils.messages import error_message
from utils.text_to_time import text_to_time


def time_handel():
    while True:
        x = input("⏱️ Enter **start time** (format HH:MM:SS): ").strip()
        if not (start := text_to_time(x)):
            error_message("❌ Invalid start time format. Please use HH:MM:SS.")
            continue

        y = input("⏱️ Enter **end time** (format HH:MM:SS): ").strip()
        if not (end := text_to_time(y)):
            error_message("❌ Invalid end time format. Please use HH:MM:SS.")
            continue

        return (start, end)
