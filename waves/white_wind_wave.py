wave_info = {
    "name": {
        "en": "White Wind Wave. Ik",
        "ru": "Волна Белого Ветра. Ик"
    },
    "period": {
        "en": "December 15 — December 27, 2025",
        "ru": "15 декабря — 27 декабря 2025"
    },
    "core_themes": {
        "en": [
            "Spirit",
            "Clean communication",
            "Movement and change",
            "Respiratory system",
            "Shadow: Outbursts of anger, loss of centeredness"
        ],
        "ru": [
            "Дух",
            "Чистая коммуникация",
            "Движение и перемены",
            "Дыхательная система",
            "Тень: Вспышки гнева, потеря внутреннего центра"
        ]
    },
    "description": {
        "en": (
            "Wave of the White Wind will bring forward themes of clear communication and the ability to build true dialogue with one another, inviting more and more connection on the level of Spirit.\n\n"
            "This is a time to catch ideas on the fly — to return to impulses that were long postponed, to activate creative realizations, and to bring into reality what once seemed impossible. White Wind carries a masculine spiritual energy — the energy of expressing ideas with ease and moving through changes that may feel extremely fast.\n"
            "Pay attention to your breathing. Over these 13 days, it will help you learn how to navigate and shape your reality more consciously.\n\n"
        ),
        "ru": (
            "«БЕЛЫЙ ВЕТЕР» (ИК) – это 2-ой знак календаря майя, его ключевые слова: Дух. Дыхание. Коммуникации и связи. Энергия: Сила Духа.\n\n"
            "Волна Белого Ветра поднимет темы чистых коммуникаций, умения выстраивать диалог друг с другом, привнося в жизнь все больше контакта на уровне Духа.\n"
            "Это время схватывания на лету многих идей, которые откладывались в долгий ящик, реализаций творческих импульсов и проявления в реальность того, что раньше казалось невозможным.\n\n"
            "Белый ветер это мужская энергия Духа, реализации своих идей в легкости и перемен, которые могут показаться экстремально быстрыми. Следите за своим дыханием, оно поможет научиться управлять своей реальностью в эти 13 дней."
        )
    },
    "archetype": {
        "en": "Wave Archetype: Messenger of Spirit, Weaver of Words, Guardian of Sacred Breath.",
        "ru": "Архетип Волны: Посланник Духа, Ткач Слов, Хранитель Священного Дыхания."
    },
    "shadow": {
        "en": "Wave Shadow: Uncontrolled emotional outbursts, losing the center of clarity and peace.",
        "ru": "Тень Волны: Неконтролируемые эмоциональные всплески, потеря ясности и внутреннего покоя."
    }
}

def get_wave_message(lang):
    name = wave_info["name"][lang]
    period = wave_info["period"][lang]
    themes = wave_info["core_themes"][lang]
    description = wave_info["description"][lang]

    themes_intro = "Основные темы:" if lang == "ru" else "Core themes:"
    themes_text = "\n".join(f"• {theme}" for theme in themes)

    return (
        f"🌊 *{name}*\n"
        f"{period}\n\n"
        f"*{themes_intro}*\n"
        f"{themes_text}\n\n"
        f"{description}"
    )



