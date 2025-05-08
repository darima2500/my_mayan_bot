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
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from reminders import save_reminders, load_reminders



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

def build_main_menu(user_id, lang):
    reminders = load_reminders()
    is_enabled = reminders.get(str(user_id), False)

    if lang == "ru":
        notify_label = "🔔 Уведомления: Вкл" if is_enabled else "🔕 Уведомления: Выкл"
        return [
            "📅 Текущая Волна",
            "🔢 Рассчитать Кин",
            "🌌 Получить Космограмму",
            "🌞 Заказать Соляр",
            "🎨 Мандала Волны",
            "📖 О проекте",
            "✨ О Календаре",
            notify_label
        ]
    else:
        notify_label = "🔔 Notifications: On" if is_enabled else "🔕 Notifications: Off"
        return [
            "📅 Today's Wave",
            "🔢 Calculate Kin",
            "🌌 Order Cosmogram",
            "🌞 Order Solar Return",
            "🎨 Wave Mandala",
            "📖 About the Project",
            "✨ About the Calendar",
            notify_label
        ]


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    lang_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    lang_keyboard.add(
        KeyboardButton("🇬🇧 English"),
        KeyboardButton("🇷🇺 Русский")
    )

    welcome_text = (
        "🌿 Welcome to the flow of Mayan time.\n\n"
        "🌿 Добро пожаловать в пространство майянских энергий! \n\n"
        "👇 Choose your language / Выбери язык:"
    )

    with open('welcome_banner.png', 'rb') as photo:
        bot.send_photo(
            message.chat.id,
            photo,
            caption=welcome_text,
            parse_mode="Markdown",
            reply_markup=lang_keyboard
        )


