wave_info = {
    "name": {
        "en": "Red Dragon Wave",
        "ru": "Волна Красного Дракона"
    },
    "period": {
        "en": "May 8 — May 20, 2025",
        "ru": "8 — 20 мая 2025"
    },
    "core_themes": {
        "en": [
            "Birth",
            "Nurturing",
            "Trust in Life",
            "Connection to Source",
            "Shadow: Overdependence, fear of separation"
        ],
        "ru": [
            "Рождение",
            "Забота",
            "Доверие к жизни",
            "Связь с Источником",
            "Тень: Зависимость, страх одиночества"
        ]
    },
    "description": {
        "en": (
            "This wave carries the energy of beginnings and deep trust in the source of life.\n\n"
            "The Red Dragon invites you to reconnect with your inner origin — to rest, be held, and allow yourself to be supported.\n"
            "Let go of the need to control, and return to the natural flow of receiving.\n\n"
            "From this place, true creativity is born."
        ),
        "ru": (
            "Эта волна несёт энергию начала и глубокого доверия к жизни.\n\n"
            "Красный Дракон приглашает вернуться к своему истоку — позволить себе быть, отдохнуть, принять поддержку.\n"
            "Отпуская контроль, ты возвращаешься к естественному потоку.\n\n"
            "Из этого состояния рождается настоящее творчество."
        )
    },
    "archetype": {
        "en": "Wave Archetype: The Cosmic Mother, the Nourisher of Life.",
        "ru": "Архетип Волны: Космическая Мать, Питающая Жизнь."
    },
    "shadow": {
        "en": "Wave Shadow: Dependency, lack of boundaries, fear of separation.",
        "ru": "Тень Волны: Зависимость, отсутствие границ, страх покинутости."
    }
}

def get_wave_message(lang):
    return wave_info["description"][lang]
