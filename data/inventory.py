"""
Inventory System: Items and Bag Management
"""
from moves_data import MOVES

ITEMS = {
    "Potion": {
        "price": 50,
        "description": "Restores 50 HP to a Pokemon.",
        "effect": {"type": "heal", "value": 50}
    },
    "Super Potion": {
        "price": 150,
        "description": "Restores 150 HP to a Pokemon.",
        "effect": {"type": "heal", "value": 150}
    },
    "Full Restore": {
        "price": 500,
        "description": "Fully restores a Pokemon's HP.",
        "effect": {"type": "heal", "value": "max"}
    },
    "Ultra Ball": {
        "price": 200,
        "description": "A high-performance ball that doubles catch rate.",
        "effect": {"type": "catch_multiplier", "value": 2.0}
    },
    "Master Ball": {
        "price": 5000,
        "description": "The ultimate ball. It never fails to catch!",
        "effect": {"type": "catch_multiplier", "value": 100.0}
    },
    "Rare Candy": {
        "price": 1000,
        "description": "Instantly levels up a Pokemon by 1.",
        "effect": {"type": "level_up", "value": 1}
    },
    "Attack Boost": {
        "price": 300,
        "description": "Permanently increases a Pokemon's damage by 5.",
        "effect": {"type": "stat_boost", "stat": "dm", "value": 5}
    },
    "Ether": {
        "price": 300,
        "description": "Restores 10 PP to one move.",
        "effect": {"type": "pp_restore", "value": 10}
    },
    "Elixir": {
        "price": 800,
        "description": "Restores 10 PP to ALL moves.",
        "effect": {"type": "pp_restore_all", "value": 10}
    },
    "Max Elixir": {
        "price": 2000,
        "description": "Fully restores PP to all moves.",
        "effect": {"type": "pp_restore_all", "value": "max"}
    },
    "Full Heal": {
        "price": 300,
        "description": "Cures all status conditions of a Pokemon.",
        "effect": {"type": "cure_status"}
    },
    "Revive": {
        "price": 1500,
        "description": "Revives a fainted Pokemon with 50% HP.",
        "effect": {"type": "revive", "value": 0.5}
    },
    "X Attack": {
        "price": 500,
        "description": "Permanently raises a Pokemon's DM by 3.",
        "effect": {"type": "stat_boost", "stat": "dm", "value": 3}
    },
    "X Speed": {
        "price": 500,
        "description": "Permanently raises a Pokemon's Speed by 3.",
        "effect": {"type": "stat_boost", "stat": "speed", "value": 3}
    },
    "Leftovers": {
        "price": 2000,
        "description": "Restores 1/16 max HP each turn.",
        "effect": {"type": "held_item"}
    },
    "Choice Band": {
        "price": 3000,
        "description": "Boosts DM by 50%, locks to one move.",
        "effect": {"type": "held_item"}
    },
    "Choice Scarf": {
        "price": 3000,
        "description": "Boosts Speed by 50%, locks to one move.",
        "effect": {"type": "held_item"}
    },
    "Life Orb": {
        "price": 2500,
        "description": "Boosts DM by 30%, costs 10% max HP per attack.",
        "effect": {"type": "held_item"}
    },
    "Expert Belt": {
        "price": 2000,
        "description": "Boosts super-effective damage by 20%.",
        "effect": {"type": "held_item"}
    },
    "Focus Sash": {
        "price": 2500,
        "description": "Survives with 1 HP from full HP (consumed).",
        "effect": {"type": "held_item"}
    },
    "Rocky Helmet": {
        "price": 2000,
        "description": "Damages attacker on contact.",
        "effect": {"type": "held_item"}
    },
    "Shell Bell": {
        "price": 1500,
        "description": "Restores HP equal to 1/8 of damage dealt.",
        "effect": {"type": "held_item"}
    },
    "Oran Berry": {
        "price": 300,
        "description": "Restores 10 HP when HP < 50%. (consumed)",
        "effect": {"type": "held_item"}
    },
    "Sitrus Berry": {
        "price": 500,
        "description": "Restores 25% max HP when HP < 50%. (consumed)",
        "effect": {"type": "held_item"}
    },
    "Lum Berry": {
        "price": 600,
        "description": "Cures any status condition. (consumed)",
        "effect": {"type": "held_item"}
    },
    "Charcoal": {
        "price": 800,
        "description": "Boosts Fire moves by 20%.",
        "effect": {"type": "held_item"}
    },
    "Mystic Water": {
        "price": 800,
        "description": "Boosts Water moves by 20%.",
        "effect": {"type": "held_item"}
    },
    "Miracle Seed": {
        "price": 800,
        "description": "Boosts Grass moves by 20%.",
        "effect": {"type": "held_item"}
    },
    "Magnet": {
        "price": 800,
        "description": "Boosts Electric moves by 20%.",
        "effect": {"type": "held_item"}
    }
}

def apply_item_effect(pokemon_stats, item_name):
    """Applies the effect of an item to a pokemon dictionary."""
    item = ITEMS.get(item_name)
    if not item:
        return False, "Item not found."
    
    effect = item["effect"]
    
    if effect["type"] == "heal":
        if effect["value"] == "max":
            pokemon_stats["hp"] = pokemon_stats["maxhp"]
        else:
            pokemon_stats["hp"] = min(pokemon_stats["maxhp"], pokemon_stats["hp"] + effect["value"])
        return True, f"Restored HP to {pokemon_stats['hp']}!"
    
    if effect["type"] == "level_up":
        return True, "rare_candy_level_up"
    
    if effect["type"] == "stat_boost":
        stat = effect["stat"]
        pokemon_stats[stat] += effect["value"]
        return True, f"Boosted {stat.upper()} by {effect['value']}!"

    if effect["type"] == "pp_restore":
        moves = [m for m in pokemon_stats.get("moves", [])]
        if not moves:
            return False, "No moves to restore PP for."
        pp = pokemon_stats.get("pp", {})
        for move in moves:
            current = pp.get(move, 0)
            max_pp = MOVES.get(move, {}).get("pp", 15)
            if current < max_pp:
                restored = min(effect["value"], max_pp - current)
                pp[move] = current + restored
                return True, f"Restored {restored} PP to {move}!"
        return False, "All moves are already at full PP."

    if effect["type"] == "pp_restore_all":
        pp = pokemon_stats.get("pp", {})
        total_restored = 0
        for move in list(pp.keys()):
            max_pp = MOVES.get(move, {}).get("pp", 15)
            current = pp[move]
            if effect["value"] == "max":
                restored = max_pp - current
            else:
                restored = min(effect["value"], max_pp - current)
            pp[move] = current + restored
            total_restored += restored
        return True, f"Restored {total_restored} PP total!"

    if effect["type"] == "cure_status":
        if pokemon_stats.get("status"):
            pokemon_stats["status"] = None
            return True, "Status condition cured!"
        return False, "No status condition to cure."

    if effect["type"] == "revive":
        if pokemon_stats.get("hp", 0) > 0:
            return False, "Pokemon is not fainted!"
        heal_hp = int(pokemon_stats.get("maxhp", 100) * effect["value"])
        pokemon_stats["hp"] = heal_hp
        return True, f"Revived with {heal_hp} HP!"

    return False, "This item cannot be used here."
