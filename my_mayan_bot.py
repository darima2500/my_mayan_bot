
import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from datetime import date, datetime, timedelta
from mayan_waves import waves

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

# Храним язык пользователя
user_language = {}

# Кнопки меню на двух языках
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
def set_language(message):
    lang = "en" if message.text == "🇬🇧 English" else "ru"
    user_language[message.chat.id] = lang
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for button in menu_buttons[lang]:
        markup.add(KeyboardButton(button))
    welcome_text = "Welcome! Choose an option below:" if lang == "en" else "Добро пожаловать! Выбери действие ниже:"
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["📅 Today's Wave", "📅 Текущая Волна"])
def send_today_wave(message):
    lang = user_language.get(message.chat.id, "en")
    today = date.today()
    found = False
    for wave in waves:
        start_date = datetime.strptime(wave['start_date'], "%Y-%m-%d")
        end_date = start_date + timedelta(days=12)
        if start_date.date() <= today <= end_date.date():
            if lang == "en":
                text = f"🌊 *{wave['name']} Wave*\n\n{wave['description']}"
            else:
                text = f"🌊 Волна *{wave['name']}*\n\n{wave['description']}"
            bot.send_message(message.chat.id, text, parse_mode='Markdown')
            found = True
            break
    if not found:
        bot.send_message(message.chat.id, "No wave found for today." if lang == "en" else "Волна на сегодня не найдена.")

@bot.message_handler(func=lambda message: message.text in ["📖 About", "📖 О проекте"])
def about(message):
    lang = user_language.get(message.chat.id, "en")
    text = (
        "This bot helps you stay in tune with the 13-day Mayan waves, offering insights and reflection questions."
        if lang == "en" else
        "Этот бот помогает тебе сонастраиваться с 13-дневными майянскими волнами, давая подсказки и вопросы для рефлексии."
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: message.text in ["🎴 Reflect", "🎴 Рефлексия"])
def reflect(message):
    lang = user_language.get(message.chat.id, "en")
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
