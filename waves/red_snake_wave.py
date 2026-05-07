wave_info = {
    "name": {
        "en": "Red Snake Wave",
        "ru": "Волна Красной Змеи"
    },
    "period": {
        "en": "May 7 — May 19, 2026",
        "ru": "7 Мая — 19 Мая 2026"
    },
    "core_themes": {
        "en": [
            "Life force and vitality",
            "Body wisdom and instincts",
            "Kundalini activation",
            "Grounding in physical being",
            "Shadow: Over-identification with the body"
        ],
        "ru": [
            "Жизненная сила и энергия",
            "Мудрость тела и инстинкты",
            "Активация энергии Кундалини",
            "Укрепление в материальном",
            "Тень: Чрезмерная фиксация на теле"
        ]
    },
    "description": {
        "en": (
            "These 13 days under the Red Serpent invite us to see life through the lens of the body, to expand through deep trust in our instincts. It’s a time to reconnect with raw, primal wisdom—the signals that pulse through every breath and movement.\n\n"
            "The Red Serpent symbolizes transformation, life force (kundalini), and rebirth. Like a snake shedding its skin, we too can release what no longer serves us.\n"
            "The Serpent is also the kundalini fire coiled at the spine’s base. Its ascent represents enlightenment through embodiment—we cannot rise spiritually without grounding in our animal nature.\n\n"
            "The Snake reminds: Feel what’s truly alive—follow impulses without judgment, Trust the body—it knows when to rest and when to act, Embrace instincts—not as chaos, but as ancient wisdom."
        ),
        "ru": (
            "Эти 13 дней под знаком Красной Змеи дарят нам уникальную возможность — взглянуть на жизнь через призму тела, ощутить подлинное расширение через доверие к своим ощущениям.\n\n"
            "Красная Змея — это символ трансформации, инстинкта и пробуждённой жизненной силы (кундалини). Во многих традициях змей считается священным существом, воплощающим циклы смерти и возрождения. Подобно тому, как змея сбрасывает кожу, мы тоже можем отпустить всё отжившее, чтобы освободить место для нового. Но истинное перерождение возможно только через глубокую сдачу смерти как части жизни.\n"
            "Змей — это не только символ физического обновления, но и проводник энергии кундалини, спящей у основания позвоночника. Его путь вверх, к коронной чакре, символизирует просветление, достижимое только через полное воплощение. Мы не можем вознестись духом, не пройдя через земное, не приняв свою животную природу.\n\n"
            "Уроком этого периода будет: Чувствовать то, что действительно живо — не игнорировать импульсы, а следовать им, Доверять телу — оно знает, когда нужно замедлиться, а когда — действовать."
        )
    },
    "archetype": {
        "en": "Wave Archetype: The Guardian of Life Force.",
        "ru": "Архетип Волны: Хранитель Жизненной Силы."
    },
    "shadow": {
        "en": "Wave Shadow: Over-identification with the body, losing the connection to inner spirit.",
        "ru": "Тень Волны: Чрезмерная фиксация на теле, потеря связи с внутренней сутью."
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

