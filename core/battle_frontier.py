"""
Battle Frontier System
7 post-game facilities with unique rules and rewards:
1. Battle Factory - Random rental Pokemon
2. Battle Tower - Streak-based battles
3. Battle Dome - Tournament bracket
4. Battle Palace - Pokemon choose their own moves
5. Battle Arena - Accuracy/evasion/crit focus
6. Battle Pike - Roulette challenges
7. Battle Hall - Face all 18 types
"""
import random

# ═══════════════════════════════════════════
# BATTLE FRONTIER FACILITIES
# ═══════════════════════════════════════════

BATTLE_FRONTIER = {
    "factory": {
        "name": "Battle Factory",
        "emoji": "🏭",
        "description": "Use randomly assigned rental Pokemon. Test your team-building skills!",
        "rules": "Random Pokemon with random moves. No items allowed.",
        "levels": [50, 100],
        "rounds": 7,
        "rewards": {
            "complete": {"coins": 5000, "trophies": 3000, "item": "Choice Band"},
            "streak_10": {"coins": 10000, "trophies": 5000, "item": "Choice Specs"},
            "streak_20": {"coins": 20000, "trophies": 10000, "item": "Choice Scarf"},
        },
        "symbol": "Knowledge Symbol"
    },
    "tower": {
        "name": "Battle Tower",
        "emoji": "🗼",
        "description": "Win streaks against increasingly difficult trainers!",
        "rules": "Use your own team. No healing between battles. LV 50 or LV 100.",
        "levels": [50, 100],
        "max_streak": 49,
        "rewards": {
            "streak_10": {"coins": 3000, "trophies": 2000, "item": "Focus Band"},
            "streak_20": {"coins": 8000, "trophies": 5000, "item": "Life Orb"},
            "streak_49": {"coins": 50000, "trophies": 25000, "item": "Lucky Egg"},
        },
        "symbol": "Tower Symbol"
    },
    "dome": {
        "name": "Battle Dome",
        "emoji": "🏟️",
        "description": "Single-elimination tournament. Choose your path wisely!",
        "rules": "Tournament bracket format. Pick your matchups. Double battles.",
        "rounds": 4,
        "rewards": {
            "complete": {"coins": 8000, "trophies": 5000, "item": "Scope Lens"},
            "flawless": {"coins": 15000, "trophies": 10000, "item": "Kings Rock"},
        },
        "symbol": "Tactics Symbol"
    },
    "palace": {
        "name": "Battle Palace",
        "emoji": "🏛️",
        "description": "Pokemon choose their own moves based on their nature!",
        "rules": "You can't choose moves. Pokemon act on their own. Test your team composition!",
        "rounds": 7,
        "rewards": {
            "complete": {"coins": 6000, "trophies": 4000, "item": "Quick Claw"},
            "streak_14": {"coins": 12000, "trophies": 8000, "item": "Razor Claw"},
        },
        "symbol": "Spirit Symbol"
    },
    "arena": {
        "name": "Battle Arena",
        "emoji": "⚔️",
        "description": "Battles decided by accuracy, evasion, and critical hits!",
        "rules": "Accuracy, evasion, and crit rate matter most. No stat-boosting moves.",
        "rounds": 7,
        "rewards": {
            "complete": {"coins": 5000, "trophies": 3000, "item": "Wide Lens"},
            "streak_14": {"coins": 10000, "trophies": 7000, "item": "Zoom Lens"},
        },
        "symbol": "Ability Symbol"
    },
    "pike": {
        "name": "Battle Pike",
        "emoji": "🐍",
        "description": "Navigate a snake-like path with random challenges!",
        "rules": "Roulette-style rooms. Random battles, status effects, healing, or traps!",
        "rooms": 14,
        "rewards": {
            "complete": {"coins": 7000, "trophies": 4000, "item": "Leftovers"},
            "flawless": {"coins": 14000, "trophies": 9000, "item": "Shell Bell"},
        },
        "symbol": "Luck Symbol"
    },
    "hall": {
        "name": "Battle Hall",
        "emoji": "🏰",
        "description": "Face all 18 types in succession. The ultimate test!",
        "rules": "18 battles in a row, one for each type. No healing between battles.",
        "types": 18,
        "rewards": {
            "complete": {"coins": 30000, "trophies": 15000, "item": "Expert Belt"},
        },
        "symbol": "Print Symbol"
    }
}

