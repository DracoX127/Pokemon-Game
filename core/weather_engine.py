"""
Weather System Engine
"""
import random

WEATHER_EFFECTS = {
    "Clear": {
        "description": "The weather is calm and clear.",
        "boost_type": None,
        "damage_type": None,
        "damage_val": 0
    },
    "Rain": {
        "description": "It's raining heavily! Water moves are boosted.",
        "boost_type": "Water",
        "damage_type": None,
        "damage_val": 0
    },
    "Sun": {
        "description": "The sunlight is harsh! Fire moves are boosted.",
        "boost_type": "Fire",
        "damage_type": None,
        "damage_val": 0
    },
    "Sandstorm": {
        "description": "A sandstorm is raging! It buffets non-Rock/Ground types.",
        "boost_type": "Rock",
        "damage_type": "Buffet",
        "damage_val": 10,
        "immune_types": ["Rock", "Ground", "Steel"]
    },
    "Hail": {
        "description": "Hail is falling! It buffets non-Ice types.",
        "boost_type": "Ice",
        "damage_type": "Buffet",
        "damage_val": 10,
        "immune_types": ["Ice"]
    },
    "Acid Rain": {
        "description": "Acid rain falls from the sky! It deals Poison damage.",
        "boost_type": "Poison",
        "damage_type": "Poison",
        "damage_val": 15,
        "immune_types": ["Poison", "Steel"]
    },
    "Solar Flare": {
        "description": "A solar flare erupts! Fire moves are MEGA boosted, others take heat damage.",
        "boost_type": "Fire",
        "damage_type": "Heat",
        "damage_val": 20,
        "immune_types": ["Fire"]
    }
}

def get_random_weather():
    return random.choice(list(WEATHER_EFFECTS.keys()))

def apply_weather_damage(weather_name, pokemon_stats):
    weather = WEATHER_EFFECTS.get(weather_name, WEATHER_EFFECTS["Clear"])
    if weather["damage_type"] and pokemon_stats.get("type") not in weather.get("immune_types", []):
        damage = weather["damage_val"]
        pokemon_stats["hp"] = max(0, pokemon_stats.get("hp", 0) - damage)
        return damage, f"The {weather_name} deals {damage} damage!"
    return 0, None
