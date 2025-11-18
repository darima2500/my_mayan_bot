wave_info = {
    "name": {
        "en": "Yellow Warrior Wave",
        "ru": "Волна Жёлтого Воина"
    },
    "period": {
        "en": "November 19 — December 1, 2025",
        "ru": "19 ноября — 1 декабря 2025"
    },
    "core_themes": {
        "en": [
            "Inner courage and authenticity",
            "Facing challenges",
            "Walking the path of truth",
            "Asking the deeper questions",
            "Shadow: Stubbornness, conflict for its own sake, fear of true inquiry"
        ],
        "ru": [
            "Внутренняя смелость и подлинность",
            "Прохождение испытаний с мудростью",
            "Следование путём истины",
            "Смелость задавать глубокие вопросы",
            "Тень: Упрямство, борьба ради борьбы, страх честного самоисследования"
        ]
    },
    "description": {
        "en": (
            "This wave calls you to walk the courageous path of truth.\n\n"
            "The Yellow Warrior teaches that true bravery lies not in outer battles, but in daring to live in full alignment with your soul.\n"
            "It is a time to confront fears, to question deeply, and to act with wisdom and heart.\n\n"
            "When courage and clarity meet, the soul's path reveals itself step by step."
        ),
        "ru": (
            "Эта волна призывает идти смелым путём истины.\n\n"
            "Жёлтый Воин учит, что истинная храбрость рождается не в сражениях снаружи, а в решимости жить в полном согласии с голосом своей души.\n"
            "Это время встретиться со страхами, задавать глубокие вопросы и действовать в согласии со своим внутренним голосом.\n\n"
            "Когда встречаются смелость и ясность, путь души начинает открываться шаг за шагом."
        )
    },
    "archetype": {
        "en": "Wave Archetype: Guardian of Truth, Courageous Seeker, Inner Strategist.",
        "ru": "Архетип Волны: Хранитель Истины, Смелый Искатель, Внутренний Стратег."
    },
    "shadow": {
        "en": "Wave Shadow: Stubborn resistance, fighting for the sake of conflict, avoiding deep truth.",
        "ru": "Тень Волны: Упрямое сопротивление, борьба ради борьбы, избегание глубинной истины."
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