# ═══════════════════════════════════════════
# RENTAL POKEMON FOR BATTLE FACTORY
# ═══════════════════════════════════════════
RENTAL_POKEMON = [
    {"name": "Dragonite", "type": ["Dragon", "Flying"], "hp": 150, "dm": 130, "speed": 80,
     "moves": ["Dragon Claw", "Earthquake", "Thunder Punch", "Fire Punch"]},
    {"name": "Tyranitar", "type": ["Rock", "Dark"], "hp": 140, "dm": 140, "speed": 61,
     "moves": ["Stone Edge", "Crunch", "Earthquake", "Ice Punch"]},
    {"name": "Metagross", "type": ["Steel", "Psychic"], "hp": 130, "dm": 145, "speed": 70,
     "moves": ["Meteor Mash", "Earthquake", "Psychic", "Bullet Punch"]},
    {"name": "Salamence", "type": ["Dragon", "Flying"], "hp": 145, "dm": 135, "speed": 100,
     "moves": ["Dragon Claw", "Earthquake", "Flamethrower", "Hydro Pump"]},
    {"name": "Garchomp", "type": ["Dragon", "Ground"], "hp": 140, "dm": 130, "speed": 102,
     "moves": ["Dragon Claw", "Earthquake", "Stone Edge", "Fire Fang"]},
    {"name": "Gyarados", "type": ["Water", "Flying"], "hp": 145, "dm": 125, "speed": 81,
     "moves": ["Waterfall", "Earthquake", "Ice Fang", "Dragon Dance"]},
    {"name": "Snorlax", "type": ["Normal", "Fighting"], "hp": 200, "dm": 110, "speed": 30,
     "moves": ["Body Slam", "Earthquake", "Crunch", "Rest"]},
    {"name": "Blissey", "type": ["Normal", "Fairy"], "hp": 250, "dm": 10, "speed": 55,
     "moves": ["Soft-Boiled", "Seismic Toss", "Thunder Wave", "Toxic"]},
    {"name": "Alakazam", "type": ["Psychic", "Ghost"], "hp": 80, "dm": 135, "speed": 120,
     "moves": ["Psychic", "Shadow Ball", "Focus Blast", "Energy Ball"]},
    {"name": "Gengar", "type": ["Ghost", "Poison"], "hp": 90, "dm": 130, "speed": 110,
     "moves": ["Shadow Ball", "Sludge Bomb", "Thunderbolt", "Focus Blast"]},
    {"name": "Machamp", "type": ["Fighting", "Steel"], "hp": 130, "dm": 130, "speed": 55,
     "moves": ["Close Combat", "Earthquake", "Stone Edge", "Bullet Punch"]},
    {"name": "Scizor", "type": ["Bug", "Steel"], "hp": 110, "dm": 130, "speed": 65,
     "moves": ["Bullet Punch", "U-turn", "Superpower", "Bug Bite"]},
    {"name": "Heracross", "type": ["Bug", "Fighting"], "hp": 120, "dm": 125, "speed": 85,
     "moves": ["Close Combat", "Megahorn", "Stone Edge", "Earthquake"]},
    {"name": "Aerodactyl", "type": ["Rock", "Flying"], "hp": 110, "dm": 105, "speed": 130,
     "moves": ["Stone Edge", "Aerial Ace", "Earthquake", "Fire Fang"]},
    {"name": "Jolteon", "type": ["Electric", "Fairy"], "hp": 95, "dm": 110, "speed": 130,
     "moves": ["Thunderbolt", "Shadow Ball", "Signal Beam", "Volt Switch"]},
    {"name": "Arcanine", "type": ["Fire", "Rock"], "hp": 130, "dm": 110, "speed": 95,
     "moves": ["Flare Blitz", "Extreme Speed", "Wild Charge", "Close Combat"]},
    {"name": "Lapras", "type": ["Water", "Ice"], "hp": 160, "dm": 85, "speed": 60,
     "moves": ["Surf", "Ice Beam", "Thunderbolt", "Psychic"]},
    {"name": "Venusaur", "type": ["Grass", "Poison"], "hp": 120, "dm": 100, "speed": 80,
     "moves": ["Solar Beam", "Sludge Bomb", "Earthquake", "Sleep Powder"]},
]

