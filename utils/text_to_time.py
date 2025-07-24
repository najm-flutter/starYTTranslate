from datetime import datetime


def text_to_time(text_time):
    try:
        time = datetime.strptime(text_time, "%H:%M:%S")
    except ValueError:
        return None
    else:
        return time
