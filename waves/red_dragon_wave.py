wave_info = {
    "name": {
        "en": "Red Dragon Wave",
        "ru": "Волна Красного Дракона"
    },
    "period": {
        "en": "October 10 — October 22, 2026",
        "ru": "10 Октября - 22 Октября 2026"
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
            "Вынашивание Нового",
            "Доверие к жизни",
            "Связь с Источником",
            "Тень: Зависимость, страх сепарации"
        ]
    },
    "description": {
        "en": (
            "This wave carries the energy of birth, beginnings, and deep trust in the very source of life. Next cycle of 260 days beginns here.\n\n"
            "The Red Dragon invites you to return to your origin — the place where you were held without conditions.\n"
            "This is a time for rest, nourishment, and being. Let yourself soften. Let go of control, and remember how it feels to be cradled by Life itself.\n\n"
            "From this softness, true creativity is born — not from effort, but from deep trust and embodied connection."
        ),
        "ru": (
            "Эта волна несёт энергию начала, запускается следующий 260-дневный цикл. Время зарождения и глубокого доверия к самому источнику жизни.\n\n"
            "Красный Дракон приглашает тебя вернуться к точке своего происхождения — туда, где ты был(а) принят(а) без условий.\n"
            "Это время отдыха, время напитаться ресурсами, чтобы совершить прыжок в Новый мир. Позвольте себе просто быть, отпустить контроль и вспомнить, каково это — быть на руках у Праматери-Жизни.\n\n"
            "Внимательно слушайте любой импульс, который рождается на уровне Души, не пропускайте его и сделайте любой, даже самый маленький, но всё-таки шаг к исполнению нового."
        )
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



