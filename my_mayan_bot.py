import os
import random
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from flask import Flask, request
from datetime import date, datetime
from waves_schedule import waves_schedule
from language_store import get_language, set_language
from dotenv import load_dotenv
from tones.tones_data import tones_data
from archetypes.archetypes_data import archetypes_data




def get_current_kin():
    # Мы знаем, что 2 мая 2025 = Кин 255 (временный старт для теста)
    start_date = date(2025, 5, 2)
    today = date.today()
    delta_days = (today - start_date).days
    return (255 + delta_days) % 260 or 260


    
def find_wave_by_kin(kin_number):
    for wave in waves_schedule:
        if wave["start_kin"] <= kin_number <= wave["end_kin"]:
            return wave
    return None
    
def get_current_tone(kin_number):
    return (kin_number - 1) % 13 + 1

    

load_dotenv()  # <-- инициализируем загрузку переменных
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = "https://web-production-93b7.up.railway.app"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

menu_buttons = {
    "en": ["📅 Today's Wave", "🔢 Calculate Kin", "🎴 Reflect", "📖 About the Project", "✨ About the Calendar"],
    "ru": ["📅 Текущая Волна", "🔢 Рассчитать Кин", "🎴 Рефлексия", "📖 О проекте", "✨ О Календаре"]
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


@bot.message_handler(func=lambda message: message.text in ["📅 Today's Wave", "📅 Текущая Волна"])
def send_today_wave(message):
    lang = get_language(message.chat.id)
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

    found_wave = find_wave_by_kin(kin_number)
    if found_wave:
        try:
            wave_message = found_wave["get_message_func"](lang)
        except Exception as e:
            wave_message = None
            bot.send_message(message.chat.id, f"⚠️ Ошибка в тексте волны:\n{e}")
            return

        if wave_message:
            full_message = f"{tone_block}\n\n{wave_message}"
            bot.send_message(message.chat.id, full_message, parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, "⚠️ Wave message is empty.")
    else:
        bot.send_message(message.chat.id, "❌ Wave not found.")



@bot.message_handler(func=lambda message: message.text in ["📖 О проекте", "📖 About the Project"])
def about_project(message):
    lang = get_language(message.chat.id)
    text = (
        "Этот бот — пространство для внутренней сонастройки, ежедневный ритуал вспоминания себя через живой ритм времени.\n\n"
        "Через синтез современных технологий и древних космических циклов, "
        "этот проект приглашает тебя сонастроить твои земные и высшие аспекты в целостную систему через синхронию в пространстве времени."
    ) if lang == "ru" else (
        "This bot is a space for attuning to yourself through the living fabric of time.\n\n"
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
    "Что я боюсь увидеть в себе?"
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
        "Цолькин — это священный 260-дневный цикл, основанный на майянской космологии. Он отображает невидимую архитектуру сознания и времени.\n\n"
        "Он объединяет 20 архетипов и 13 тонов (дней), создавая уникальный энергетический отпечаток каждого дня. "
        "В нашем проекте используется система подсчёта по доктору Карлу Кальману, которая фокусируется на эволюции сознания. Это инструмент настройки с естественными циклами. \n\n"
        "Сонастраиваясь с этими энергиями, ты можешь глубже вспомнить свою природу и двигаться по жизни с большей ясностью, свободой и глубиной."
    ) if lang == "ru" else (
        "Tzolkin is a sacred 260-day cycle rooted in Mayan cosmology. It maps the invisible architecture of consciousness and time.\n\n"
        "It combines 20 archetypes (universal forces of life) and 13 tones (phases of evolution), forming a unique energetic signature for each day. "
        "Our project follows the approach of Dr. Carl Calleman, focusing on the evolution of consciousness. "
        "Each day carries a distinct pulse in the dance of creation, helping you tune into the deeper currents shaping your experience..\n\n"
    )
    bot.send_message(message.chat.id, text)
    
ALLOWED_TEXTS = [
    "/start",
    "📅 Today's Wave",
    "📅 Текущая Волна",
    "🔢 Calculate Kin"  # в en
    "🔢 Рассчитать Кин"  # в ru
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

# --- Словарь для хранения временного состояния пользователей
user_states = {}

# --- Обработчик кнопки "Рассчитать Кин"
@bot.message_handler(func=lambda message: message.text in ["🔢 Рассчитать Кин", "🔢 Calculate Kin"])
def ask_birthdate(message):
    lang = get_language(message.chat.id)
    user_states[message.chat.id] = "awaiting_birthdate"
    text = "Введите дату рождения в формате ДД.ММ.ГГГГ (например, 21.06.1991):" if lang == "ru" else "Enter your birth date in format DD.MM.YYYY (e.g. 21.06.1991):"
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == "awaiting_birthdate")
def handle_birthdate(message):
    lang = get_language(message.chat.id)
    try:
        print("🧪 Получено сообщение:", repr(message.text))
        print("📎 Тип данных:", type(message.text))
        print("✂️ После strip():", repr(message.text.strip()))

        birth_date = datetime.strptime(message.text.strip(), "%d.%m.%Y").date()
        start_date = date(2025, 5, 8)
        delta = (birth_date - start_date).days
        kin_number = (delta % 260) + 1
        tone_number = (kin_number - 1) % 13 + 1

        wave = find_wave_by_kin(kin_number)
        wave_name = wave["name"] if wave else "Unknown"

        archetype_number = ((kin_number - 1) % 20) + 1
        archetype_entry = archetypes_data.get(archetype_number, {})
        print("🌐 Язык пользователя:", lang)
        print("🔍 Доступные ключи архетипа:", list(archetype_entry.keys()))
        archetype = archetype_entry.get(lang) or archetype_entry.get("ru") or {
            "name": "Неизвестно",
            "keywords": [],
            "description": "Описание архетипа недоступно."
        }

        response = (
            f"🔢 *Кин*: {kin_number}\n"
            f"💠 *Архетип*: {archetype['name']} — {', '.join(archetype['keywords'])}\n"
            f"🎵 *Тон*: {tone_number}\n"
            f"🌊 *Волна*: {wave_name}"
        ) if lang == "ru" else (
            f"🔢 *Kin*: {kin_number}\n"
            f"💠 *Archetype*: {archetype['name']} — {', '.join(archetype['keywords'])}\n"
            f"🎵 *Tone*: {tone_number}\n"
            f"🌊 *Wave*: {wave_name}"
        )

        bot.send_message(message.chat.id, response, parse_mode="Markdown")

    except Exception as e:
        print("❌ Ошибка парсинга даты:", e)
        error_text = (
            "Неверный формат даты. Попробуйте снова: ДД.ММ.ГГГГ"
            if lang == "ru"
            else "Invalid date format. Please try again: DD.MM.YYYY"
        )
        bot.send_message(message.chat.id, error_text)

    finally:
        user_states.pop(message.chat.id, None)

        
# --- Настройка webhook и запуск Flask-сервера
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"{WEBHOOK_URL}/{TOKEN}", allowed_updates=["message"])
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
