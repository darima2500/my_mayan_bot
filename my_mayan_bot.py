import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from datetime import date, datetime, timedelta
from mayan_waves import waves
from yellow_star_wave_bilingual import messages
from language_store import get_language, set_language

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

menu_buttons = {
    "en": ["📅 Today's Wave", "🎴 Reflect", "📖 About"],
    "ru": ["📅 Текущая Волна", "🎴 Рефлексия", "📖 О проекте"]
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    lang_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    lang_keyboard.add(KeyboardButton("🇬🇧 English"), KeyboardButton("🇷🇺 Русский"))
    bot.send_message(message.chat.id, "Choose your language / Выбери язык:", reply_markup=lang_keyboard)

@bot.message_handler(func=lambda message: message.text in ["🇬🇧 English", "🇷🇺 Русский"])
def set_user_language(message):
    lang = "en" if message.text == "🇬🇧 English" else "ru"
    set_language(message.chat.id, lang)
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for button in menu_buttons[lang]:
        markup.add(KeyboardButton(button))
    welcome_text = "Welcome! Choose an option below:" if lang == "en" else "Добро пожаловать! Выбери действие ниже:"
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["📅 Today's Wave", "📅 Текущая Волна"])
def send_today_wave(message):
    lang = get_language(message.chat.id)
    today = date.today()
    wave_start = datetime(2025, 4, 25).date()
    delta = (today - wave_start).days

    if 0 <= delta < len(messages):
        msg = messages[delta]
        tone = msg['tone'][lang]
        archetype = msg['archetype'][lang]
        text = msg['text'][lang]
        question = msg['question'][lang]

        day_info = (
            f"🗓️ Day {delta + 1} — Tone: {tone}\n"
            f"🌟 Archetype: {archetype}\n\n"
            f"{text}\n\n"
            f"❓ {question}"
        )
        bot.send_message(message.chat.id, day_info)
    else:
        bot.send_message(message.chat.id, "No wave info for today." if lang == "en" else "Информация о волне на сегодня не найдена.")

@bot.message_handler(func=lambda message: message.text in ["📖 About", "📖 О проекте"])
def about(message):
    lang = get_language(message.chat.id)
    text = (
        "This bot helps you stay in tune with the 13-day Mayan waves, offering insights and reflection questions."
        if lang == "en" else
        "Этот бот помогает тебе сонастраиваться с 13-дневными майянскими волнами, давая подсказки и вопросы для рефлексии."
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: message.text in ["🎴 Reflect", "🎴 Рефлексия"])
def reflect(message):
    lang = get_language(message.chat.id)
    import random
    questions = [
        "What in me is ready to be nourished, not pushed?",
        "Where in my life am I pretending?",
        "What am I ready to complete?",
        "Can I meet myself fully?",
        "What does my body know that my mind ignores?"
    ] if lang == "en" else [
        "Что внутри меня готово к заботе, а не к давлению?",
        "Где в моей жизни я притворяюсь?",
        "Что я готов(а) завершить с любовью?",
        "Могу ли я полностью встретиться с собой?",
        "Что знает моё тело, о чём забывает разум?"
    ]
    bot.send_message(message.chat.id, random.choice(questions))

bot.polling()
