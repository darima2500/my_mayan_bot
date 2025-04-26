# my_mayan_bot.py (обновлённый для webhook)

import os
import telebot
from telebot.types import Update
from flask import Flask, request
from waves_data import waves
from language_store import get_language, set_language

TOKEN = "8056299109:AAGalA54I7CoZ2mfR0FLtVohgAJ9zmmYEPc"
WEBHOOK_URL = "https://mymayanbot-production.up.railway.app"  # Мы добавим эту переменную в Railway после

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

menu_buttons = {
    "en": ["\ud83d\udcc5 Today's Wave", "\ud83c\udfb4 Reflect", "\ud83d\udcd3 About the Project", "\u2728 About the Calendar"],
    "ru": ["\ud83d\udcc5 \u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0412\u043e\u043b\u043d\u0430", "\ud83c\udfb4 \u0420\u0435\u0444\u043b\u0435\u043a\u0441\u0438\u044f", "\ud83d\udcd3 \u041e \u043f\u0440\u043e\u0435\u043a\u0442\u0435", "\u2728 \u041e \u041a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u0435"]
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    lang_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    lang_keyboard.add(telebot.types.KeyboardButton("\ud83c\uddec\ud83c\udde7 English"), telebot.types.KeyboardButton("\ud83c\uddf7\ud83c\uddfa \u0420\u0443\u0441\u0441\u043a\u0438\u0439"))
    bot.send_message(message.chat.id, "Choose your language / \u0412\u044b\u0431\u0435\u0440\u0438 \u044f\u0437\u044b\u043a:", reply_markup=lang_keyboard)

@bot.message_handler(func=lambda message: message.text in ["🇬🇧 English", "🇷🇺 Русский"])
def set_user_language(message):
    lang = "en" if message.text == "🇬🇧 English" else "ru"
    set_language(message.chat.id, lang)

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for button in menu_buttons[lang]:
        markup.add(telebot.types.KeyboardButton(button))
    
    welcome_text = "Welcome! Choose an option below:" if lang == "en" else "Добро пожаловать! Выбери действие ниже:"
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)


# Другие обработчики кнопок (Today's Wave, Reflect, About the Project) остаются БЕЗ изменений
# (...)

# Flask обработка webhook запроса
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = Update.de_json(json_string)
        bot.process_new_updates([update])
        return "", 200
    else:
        return "Invalid request", 400

# Корневая страница просто говорит, что бот жив
@app.route("/")
def index():
    return "Hello, this is Mayan Bot!"

if __name__ == "__main__":
    bot.remove_webhook()
    
    if not WEBHOOK_URL or not TOKEN:
        print(f"CRITICAL ERROR: Missing WEBHOOK_URL or TOKEN!")
        print(f"WEBHOOK_URL: {WEBHOOK_URL}")
        print(f"TOKEN: {TOKEN}")
        exit(1)  # <-- остановить выполнение если что-то не передано
    
    bot.set_webhook(url=f"{WEBHOOK_URL}/{TOKEN}", allowed_updates=["message"])
    print("Webhook set successfully!")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


