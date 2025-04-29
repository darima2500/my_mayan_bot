wave_info = {
    "name": {
        "en": "Red Earth Wave",
        "ru": "Волна Красной Земли"
    },
    "period": {
        "en": "October 11 — October 23, 2025",
        "ru": "11 октября — 23 октября 2025"
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
            "Синхрония и правильный момент",
            "Заземлённое движение",
            "Прислушивание к внутреннему компасу",
            "Мудрость и осознанная навигация",
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
            "Эта волна приглашает настроиться на ритм Земли и на более глубокий внутренний тайминг жизни.\n\n"
            "Красная Земля учит двигаться с осознанностью, улавливая тонкие знаки и синхронии, которые направляют твой путь.\n"
            "Это время заземления на всех уровнях. Семя, посаженное в предыдущей волне, теперь зовёт к проявлению.\n\n"
            "Когда ты начинаешь внимательно слушать, ты понимаешь: сама Земля говорит с тобой через каждый шаг."
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
    return wave_info["description"][lang]
