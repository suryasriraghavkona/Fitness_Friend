import re

def parse_input(text):
    if "walk" in text or "steps" in text:
        activity = "walk"
    elif "run" in text:
        activity = "run"
    elif "sleep" in text:
        activity = "sleep"
    elif "water" in text:
        activity = "water"
    elif "workout" in text:
        activity = "workout"
    else:
        activity = None

    numbers = re.findall(r'\d+', text)
    value = int(numbers[0]) if numbers else None

    return activity, value