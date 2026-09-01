wave_info = {
    "name": {
        "en": "White Wind Wave. Ik",
        "ru": "Волна Белого Ветра. Ик"
    },
    "period": {
        "en": "September 1 — September 13, 2026",
        "ru": "1 Сентября — 13 Сентября 2026"
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
            "WHITE WIND" is the 2nd sign of the Maya calendar. Its keywords are Spirit, Breath, Communication, and Connections. Energy: Power of Spirit.\n\n"
            "The Wave of the White Wind will bring up topics of pure communication and the ability to build dialogue with one another, bringing more contact at the Spirit level into life.\n"
            "This is a time for catching on the fly many ideas that were put on the back burner, realizing creative impulses, and bringing into reality what previously seemed impossible. White Wind represents the masculine energy of Spirit, bringing your ideas to life with ease, and changes that may seem extremely fast. Watch your breath—it will help you learn to master your reality over these 13 days.Pay attention to your breathing. Over these 13 days, it will help you learn how to navigate and shape your reality more consciously.\n\n"
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



