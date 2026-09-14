wave_info = {
    "name": {
        "en": "Blue Eagle Wave",
        "ru": "Волна Голубого Орла"
    },
    "period": {
        "en": "September 14 2026 — September 26, 2026",
        "ru": "14 Сентября 2026 — 26 Сентября 2026"
    },
    "core_themes": {
        "en": [
            "Vision and higher perspective",
            "Spiritual clarity",
            "Collective consciousness and cooperation",
            "Manifestation through seeing the whole",
            "Shadow: Savior complex, over-involvement in others' paths"
        ],
        "ru": [
            "Видение и расширение перспективы",
            "Духовная ясность",
            "Коллективное сознание и сотрудничество",
            "Проявление через целостное восприятие",
            "Тень: Синдром спасателя, чрезмерное вмешательство в чужие пути"
        ]
    },
    "description": {
        "en": (
            "This wave invites you to step slightly back from everyday bustle and look at what is happening from a wider perspective — not from tension or control, but from a state of inner clarity. When you stop getting stuck in details, it becomes easier to see what truly matters right now and what merely consumes your attention.\n\n"
            "The Blue Eagle teaches that true success and healing come from understanding the bigger picture and acting from this perspective.\n"
            "It is a time to align with collective dreams, to support without rescuing, and to let your sight guide your service.\n\n"
            "When you hold this inner perspective, everyday tasks no longer feel like obstacles. They naturally integrate into a wider path and stop slowing you down, because you understand why you take each step and what you are moving toward."
        ),
        "ru": (
            "Эта волна предлагает немного отступить назад от повседневной суеты и посмотреть на происходящее шире — не из точки напряжения и контроля, а из состояния внутренней ясности. Когда ты перестаёшь застревать в деталях, становится видно, что именно сейчас действительно важно, а что лишь забирает внимание.\n\n"
            "Голубой Орёл учит, что настоящий успех и исцеление приходят через понимание целостной картины и действий, исходящих из этого понимания.\n"
            "Это время настроиться на коллективные мечты, поддерживать, не спасая, и позволить своему видению направлять тебя.\n\n"
            "Когда у тебя есть эта внутренняя перспектива, повседневные задачи перестают выглядеть как препятствия. Они просто встраиваются в более широкий путь и больше не замедляют движение, потому что ты понимаешь, зачем и ради чего делаешь каждый шаг."
        )
    },
    "archetype": {
        "en": "Wave Archetype: Visionary Messenger, Guardian of Higher Consciousness, Weaver of Collective Dreams.",
        "ru": "Архетип Волны: Посланник Видения, Хранитель Высшего Сознания, Ткач Коллективных Мечт."
    },
    "shadow": {
        "en": "Wave Shadow: Getting trapped in the savior complex, losing healthy boundaries in helping others.",
        "ru": "Тень Волны: Погружение в синдром спасателя, потеря здоровых границ при помощи другим."
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


