import json
import os

REMINDERS_FILE = "reminder_users.json"

def load_reminders():
    try:
        with open(REMINDERS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_reminders(data):
    with open(REMINDERS_FILE, "w") as f:
        json.dump(data, f)
