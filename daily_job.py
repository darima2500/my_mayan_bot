# daily_job.py
import os
import telebot
from dotenv import load_dotenv
from language_store import get_language
from reminders import load_reminders
from waves_schedule import waves_schedule
from tones.tones_data import tones_data
from main import get_current_kin, get_current_tone, find_wave_by_kin

load_dotenv()
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

def get_daily_message(lang="en"):
    kin_number = get_current_kin()
    tone_number = get_current_tone(kin_number)

    tone_data = tones_data[tone_number][lang]
    tone_name = tone_data["name"]
    tone_keywords = tone_data["keywords"]
    tone_description = tone_data["description"]

    tone_block = (
        f"🌟 *{tone_name}* (Tone {tone_number})\n"
        f"_{tone_keywords}_\n\n"
        f"{tone_description}"
    )

    wave = find_wave_by_kin(kin_number)
    if wave:
        try:
            wave_text = wave["get_message_func"](lang)
            return f"{tone_block}\n\n{wave_text}"
        except Exception as e:
            return f"{tone_block}\n\n⚠️ Ошибка в тексте волны: {e}"
    else:
        return tone_block

def send_morning_updates():
    print("🚀 Начинаем рассылку...")
    reminders = load_reminders()
    print(f"📋 Загружено пользователей: {len(reminders)}")

    for user_id, enabled in reminders.items():
        print(f"🔍 Проверяем пользователя {user_id} (enabled={enabled})")
        if enabled:
            lang = get_language(int(user_id))
            print(f"🌐 Язык пользователя: {lang}")
            text = get_daily_message(lang=lang)
            print(f"✉️ Отправка сообщения пользователю {user_id}...")
            bot.send_message(int(user_id), text, parse_mode="Markdown")
    print("✅ Рассылка завершена.")


if __name__ == "__main__":
    send_morning_updates()
