wave_info = {
    "name": {
        "en": "Blue Hand Wave",
        "ru": "Волна Голубой Руки"
    },
    "period": {
        "en": "June 3 — June 15, 2025",
        "ru": "3 июня — 15 июня 2025"
    },

"core_themes": {
    "en": [
        "Healing",
        "Sacred Action",
        "Manifestation",
        "Service through wisdom and presence",
        "Spiritual and communal leadership",
        "Completing through heart-centered power",
        "Shadow: Manipulation, fixing instead of accepting"
    ],
    "ru": [
        "Исцеление",
        "Священное Действие",
        "Проявление",
        "Служение через мудрость и присутствие",
        "Духовное и общественное руководство",
        "Завершение через силу сердца",
        "Тень: Манипуляция, исправление вместо принятия"
    ]
},


    "description": {
        "en": (
            "This wave carries the energies of accomplishment, sacred action, healing, and community.\n\n"
            "The Blue Hand invites you to move with conscious intent — to act not for personal gain, but as a vessel of service, memory, and spiritual alignment.\n"
            "It is a time to remember your role within the greater field of life, to heal through presence, and to build with heart-centered power.\n\n"
            "The Hand reminds: true mastery is the art of guiding without manipulation, creating without force, and leading through the strength of integrity."
        ),
        "ru": (
            "Эта волна несёт энергии свершения, священного действия, исцеления и коллективной памяти.\n\n"
            "Голубая Рука приглашает двигаться с осознанным намерением — действовать не ради личной выгоды, а как сосуд служения, памяти и духовной сонастройки.\n"
            "Это время вспомнить свою роль в великом поле жизни, исцелять присутствием и созидать силой сердца.\n\n"
            "Рука напоминает: истинное мастерство — это искусство вести без манипуляции, творить без насилия и направлять через силу внутренней целостности."
        )
    },
    "archetype": {
        "en": "Wave Archetype: The Healer and Keeper of the Sacred Directions.",
        "ru": "Архетип Волны: Целитель и Хранитель Священных Сторон Света."
    },
    "shadow": {
        "en": "Wave Shadow: Manipulation, misuse of spiritual authority, striving to fix what requires deep acceptance.",
        "ru": "Тень Волны: Манипуляция, злоупотребление духовной силой, попытки исправить то, что требует глубокого принятия."
    }
}

def get_wave_message(lang):
    return wave_info["description"][lang]
