import os
import random
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from flask import Flask, request
from datetime import date, datetime
from waves_schedule import waves_schedule
from language_store import get_language, set_language

TOKEN = "7645205403:AAEwNR8zxExLwv0YMpH7ddcCaJUCFJ0G-sA"
WEBHOOK_URL = "https://web-production-93b7.up.railway.app"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

menu_buttons = {
    "en": ["📅 Today's Wave", "🎴 Reflect", "📖 About the Project", "✨ About the Calendar"],
    "ru": ["📅 Текущая Волна", "🎴 Рефлексия", "📖 О проекте", "✨ О Календаре"]
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

@bot.message_handler(func=lambda message: message.text in ["📖 О проекте", "📖 About the Project"])
def about_project(message):
    lang = get_language(message.chat.id)
    text = (
        "Этот бот — пространство для созвучия с собой через живую ткань времени.\n\n"
        "Здесь нет предсказаний и инструкций. "
        "Цолькин — не календарь событий, а карта внутреннего пути. "
        "Он помогает ощутить глубинный ритм жизни, где каждый день — уникальная вибрация на пути Души, Тела и Духа.\n\n"
        "Через синтез современных технологий и древних космических циклов, "
        "этот проект приглашает тебя сонастроить твои земные и высшие аспекты в целостную систему через синхронию в пространстве времени."
    ) if lang == "ru" else (
        "This bot is a space for attuning to yourself through the living fabric of time.\n\n"
        "Here there are no predictions or instructions. "
        "Only the day's energies — the rhythme of the Earth and cosmos — inviting you to remember your true nature.\n\n"
        "Tzolkin is not a calendar of events, but a map of your inner journey. "
        "It helps you feel the deeper rhythm of life, where each day is a unique vibration on your path of the soul's growth.\n\n"
        "Through the synthesis of modern technologies and ancient cosmic cycles, "
        "this project builds a bridge between the eternal and the current, inviting you to attune your body, soul and a spirit into a wholeness once again."
    )
    bot.send_message(message.chat.id, text)


questions_ru = [
    "Что моё тело хочет сказать мне прямо сейчас?",
    "В каком месте моей жизни я притворяюсь?",
    "Что мне стоит отпустить сегодня?",
    "Какая часть меня хочет быть услышанной?",
    "Где я чувствую напряжение внутри?",
    "О чём тоскует моё сердце?",
    "Что я прячу от самого себя?",
    "Что во мне готово расцвести?",
    "Где я могу быть мягче к себе?",
    "Что я боюсь признать перед собой?"
]

questions_en = [
    "What is my body trying to tell me right now?",
    "Where in my life am I pretending?",
    "What am I ready to let go of today?",
    "Which part of me wants to be heard?",
    "Where do I feel tension inside?",
    "What is my heart longing for?",
    "What am I hiding from myself?",
    "What within me is ready to bloom?",
    "Where can I be softer with myself?",
    "What am I afraid to admit to myself?"
]

@bot.message_handler(func=lambda message: message.text in ["🎴 Рефлексия", "🎴 Reflect"])
def reflect(message):
    lang = get_language(message.chat.id)
    
    questions = questions_ru if lang == "ru" else questions_en
    selected_question = random.choice(questions)
    
    bot.send_message(message.chat.id, selected_question)
    
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

ALLOWED_TEXTS = [
    "📅 Today's Wave",
    "📅 Текущая Волна",
    "🎴 Reflect",
    "🎴 Рефлексия",
    "📖 About the Project",
    "📖 О проекте",
    "✨ About the Calendar",
    "✨ О Календаре",
    "🇬🇧 English",
    "🇷🇺 Русский"
]

@bot.message_handler(func=lambda message: message.text in ALLOWED_TEXTS)
def handle_allowed_buttons(message):
    # ничего не делаем, просто позволяем основным обработчикам работать
    pass

# --- Обработчик webhook для Telegram
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    else:
        return 'Invalid request', 400

# --- Корневая страничка Railway (чтобы видеть, что проект живой)
@app.route("/")
def index():
    return "Hello, this is Mayan Bot!"

# --- Настройка webhook и запуск Flask-сервера
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"{WEBHOOK_URL}/{TOKEN}", allowed_updates=["message"])
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
