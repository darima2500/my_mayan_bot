from waves.yellow_star_wave import get_wave_message as get_yellow_star_wave_message
from waves.red_dragon_wave import get_wave_message as get_red_dragon_wave_message
from waves.white_jaguar_wave import get_wave_message as get_white_jaguar_wave_message
from waves.blue_hand_wave import get_wave_message as get_blue_hand_wave_message
from waves.yellow_sun_wave import get_wave_message as get_yellow_sun_wave_message
from waves.red_skywalker_wave import get_wave_message as get_red_skywalker_wave_message
from waves.white_worldbridger_wave import get_wave_message as get_white_worldbridger_wave_message
from waves.blue_storm_wave import get_wave_message as get_blue_storm_wave_message
from waves.yellow_man_wave import get_wave_message as get_yellow_man_wave_message
from waves.red_snake_wave import get_wave_message as get_red_snake_wave_message
from waves.white_mirror_wave import get_wave_message as get_white_mirror_wave_message
from waves.blue_monkey_wave import get_wave_message as get_blue_monkey_wave_message
from waves.yellow_seed_wave import get_wave_message as get_yellow_seed_wave_message
from waves.red_earth_wave import get_wave_message as get_red_earth_wave_message
from waves.white_dog_wave import get_wave_message as get_white_dog_wave_message
from waves.blue_night_wave import get_wave_message as get_blue_night_wave_message
from waves.yellow_warrior_wave import get_wave_message as get_yellow_warrior_wave_message
from waves.red_moon_wave import get_wave_message as get_red_moon_wave_message
from waves.white_wind_wave import get_wave_message as get_white_wind_wave_message
from waves.blue_eagle_wave import get_wave_message as get_blue_eagle_wave_message
from waves.yellow_star_wave import get_wave_message as get_yellow_star_wave_message_repeat  # Вторая волна Жёлтой Звезды в январе 2026

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
    {
        "start_date": "2025-05-21",
        "end_date": "2025-06-02",
        "get_message_func": get_white_jaguar_wave_message
    },
    {
        "start_date": "2025-06-03",
        "end_date": "2025-06-15",
        "get_message_func": get_blue_hand_wave_message
    },
    {
        "start_date": "2025-06-16",
        "end_date": "2025-06-28",
        "get_message_func": get_yellow_sun_wave_message
    },
    {
        "start_date": "2025-06-29",
        "end_date": "2025-07-11",
        "get_message_func": get_red_skywalker_wave_message
    },
    {
        "start_date": "2025-07-12",
        "end_date": "2025-07-24",
        "get_message_func": get_white_worldbridger_wave_message
    },
    {
        "start_date": "2025-07-25",
        "end_date": "2025-08-06",
        "get_message_func": get_blue_storm_wave_message
    },
    {
        "start_date": "2025-08-07",
        "end_date": "2025-08-19",
        "get_message_func": get_yellow_man_wave_message
    },
    {
        "start_date": "2025-08-20",
        "end_date": "2025-09-01",
        "get_message_func": get_red_snake_wave_message
    },
    {
        "start_date": "2025-09-02",
        "end_date": "2025-09-14",
        "get_message_func": get_white_mirror_wave_message
    },
    {
        "start_date": "2025-09-15",
        "end_date": "2025-09-27",
        "get_message_func": get_blue_monkey_wave_message
    },
    {
        "start_date": "2025-09-28",
        "end_date": "2025-10-10",
        "get_message_func": get_yellow_seed_wave_message
    },
    {
        "start_date": "2025-10-11",
        "end_date": "2025-10-23",
        "get_message_func": get_red_earth_wave_message
    },
    {
        "start_date": "2025-10-24",
        "end_date": "2025-11-05",
        "get_message_func": get_white_dog_wave_message
    },
    {
        "start_date": "2025-11-06",
        "end_date": "2025-11-18",
        "get_message_func": get_blue_night_wave_message
    },
    {
        "start_date": "2025-11-19",
        "end_date": "2025-12-01",
        "get_message_func": get_yellow_warrior_wave_message
    },
    {
        "start_date": "2025-12-02",
        "end_date": "2025-12-14",
        "get_message_func": get_red_moon_wave_message
    },
    {
        "start_date": "2025-12-15",
        "end_date": "2025-12-27",
        "get_message_func": get_white_wind_wave_message
    },
    {
        "start_date": "2025-12-28",
        "end_date": "2026-01-09",
        "get_message_func": get_blue_eagle_wave_message
    },
    {
        "start_date": "2026-01-10",
        "end_date": "2026-01-22",
        "get_message_func": get_yellow_star_wave_message_repeat
    }
]
