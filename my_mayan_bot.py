# bot.py

import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from datetime import date, datetime
from waves_data import waves
from language_store import get_language, set_language

TOKEN = "8056299109:AAGalA54I7CoZ2mfR0FLtVohgAJ9zmmYEPc"
bot = telebot.TeleBot(TOKEN)

menu_buttons = {
    "en": ["\ud83d\udcc5 Today's Wave", "\ud83c\udfb4 Reflect", "\ud83d\udcd3 About the Project", "\u2728 About the Calendar"],
    "ru": ["\ud83d\udcc5 \u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0412\u043e\u043b\u043d\u0430", "\ud83c\udfb4 \u0420\u0435\u0444\u043b\u0435\u043a\u0441\u0438\u044f", "\ud83d\udcd3 \u041e \u043f\u0440\u043e\u0435\u043a\u0442\u0435", "\u2728 \u041e \u041a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u0435"]
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    lang_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    lang_keyboard.add(KeyboardButton("\ud83c\uddec\ud83c\udde7 English"), KeyboardButton("\ud83c\uddf7\ud83c\uddfa \u0420\u0443\u0441\u0441\u043a\u0438\u0439"))
    bot.send_message(message.chat.id, "Choose your language / \u0412\u044b\u0431\u0435\u0440\u0438 \u044f\u0437\u044b\u043a:", reply_markup=lang_keyboard)

@bot.message_handler(func=lambda message: message.text in ["\ud83c\uddec\ud83c\udde7 English", "\ud83c\uddf7\ud83c\uddfa \u0420\u0443\u0441\u0441\u043a\u0438\u0439"])
def set_user_language(message):
    lang = "en" if message.text == "\ud83c\uddec\ud83c\udde7 English" else "ru"
    set_language(message.chat.id, lang)
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for button in menu_buttons[lang]:
        markup.add(KeyboardButton(button))
    welcome_text = "Welcome! Choose an option below:" if lang == "en" else "\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c! \u0412\u044b\u0431\u0435\u0440\u0438 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435 \u043d\u0438\u0436\u0435:"
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)


def find_current_wave(today):
    for wave in waves:
        start = datetime.strptime(wave["start_date"], "%Y-%m-%d").date()
        end = datetime.strptime(wave["end_date"], "%Y-%m-%d").date()
        if start <= today <= end:
            return wave, (today - start).days
    return None, None

@bot.message_handler(func=lambda message: message.text in ["\ud83d\udcc5 Today's Wave", "\ud83d\udcc5 \u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0412\u043e\u043b\u043d\u0430"])
def send_today_wave(message):
    lang = get_language(message.chat.id)
    today = date.today()
    wave, delta = find_current_wave(today)

    if wave and 0 <= delta < len(wave["messages"]):
        msg = wave["messages"][delta]
        tone = msg['tone'][lang]
        archetype = msg['archetype'][lang]
        text = msg['text'][lang]

        response = (
            f"\ud83c\udf1e *Today: Kin {delta + 1} — {tone}*\n\n"
            f"\ud83c\udf1f *{wave['name'][lang]}* ({wave['period'][lang]})\n"
            f"{wave['description'][lang]}\n\n"
            f"{wave['archetype'][lang]}\n"
            f"{wave['shadow'][lang]}\n\n"
            f"\ud83d\uddd3\ufe0f *Day {delta + 1}*\n"
            f"\ud83c\udf1f *Archetype:* {archetype}\n\n"
            f"{text}\n\n"
            f"Today is a day of returning to the source of your inner light." if lang == "en" else "Сегодня — день возвращения к источнику своего света."
        )
        bot.send_message(message.chat.id, response, parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "No wave info for today." if lang == "en" else "\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0432\u043e\u043b\u043d\u0435 \u043d\u0430 \u0441\u0435\u0433\u043e\u0434\u043d\u044f \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u0430.")

@bot.message_handler(func=lambda message: message.text in ["\ud83d\udcd3 About the Project", "\ud83d\udcd3 \u041e \u043f\u0440\u043e\u0435\u043a\u0442\u0435"])
def about_project(message):
    lang = get_language(message.chat.id)
    text = (
        "Time is a living flow, not a linear path.\n\n"
        "This bot was created as a space for connecting with the ancient wisdom of the Mayan calendar.\n"
        "Here, there are no predictions or instructions — only subtle hints from the energies of the day, helping you attune to yourself and the cosmic rhythms.\n\n"
        "This project was born from the desire to remind: each day carries a unique vibration. Through the Mayan calendar, we can feel the flow of time differently — like music, where you become both the listener and the creator.\n\n"
        "May these energies help you remember yourself, your true nature, and the beauty of Life's unfolding."
        if lang == "en" else
        "\u0412\u0440\u0435\u043c\u044f — это живой поток, а не линейная дорога.\n\n"
        "\u042dтот бот создан как пространство соприкосновения с древней мудростью майянского календаря.\n"
        "\u0417десь нет предсказаний и инструкций — только подсказки энергий дня, которые помогают \u0441\u043e\u043d\u0430\u0441\u0442рои\u0442\u044c\u0441\u044f \u0441 собой и \u0441 \u044dн\u0435р\u0433и\u044f\u043cи \u043aосмическ\u043eго п\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0441\u0442\u0432а.\n\n"
        "\u042dтот пр\u043e\u0435к\u0442 р\u043e\u0434\u0438\u043b\u0441\u044f \u0438\u0437 \u0441\u0442\u0440\u0435\u043c\u043b\u0435\u043d\u0438\u044f \u043d\u0430п\u043eм\u043d\u0438\u0442\u044c: \u043a\u0430\u0436\u0434\u044b\u0439 \u0434\u0435\u043d\u044c зв\u0443\u0447\u0438т \u043e\u0441\u043e\u0431о\u0439 \u0432\u0438\u0431\u0440\u0430\u0446\u0438\u0435\u0439. \u0427\u0435\u0440\u0435\u0437 \u043c\u0430\u0439\u044fн\u0441\u043a\u0438\u0439 \u043a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c м\u044b \u043c\u043e\u0436\u0435м \u043f\u043e\u0447\u0443\u0432\u0441\u0442\u0432\u043e\u0432\u0430\u0442\u044c \u0442\u0435\u0447\u0435\u043d\u0438\u0435 \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u043f\u043e-\u043d\u043e\u0432\u043e\u043c\u0443 — \u043a\u0430\u043a \u043c\u0443\u0437\u044b\u043a\u0443, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0442\u044b \u0441\u0430\u043c \u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0448\u044c\u0441\u044f \u0438 \u0441\u043b\u0443\u0448\u0430\u0442\u0435\u043b\u0435\u043c, \u0438 \u0442\u0432\u043e\u0440\u0446\u043e\u043c.\n\n"
        "\u041f\u0443\u0441\u0442\u044c \u044d\u0442\u0438 \u044d\u043d\u0435\u0440\u0433\u0438\u0438 \u043f\u043e\u043c\u043e\u0433\u0430\u044e\u0442 \u0442\u0435\u0431\u0435 \u0432\u0441\u043f\u043e\u043c\u043d\u0438\u0442\u044c \u043e \u0441\u0435\u0431\u0435, \u043e \u0441\u0432\u043e\u0435\u0439 \u0438\u0441\u0442\u0438\u043d\u043d\u043e\u0439 \u043f\u0440\u0438\u0440\u043e\u0434\u0435 \u0438 \u043e \u043a\u0440\u0430\u0441\u043e\u0442\u0435 \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044f \u0416\u0438\u0437\u043d\u0438."
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

bot.polling()
