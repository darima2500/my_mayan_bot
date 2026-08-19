wave_info = {
    "name": {
        "en": "Red Moon Wave",
        "ru": "Волна Красной Луны"
    },
    "period": {
        "en": "19 August — August 31, 2026",
        "ru": "19 Августа — 31 Августа 2026"
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
            "Эмоциональное очищение",
            "Повышенная чувствительность",
            "Баланс между отдачей и принятием",
            "Доверие своим интуиции",
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
            "Период Красной Луны — это 13 дней эмоциональной и телесной перезагрузки.\n\n"
            "Главный механизм этого периода — переключить внимание с постоянного контроля и подавления эмоций на их проживание и выгрузку. Перестать сопротивляться тому, что вы на самом деле чувствуете.\n"
            "Очищение через тело: Накопленный стресс, подавленный гнев или старая обида всегда проявляются телесно — зажимами в плечах, тяжестью в груди или хронической усталостью. Когда вы разрешаете себе прожить эмоцию (поплакать, выговориться, интенсивно подвигаться), тело скидывает этот балласт, и возвращается ресурс.\n\n"
            "Баланс отдачи и принятия (Инь/Ян): Проверьте, где у вас перекос. Вы только отдаете ресурсы, заставляя себя «держать удар» (переизбыток контроля), или умеете принимать помощь, отдыхать и восстанавливаться? Это время сбалансировать отдачу и восполнение. Интуиция в этот период — это не мистика, а сигналы вашего тела (первая реакция, телесный отклик, чувство «свое / не свое»). Если перестать глушить эти сигналы логическими оправданиями, решения становятся очевидными, а эмоциональное напряжение спадает."
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
