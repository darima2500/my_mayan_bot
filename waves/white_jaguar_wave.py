wave_info = {
    "name": {
        "en": "White Jaguar Wave",
        "ru": "Волна Белого Ягуара"
    },
    "period": {
        "en": "February 05 — February 17, 2026",
        "ru": "05 Февраля — 17 Февраля 2026"
    },
"core_themes": {
    "en": [
        "Intuition",
        "Purity",
        "Inner Alignment",
        "Spiritual healing",
        "Astral journeys",
        "Sacred power and wisdom of Earth",
        "Walking between worlds",
        "Shadow: Illusions, distrust of inner knowing"
    ],
    "ru": [
        "Интуиция",
        "Чистота",
        "Внутренняя Сонастройка",
        "Духовное исцеление",
        "Астральные путешествия",
        "Священная сила и мудрость Земли",
        "Путь между мирами",
        "Тень: Иллюзии, недоверие внутреннему знанию"
    ]
},



    "description": {
        "en": (
            "This wave carries the energies of intuition, sacred power, and deep connection with the Earth.\n\n"
            "The White Jaguar invites you to walk between worlds — to listen to the silent teachings of nature, to heal distortions within, and to reclaim the pure force of life.\n\n"
            "It is a time to awaken your inner Seer and Healer, to walk with grace and reverence for all living beings.\n"
            "Yet it also asks for humility — for great power without heart may turn into illusion or misuse."
        ),
        "ru": (
            "Эта волна несёт энергии интуиции, священной силы и глубокой связи с Землёй.\n\n"
            "Белый Ягуар приглашает идти между мирами — слушать безмолвные наставления природы, исцелять внутренние искажения и пробуждать чистую силу жизни внутри себя.\n\n"
            "Это время пробуждения внутреннего Провидца и Целителя, путь через уважение ко всему живому.\n"
            "Но также оно напоминает о смирении: великая сила без сердца может превратиться в иллюзию или злоупотребление."
        )
    },
    "archetype": {
        "en": "Wave Archetype: The Seer and Shaman, guardian of the sacred Earth.",
        "ru": "Архетип Волны: Провидец и Шаман, хранитель священной Земли."
    },
    "shadow": {
        "en": "Wave Shadow: Misuse of power, losing the way in illusions, disconnection from true integrity.",
        "ru": "Тень Волны: Злоупотребление силой, потеря истинности, запутанность в иллюзиях."
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

