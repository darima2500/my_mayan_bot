wave_info = {
    "name": {
        "en": "Red Moon Wave",
        "ru": "Волна Красной Луны"
    },
    "period": {
        "en": "December 2 — December 14, 2025",
        "ru": "2 декабря — 14 декабря 2025"
    },
    "core_themes": {
        "en": [
            "Emotional cleansing and flow",
            "Remembering true essence",
            "Balance between giving and receiving",
            "Trusting inner feelings",
            "Shadow: Self-pity, emotional overwhelm"
        ],
        "ru": [
            "Эмоциональное очищение и поток",
            "Воспоминание о своей истинной природе",
            "Баланс между отдачей и принятием",
            "Доверие своим чувствам",
            "Тень: Жалость к себе, эмоциональная перегруженность"
        ]
    },
    "description": {
        "en": (
            "This wave invites you to surrender to the flow — to cleanse, to feel, and to remember who you truly are.\n\n"
            "The Red Moon teaches that true strength lies in allowing emotions to move freely, without resistance.\n"
            "It is a time to trust the inner waters, to balance giving and receiving, and to honor the tides within.\n\n"
            "When you align with the sacred current of life, healing and clarity naturally unfold."
        ),
        "ru": (
            "Эта волна приглашает сдаться потоку — очиститься, прочувствовать и вспомнить свою истинную природу.\n\n"
            "Красная Луна учит сдаваться чувствам без сопротивления, облегчая тем самым свое тело на многих уровнях.\n"
            "Это время доверять течениям и каналам Инь и Ян, находить баланс между отдачей и принятием.\n\n"
            "В этот период особенно важно слышать свою интуицию, если не пропустить ее голос, исцеление и ясность придут естественным образом."
        )
    },
    "archetype": {
        "en": "Wave Archetype: Keeper of Sacred Waters, Emotional Alchemist, Guardian of Renewal.",
        "ru": "Архетип Волны: Хранитель Священных Вод, Эмоциональный Алхимик, Страж Обновления."
    },
    "shadow": {
        "en": "Wave Shadow: Getting trapped in self-pity, emotional heaviness blocking flow.",
        "ru": "Тень Волны: Застревание в жалости к себе, эмоциональная тяжесть, мешающая потоку."
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
