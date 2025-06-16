wave_info = {
    "name": {
        "en": "Yellow Sun Wave",
        "ru": "Волна Жёлтого Солнца"
    },
    "period": {
        "en": "June 16 — June 28, 2025",
        "ru": "16 июня — 28 июня 2025"
    },

"core_themes": {
    "en": [
        "Enlightenment",
        "Unconditional Love",
        "Connection with Source and Ancestors",
        "Living as radiant authenticity",
        "Sacred play and beauty",
        "Shadow: Arrogance, rejection of feedback"
    ],
    "ru": [
        "Просветление",
        "Безусловная Любовь",
        "Связь с Истоком и Предками",
        "Проявление своей аутентичности",
        "Божественная игра",
        "Тень: Гордыня, отказ воспринимать обратную связь"
    ]
},


    "description": {
        "en": (
            "This wave carries the energies of enlightenment, unconditional love, divine play, and deep connection with the Source and the Ancestors.\n\n"
            "The Yellow Sun invites you to remember the radiant spark within you — the sacred light that connects you to all life.\n"
            "It is a time to celebrate your wholeness, to embody love without conditions, and to weave beauty, poetry, and joy into existence.\n\n"
            "The Sun teaches: sometimes it is neccessary to face your darkness and bring it into a light to fully embrace the wholeness of life."
        ),
        "ru": (
            "Эта волна включает мощные энергии Света, любви, не обусловленной детерминизмом, божественной игры и глубинной связи с Истоком и Предками.\n\n"
            "Жёлтое Солнце открывает пространство полной сдачи и доверия, предлагает вспомнить сияющую искру внутри — священный свет, который соединяет тебя со всей жизнью.\n"
            "Это время празднования целостности, воплощения любви без условий и сотворения красоты, поэзии и радости, через соединение со своим внутренним ребенком.\n\n"
            "Солнце учит: истинное просветление — это объем энергии жизни, объединяющий земное и небесное."
        )
    },
    "archetype": {
        "en": "Wave Archetype: The Sovereign Light, the Tree of Life, the Singer of Beauty.",
        "ru": "Архетип Волны: Суверенный Свет, Древо Жизни, Певец Красоты."
    },
    "shadow": {
        "en": "Wave Shadow: Arrogance, rejection of feedback, forgetting the sacred flow that nurtures all beings.",
        "ru": "Тень Волны: Гордыня, отказ воспринимать обратную связь, забвение священного потока, питающего всё сущее."
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
