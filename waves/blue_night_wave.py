wave_info = {
    "name": {
        "en": "Blue Night Wave",
        "ru": "Волна Голубой Ночи"
    },
    "period": {
        "en": "November 6 — November 18, 2025",
        "ru": "6 ноября — 18 ноября 2025"
    },
    "core_themes": {
        "en": [
            "Intuition and inner richness",
            "Dreaming the new into being",
            "Trusting the unseen",
            "Cultivating inner abundance",
            "Shadow: Fear of abundance, disconnection from inner truth"
        ],
        "ru": [
            "Интуиция и внутреннее богатство",
            "Мечты как основа нового",
            "Доверие невидимому",
            "Взращивание внутреннего изобилия",
            "Тень: Страх изобилия, потеря связи с внутренней правдой"
        ]
    },
    "description": {
        "en": (
            "This wave invites you into the fertile darkness of dreams — the deep well of intuition and unseen potentials.\n\n"
            "The Blue Night teaches that true abundance begins within, in the realms where imagination weaves reality.\n"
            "It is a time to rest, to trust the invisible currents, and to dream boldly without fear.\n\n"
            "When you honor your inner richness, new worlds begin to form around you."
        ),
        "ru": (
            "Эта волна приглашает войти в плодородную тьму сновидений — в глубокие источники интуиции и скрытых потенциалов.\n\n"
            "Голубая Ночь учит, что истинное изобилие рождается внутри, там, где воображение начинает ткать реальность.\n"
            "Это время отдыха, доверия невидимым течениям и смелых мечтаний без страха.\n\n"
            "Когда ты почитаешь своё внутреннее богатство, вокруг тебя начинают рождаться новые миры."
        )
    },
    "archetype": {
        "en": "Wave Archetype: Dreamweaver, Keeper of Inner Treasures, Guardian of Abundance.",
        "ru": "Архетип Волны: Ткач Сновидений, Хранитель Внутренних Сокровищ, Страж Изобилия."
    },
    "shadow": {
        "en": "Wave Shadow: Fear of receiving abundance, loss of inner connection, entrapment in illusions.",
        "ru": "Тень Волны: Страх принять изобилие, потеря внутренней связи, запутанность в иллюзиях."
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




