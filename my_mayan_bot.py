# my_mayan_bot.py (обновлённый для webhook)

import os
import telebot
from telebot.types import Update
from flask import Flask, request
from waves_schedule import waves_schedule
from datetime import date, datetime
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
    # Шлём красивое приветствие
    bot.send_message(
        message.chat.id,
        "🌿 Welcome to the flow of Mayan time.\n\n"
        "Here you can tune into the energies of each day and reconnect with your natural rhythm.\n\n"
        "Добро пожаловать в пространство майянских энергий! 🌿\n\n"
        "Этот бот поможет тебе сонастроиться со временем по-новому"
    )
    # Показываем выбор языка
    lang_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    lang_keyboard.add(
        telebot.types.KeyboardButton("🇬🇧 English"),
        telebot.types.KeyboardButton("🇷🇺 Русский")
    )
    bot.send_message(message.chat.id, "Choose your language / Выбери язык:", reply_markup=lang_keyboard)

@bot.message_handler(func=lambda message: message.text in ["🇬🇧 English", "🇷🇺 Русский"])
def set_user_language(message):
    lang = "en" if message.text == "🇬🇧 English" else "ru"
    set_language(message.chat.id, lang)

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for button in menu_buttons[lang]:
        markup.add(telebot.types.KeyboardButton(button))
    
    welcome_text = "Welcome! Choose an option below:" if lang == "en" else "Добро пожаловать! Выбери действие ниже:"
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)



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


# 🎴 Рефлексия или Reflect
@bot.message_handler(func=lambda message: message.text in ["🎴 Рефлексия", "🎴 Reflect"])
def reflect(message):
    lang = get_language(message.chat.id)
    questions = [
        "Что внутри меня готово к заботе, а не к давлению?",
        "Где в моей жизни я притворяюсь?",
        "Что я готов(а) завершить с любовью?",
        "Могу ли я полностью встретиться с собой?",
        "Что знает моё тело, о чём забывает разум?"
    ] if lang == "ru" else [
        "What in me is ready to be nourished, not pushed?",
        "Where in my life am I pretending?",
        "What am I ready to complete?",
        "Can I meet myself fully?",
        "What does my body know that my mind ignores?"
    ]
    import random
    bot.send_message(message.chat.id, random.choice(questions))

# 📖 О проекте или About the Project
@bot.message_handler(func=lambda message: message.text in ["📖 О проекте", "📖 About the Project"])
def about_project(message):
    lang = get_language(message.chat.id)
    text = (
        "Этот бот создан как пространство соприкосновения с древней мудростью майянского календаря. "
        "Здесь нет предсказаний — только подсказки энергий дня, помогающие сонастроиться с собой."
    ) if lang == "ru" else (
        "This bot is a space to connect with the ancient wisdom of the Mayan calendar. "
        "No predictions — only hints from the day's energies to help you align with yourself."
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: message.text in ["✨ О Календаре", "✨ About the Calendar"])
def about_calendar(message):
    lang = get_language(message.chat.id)
    text = (
        "Цолькин — это священный календарь майя из 260 дней, отражающий внутреннюю архитектуру самого творения.\n\n"
        "Он сплетает 20 архетипов — универсальных сил сознания — и 13 тонов — этапов движения и роста. "
        "Каждый день представляет собой уникальную встречу архетипа и тона, рождая живую вибрацию, которая зеркалит разворачивание жизни.\n\n"
        "Цолькин — это не просто способ отслеживать время. "
        "Это космическая карта твоего внутреннего пути, показывающая, как циклы рождения, роста, трансформации и обновления движутся через тебя, "
        "соединяя тебя с ритмами Земли, звёзд и самого источника жизни.\n\n"
        "Сонастраиваясь с энергиями Цолькина, ты можешь глубже вспомнить свою истинную природу, "
        "углубить присутствие в настоящем моменте и идти по своему пути с большей ясностью и лёгкостью."
    ) if lang == "ru" else (
        "Tzolkin is the sacred Mayan calendar of 260 days, reflecting the inner architecture of creation itself.\n\n"
        "It weaves together 20 archetypes — universal forces of consciousness — and 13 tones — stages of movement and growth. "
        "Each day is a unique meeting point between an archetype and a tone, creating a living vibration that mirrors the unfolding of life.\n\n"
        "Tzolkin is not just a way to track time — it is a cosmic map of your inner journey. "
        "It shows how cycles of birth, growth, transformation, and renewal move through your being, "
        "connecting you with the rhythms of the Earth, the stars, and the source of life itself.\n\n"
        "Through attunement to the Tzolkin, you can remember your true nature, deepen your awareness of the present moment, "
        "and walk your path with greater clarity and grace."
    )
    bot.send_message(message.chat.id, text)
    
@bot.message_handler(func=lambda message: True)
def debug_message(message):
    print(f"🔍 User sent text: {message.text}")
# Обработчик всех неожиданных сообщений
@bot.message_handler(func=lambda message: True)
def handle_unexpected_message(message):
    # Игнорируем всё, что не подошло под основные кнопки
    pass
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



