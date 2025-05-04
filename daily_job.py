# daily_job.py
import os
import telebot
from dotenv import load_dotenv
from main import get_daily_message
from language_store import get_language
from reminders import load_reminders  # это твоя функция, может быть в отдельном файле

load_dotenv()
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

def send_morning_updates():
    reminders = load_reminders()
    for user_id, enabled in reminders.items():
        if enabled:
            lang = get_language(int(user_id))
            text = get_daily_message(lang=lang)
            bot.send_message(int(user_id), text)

if __name__ == "__main__":
    send_morning_updates()