# ═══════════════════════════════════════════
# BATTLE HALL OPPONENTS (18 types)
# ═══════════════════════════════════════════
BATTLE_HALL_OPPONENTS = {
    "Normal": {"name": "Snorlax", "type": "Normal", "hp": 200, "dm": 110, "speed": 30,
               "moves": ["Body Slam", "Earthquake", "Crunch", "Rest"]},
    "Fire": {"name": "Arcanine", "type": "Fire", "hp": 130, "dm": 110, "speed": 95,
             "moves": ["Flare Blitz", "Extreme Speed", "Wild Charge", "Close Combat"]},
    "Water": {"name": "Gyarados", "type": "Water", "hp": 145, "dm": 125, "speed": 81,
              "moves": ["Waterfall", "Earthquake", "Ice Fang", "Dragon Dance"]},
    "Electric": {"name": "Jolteon", "type": "Electric", "hp": 95, "dm": 110, "speed": 130,
                 "moves": ["Thunderbolt", "Shadow Ball", "Signal Beam", "Volt Switch"]},
    "Grass": {"name": "Venusaur", "type": "Grass", "hp": 120, "dm": 100, "speed": 80,
              "moves": ["Solar Beam", "Sludge Bomb", "Earthquake", "Sleep Powder"]},
    "Ice": {"name": "Lapras", "type": "Ice", "hp": 160, "dm": 85, "speed": 60,
            "moves": ["Surf", "Ice Beam", "Thunderbolt", "Psychic"]},
    "Fighting": {"name": "Machamp", "type": "Fighting", "hp": 130, "dm": 130, "speed": 55,
                 "moves": ["Close Combat", "Earthquake", "Stone Edge", "Bullet Punch"]},
    "Poison": {"name": "Gengar", "type": "Poison", "hp": 90, "dm": 130, "speed": 110,
               "moves": ["Shadow Ball", "Sludge Bomb", "Thunderbolt", "Focus Blast"]},
    "Ground": {"name": "Garchomp", "type": "Ground", "hp": 140, "dm": 130, "speed": 102,
               "moves": ["Dragon Claw", "Earthquake", "Stone Edge", "Fire Fang"]},
    "Flying": {"name": "Dragonite", "type": "Flying", "hp": 150, "dm": 130, "speed": 80,
               "moves": ["Dragon Claw", "Earthquake", "Thunder Punch", "Fire Punch"]},
    "Psychic": {"name": "Alakazam", "type": "Psychic", "hp": 80, "dm": 135, "speed": 120,
                "moves": ["Psychic", "Shadow Ball", "Focus Blast", "Energy Ball"]},
    "Bug": {"name": "Scizor", "type": "Bug", "hp": 110, "dm": 130, "speed": 65,
            "moves": ["Bullet Punch", "U-turn", "Superpower", "Bug Bite"]},
    "Rock": {"name": "Tyranitar", "type": "Rock", "hp": 140, "dm": 140, "speed": 61,
             "moves": ["Stone Edge", "Crunch", "Earthquake", "Ice Punch"]},
    "Ghost": {"name": "Gengar", "type": "Ghost", "hp": 90, "dm": 130, "speed": 110,
              "moves": ["Shadow Ball", "Sludge Bomb", "Thunderbolt", "Focus Blast"]},
    "Dragon": {"name": "Salamence", "type": "Dragon", "hp": 145, "dm": 135, "speed": 100,
               "moves": ["Dragon Claw", "Earthquake", "Flamethrower", "Hydro Pump"]},
    "Dark": {"name": "Tyranitar", "type": "Dark", "hp": 140, "dm": 140, "speed": 61,
             "moves": ["Stone Edge", "Crunch", "Earthquake", "Ice Punch"]},
    "Steel": {"name": "Metagross", "type": "Steel", "hp": 130, "dm": 145, "speed": 70,
              "moves": ["Meteor Mash", "Earthquake", "Psychic", "Bullet Punch"]},
    "Fairy": {"name": "Blissey", "type": "Fairy", "hp": 250, "dm": 10, "speed": 55,
              "moves": ["Soft-Boiled", "Seismic Toss", "Thunder Wave", "Toxic"]},
}

