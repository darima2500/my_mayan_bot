from waves.yellow_star_wave import get_wave_message as get_yellow_star_wave_message
from waves.red_dragon_wave import get_wave_message as get_red_dragon_wave_message
from waves.white_jaguar_wave import get_wave_message as get_white_jaguar_wave_message
# и так далее


waves_schedule = [
    {
        "name": "Yellow Star Wave",
        "start_kin": 1,
        "end_kin": 13,
        "get_message_func": get_yellow_star_wave_message,
    },
    {
        "name": "Red Dragon Wave",
        "start_kin": 14,
        "end_kin": 26,
        "get_message_func": get_red_dragon_wave_message,
    },
    {
        "name": "White Jaguar Wave",
        "start_kin": 27,
        "end_kin": 39,
        "get_message_func": get_white_jaguar_wave_message,
    },
    # и так далее
]
