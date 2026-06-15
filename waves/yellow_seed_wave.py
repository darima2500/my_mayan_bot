wave_info = {
    "name": {
        "en": "Yellow Seed Wave",
        "ru": "Волна Жёлтого Семени"
    },
    "period": {
        "en": "June 15 — June 27, 2026",
        "ru": "15 Июня — 27 Июня 2026"
    },
    "core_themes": {
        "en": [
            "Growth and potential",
            "Conscious cultivation",
            "Building meaningful connections",
            "Ripening of inner gifts",
            "Shadow: Over-controlling others, impatience"
        ],
        "ru": [
            "Рост и потенциал",
            "Терпение",
            "Созидание",
            "Форма и материализация",
            "Тень: Чрезмерный контроль, нетерпение"
        ]
    },
    "description": {
        "en": (
            "We are entering a period where things begin to fall into place on their own. It is a time when your past efforts finally bear fruit, and everything starts to move without unnecessary pressure.\n\n"
            "The Over the next 13 days, it is important not to force the situation or scramble where the process is already underway. Just do what is necessary and let events take their course. True results now come not from pushing hard, but from creating the conditions where everything unfolds naturally and on time.\n"
            "Stay grounded in what you have already started and allow your projects to simply mature.\n\n"
            "This is a period of materialization: every step must be concrete, and the work must be methodical. This is not a time for abstractions; it is a time for creation, where through persistence and attention, your intentions gain structure and substance."
        ),
        "ru": (
            "Сейчас идет период, когда дела начинают складываться сами собой. Это время, когда твои прошлые усилия наконец-то дают всходы, и всё начинает работать без лишнего давления.\n\n"
            "В ближайшие 13 дней важно не пытаться «подгонять» ситуацию и не суетиться там, где процесс уже пошел. Просто делай то, что нужно, и дай событиям идти своим чередом. Истинный результат сейчас дает не избыток сил, вложенных в «проталкивание» дела, а создание условий, в которых всё раскрывается естественно и вовремя.\n"
            "Укрепись в том, что ты уже начала, и дай своим проектам просто созреть.\n\n"
            "Это период материализации: когда каждый шаг должен быть конкретным, а работа — методичной. Сейчас не время для абстракций, сейчас время для созидания, где через упорство и внимательность задуманное обретает структуру и вес."
        )
    },
    "archetype": {
        "en": "Wave Archetype: The Gardener of Potential, the Weaver of Networks.",
        "ru": "Архетип Волны: Садовник Потенциала, Ткач Связей."
    },
    "shadow": {
        "en": "Wave Shadow: Over-controlling others' growth, impatience with the natural unfolding.",
        "ru": "Тень Волны: Чрезмерное руководство чужим ростом, нетерпение к естественному процессу."
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

