wave_info = {
    "name": {
        "en": "Blue Storm Wave",
        "ru": "Волна Синей Бури"
    },
    "period": {
        "en": "April 11 — April 23, 2026",
        "ru": "11 апреля — 23 апреля 2026"
    },
    "core_themes": {
        "en": [
            "Radical transformation",
            "Purification through storm and fire",
            "Emotional catharsis",
            "Healing of body and mind",
            "Rebirth through surrender",
            "Shadow: Chaos, emotional overwhelm"
        ],
        "ru": [
            "Радикальная трансформация",
            "Очищение через шторм или огонь",
            "Эмоциональный катарсис",
            "Время Перемен",
            "Перерождение",
            "Тень: Хаос, эмоциональное перенасыщение, страх перед неизбежной трансформацией."
        ]
    },
    "description": {
        "en": (
            "This wave carries the energies of transformation, purification, and the fierce power of rebirth.\n\n"
            "The Blue Storm invites you to surrender to the forces of change — to allow old structures to dissolve, so that a new clarity and vitality can emerge.\n"
            "It is a time of intense cleansing, emotional catharsis, and deep realignment with your authentic self.\n\n"
            "The Storm teaches: true purification is not destruction for its own sake, but the sacred fire that clears the path for new life to grow."
        ),
        "ru": (
            "Эта волна несёт энергии трансформации, очищения, перерождения, сейчас не время держаться за старое.\n\n"
            "Синий Шторм дает возможность сдаться силам перемен — позволить старым структурам раствориться полностью, чтобы на их месте родилось Новое.\n"
            "Это время интенсивной чистки, эмоционального катарсиса и глубокой перенастройки с истинной своей природой.\n\n"
            "Уроком этого периода будет переосмысление понятия очищения, когда это не разрушение ради разрушения, а огонь правды, который освобождает путь для новой жизни."
        )
    },
    "archetype": {
        "en": "Wave Archetype: The Initiator, Keeper of the Lightning and Primordial Forces.",
        "ru": "Архетип Волны: Инициатор, Хранитель Молнии и Первозданных Сил."
    },
    "shadow": {
        "en": "Wave Shadow: Chaos without grounding, emotional overwhelm, fear of surrendering to necessary transformation.",
        "ru": "Тень Волны: Хаос без заземления, эмоциональное перенасыщение, страх перед неизбежной трансформацией."
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
