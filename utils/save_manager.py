import json
import os

SAVE_FILE = "save_game.json"

def save_game(name, pokemon, money, heal_tickets, trophies, inventory, location, badges=None, tower_record=0, pokedex_seen=None, pokedex_caught=None, elite_four_defeated=None, achievements=None, daycare=None):
    if badges is None: badges = []
    if pokedex_seen is None: pokedex_seen = set()
    if pokedex_caught is None: pokedex_caught = set()
    if elite_four_defeated is None: elite_four_defeated = []
    if achievements is None: achievements = {}
    if daycare is None: daycare = {"slots": [], "steps": 0, "egg_waiting": False}
    state = {
        "name": name,
        "pokemon": pokemon,
        "money": money,
        "heal_tickets": heal_tickets,
        "trophies": trophies,
        "inventory": inventory,
        "location": location,
        "badges": badges,
        "tower_record": tower_record,
        "pokedex_seen": list(pokedex_seen),
        "pokedex_caught": list(pokedex_caught),
        "elite_four_defeated": elite_four_defeated,
        "achievements": achievements,
        "daycare": daycare
    }
    try:
        with open(SAVE_FILE, 'w') as f:
            json.dump(state, f, indent=4)
        return True
    except Exception as e:
        print(f"Failed to save game: {e}")
        return False

def load_game():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, 'r') as f:
                data = json.load(f)
                if "pokedex_seen" not in data:
                    data["pokedex_seen"] = []
                if "pokedex_caught" not in data:
                    data["pokedex_caught"] = []
                if "elite_four_defeated" not in data:
                    data["elite_four_defeated"] = []
                if "achievements" not in data:
                    data["achievements"] = {"unlocked": [], "counters": {}}
                if "heal_tickets" not in data:
                    data["heal_tickets"] = 50
                if "daycare" not in data:
                    data["daycare"] = {"slots": [], "steps": 0, "egg_waiting": False}
                for pname, pdata in data.get("pokemon", {}).items():
                    if "ability" not in pdata:
                        pdata["ability"] = None
                    if "hold_item" not in pdata:
                        pdata["hold_item"] = None
                return data
        except Exception as e:
            print(f"Failed to load game: {e}")
            return None
    return None