# Обработчик выбора языка
@bot.message_handler(func=lambda message: message.text in ["🇬🇧 English", "🇷🇺 Русский"])
def set_user_language(message):
    lang = "en" if message.text == "🇬🇧 English" else "ru"
    set_language(message.chat.id, lang)

    # Строим новое меню
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for button in build_main_menu(message.chat.id, lang):
        markup.add(KeyboardButton(button))

    # Отправляем приветствие
    welcome_text = (
        "Welcome! Choose an option below:" if lang == "en"
        else "Добро пожаловать! Выбери действие ниже:"
    )

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
        # Получаем номер волны по порядку в календаре
        wave_index = waves_schedule.index(found_wave)
        wave_number = wave_index + 1
        wave_image_path = f"wave_images/wave_{wave_number}.png"

        # Пробуем отправить картинку волны
        print("Путь к картинке:", wave_image_path)
        try:
            with open(wave_image_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        except FileNotFoundError:
            bot.send_message(message.chat.id, "📷 Картинка для этой волны пока не добавлена.")

        # Получаем и отправляем текст волны
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


@bot.message_handler(func=lambda m: "About the Project" in m.text or "О проекте" in m.text) 
def about_project(message):
    lang = get_language(message.chat.id)
    text = (
        "Этот бот — пространство для внутренней сонастройки, ежедневный ритуал вспоминания себя через живой ритм времени.\n\n"
        "Через синтез современных технологий и древних космических циклов, "
        "этот проект приглашает тебя сонастроить твои земные и высшие аспекты в целостную систему через синхронию в пространстве времени.\n\n"
        "Все изображения волн — это оригинальные картины художницы Даримы Цыремпиловой, написанные вручную и отражающие энергию каждой фазы.\n"
        "🌐 Подробнее: [theartofreconnection.info](https://theartofreconnection.info)\n"
        "📩 Связь: @darimacello"
    ) if lang == "ru" else (
        "This bot is a space for inner alignment — a daily ritual of remembering yourself through the living rhythm of time.\n\n"
        "Through the synthesis of modern technologies and ancient cosmic cycles, "
        "this project invites you to attune your earthly and higher aspects into one harmonious flow.\n\n"
        "All wave visuals are original paintings by the artist Darima Tcyrempilova, created by hand to embody each phase’s energy.\n"
        "🌐 More: [theartofreconnection.info](https://theartofreconnection.info)\n"
        "📩 Contact: @darimacello"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

    

@bot.message_handler(func=lambda message: message.text in ["✨ О Календаре", "✨ About the Calendar"])
def about_calendar(message):
    lang = get_language(message.chat.id)

    # Путь к картинке (если она лежит локально в папке проекта)
    image_path = "images/tzolkin_visual.png"

    text = (
        "Цолькин — это священный 260-дневный цикл, основанный на майянской космологии. Он отображает невидимую архитектуру сознания и времени.\n\n"
        "Он объединяет 20 архетипов и 13 тонов (дней), создавая уникальный энергетический отпечаток каждого дня. "
        "В нашем проекте используется система подсчёта по доктору Карлу Кальману, которая фокусируется на эволюции сознания. Это инструмент настройки с естественными циклами. \n\n"
        "Сонастраиваясь с этими энергиями, ты можешь глубже вспомнить свою природу и двигаться по жизни с большей ясностью, свободой и глубиной."
    ) if lang == "ru" else (
        "Tzolkin is a sacred 260-day cycle rooted in Mayan cosmology. It maps the invisible architecture of consciousness and time.\n\n"
        "It combines 20 archetypes (universal forces of life) and 13 tones (phases of evolution), forming a unique energetic signature for each day. "
        "Our project follows the approach of Dr. Carl Calleman, focusing on the evolution of consciousness. "
        "Each day carries a distinct pulse in the dance of creation, helping you tune into the deeper currents shaping your experience."
    )

    # Сначала отправляем изображение
    with open(image_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo)

    # Потом — текст
    bot.send_message(message.chat.id, text)




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
    text = (
        "Введите дату рождения в формате ДД.ММ.ГГГГ (например, 21.06.1991):"
        if lang == "ru"
        else "Enter your birth date in format DD.MM.YYYY (e.g. 21.06.1991):"
    )
    bot.send_message(message.chat.id, text)

# --- Обработка даты
@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == "awaiting_birthdate")
def handle_birthdate(message):
    lang = get_language(message.chat.id)
    try:
        birth_date = datetime.strptime(message.text.strip(), "%d.%m.%Y").date()
        start_date = date(2025, 5, 8)
        delta = (birth_date - start_date).days
        kin_number = (delta % 260) + 1
        tone_number = (kin_number - 1) % 13 + 1

        wave = find_wave_by_kin(kin_number)
        wave_name = wave["name"] if wave else "Unknown"

        archetype_number = ((kin_number - 1) % 20) + 1
        archetype_entry = archetypes_data.get(archetype_number, {})
        archetype = archetype_entry.get(lang) or archetype_entry.get("ru") or {
            "name": "Неизвестно",
            "keywords": [],
            "description": "Описание архетипа недоступно."
        }

        if lang == "ru":
            response = (
                f"🔢 *Кин*: {kin_number}\n"
                f"💠 *Архетип*: *{archetype['name']}* — _{', '.join(archetype['keywords'])}_\n\n"
                f"{archetype['description']}\n\n"
                f"🎵 *Тон*: {tone_number}\n"
                f"🌊 *Волна*: {wave_name}"
            )
        else:
            response = (
                f"🔢 *Kin*: {kin_number}\n"
                f"💠 *Archetype*: *{archetype['name']}* — _{', '.join(archetype['keywords'])}_\n\n"
                f"{archetype['description']}\n\n"
                f"🎵 *Tone*: {tone_number}\n"
                f"🌊 *Wave*: {wave_name}"
            )

        bot.send_message(message.chat.id, response, parse_mode="Markdown")

    except Exception as e:
        error_text = (
            "❌ Неверный формат даты. Попробуйте снова: ДД.ММ.ГГГГ"
            if lang == "ru"
            else "❌ Invalid date format. Please try again: DD.MM.YYYY"
        )
        bot.send_message(message.chat.id, error_text)

    finally:
        user_states.pop(message.chat.id, None)



        
@bot.message_handler(func=lambda m: m.text in [
    "🔔 Уведомления", "🔕 Уведомления", "🔔 Уведомления: Вкл", "🔕 Уведомления: Выкл",
    "🔔 Notifications", "🔕 Notifications", "🔔 Notifications: On", "🔕 Notifications: Off"
])
def toggle_reminder(message):
    user_id = str(message.chat.id)
    lang = get_language(message.chat.id)
    reminders = load_reminders()
    current = reminders.get(user_id, False)
    reminders[user_id] = not current
    save_reminders(reminders)

    is_now = reminders[user_id]

    text = (
        f"{'✅ Утреннее сообщение *включено*.' if is_now else '🚫 Утреннее сообщение *отключено*.'}\n\n"
        "Каждое утро ты будешь получать описание текущего дня по майянскому календарю."
    ) if lang == "ru" else (
        f"{'✅ Morning reminder *enabled*.' if is_now else '🚫 Morning reminder *disabled*.'}\n\n"
        "Each morning you'll receive the Mayan energy update for the day."
    )

    # Обновим меню
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for button in build_main_menu(message.chat.id, lang):
        markup.add(KeyboardButton(button))

    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)



