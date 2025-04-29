wave_info = {
    "name": {
        "en": "White Mirror Wave",
        "ru": "Волна Белого Зеркала"
    },
    "period": {
        "en": "September 2 — September 14, 2025",
        "ru": "2 сентября — 14 сентября 2025"
    },
    "core_themes": {
        "en": [
            "Truth and clarity",
            "Seeing beyond illusions",
            "Inner freedom through honesty",
            "Cutting through falsehoods",
            "Shadow: Fanaticism, harsh judgment"
        ],
        "ru": [
            "Истина и ясность",
            "Прозрение сквозь иллюзии",
            "Внутренняя свобода через честность",
            "Отсечение ложных образов",
            "Тень: Фанатизм, жёсткость суждений"
        ]
    },
    "description": {
        "en": (
            "This wave carries the energies of truth, clarity, and the power of inner liberation.\n\n"
            "The White Mirror invites you to see yourself and the world without distortion — to recognize illusions, to release false images, and to stand in your own simple truth.\n"
            "It is a time for deep reflection, honest confrontation, and clear choices that align with what is real.\n\n"
            "The Mirror teaches: true freedom comes from within, through the courage to face what is, without clinging to illusions."
        ),
        "ru": (
            "Эта волна несёт энергии истины, ясности и силы внутреннего освобождения.\n\n"
            "Белое Зеркало приглашает видеть себя и мир без искажений — распознавать иллюзии, отпускать ложные образы и стоять в своей простой истине.\n"
            "Это время глубокого отражения, честной встречи с собой и ясного выбора, который соотносится с тем, что реально.\n\n"
            "Зеркало учит: настоящая свобода рождается внутри — через смелость встретиться с тем, что есть, без попыток удерживать иллюзии."
        )
    },
    "archetype": {
        "en": "Wave Archetype: The Blade of Clarity, the Guardian of Inner Liberation.",
        "ru": "Архетип Волны: Клинок Ясности, Хранитель Внутреннего Освобождения."
    },
    "shadow": {
        "en": "Wave Shadow: Fanaticism, harsh judgment, fighting illusions outside instead of inside.",
        "ru": "Тень Волны: Фанатизм, жёсткость суждений, борьба с иллюзиями вовне вместо работы внутри."
    }
}

def get_wave_message(lang):
    return wave_info["description"][lang]
