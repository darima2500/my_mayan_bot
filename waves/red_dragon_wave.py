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
            "This wave carries the energy of birth, beginnings, and deep trust in the very source of life.\n\n"
            "The Red Dragon invites you to return to your origin — the place where you were held without conditions.\n"
            "This is a time for rest, nourishment, and being. Let yourself soften. Let go of control, and remember how it feels to be cradled by Life itself.\n\n"
            "From this softness, true creativity is born — not from effort, but from deep trust and embodied connection."
        ),
        "ru": (
            "Эта волна несёт энергию начала, рождения и глубокого доверия к самому источнику жизни.\n\n"
            "Красный Дракон приглашает тебя вернуться к точке своего происхождения — туда, где ты был(а) принят(а) без условий.\n"
            "Это время отдыха, укутанности, питания. Позволь себе просто быть, отпустить контроль и вспомнить, каково это — быть на руках у Жизни.\n\n"
            "Из этой мягкости рождается настоящее творчество — не из усилия, а из глубинного доверия и соединённости с телом."
        )
    }
}


def get_wave_message(lang):
    return wave_info["description"][lang]
