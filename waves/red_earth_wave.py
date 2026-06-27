wave_info = {
    "name": {
        "en": "Red Earth Wave",
        "ru": "Волна Красной Земли"
    },
    "period": {
        "en": "June 28 — July 10, 2026",
        "ru": "28 Июня — 10 Июля 2026"
    },
    "core_themes": {
        "en": [
            "Synchronicity and timing",
            "Grounded movement",
            "Listening to inner guidance",
            "Wisdom and intelligent navigation",
            "Shadow: Losing oneself in fantasies, confusion"
        ],
        "ru": [
            "Синхроничность",
            "Правильное действие в нужный момент",
            "",
            "Мудрость и осознанная навигация в пространстве событий",
            "Тень: Потеря реальности, путаница"
        ]
    },
    "description": {
        "en": (
            "This wave invites you to align with the Earth's rhythm and the deeper timing of life.\n\n"
            "The Red Earth teaches you to move with awareness, sensing the subtle signs and synchronicities guiding your path.\n"
            "It is a time to root yourself in reality, trust your internal compass, the seed you planted before is ready to grow in the material realm.\n\n"
            "When you listen deeply, you discover that the Earth itself is speaking through every step you take."
        ),
        "ru": (
            "Мы привыкли жить в режиме жесткого планирования: «есть цель — есть план — есть результат». Но жизнь часто вносит хаос. Красная Земля — это альтернативная стратегия, которая работает лучше: стратегия навигации.В ближайшие 13 дней задача — переключиться с «проламывания реальности» на «считывание пространства».\n\n"
            "Слушайте «внутренний тайминг»: У каждого процесса есть свой темп. Если вы чувствуете, что сейчас не время для резких рывков — не давите. Это не лень, это экономия ресурса. И наоборот: если чувствуете импульс «пора» — делайте, даже если по плану это было намечено на потом. Внутреннее чутье сейчас точнее графиков.\n"
            "Это время заземления на всех уровнях. Семя, посаженное в предыдущей волне, теперь зовёт к проявлению и к более проявленным и активным действиям. Красная Земля не про «думать», а про «делать». Если у вас висела идея, к которой вы боялись подступиться — сейчас идеальный момент для первого шага. Это время, когда «семена» (ваши замыслы) легче всего пускают корни в физической реальности.\n\n"
            "Заземление как фильтр: Чем больше вокруг суеты и информации, тем важнее контакт с реальностью. Если вас «уносит» в тревогу или абстрактные рассуждения — вернитесь в тело. Простая уборка, прогулка без телефона, физический труд или готовка еды — это «перезагрузка», которая возвращает ясность мышления.\n"
        )
    },
    "archetype": {
        "en": "Wave Archetype: Guardian of the Earth's Garden, Wisdom Keeper, Crystal Healer.",
        "ru": "Архетип Волны: Хранитель Сада Земли, Хранитель Мудрости, Целитель Кристаллов."
    },
    "shadow": {
        "en": "Wave Shadow: Getting lost in dreams and illusions, losing clarity of direction.",
        "ru": "Тень Волны: Потеря ясности пути, уход в мечты и иллюзии."
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


