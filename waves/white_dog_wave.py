wave_info = {
    "name": {
        "en": "White Dog Wave",
        "ru": "Волна Белой Собаки"
    },
    "period": {
        "en": "July 11 — July 23, 2026",
        "ru": "11 Июля — 23 Июля 2026"
    },
    "core_themes": {
        "en": [
            "Loyalty and heart-centered relationships",
            "Commitment to truth and justice",
            "Protection and guidance",
            "Living with integrity",
            "Shadow: Overindulgence in passions, emotional dependency"
        ],
        "ru": [
            "Верность и сердечные отношения",
            "Преданность истине и справедливости",
            "Защита и проводничество",
            "Жизнь в целостности и честности",
            "Тень: Погружение в страсти, эмоциональная зависимость"
        ]
    },
    "description": {
        "en": (
            "This wave calls you back to the heart center — to loyalty, authenticity, and true connection.\n\n"
            "During these 13 days, the space reminds us that love is born in contact, intimacy, and in being true to one's soul.\n"
            "It's time to reconsider your thoughts and ideas about relationships, friendship, and attachment. What is true there, and where it's time to let go of your fears and emerge from isolation. \n\n"
            "When loyalty is rooted in the heart, it becomes a guiding light through all transformations."
        ),
        "ru": (
            "Эта волна возвращает к сердцу — к верности, подлинности и контакту в своей правде.\n\n"
            "В эти 13 дней пространство напоминает нам, что любовь рождается в контакте, в близости и в верности своей душе.\n"
            "Время пересмотреть свои мысли и идеи, касающиеся отношений, дружбы и привязанности. Что там истинно, а где пора уже отпустить свои страхи и выйти из изоляции.\n\n"
            "Когда верность укоренена внутри, она становится путеводным светом сквозь любые внешние трансформации и проверки."
        )
    },
    "archetype": {
        "en": "Wave Archetype: Guardian of Sacred Bonds, Keeper of Justice, Heart-Centered Guide.",
        "ru": "Архетип Волны: Хранитель Священных Уз, Хранитель Справедливости, Проводник Сердца."
    },
    "shadow": {
        "en": "Wave Shadow: Overindulgence in desires, emotional entanglements, losing the path of integrity.",
        "ru": "Тень Волны: Погружение в страсти, эмоциональные запутанности, потеря пути целостности."
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

