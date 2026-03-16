# Описание волны Красного Небесного Странника
wave_info = {
    "name": {
        "en": "Red Skywalker Wave",
        "ru": "Волна Красного Небесного Странника"
    },
    "period": {
        "en": "March 16 — March 28, 2026",
        "ru": "16 марта — 28 марта 2026"
    },
    "core_themes": {
        "en": [
            "Avangard",
            "Travel",
            "Vision",
            "Bridging Heaven and Earth",
            "Cosmic connection",
            "Inner expansion through rootedness",
            "Shadow: Restlessness, loss of grounding"
        ],
        "ru": [
            "Авангард",
            "Путешествия",
            "Видение",
            "Космос",
            "Потребность в экспансии",
            "Интерес к постоянному расширению",
            "Тень: Непостоянство, потеря связи с землей."
        ]
    },
    "description": {
        "en": (
            "This wave carries the energies of exploration, connection, and spiritual guidance.\n\n"
            "The Red Skywalker invites you to walk as a bridge between worlds — to root deeply into the Earth while reaching for the infinite sky.\n"
            "It is a time to plant seeds of vision, to nurture family and community, and to serve as a living pillar connecting heaven and earth.\n\n"
            "The Skywalker teaches: true expansion begins with inner stability — with the courage to open, while remaining grounded in essence."
        ),
        "ru": (
            "Эта волна несёт энергии исследователя в широком понимании, расширения горизонтов познания реальности, исследования пути, по которому еще никто не ходил.\n\n"
            "Красный Небесный Странник приглашает идти как мост между мирами — как на тонком уровне, так и в материи: выход в расширение может случиться через путешествия на новые земли, так и через внутреннюю работу, но важно оставаться ориентированным на новые пути.\n"
            "Это время исследовать, экспериментировать, не бояться быть белой вороной и быть первопроходцем.\n\n"
            "Небесный Странник учит: истинное расширение начинается с внутренней устойчивости — с мужества открываться, оставаясь укоренённым в своей сути."
        )
    },
    "archetype": {
        "en": "Wave Archetype: The World Tree, the Keeper of Home and Spirit.",
        "ru": "Архетип Волны: Древо Жизни, Хранитель Дома и Духа."
    },
    "shadow": {
        "en": "Wave Shadow: Restlessness, inconsistency, losing connection with roots while chasing the stars.",
        "ru": "Тень Волны: Непостоянство, неустойчивость, потеря связи с корнями в стремлении к звёздам."
    }
}

# Правильное определение функции на новой строке
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