# ═══════════════════════════════════════════
# PIKE ROOM EVENTS
# ═══════════════════════════════════════════
PIKE_ROOMS = [
    {"type": "battle", "name": "Wild Battle", "desc": "A wild Pokemon appears!", "effect": "battle"},
    {"type": "heal", "name": "Healing Spring", "desc": "Your team recovers HP!", "effect": "heal"},
    {"type": "trap", "name": "Poison Trap", "desc": "Your team gets poisoned!", "effect": "poison"},
    {"type": "trap", "name": "Paralysis Trap", "desc": "Your team gets paralyzed!", "effect": "paralyze"},
    {"type": "bonus", "name": "Coin Room", "desc": "You found coins!", "effect": "coins"},
    {"type": "bonus", "name": "Item Room", "desc": "You found an item!", "effect": "item"},
    {"type": "battle", "name": "Trainer Battle", "desc": "A trainer challenges you!", "effect": "trainer"},
    {"type": "rest", "name": "Rest Area", "desc": "Take a breather. Full heal!", "effect": "full_heal"},
]

# ═══════════════════════════════════════════
# HELPER FUNCTIONS
# ═══════════════════════════════════════════

def get_rental_team(count=3):
    """Get a random rental team for Battle Factory."""
    return random.sample(RENTAL_POKEMON, min(count, len(RENTAL_POKEMON)))

def get_pike_room():
    """Get a random Pike room event."""
    return random.choice(PIKE_ROOMS)

def get_battle_hall_order():
    """Get the order of types for Battle Hall."""
    types = list(BATTLE_HALL_OPPONENTS.keys())
    random.shuffle(types)
    return types

def get_frontier_progress(save_data, facility):
    """Get progress for a specific frontier facility."""
    frontier = save_data.get("frontier_progress", {})
    return frontier.get(facility, {"best_streak": 0, "completed": False, "symbols": []})

def update_frontier_progress(save_data, facility, streak=0, completed=False, symbol=None):
    """Update progress for a frontier facility."""
    if "frontier_progress" not in save_data:
        save_data["frontier_progress"] = {}
    if facility not in save_data["frontier_progress"]:
        save_data["frontier_progress"][facility] = {"best_streak": 0, "completed": False, "symbols": []}
    
    prog = save_data["frontier_progress"][facility]
    if streak > prog["best_streak"]:
        prog["best_streak"] = streak
    if completed:
        prog["completed"] = True
    if symbol and symbol not in prog["symbols"]:
        prog["symbols"].append(symbol)
    
    return prog

def count_frontier_symbols(save_data):
    """Count total Frontier Symbols earned."""
    frontier = save_data.get("frontier_progress", {})
    total = 0
    for fac in frontier.values():
        total += len(fac.get("symbols", []))
    return total
