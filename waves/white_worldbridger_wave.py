wave_info = {
    "name": {
        "en": "White Worldbridger Wave",
        "ru": "Волна Белого Соединителя миров"
    },
    "period": {
        "en": "July 12 — July 24, 2025",
        "ru": "12 июля — 24 июля 2025"
    },
    "core_themes": {
        "en": [
            "Bridging worlds",
            "Ancestral wisdom",
            "Lunar connection between seen and unseen",
            "Inner death and rebirth",
            "Deep psychic perception, second sight",
            "Shadow: Emotional coldness, detachment"
        ],
        "ru": [
            "Переходы между мирами",
            "Лунная связь между видимым и невидимым",
            "Внутренние смерти и возрождения",
            "Глубокое Видение",
            "Тень: Эмоциональная холодность, отчуждённость"
        ]
    },
    "description": {
        "en": (
            "This wave carries the energies of surrender, transformation, and the sacred art of bridging worlds.\n\n"
            "The White Worldbridger invites you to release what no longer serves, to cross thresholds with grace, and to honor the cycles of death and rebirth within.\n"
            "It is a time to embrace the mystery of endings, to trust the unseen, and to allow deeper wisdom to emerge through letting go.\n\n"
            "The Worldbridger teaches: true passage is not about clinging, but about meeting change with an open and surrendered heart."
        ),
        "ru": (
            "Эта волна несёт энергии отпускания, трансформации и искусства вмещать в себя энергии будущего, находясь внутри перехода.\n\n"
            "Белый Соединитель Миров приглашает попрощаться с тем, что более не служит, научиться отпускать с благодарностью, почитать циклы смерти и возрождения внутри себя.\n"
            "Время по-настоящему довериться Духу и позволить глубокой мудрости проявиться через урок отпускания.\n\n"
            "Этот период учит: истинный переход происходит не через удержание, а через встречу перемен с открытым и смиренным сердцем."
        )
    },
    "archetype": {
        "en": "Wave Archetype: The Moonkeeper, the Shaman of Thresholds, the Silent Guide.",
        "ru": "Архетип Волны: Хранитель Луны, Шаман Порогов, Безмолвный Проводник."
    },
    "shadow": {
        "en": "Wave Shadow: Fear of loss, emotional detachment, resistance to surrendering to life's flow.",
        "ru": "Тень Волны: Страх потерь, эмоциональная холодность, сопротивление потоку жизни."
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
