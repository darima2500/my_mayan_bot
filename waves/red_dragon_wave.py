from datetime import date, datetime
from tones.tones_data import tones_data

wave_info = {
    "name": {
        "en": "Red Dragon Wave",
        "ru": "Волна Красного Дракона"
    },
    "start_date": "2025-05-08",
    "end_date": "2025-05-20",
    "description": {
        "en": (
            "🐉 *Red Dragon Wave (May 8 — May 20, 2025)*\n"
            "This wave carries energies of birth, initiating a new cycle, and returning to the primal source. "
            "The Red Dragon awakens your life force, replenishes your resources, and invites you to feel the world's support like a mother's care. "
            "It is a time to reconnect with your roots, feel your bond with Earth, and allow yourself to receive nourishment and care on all levels.\n\n"
            "*Wave Archetype:* The Great Mother, Source of Life.\n"
            "*Wave Shadow:* Feelings of abandonment, difficulty accepting support, fear of new beginnings."
        ),
        "ru": (
            "🐉 *Волна Красного Дракона (8 мая — 20 мая 2025)*\n"
            "Эта волна несёт энергии рождения, начала нового цикла и возвращения к первоисточнику. "
            "Красный Дракон пробуждает жизненную силу, наполняет ресурсами и приглашает почувствовать поддержку мира, словно заботу матери. "
            "Это время вспомнить о своих корнях, ощутить связь с Землёй и позволить себе принять заботу и питание на всех уровнях.\n\n"
            "*Архетип Волны:* Великая Мать, Источник Жизни.\n"
            "*Тень Волны:* Чувство покинутости, трудности с принятием поддержки, страх начала нового."
        )
    }
}

def get_wave_message(lang='en'):
    today = date.today()
    start_date = datetime.strptime(wave_info["start_date"], "%Y-%m-%d").date()
    end_date = datetime.strptime(wave_info["end_date"], "%Y-%m-%d").date()

    if start_date <= today <= end_date:
        day_number = (today - start_date).days + 1
        tone_info = tones_data[day_number][lang]

        return (
            f"🌞 *{'Сегодня' if lang == 'ru' else 'Today'}: Кин {day_number} — {tone_info['name']}*\n"
            f"*{tone_info['keywords']}*\n"
            f"{tone_info['description']}\n\n"
            f"{wave_info['description'][lang]}"
        )
    else:
        return None
