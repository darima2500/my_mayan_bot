wave_info = {
    "name": {
        "en": "Yellow Star Wave",
        "ru": "Волна Жёлтой Звезды"
    },
    "start_date": "2025-04-25",
    "end_date": "2025-05-07",
    "core_themes": {
        "en": [
            "Art",
            "Harmony",
            "Inner Light",
            "Beauty as a spiritual expression",
        ],
        "ru": [
            "Искусство",
            "Гармония",
            "Красота как духовное выражение",
            ]
    },
    "description": {
        "en": (
            "🌟 *Yellow Star Wave *\n"
            "This wave carries the energies of art, harmony, and inner radiance. "
            "It is connected to the planet Venus — the guide of beauty, maturity, creativity, and love. "
            "The wave invites you to explore your maturity, sense the natural beauty of life in every moment, "
            "and create in attunement with cosmic rhythms.\n\n"
            "*Wave Archetype:* The light carrying seeds of the future.\n"
            "*Wave Shadow:* Dependence on external validation, striving for unattainable perfection."
        ),
        "ru": (
            "🌟 *Волна Жёлтой Звезды *\n"
            "Эта волна несёт энергии искусства, гармонии и внутреннего сияния. "
            "Она связана с энергией планеты Венеры — покровительницы красоты, зрелости, творчества и любви. "
            "Волна приглашает исследовать свою зрелость, чувствовать естественную красоту жизни в каждом моменте "
            "и творить в сонастроенности с космическими ритмами.\n\n"
            "*Архетип Волны:* Свет, несущий семена будущего.\n"
            "*Тень Волны:* Зависимость от внешнего признания, стремление к недостижимому совершенству."
        )
    }
}  # ← добавил закрывающую скобку


def get_wave_message(lang):
    return wave_info["description"][lang]

