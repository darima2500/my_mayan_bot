wave_info = {
    "name": {
        "en": "Yellow Man Wave",
        "ru": "Волна Жёлтого Человека"
    },
    "period": {
        "en": "April 24 — May 6, 2026",
        "ru": "24 Апреля — 6 Мая 2026"
    },
    "core_themes": {
        "en": [
            "Free will and soul path",
            "Sacred human potential",
            "Guidance and service",
            "Ability to create your own reality",
            "Shadow: Loneliness, impatience"
        ],
        "ru": [
            "Свободная воля",
            "Высший потенциал человечества",
            "Наставничество и служение",
            "Умение созидать свою реальность",
            "Тень: Одиночество, ригидность, потеря доверия к собственному пути"
        ]
    },
    "description": {
        "en": (
            "This wave carries the energies of free will, soul path, and sacred human potential.\n\n"
            "The Yellow Man teaches us to walk through life with dignity - realizing the power of our ability to create this reality by making our choices every day.\n"
            "This is a time of alignment with the deepest intention of your soul, and subsequently the ability to live and make choices based on this state of uncompromising integrity of the Body, Soul and Spirit.\n\n"
            "The yellow man is the archetype of the highest level of awareness, as well as the ability to interact with the system."
        ),
        "ru": (
            "Эта волна несёт энергии свободной воли, созидания своей реальности и раскрытия истинного потенциала человека.\n\n"
            "Жёлтый Человек учит идти по жизни с достоинством — осознавая силу своего умения созидать эту реальность, делая свои выборы каждый день.\n"
            "Это время согласования с глубочайшим намерением своей души, и впоследствии умение жить и делать выборы, исходя из этого состояния бескомпромиссной целостности Тела Души и Духа.\n\n"
            "Желтый человек это архетип наивысшего уровня осознанности, и в следствии этого следующим этапом является его умение создавать системы и взаимодействовать с ними."
        )
    },
    "archetype": {
        "en": "Wave Archetype: The Guardian of Life's Path, the Silent Servant of Growth.",
        "ru": "Архетип Волны: Хранитель Пути Жизни, Безмолвный Служитель Роста."
    },
    "shadow": {
        "en": "Wave Shadow: Loneliness, impatience, losing trust in one's own unfolding.",
        "ru": "Тень Волны: Одиночество, нетерпение, потеря доверия к собственному пути."
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

