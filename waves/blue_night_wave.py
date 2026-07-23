wave_info = {
    "name": {
        "en": "Blue Night Wave",
        "ru": "Волна Голубой Ночи"
    },
    "period": {
        "en": "July 24 — August 5, 2026",
        "ru": "24 Июля — 5 Августа 2026"
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
            "Интуиция",
            "Мечты как основа нового",
            "Доверие непроявленному",
            "Плодородная тьма",
            "Тень: Страх неопознанного, потеря связи с внутренним голосом"
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
            "Переход от внешнего к внутреннему. Это время, когда фокус внимания неизбежно смещается внутрь — от бесконечной суеты, людей и внешних задач к вашей личной тишине, мыслям и глубинным процессам.\n\n"
            "В традициях майя Ночь связана с темнотой, но не пугающей, а плодородной — как почва, в которой зреет семя. Изобилие здесь понимается не как случайный успех или удача, а как внутреннее богатство: ваши идеи, потенциал, видение и понимание того, чего вы на самом деле хотите.\n"
            "В такие периоды активизируется способность видеть то, что обычно скрыто за логикой и шумом повседневности — интуитивные озарения, знаки, сны, подсознательные страхи или неочевидные выходы из тупиков. \n\n"
            "Доверие мечтам и потенциалу. Период призывает опираться на свои мечты и скрытые возможности, позволяя себе заглянуть в собственные процессы без страха."
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




