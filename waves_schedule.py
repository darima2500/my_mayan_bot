from waves.yellow_star_wave import get_wave_message as get_yellow_star_wave_message
from waves.red_dragon_wave import get_wave_message as get_red_dragon_wave_message
# и так далее...

waves_schedule = [
    {
        "start_date": "2025-04-25",
        "end_date": "2025-05-07",
        "get_message_func": get_yellow_star_wave_message
    },
    {
        "start_date": "2025-05-08",
        "end_date": "2025-05-20",
        "get_message_func": get_red_dragon_wave_message
    },
    # и так далее
]
