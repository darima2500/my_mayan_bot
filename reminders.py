import json
import os

REMINDER_FILE = "reminder_users.json"

def load_reminders():
    if os.path.exists(REMINDER_FILE):
        with open(REMINDER_FILE, "r") as f:
            return json.load(f)
    return {}

def save_reminders(data):
    with open(REMINDER_FILE, "w") as f:
        json.dump(data, f)
