import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from flask import Flask, request
from datetime import date, datetime
from waves_schedule import waves_schedule
from language_store import get_language, set_language

TOKEN = "ТВОЙ_ТОКЕН_ЗДЕСЬ"
WEBHOOK_URL = "https://ТВОЙ_АДРЕС_RAILWAY_ЗДЕСЬ"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Меню кнопок
menu_buttons = {
    "en": ["📅 Today's Wave"],
    "ru": ["📅 Текущая Волна"]
}

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    lang_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    lang_keyboard.add(
        KeyboardButton("🇬🇧 English"),
        KeyboardButton("🇷🇺 Русский")
    )
    bot.send_message(
        message.chat.id,
        "🌿 Welcome to the flow of Mayan time.\n\n"
        "Добро пожаловать в пространство майянских энергий! 🌿\n\n"
        "👇 Choose your language / Выбери язык:",
        reply_markup=lang_keyboard
    )

# Обработчик выбора языка
@bot.message_handler(func=lambda message: message.text in ["🇬🇧 English", "🇷🇺 Русский"])
def set_user_language(message):
    lang = "en" if message.text == "🇬🇧 English" else "ru"
    set_language(message.chat.id, lang)

    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for button in menu_buttons[lang]:
        markup.add(KeyboardButton(button))
    
    welcome_text = "Welcome! Choose an option below:" if lang == "en" else "Добро пожаловать! Выбери действие ниже:"
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# Обработчик кнопки 📅 Today's Wave
@bot.message_handler(func=lambda message: message.text in ["📅 Today's Wave", "📅 Текущая Волна"])
def send_today_wave(message):
    lang = get_language(message.chat.id)
    today = date.today()

    found_wave = None
    for wave in waves_schedule:
        start = datetime.strptime(wave["start_date"], "%Y-%m-%d").date()
        end = datetime.strptime(wave["end_date"], "%Y-%m-%d").date()
        if start <= today <= end:
            found_wave = wave
            break

    if found_wave:
        wave_message = found_wave["get_message_func"](lang)
        if wave_message:
            bot.send_message(message.chat.id, wave_message, parse_mode="Markdown")
        else:
            bot.send_message(
                message.chat.id,
                "Информация о текущей волне недоступна." if lang == "ru" else "Wave information is not available."
            )
    else:
        bot.send_message(
            message.chat.id,
            "Информация о текущей волне недоступна." if lang == "ru" else "Wave information is not available."
        )

# Обработчик ВСЕХ неожиданных сообщений
@bot.message_handler(func=lambda message: True)
def handle_unexpected_message(message):
    pass

# Настройка webhook для Railway
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"{WEBHOOK_URL}/{TOKEN}", allowed_updates=["message"])
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
