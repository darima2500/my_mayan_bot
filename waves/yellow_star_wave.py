wave_info = {
    "name": {
        "en": "Yellow Star Wave",
        "ru": "Волна Жёлтой Звезды"
    },
    "start_date": "2026-01-10",
    "end_date": "2026-01-22",
    "core_themes": {
        "en": [
            "Art",
            "Harmony",
            "Inner Light",
            "Beauty as a spiritual expression",
            "Reconnection with your starseed",
            "Wave Shadow: Dependence on external validation, striving for unattainable perfection."
        ],
        "ru": [
            "Искусство",
            "Гармония",
            "Красота как выражение Духа в Материи",
            "Соединение со своей звездной природой",
            "Тень Волны: Зависимость от внешнего признания, стремление к недостижимому совершенству.",
            ]
    },
    "description": {
        "en": (
            "🌟 *Yellow Star Wave *\n"
            "This wave carries the energies of art, harmony, and inner radiance. "
            "It brings forward themes of balance and alignment between the inner and the outer. In the Mayan tradition, the Yellow Star is associated with the energy of the planet Venus — the patron of the Feminine, beauty, grace, creativity, and love. "
            "After the active processes of the previous wave, a sense of stability, simplicity, and enjoyment of everyday moments emerges. "
            "The focus shifts to the beauty of small things: light, space, gestures, sounds, and embodied presence. There is a natural impulse to bring order to your surroundings, to make the environment more harmonious, and actions more conscious.\n\n"
            "This wave supports creativity as a way of living. By trusting your sense of taste and your feeling for beauty, you can learn to harmonize your life — through everyday choices, attunement to inner symmetry, and a more sensual awareness of how you inhabit each day.\n"
        ),
        "ru": (
            "🌟 *Волна Жёлтой Звезды *\n"
            "Эта волна несёт энергии искусства, гармонии и внутреннего сияния."
            "Она будет поднимать темы баланса и выравнимания внутреннего со внешним. Желтая Звезда у майя связана с энергией планеты Венеры — покровительницы Женского, красоты, изящества, творчества и любви. "
            "После активных процессов предыдущей волны приходит ощущение устойчивости, простоты и наслаждения в повседневных моментах. "
            "В фокусе — красота мелочей: свет, пространство, жесты, звуки, присутствие в теле. Возникает естественное желание упорядочить пространство вокруг себя, сделать среду более гармоничной, а действия — более осознанными.\n\n"
            "Эта волна поддерживает творчество как состояние жизни. Доверяя своему вкусу и чувству прекрасного, можно научиться гармонизировать свою жизнь — через каждодневные выборы, сонастроенность с внутренней симметрией и более чувственным вниманием к тому, как ты проживаешь каждый день."
        )
    }
}  # ← добавил закрывающую скобку


def get_wave_message(lang):
    name = wave_info["name"][lang]
    themes = wave_info["core_themes"][lang]
    description = wave_info["description"][lang]

    themes_intro = "Основные темы:" if lang == "ru" else "Core themes:"
    themes_text = "\n".join(f"• {theme}" for theme in themes)

    return (
        f"🌊 *{name}*\n\n"
        f"*{themes_intro}*\n"
        f"{themes_text}\n\n"
        f"{description}"
    )