# --- ОБРАБОТЧИК "Получить Космограмму" ---
@bot.message_handler(func=lambda m: m.text in ["🌌 Получить Космограмму", "🌌 Order Cosmogram"])
def handle_cosmogram_simple(message):
    lang = get_language(message.chat.id)
    if lang == "ru":
        text = (
            "🌌 *Личная космограмма* — полный разбор энергетической карты рождения по майянскому календарю.\n"
            "В подарок ты получишь 5 мандал для рисования по энергиям своей космограммы.\n\n"
            "*Что внутри:*\n"
            "— Архетип твоего духа (Кин рождения)\n"
            "— Способ реализации (Тон)\n"
            "— Волна как путь и ритм твоего воплощения\n"
            "— Мужская и женская энергия (твои активные и принимающие стороны)\n"
            "— Энергия прошлого и будущего (две опоры души)\n"
            "— Мандала для сонастройки\n\n"
            "⚪ *Формат:* PDF-документ с описанием и визуалом\n\n"
            "💌 Заказать: [@darimacello](https://t.me/darimacello)"
        )
        bot.send_message(message.chat.id, text, parse_mode="Markdown")

    else:
        text = (
            "🌌 *Personal Cosmogram* — a full energetic reading based on your Mayan birth energies.\n\n"
            "*What’s inside:*\n"
            "— Archetype of your spirit (Birth Kin)\n"
            "— Mode of realization (Tone)\n"
            "— The wave as your soul’s rhythm and path\n"
            "— Masculine and feminine energies (your active and receptive sides)\n"
            "— Past and future energies (soul anchors)\n"
            "— A mandala for deep alignment\n\n"
            "⚪ *Format:* PDF with interpretation and visual\n\n"
            "💌 To order: [@darimacello](https://t.me/darimacello)"
        )
        bot.send_message(message.chat.id, text, parse_mode="Markdown")


# --- ОБРАБОТЧИК "Соляр" ---
@bot.message_handler(func=lambda m: m.text in ["🌞 Заказать Соляр", "🌞 Order Solar Return"])
def handle_solar_simple(message):
    lang = get_language(message.chat.id)
    if lang == "ru":
        text = (
            "🌞 *Личный Соляр* — твоя энергетическая карта года по майянскому календарю.\n\n"
            "*Что внутри:*\n"
            "— Главный Кин года (тема твоего цикла)\n"
            "— Волна, в которой он разворачивается\n"
            "— Чувствительные волны года (моменты силы и трансформации)\n"
            "— Мужская и женская энергия года (что активировать и что принимать)\n"
            "— Энергия входа в год и та, которую важно отпустить\n"
            "— Мандалы в подарок для глубокой настройки\n\n"
            "⚪ *Формат:* PDF-документ с трактовкой и визуалом\n\n"
            "💌 Заказать: [@darimacello](https://t.me/darimacello)"
        )
    else:
        text = (
            "🌞 *Personal Solar Chart* — your energetic map of the current year based on the Mayan calendar.\n\n"
            "*What’s inside:*\n"
            "— Your year's guiding Kin (theme of the cycle)\n"
            "— The wave it unfolds in\n"
            "— Sensitive waves of the year (moments of strength and transformation)\n"
            "— Masculine and feminine energies of the year (what to activate and receive)\n"
            "— The energy you enter the year with, and what to release\n"
            "— Mandalas as a gift for deep attunement\n\n"
            "⚪ *Format:* PDF with guidance and visuals\n\n"
            "💌 To order: [@darimacello](https://t.me/darimacello)"
        )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")



# --- ОБРАБОТЧИК "Мандала Волны" ---
@bot.message_handler(func=lambda m: m.text in ["🎨 Мандала Волны", "🎨 Wave Mandala"])
def handle_wave_mandala(message):
    lang = get_language(message.chat.id)
    if lang == "ru":
        text = (
            "🎨 *Мандала Волны*\n\n"
            "Каждые 13 дней ты можешь получать новую мандалу для рисования и сонастройки с текущими энергиями.\n\n"
            "Вот текущая мандала:"
        )
        caption = "🌀 Текущая мандала. Обновляется каждые 13 дней."
    else:
        text = (
            "🎨 *Wave Mandala*\n\n"
            "Every 13 days you can receive a new mandala to tune into the current wave's energy.\n\n"
            "Just print it and connect the dotes on the mandala. Here is the current one:"
        )
        caption = "🌀 Current mandala. Updated every 13 days."

    bot.send_message(message.chat.id, text, parse_mode="Markdown")
    try:
        with open("wave_mandalas/mandala_current.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo, caption=caption)
    except FileNotFoundError:
        bot.send_message(message.chat.id, "⚠️ Файл мандалы не найден. Пожалуйста, добавь mandala_current.jpg в папку wave_mandalas/")
    
# --- ЛОГИРОВАНИЕ ВСЕХ ВХОДЯЩИХ СООБЩЕНИЙ ---
@bot.message_handler(func=lambda message: True)
def log_all_messages(message):
    print("📥 Поймано сообщение:", repr(message.text))

# --- Настройка webhook и запуск Flask-сервера
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"{WEBHOOK_URL}/{TOKEN}", allowed_updates=["message"])
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
