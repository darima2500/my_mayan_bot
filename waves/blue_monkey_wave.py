wave_info = {
    "name": {
        "en": "Blue Monkey Wave",
        "ru": "Волна Голубой Обезьяны"
    },
    "period": {
        "en": "September 15 — September 27, 2025",
        "ru": "15 сентября — 27 сентября 2025"
    },
    "core_themes": {
        "en": [
            "Playfulness and creativity",
            "Quantum field, illogical way of creation",
            "Art and creative thinking",
            "Inner child connection",
            "Shadow: Cynicism, ego-centeredness"
        ],
        "ru": [
            "Игра и творчество",
            "Квантовое, нелинейное поле реальности",
            "Искусство и креативное мышление",
            "Связь с внутренним ребёнком",
            "Тень: Цинизм, эгоцентризм"
        ]
    },
    "description": {
        "en": (
            "This energy is linked to creative thinking as a key to perceiving reality as a quantum field. It does not follow linear logic but flows through the play of possibilities.\n\n"
            "The Blue Monkey opens the ability to see every moment as a space of choice, where thought and intention themselves become acts of creation. Within this energy lives the Divine principle of play — a light, joyful impulse from which entire worlds are born. \n"
            "In its light, it brings flexibility of mind, the gift of creating new forms, weaving the unconnected, and perceiving more than what is given directly. It is the energy of generating new fields of reality — through the courage to think differently and the joy of discovery.\n\n"
            "At its deepest level, this energy shows that creation does not require heaviness or force. True mastery lives in lightness, in laughter, in trust in the flow. It is through this play that the divine nature of the human being as a Creator is revealed."
        ),
        "ru": (
            "Эта энергия связана с креативным мышлением, которое становится ключом к восприятию реальности как квантового поля. Здесь всё строится не на линейной логике, а на игре возможностей.n\n"
            "Синяя Обезьяна раскрывает способность видеть в каждом моменте пространство выбора, где сама мысль и намерение уже становятся актом творения. В этой энергии присутствует Божественный принцип игры — лёгкий, радостный импульс, из которого рождаются миры.\n"
            "В тени Синяя Обезьяна может проявляться как хаос, иллюзия, уход от сути в бесконечные игры или самообман. Здесь возникает соблазн подменить истинное творчество поверхностными забавами. Но именно эта тень учит различать: где игра ведёт к раскрытию, а где — к разобщению с собой.\n\n"
            "На глубинном уровне эта энергия показывает, что творение не требует тяжести усилия. Истинное мастерство — в лёгкости, искренности и доверии потоку. В этой игре и раскрывается божественная природа человека как Творца."
        ]
    },
    "archetype": {
        "en": "Wave Archetype: The Weaver of Joy, the Guardian of Play and Art.",
        "ru": "Архетип Волны: Хранитель Игры и Искусства."
    },
    "shadow": {
        "en": "Wave Shadow: Cynicism, ego-centeredness, losing the thread of trust and wonder.",
        "ru": "Тень Волны: Цинизм, эгоцентризм, потеря доверия и восхищения жизнью."
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


