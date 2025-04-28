
import json
import os

FILE_NAME = "user_language.json"

def load_languages():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_languages(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_language(user_id):
    data = load_languages()
    return data.get(str(user_id), "en")

def set_language(user_id, lang):
    data = load_languages()
    data[str(user_id)] = lang
    save_languages(data)
