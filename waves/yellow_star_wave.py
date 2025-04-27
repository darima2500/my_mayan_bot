from datetime import date, datetime
from tones.tones_data import tones_data

wave_info = {
    "name": {
        "en": "Yellow Star Wave",
        "ru": "Волна Жёлтой Звезды"
    },
    "start_date": "2025-04-25",
    "end_date": "2025-05-07",
    "description": {
        "en": (
            "🌟 *Yellow Star Wave (April 25 — May 7, 2025)*\n"
            "This wave carries the energies of art, harmony, and inner radiance. "
            "It is connected to the planet Venus — the guide of beauty, maturity, creativity, and love. "
            "The wave invites you to explore your maturity, sense the natural beauty of life in every moment, "
            "and create in attunement with cosmic rhythms.\n\n"
            "*Wave Archetype:* The light carrying seeds of the future.\n"
            "*Wave Shadow:* Dependence on external validation, striving for unattainable perfection."
        ),
        "ru": (
            "🌟 *Волна Жёлтой Звезды (25 апреля — 7 мая 2025)*\n"
            "Эта волна несёт энергии искусства, гармонии и внутреннего сияния. "
            "Она связана с энергией планеты Венеры — покровительницы красоты, зрелости, творчества и любви. "
            "Волна приглашает исследовать свою зрелость, чувствовать естественную красоту жизни в каждом моменте "
            "и творить в сонастроенности с космическими ритмами.\n\n"
            "*Архетип Волны:* Свет, несущий семена будущего.\n"
            "*Тень Волны:* Зависимость от внешнего признания, стремление к недостижимому совершенству."
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
