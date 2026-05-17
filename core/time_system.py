"""Day/Night Cycle System: time tracking, visuals, spawn modifiers."""

import random

HOUR = 0
ACTIONS_SINCE_TICK = 0
ACTIONS_PER_HOUR = 4

TIME_NAMES = {
    0:"Midnight",1:"Late Night",2:"Dead of Night",3:"Early Morning",
    4:"Dawn",5:"Sunrise",6:"Morning",7:"Morning",8:"Morning",
    9:"Late Morning",10:"Late Morning",11:"Approaching Noon",
    12:"Noon",13:"Early Afternoon",14:"Afternoon",15:"Afternoon",
    16:"Late Afternoon",17:"Evening",18:"Dusk",19:"Twilight",
    20:"Night",21:"Night",22:"Late Night",23:"Late Night",
}

TIME_PERIODS = {
    "Dawn":     (4,6),
    "Morning":  (6,11),
    "Day":      (11,17),
    "Evening":  (17,20),
    "Night":    (20,24),
    "Late Night":(0,4),
}

def get_period(hour=None):
    if hour is None:
        hour = HOUR
    for period, (start, end) in TIME_PERIODS.items():
        if start <= hour < end:
            return period
    return "Day"

def get_time_name(hour=None):
    if hour is None:
        hour = HOUR
    return TIME_NAMES.get(hour, "")

def advance_time(actions=1):
    global HOUR, ACTIONS_SINCE_TICK
    ACTIONS_SINCE_TICK += actions
    if ACTIONS_SINCE_TICK >= ACTIONS_PER_HOUR:
        hours = ACTIONS_SINCE_TICK // ACTIONS_PER_HOUR
        HOUR = (HOUR + hours) % 24
        ACTIONS_SINCE_TICK = ACTIONS_SINCE_TICK % ACTIONS_PER_HOUR

def set_hour(h):
    global HOUR
    HOUR = h % 24

def is_night():
    return get_period() in ("Night", "Late Night")

def is_day():
    return get_period() in ("Day", "Morning")

def time_spawn_modifier():
    period = get_period()
    if period in ("Night", "Late Night"):
        return "night"
    elif period in ("Dawn", "Evening"):
        return "twilight"
    return "day"

NIGHT_SPAWN_BONUS = ["Gastly","Haunter","Zubat","Misdreavus","Houndour","Murkrow",
                     "Sneasel","Poochyena","Mightyena","Duskull","Shuppet","Sableye",
                     "Absol","Spiritomb","Darkrai","Umbreon","Lunala","Cresselia"]
DAY_SPAWN_BONUS = ["Pidgey","Rattata","Eevee","Pikachu","Growlithe","Vulpix",
                   "Lotad","Seedot","Solrock","Espeon","Solgaleo","Lilligant"]

def get_time_spawns(spawn_list):
    mod = time_spawn_modifier()
    extra = []
    if mod == "night":
        extra = [s for s in NIGHT_SPAWN_BONUS if s not in spawn_list]
    elif mod == "day":
        extra = [s for s in DAY_SPAWN_BONUS if s not in spawn_list]
    if extra and random.random() < 0.3:
        spawn_list = spawn_list + [random.choice(extra)]
    return spawn_list

TIME_COLORS = {
    "Dawn":       (255,180,100),
    "Morning":    (255,220,150),
    "Day":        (255,255,200),
    "Evening":    (255,150,80),
    "Night":      (80,80,150),
    "Late Night": (40,40,80),
}

def get_time_color():
    period = get_period()
    return TIME_COLORS.get(period, (255,255,200))

def get_time_icon():
    p = get_period()
    icons = {"Dawn":"🌅","Morning":"☀️","Day":"☀️","Evening":"🌆","Night":"🌙","Late Night":"🌑"}
    return icons.get(p, "☀️")
