import telebot
from datetime import date, datetime, timedelta
from mayan_waves import waves  # Импортируем данные о волнах

# 🔐 Вставь сюда свой токен:
TOKEN = "8056299109:AAGalA54I7CoZ2mfR0FLtVohgAJ9zmmYEPc"

bot = telebot.TeleBot(TOKEN)

# Функция для создания клавиатуры с кнопками
def create_main_menu():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_today = telebot.types.KeyboardButton("/today")
    button_waves = telebot.types.KeyboardButton("/waves")
    button_mandala = telebot.types.KeyboardButton("/mandala")
    button_reflection = telebot.types.KeyboardButton("/reflection")
    button_help = telebot.types.KeyboardButton("/help")
    button_about = telebot.types.KeyboardButton("/about")
    
    # Добавляем кнопки на клавиатуру
    markup.add(button_today, button_waves, button_mandala, button_reflection, button_help, button_about)
    return markup

# 📅 Команда /today — покажет текущую волну по дате
@bot.message_handler(commands=['today'])
def send_today_wave(message):
    today_str = date.today().isoformat()
    for wave in waves:
        start_date = datetime.strptime(wave['start_date'], "%Y-%m-%d")
        end_date = start_date + timedelta(days=12)
        if start_date.date() <= date.today() <= end_date.date():
            text = f"🌊 *{wave['name']} Wave*\n\n{wave['description']}"
            bot.send_message(message.chat.id, text, parse_mode='Markdown')
            break
    else:
        bot.send_message(message.chat.id, "No wave found for today 😕")

# 🔁 Команда /start — приветствие с кнопками меню
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "✨ *Welcome to the Mayan Waves Bot!* ✨\n\n"
                     "In the Mayan calendar, each day flows within a *13-day wave* — a cycle of energy that invites reflection, creativity, rest, or action.\n\n"
                     "These waves aren’t about prediction. They’re about *resonance*. Each one offers a theme, a rhythm, a feeling — and you’re invited to tune in.\n\n"
                     "To discover today’s wave and its guidance, tap /today 🌊\n\n"
                     "_May you ride the wave with presence._",
                     parse_mode='Markdown', reply_markup=create_main_menu())

# 🚀 Запускаем бота
bot.polling()
