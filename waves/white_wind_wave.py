wave_info = {
    "name": {
        "en": "White Wind Wave",
        "ru": "Волна Белого Ветра"
    },
    "period": {
        "en": "December 15 — December 27, 2025",
        "ru": "15 декабря — 27 декабря 2025"
    },
    "core_themes": {
        "en": [
            "Spirit and breath",
            "Truthful communication",
            "Movement and change",
            "Integration of polarities",
            "Shadow: Outbursts of anger, loss of centeredness"
        ],
        "ru": [
            "Дух и дыхание",
            "Истинное общение",
            "Движение и перемены",
            "Интеграция противоположностей",
            "Тень: Вспышки гнева, потеря внутреннего центра"
        ]
    },
    "description": {
        "en": (
            "This wave invites you to become a vessel for Spirit — to speak, to move, and to breathe with clarity and truth.\n\n"
            "The White Wind teaches that true communication flows from an open and pure heart, carrying the essence of spirit into the world.\n"
            "It is a time to listen deeply, to express authentically, and to learn to connect with others from your true essence.\n\n"
            "When breath, word, and spirit align, life becomes a dance of pure connection."
        ),
        "ru": (
            "Эта волна приглашает стать сосудом для Духа — говорить, двигаться и дышать с ясностью и истиной.\n\n"
            "Белый Ветер учит, что подлинное общение рождается из открытого и чистого сердца, неся в мир суть духа.\n"
            "Это время глубоко слушать, искренне выражаться и учиться коммуницировать, оставаясь в своей аутентичности.\n\n"
            "Когда дыхание, слово и дух соединяются, жизнь становится чистым танцем индивидуальностей, осознающих свое единство."
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
