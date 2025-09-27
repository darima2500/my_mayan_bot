wave_info = {
    "name": {
        "en": "Yellow Seed Wave",
        "ru": "Волна Жёлтого Семени"
    },
    "period": {
        "en": "September 28 — October 10, 2025",
        "ru": "28 сентября — 10 октября 2025"
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
            "Осознанное взращивание",
            "Создание значимых связей",
            "Созревание внутренних даров",
            "Тень: Чрезмерное руководство, нетерпение"
        ]
    },
    "description": {
        "en": (
            "This wave carries the energies of growth, potential, and conscious cultivation.\n\n"
            "The Yellow Seed invites you to plant yourself where you can thrive — to nourish your dreams patiently and to trust the natural pace of growth.\n"
            "It is a time to strengthen your roots, build meaningful connections, and allow your unique gifts to ripen.\n\n"
            "The Seed reminds: true flourishing happens not by forcing, but by creating the right conditions for life to unfold."
        ),
        "ru": (
            "Эта волна несёт энергии роста, потенциала и сонастроенности с естественным темпом вещей и событий вокруг.\n\n"
            "Жёлтое Семя приглашает укорениться там, где ты можешь процветать — питать свои мечты с терпением и доверять естественному развитию.\n"
            "Это время укреплять свои корни, строить значимые связи и позволять своим дарам созревать.\n\n"
            "Семя напоминает: настоящее процветание рождается не через искусственное усилие, а через создание условий для естественного раскрытия жизни."
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

