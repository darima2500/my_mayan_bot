from waves.red_dragon_wave import get_wave_message as get_red_dragon_wave_message
from waves.white_jaguar_wave import get_wave_message as get_white_jaguar_wave_message
from waves.blue_hand_wave import get_wave_message as get_blue_hand_wave_message
from waves.yellow_sun_wave import get_wave_message as get_yellow_sun_wave_message
from waves.red_skywalker_wave import get_wave_message as get_red_skywalker_wave_message
from waves.white_worldbridger_wave import get_wave_message as get_white_worldbridger_wave_message
from waves.blue_storm_wave import get_wave_message as get_blue_storm_wave_message
from waves.yellow_human_wave import get_wave_message as get_yellow_human_wave_message
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
from waves.yellow_star_wave import get_wave_message as get_yellow_star_wave_message

waves_schedule = [
    {
        "name": "Red Dragon Wave",
        "start_kin": 1,
        "end_kin": 13,
        "get_message_func": get_red_dragon_wave_message,
    },
    {
        "name": "White Jaguar Wave",
        "start_kin": 14,
        "end_kin": 26,
        "get_message_func": get_white_jaguar_wave_message,
    },
    {
        "name": "Blue Hand Wave",
        "start_kin": 27,
        "end_kin": 39,
        "get_message_func": get_blue_hand_wave_message,
    },
    {
        "name": "Yellow Sun Wave",
        "start_kin": 40,
        "end_kin": 52,
        "get_message_func": get_yellow_sun_wave_message,
    },
    {
        "name": "Red Skywalker Wave",
        "start_kin": 53,
        "end_kin": 65,
        "get_message_func": get_red_skywalker_wave_message,
    },
    {
        "name": "White Worldbridger Wave",
        "start_kin": 66,
        "end_kin": 78,
        "get_message_func": get_white_worldbridger_wave_message,
    },
    {
        "name": "Blue Storm Wave",
        "start_kin": 79,
        "end_kin": 91,
        "get_message_func": get_blue_storm_wave_message,
    },
    {
        "name": "Yellow Human Wave",
        "start_kin": 92,
        "end_kin": 104,
        "get_message_func": get_yellow_human_wave_message,
    },
    {
        "name": "Red Snake Wave",
        "start_kin": 105,
        "end_kin": 117,
        "get_message_func": get_red_snake_wave_message,
    },
    {
        "name": "White Mirror Wave",
        "start_kin": 118,
        "end_kin": 130,
        "get_message_func": get_white_mirror_wave_message,
    },
    {
        "name": "Blue Monkey Wave",
        "start_kin": 131,
        "end_kin": 143,
        "get_message_func": get_blue_monkey_wave_message,
    },
    {
        "name": "Yellow Seed Wave",
        "start_kin": 144,
        "end_kin": 156,
        "get_message_func": get_yellow_seed_wave_message,
    },
    {
        "name": "Red Earth Wave",
        "start_kin": 157,
        "end_kin": 169,
        "get_message_func": get_red_earth_wave_message,
    },
    {
        "name": "White Dog Wave",
        "start_kin": 170,
        "end_kin": 182,
        "get_message_func": get_white_dog_wave_message,
    },
    {
        "name": "Blue Night Wave",
        "start_kin": 183,
        "end_kin": 195,
        "get_message_func": get_blue_night_wave_message,
    },
    {
        "name": "Yellow Warrior Wave",
        "start_kin": 196,
        "end_kin": 208,
        "get_message_func": get_yellow_warrior_wave_message,
    },
    {
        "name": "Red Moon Wave",
        "start_kin": 209,
        "end_kin": 221,
        "get_message_func": get_red_moon_wave_message,
    },
    {
        "name": "White Wind Wave",
        "start_kin": 222,
        "end_kin": 234,
        "get_message_func": get_white_wind_wave_message,
    },
    {
        "name": "Blue Eagle Wave",
        "start_kin": 235,
        "end_kin": 247,
        "get_message_func": get_blue_eagle_wave_message,
    },
    {
        "name": "Yellow Star Wave",
        "start_kin": 248,
        "end_kin": 260,
        "get_message_func": get_yellow_star_wave_message,
    },
]
