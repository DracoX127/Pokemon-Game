"""
Status Effect Manager
"""
import random

STATUS_EFFECTS = {
    "Burn": {
        "color": "\033[91m", # BRIGHT_RED
        "dmg_per_turn": 0.06, # 6% of max hp
        "atk_reduction": 0.5,
        "msg": "is burned!"
    },
    "Poison": {
        "color": "\033[95m", # BRIGHT_MAGENTA
        "dmg_per_turn": 0.12, # 12% of max hp
        "atk_reduction": 1.0,
        "msg": "is poisoned!"
    },
    "Paralyze": {
        "color": "\033[93m", # BRIGHT_YELLOW
        "dmg_per_turn": 0,
        "skip_chance": 0.25,
        "msg": "is paralyzed!"
    },
    "Sleep": {
        "color": "\033[94m", # BRIGHT_BLUE
        "dmg_per_turn": 0,
        "skip_chance": 1.0,
        "msg": "is fast asleep!"
    }
}

def apply_status_tick(pokemon_stats):
    status_name = pokemon_stats.get("status")
    if not status_name:
        return 0, None
    
    effect = STATUS_EFFECTS.get(status_name)
    if not effect:
        return 0, None
    
    damage = 0
    if effect["dmg_per_turn"] > 0:
        damage = int(pokemon_stats["maxhp"] * effect["dmg_per_turn"])
        pokemon_stats["hp"] = max(0, pokemon_stats["hp"] - damage)
        
    return damage, f"takes {damage} {status_name} damage" if damage > 0 else None

def can_attack(pokemon_stats):
    status_name = pokemon_stats.get("status")
    if not status_name:
        return True, None
    
    effect = STATUS_EFFECTS.get(status_name)
    if not effect:
        return True, None
    
    if effect["skip_chance"] > 0:
        if random.random() < effect["skip_chance"]:
            # Check if sleep wears off
            if status_name == "Sleep" and random.random() < 0.3:
                pokemon_stats["status"] = None
                return True, "woke up"
            return False, effect["msg"]
            
    return True, None
