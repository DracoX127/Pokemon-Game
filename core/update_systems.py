"""Large update systems for the Pokemon terminal RPG.

This module keeps the new feature work out of the already-large main loop:
notifications, battle recaps, catch grading, drops, TM crafting, fusion
preview/stability, personality traits, bond, world events, base building,
reputation, NPC trainers, Professor advice, and codex research.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
import hashlib
import random
import time


PERSONALITY_TRAITS = {
    "Brave": {
        "battle_mult": 1.06,
        "speed_mult": 0.98,
        "bond_gain": 2,
        "drop_bonus": 0.00,
        "note": "hits harder when the battle gets loud",
    },
    "Calm": {
        "battle_mult": 1.00,
        "speed_mult": 1.00,
        "bond_gain": 1,
        "drop_bonus": 0.04,
        "note": "keeps rewards and risky fights steady",
    },
    "Curious": {
        "battle_mult": 1.01,
        "speed_mult": 1.02,
        "bond_gain": 2,
        "drop_bonus": 0.08,
        "note": "finds more materials after battles",
    },
    "Loyal": {
        "battle_mult": 1.02,
        "speed_mult": 1.00,
        "bond_gain": 3,
        "drop_bonus": 0.02,
        "note": "bonds quickly and resists bad luck",
    },
    "Reckless": {
        "battle_mult": 1.10,
        "speed_mult": 1.03,
        "bond_gain": 1,
        "drop_bonus": -0.02,
        "note": "big damage, rough edges",
    },
    "Genius": {
        "battle_mult": 1.04,
        "speed_mult": 1.04,
        "bond_gain": 2,
        "drop_bonus": 0.05,
        "note": "learns and adapts quickly",
    },
    "Lazy": {
        "battle_mult": 0.96,
        "speed_mult": 0.94,
        "bond_gain": 1,
        "drop_bonus": 0.10,
        "note": "slow starter, surprisingly good at finding stuff",
    },
    "Focused": {
        "battle_mult": 1.05,
        "speed_mult": 1.01,
        "bond_gain": 2,
        "drop_bonus": 0.03,
        "note": "consistent in long fights",
    },
}


BOND_TITLES = [
    (0, "New Partner"),
    (20, "Trusted"),
    (50, "Close"),
    (90, "Devoted"),
    (140, "Soulbound"),
]


TYPE_MATERIALS = {
    "Normal": "Plain Thread",
    "Fire": "Ember Shard",
    "Water": "Tide Pearl",
    "Grass": "Bloom Resin",
    "Electric": "Spark Shard",
    "Ice": "Frost Crystal",
    "Fighting": "Valor Wrap",
    "Poison": "Toxin Sac",
    "Ground": "Terra Dust",
    "Flying": "Sky Feather",
    "Psychic": "Mind Shard",
    "Bug": "Silk Thread",
    "Rock": "Stone Core",
    "Ghost": "Wisp Cloth",
    "Dragon": "Dragon Scale",
    "Dark": "Umbral Fang",
    "Steel": "Steel Plate",
    "Fairy": "Glimmer Dust",
}


COMMON_DROPS = ["TM Shard", "Battle Scrap", "Stardust", "Medicinal Herb"]


TM_RECIPES = {
    "Thunderbolt": {
        "item": "TM: Thunderbolt",
        "ingredients": {"Spark Shard": 3, "TM Shard": 2, "Battle Scrap": 1},
        "coin_cost": 350,
        "difficulty": "advanced",
    },
    "Flamethrower": {
        "item": "TM: Flamethrower",
        "ingredients": {"Ember Shard": 3, "TM Shard": 2, "Stardust": 1},
        "coin_cost": 350,
        "difficulty": "advanced",
    },
    "Surf": {
        "item": "TM: Surf",
        "ingredients": {"Tide Pearl": 3, "TM Shard": 2, "Medicinal Herb": 1},
        "coin_cost": 350,
        "difficulty": "advanced",
    },
    "Giga Drain": {
        "item": "TM: Giga Drain",
        "ingredients": {"Bloom Resin": 3, "TM Shard": 2, "Medicinal Herb": 2},
        "coin_cost": 325,
        "difficulty": "advanced",
    },
    "Ice Beam": {
        "item": "TM: Ice Beam",
        "ingredients": {"Frost Crystal": 3, "TM Shard": 2, "Stardust": 1},
        "coin_cost": 375,
        "difficulty": "advanced",
    },
    "Dragon Pulse": {
        "item": "TM: Dragon Pulse",
        "ingredients": {"Dragon Scale": 2, "Mind Shard": 1, "TM Shard": 3},
        "coin_cost": 500,
        "difficulty": "expert",
    },
    "Shadow Ball": {
        "item": "TM: Shadow Ball",
        "ingredients": {"Wisp Cloth": 3, "Umbral Fang": 1, "TM Shard": 2},
        "coin_cost": 450,
        "difficulty": "expert",
    },
    "Earthquake": {
        "item": "TM: Earthquake",
        "ingredients": {"Terra Dust": 4, "Stone Core": 2, "TM Shard": 3},
        "coin_cost": 600,
        "difficulty": "expert",
    },
}


FUSION_STABILITIES = {
    "Perfect": {"stat_mult": 1.28, "damage_mult": 1.08, "risk": 0.00},
    "Stable": {"stat_mult": 1.15, "damage_mult": 1.03, "risk": 0.00},
    "Volatile": {"stat_mult": 1.30, "damage_mult": 1.10, "risk": 0.08},
    "Chaotic": {"stat_mult": 1.45, "damage_mult": 1.16, "risk": 0.15},
    "Fractured": {"stat_mult": 0.92, "damage_mult": 0.96, "risk": 0.05},
}


MUTATION_PATHS = {
    "Radiant": {"stat_mult": 1.10, "note": "bonus HP and cleaner stability"},
    "Ancient": {"stat_mult": 1.12, "note": "higher damage and lore value"},
    "Mega": {"stat_mult": 1.18, "note": "rare burst of battle power"},
    "Corrupted": {"stat_mult": 1.25, "note": "huge stats with volatile behavior"},
    "None": {"stat_mult": 1.00, "note": "standard fusion pattern"},
}


BASE_ROOMS = {
    "Lab": {
        "desc": "Improves fusion previews and mutation odds.",
        "cost": {"coins": 700, "materials": {"TM Shard": 2, "Spark Shard": 1}},
    },
    "Workshop": {
        "desc": "Improves TM crafting and reduces crafting coin costs.",
        "cost": {"coins": 650, "materials": {"Battle Scrap": 3, "Steel Plate": 1}},
    },
    "Trophy Hall": {
        "desc": "Boosts reputation gains from gyms, raids, and ranked battles.",
        "cost": {"coins": 800, "materials": {"Stardust": 2, "Glimmer Dust": 1}},
    },
    "Greenhouse": {
        "desc": "Increases passive healing and herb rewards.",
        "cost": {"coins": 600, "materials": {"Bloom Resin": 2, "Medicinal Herb": 3}},
    },
    "Raid Board": {
        "desc": "Improves what-now suggestions and event notifications.",
        "cost": {"coins": 900, "materials": {"Dragon Scale": 1, "Battle Scrap": 4}},
    },
    "Fusion Reactor": {
        "desc": "Unlocks stronger stability outcomes for high-bond parents.",
        "cost": {"coins": 1200, "materials": {"Stone Core": 2, "Wisp Cloth": 1, "Spark Shard": 2}},
    },
}


FACTIONS = {
    "Champion": "Win battles, gyms, and raids.",
    "Collector": "Catch Pokemon and complete research.",
    "Scientist": "Craft TMs and perform fusions.",
    "Breeder": "Use daycare, hatch eggs, and build bonds.",
    "Raider": "Clear raids, dungeons, and frontier facilities.",
    "Fusion Scholar": "Create stable, rare, and mutated fusions.",
}


SEASONAL_EVENTS = [
    {
        "name": "Shiny Storm",
        "condition": lambda now: now.day % 10 == 0,
        "desc": "Wild shiny odds feel charged today.",
        "bonus": "Shiny chains are worth more.",
    },
    {
        "name": "Fusion Festival",
        "condition": lambda now: now.day % 7 in (2, 5),
        "desc": "Fusion Lab outcomes lean more stable.",
        "bonus": "Better fusion preview confidence.",
    },
    {
        "name": "Raid Surge",
        "condition": lambda now: now.weekday() in (4, 5, 6),
        "desc": "Raid boards are busy all weekend.",
        "bonus": "More raid and trainer notifications.",
    },
    {
        "name": "Workshop Rush",
        "condition": lambda now: now.day % 3 == 0,
        "desc": "Crafters are trading spare TM parts.",
        "bonus": "TM crafting feels cheaper to plan.",
    },
]


TRAINER_ARCHETYPES = [
    {"title": "Ace Trainer", "persona": "Tactical", "types": ["Dragon", "Steel", "Electric"]},
    {"title": "Fusion Mystic", "persona": "Trickster", "types": ["Psychic", "Ghost", "Fairy"]},
    {"title": "Roughneck", "persona": "Bully", "types": ["Fighting", "Dark", "Rock"]},
    {"title": "Field Researcher", "persona": "Support", "types": ["Grass", "Water", "Bug"]},
    {"title": "Speedrunner", "persona": "Hyper-Offense", "types": ["Flying", "Electric", "Fire"]},
    {"title": "Wallmaker", "persona": "Staller", "types": ["Steel", "Water", "Ground"]},
]


@dataclass
class BattleRecap:
    mode: str
    enemies: list[str]
    started_at: float = field(default_factory=time.time)
    turns: int = 0
    events: list[str] = field(default_factory=list)
    drops: list[dict] = field(default_factory=list)
    xp: dict = field(default_factory=dict)
    money: int = 0
    won: bool = False


def _stable_int(*parts) -> int:
    raw = "|".join(str(p) for p in parts)
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    return int(digest[:12], 16)


def clamp(value, low, high):
    return max(low, min(high, value))


def choose_personality(name=None, type_name="Normal", shiny=False):
    traits = list(PERSONALITY_TRAITS)
    idx = _stable_int(name or "unknown", type_name, shiny) % len(traits)
    return traits[idx]


def get_bond_title(points):
    title = BOND_TITLES[0][1]
    for threshold, candidate in BOND_TITLES:
        if points >= threshold:
            title = candidate
    return title


def ensure_pokemon_profile(stats, name=None, type_name=None):
    """Add new-system metadata to a Pokemon dict without breaking old saves."""
    type_name = type_name or stats.get("type", "Normal")
    if "personality" not in stats:
        stats["personality"] = choose_personality(name, type_name, stats.get("shiny", False))
    if "bond" not in stats:
        stats["bond"] = {"points": 0, "title": get_bond_title(0), "clutch_used": False}
    else:
        points = int(stats["bond"].get("points", 0))
        stats["bond"]["title"] = get_bond_title(points)
        stats["bond"].setdefault("clutch_used", False)
    stats.setdefault("research", {"caught_grades": [], "battles": 0, "fusions": 0})
    stats.setdefault("fusion_stability", "Stable" if stats.get("generation", 0) else "Natural")
    stats.setdefault("fusion_mutation", "None")
    stats.setdefault("origin_note", "Met during your journey")
    return stats


def trait_damage_multiplier(stats):
    trait = stats.get("personality")
    return PERSONALITY_TRAITS.get(trait, {}).get("battle_mult", 1.0)


def fusion_damage_multiplier(stats):
    stability = stats.get("fusion_stability", "Natural")
    if stability == "Natural":
        return 1.0
    mult = FUSION_STABILITIES.get(stability, {}).get("damage_mult", 1.0)
    mutation = stats.get("fusion_mutation", "None")
    if mutation == "Corrupted":
        mult *= 1.04
    elif mutation == "Mega":
        mult *= 1.05
    elif mutation == "Radiant":
        mult *= 1.02
    return mult


def bond_damage_multiplier(stats):
    points = stats.get("bond", {}).get("points", 0)
    if points >= 140:
        return 1.08
    if points >= 90:
        return 1.05
    if points >= 50:
        return 1.03
    return 1.0


def total_damage_multiplier(stats):
    return trait_damage_multiplier(stats) * fusion_damage_multiplier(stats) * bond_damage_multiplier(stats)


def add_bond(stats, amount, reason="battle"):
    ensure_pokemon_profile(stats)
    trait = stats.get("personality", "Calm")
    gain = amount + PERSONALITY_TRAITS.get(trait, {}).get("bond_gain", 1)
    stats["bond"]["points"] = clamp(int(stats["bond"].get("points", 0)) + gain, 0, 999)
    stats["bond"]["title"] = get_bond_title(stats["bond"]["points"])
    stats["bond"]["last_reason"] = reason
    if stats.get("hp", 1) >= stats.get("maxhp", 1):
        stats["bond"]["clutch_used"] = False
    return stats["bond"]


def maybe_bond_clutch_survival(stats, damage):
    """High-bond Pokemon can survive lethal damage once between full heals."""
    ensure_pokemon_profile(stats)
    hp = stats.get("hp", 0)
    if damage < hp:
        return False, ""
    bond = stats.get("bond", {})
    points = bond.get("points", 0)
    if points < 90 or bond.get("clutch_used"):
        return False, ""
    chance = 0.10 + min(0.25, (points - 90) / 400.0)
    if random.random() <= chance:
        stats["hp"] = 1
        bond["clutch_used"] = True
        return True, f"{stats.get('name', 'Pokemon')} endured the hit through bond!"
    return False, ""


def calculate_catch_grade(context):
    hp_ratio = clamp(float(context.get("hp_ratio", 1.0)), 0.0, 1.0)
    probability = clamp(float(context.get("catch_probability", 40)), 1.0, 100.0)
    attempts = max(1, int(context.get("attempts", 1)))
    status_bonus = 8 if context.get("status") else 0
    shiny_bonus = 8 if context.get("shiny") else 0
    throw_rating = context.get("throw_rating") or "RAW"

    score = 35
    score += int((1.0 - hp_ratio) * 35)
    score += int(probability / 5)
    score += status_bonus + shiny_bonus
    score -= max(0, attempts - 1) * 7
    if throw_rating == "PERFECT":
        score += 18
    elif throw_rating == "GREAT":
        score += 12
    elif throw_rating == "GOOD":
        score += 6
    elif throw_rating == "MISS":
        score -= 10

    score = clamp(score, 0, 120)
    if score >= 105:
        grade = "SS"
    elif score >= 90:
        grade = "S"
    elif score >= 75:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 45:
        grade = "C"
    else:
        grade = "D"
    return {
        "grade": grade,
        "score": int(score),
        "hp_ratio": round(hp_ratio, 3),
        "attempts": attempts,
        "throw_rating": throw_rating,
    }


def catch_grade_rewards(grade_info, type_name="Normal", shiny=False):
    grade = grade_info["grade"]
    table = {
        "SS": {"coins": 700, "items": {"Rare Candy": 1, "TM Shard": 3}},
        "S": {"coins": 450, "items": {"Rare Candy": 1, "TM Shard": 2}},
        "A": {"coins": 275, "items": {"TM Shard": 2}},
        "B": {"coins": 125, "items": {"TM Shard": 1}},
        "C": {"coins": 50, "items": {"Medicinal Herb": 1}},
        "D": {"coins": 0, "items": {}},
    }
    reward = {"coins": table[grade]["coins"], "items": dict(table[grade]["items"])}
    material = TYPE_MATERIALS.get(type_name, "Plain Thread")
    if grade in ("A", "S", "SS"):
        reward["items"][material] = reward["items"].get(material, 0) + (2 if grade == "SS" else 1)
    if shiny:
        reward["items"]["Stardust"] = reward["items"].get("Stardust", 0) + 2
    return reward


def apply_reward_bundle(inventory, reward):
    for item, qty in reward.get("items", {}).items():
        inventory[item] = inventory.get(item, 0) + qty
    return reward.get("coins", 0)


def generate_item_drops(species, type_name="Normal", level=1, shiny=False, grade=None, victory=True, trait=None):
    if not victory:
        return []
    level = max(1, int(level or 1))
    base_chance = 0.38 + min(0.25, level / 200.0)
    if shiny:
        base_chance += 0.20
    if grade in ("A", "S", "SS"):
        base_chance += {"A": 0.08, "S": 0.16, "SS": 0.25}[grade]
    if trait:
        base_chance += PERSONALITY_TRAITS.get(trait, {}).get("drop_bonus", 0.0)

    drops = []
    material = TYPE_MATERIALS.get(type_name, "Plain Thread")
    if random.random() < clamp(base_chance, 0.05, 0.95):
        qty = 1 + (1 if level >= 30 else 0) + (1 if shiny else 0)
        drops.append({"item": material, "qty": qty, "source": species})
    if random.random() < clamp(base_chance * 0.65, 0.02, 0.80):
        drops.append({"item": random.choice(COMMON_DROPS), "qty": 1, "source": species})
    if grade in ("S", "SS") and random.random() < 0.35:
        drops.append({"item": "Rare Candy", "qty": 1, "source": f"{grade} grade bonus"})
    return drops


def apply_item_drops(inventory, drops):
    for drop in drops:
        item = drop["item"]
        qty = int(drop.get("qty", 1))
        inventory[item] = inventory.get(item, 0) + qty
    return drops


def format_drops(drops):
    if not drops:
        return "No material drops."
    return ", ".join(f"{d['qty']}x {d['item']}" for d in drops)


def can_craft_tm(inventory, move_name, coins=0, base=None):
    recipe = TM_RECIPES.get(move_name)
    if not recipe:
        return False, "Unknown TM recipe."
    discount = get_base_bonus(base).get("tm_discount", 0)
    coin_cost = max(0, int(recipe["coin_cost"] * (1 - discount)))
    if coins < coin_cost:
        return False, f"Need {coin_cost} coins."
    missing = []
    for item, qty in recipe["ingredients"].items():
        if inventory.get(item, 0) < qty:
            missing.append(f"{item} x{qty - inventory.get(item, 0)}")
    if missing:
        return False, "Missing " + ", ".join(missing)
    return True, "Ready"


def craft_tm(inventory, move_name, coins=0, base=None):
    ok, msg = can_craft_tm(inventory, move_name, coins, base)
    if not ok:
        return False, coins, msg
    recipe = TM_RECIPES[move_name]
    discount = get_base_bonus(base).get("tm_discount", 0)
    coin_cost = max(0, int(recipe["coin_cost"] * (1 - discount)))
    for item, qty in recipe["ingredients"].items():
        inventory[item] -= qty
        if inventory[item] <= 0:
            del inventory[item]
    tm_item = recipe["item"]
    inventory[tm_item] = inventory.get(tm_item, 0) + 1
    return True, coins - coin_cost, f"Crafted {tm_item}"


def teach_tm_from_inventory(inventory, pokemon_stats, move_name):
    tm_item = f"TM: {move_name}"
    if inventory.get(tm_item, 0) <= 0:
        return False, f"You do not have {tm_item}."
    moves = pokemon_stats.setdefault("moves", [])
    if move_name in moves:
        return False, f"Already knows {move_name}."
    if len(moves) >= 4:
        return False, "Move slots full. Use the Move Relearner replacement flow."
    moves.append(move_name)
    pokemon_stats.setdefault("pp", {})[move_name] = 15
    inventory[tm_item] -= 1
    if inventory[tm_item] <= 0:
        del inventory[tm_item]
    return True, f"Learned {move_name}."


def _type_tokens(type_name):
    if isinstance(type_name, (list, tuple, set)):
        return {str(t) for t in type_name}
    return {part.strip() for part in str(type_name).replace("/", ",").split(",") if part.strip()}


def type_synergy(type_a, type_b):
    a = _type_tokens(type_a)
    b = _type_tokens(type_b)
    if a & b:
        return 18
    combos = [
        {"Fire", "Dragon"},
        {"Water", "Ice"},
        {"Grass", "Poison"},
        {"Electric", "Steel"},
        {"Psychic", "Fairy"},
        {"Ghost", "Dark"},
        {"Rock", "Ground"},
    ]
    for combo in combos:
        if a | b <= combo or combo <= a | b:
            return 12
    return 4


def preview_fusion(name1, stats1, name2, stats2, fusion_dex=None, base=None):
    part1 = name1.lower()[: max(1, len(name1) // 2)]
    part2 = name2.lower()[len(name2) // 2 :]
    fusion_name = (part1 + part2).capitalize()

    avg_hp = (stats1.get("maxhp", stats1.get("hp", 50)) + stats2.get("maxhp", stats2.get("hp", 50))) // 2
    avg_dm = (stats1.get("dm", 20) + stats2.get("dm", 20)) // 2
    avg_speed = (stats1.get("speed", 50) + stats2.get("speed", 50)) // 2
    moves = list(dict.fromkeys(stats1.get("moves", ["Tackle"]) + stats2.get("moves", ["Tackle"])))[:4]
    type_name = stats1.get("type", "Normal")

    if fusion_dex:
        dex = fusion_dex.get(fusion_name.lower())
        if dex:
            avg_hp = dex.get("hp", avg_hp)
            avg_dm = dex.get("dm", avg_dm)
            avg_speed = dex.get("speed", avg_speed)
            type_name = dex.get("type", type_name)
            moves = list(dex.get("moves", moves))[:4]

    bond_score = stats1.get("bond", {}).get("points", 0) + stats2.get("bond", {}).get("points", 0)
    gen = max(stats1.get("generation", 0), stats2.get("generation", 0)) + 1
    synergy = type_synergy(stats1.get("type", "Normal"), stats2.get("type", "Normal"))
    lab_bonus = get_base_bonus(base).get("fusion_stability", 0)
    stability_score = 42 + synergy + min(25, bond_score // 8) + int(lab_bonus * 100) - (gen - 1) * 7

    if stability_score >= 88:
        stability = "Perfect"
    elif stability_score >= 66:
        stability = "Stable"
    elif stability_score >= 46:
        stability = "Volatile"
    elif stability_score >= 28:
        stability = "Chaotic"
    else:
        stability = "Fractured"

    mutation_chance = clamp(0.04 + bond_score / 1000.0 + get_base_bonus(base).get("mutation_chance", 0), 0.04, 0.35)
    mutation_hint = "possible" if mutation_chance >= 0.12 else "rare"
    rank_score = int((avg_hp / 10) + avg_dm + (avg_speed / 3) + stability_score)
    if rank_score >= 240:
        rank = "S"
    elif rank_score >= 190:
        rank = "A"
    elif rank_score >= 145:
        rank = "B"
    else:
        rank = "C"

    return {
        "name": fusion_name,
        "generation": gen,
        "base_hp": int(avg_hp),
        "base_dm": int(avg_dm),
        "base_speed": int(avg_speed),
        "type": type_name,
        "moves": moves,
        "stability": stability,
        "stability_score": int(clamp(stability_score, 0, 100)),
        "mutation_chance": mutation_chance,
        "mutation_hint": mutation_hint,
        "rank": rank,
    }


def roll_fusion_result(preview):
    stability = preview["stability"]
    stability_mult = FUSION_STABILITIES.get(stability, FUSION_STABILITIES["Stable"])["stat_mult"]
    mutation = "None"
    roll = random.random()
    if roll < preview.get("mutation_chance", 0.04):
        weighted = [
            ("Radiant", 35),
            ("Ancient", 28),
            ("Mega", 18),
            ("Corrupted", 12),
        ]
        total = sum(w for _, w in weighted)
        pick = random.randint(1, total)
        acc = 0
        for name, weight in weighted:
            acc += weight
            if pick <= acc:
                mutation = name
                break
    mutation_mult = MUTATION_PATHS[mutation]["stat_mult"]
    wobble = random.uniform(0.96, 1.08)
    final_mult = stability_mult * mutation_mult * wobble
    return {
        **preview,
        "hp": max(1, int(preview["base_hp"] * final_mult)),
        "dm": max(1, int(preview["base_dm"] * final_mult)),
        "speed": max(1, int(preview["base_speed"] * final_mult)),
        "mutation": mutation,
        "final_mult": final_mult,
        "mutation_note": MUTATION_PATHS[mutation]["note"],
    }


def new_battle_recap(mode, enemies):
    return BattleRecap(mode=mode or "Battle", enemies=list(enemies or []))


def record_battle_event(recap, event):
    if isinstance(recap, BattleRecap) and event:
        recap.events.append(str(event))


def get_battle_commentary(event, **kwargs):
    if event == "super_effective":
        return f"Professor: Clean read. {kwargs.get('move', 'That move')} hit the matchup perfectly."
    if event == "crit":
        return "Professor: Critical hit. That momentum swing matters."
    if event == "low_hp":
        return f"Professor: {kwargs.get('name', 'Your Pokemon')} is in danger. Heal, switch, or finish fast."
    if event == "faint":
        return f"Professor: {kwargs.get('name', 'The target')} fainted. Good pressure."
    if event == "resisted":
        return "Professor: Low impact hit. Consider a different type next turn."
    return ""


def finish_battle_recap(recap, won, xp=None, money=0, drops=None):
    if not isinstance(recap, BattleRecap):
        return recap
    recap.won = bool(won)
    recap.xp = dict(xp or {})
    recap.money = int(money or 0)
    recap.drops = list(drops or [])
    return recap


def render_battle_recap(recap):
    if not isinstance(recap, BattleRecap):
        return []
    lines = [
        "BATTLE RECAP",
        f"Mode: {recap.mode}",
        f"Result: {'Victory' if recap.won else 'Defeat'}",
        f"Turns: {recap.turns}",
    ]
    if recap.xp:
        lines.append("XP: " + ", ".join(f"{k}+{v}" for k, v in recap.xp.items()))
    if recap.money:
        lines.append(f"Coins: +{recap.money}")
    if recap.drops:
        lines.append("Drops: " + format_drops(recap.drops))
    if recap.events:
        lines.append("Highlights:")
        for event in recap.events[-5:]:
            lines.append(f"- {event}")
    return lines


class NotificationCenter:
    def __init__(self, poll_interval=5):
        self.poll_interval = poll_interval
        self.last_poll = 0.0
        self.items = []
        self.counter = 0

    def notify(self, title, body, kind="info"):
        self.counter += 1
        self.items.insert(
            0,
            {
                "id": self.counter,
                "title": str(title),
                "body": str(body),
                "kind": kind,
                "time": datetime.now().strftime("%H:%M:%S"),
            },
        )
        self.items = self.items[:12]

    def poll(self, state, force=False):
        now = time.time()
        if not force and now - self.last_poll < self.poll_interval:
            return []
        self.last_poll = now
        generated = []

        team = state.get("pokemon", {})
        low_hp = [
            name
            for name, stats in team.items()
            if stats.get("maxhp", 0) and 0 < stats.get("hp", 0) <= stats.get("maxhp", 1) * 0.25
        ]
        if low_hp:
            generated.append(("Low HP", f"Heal {', '.join(low_hp[:3])} soon.", "danger"))

        if state.get("daycare", {}).get("egg_waiting"):
            generated.append(("Egg Ready", "Daycare has an egg waiting.", "reward"))

        daily = state.get("daily_challenge", {})
        species = daily.get("daily_species") or []
        if species:
            generated.append(("Daily Target", f"Catch {species[0]} for bonus XP.", "quest"))

        for event in get_active_seasonal_events()[:1]:
            generated.append(("World Event", f"{event['name']}: {event['bonus']}", "event"))

        suggestion = get_what_now_recommendations(state, limit=1)
        if suggestion:
            generated.append(("What Now", suggestion[0], "tip"))

        for title, body, kind in generated:
            key = (title, body)
            if not any((item["title"], item["body"]) == key for item in self.items[:5]):
                self.notify(title, body, kind)
        return generated

    def render(self, max_items=5):
        lines = ["REALTIME NOTIFICATIONS"]
        if not self.items:
            lines.append("No alerts yet. Polling every 5s.")
            return lines
        for item in self.items[:max_items]:
            lines.append(f"[{item['time']}] {item['title']}: {item['body']}")
        return lines


def create_default_base():
    return {"rooms": {name: 0 for name in BASE_ROOMS}, "upgrades": 0}


def create_default_reputation():
    return {name: 0 for name in FACTIONS}


def get_base_bonus(base):
    base = base or create_default_base()
    rooms = base.get("rooms", {})
    return {
        "fusion_stability": rooms.get("Lab", 0) * 0.03 + rooms.get("Fusion Reactor", 0) * 0.04,
        "mutation_chance": rooms.get("Fusion Reactor", 0) * 0.025,
        "tm_discount": min(0.35, rooms.get("Workshop", 0) * 0.06),
        "rep_bonus": rooms.get("Trophy Hall", 0) * 0.04,
        "greenhouse_heal": rooms.get("Greenhouse", 0) * 0.01,
        "notification_depth": 5 + rooms.get("Raid Board", 0),
    }


def can_upgrade_room(base, inventory, coins, room):
    if room not in BASE_ROOMS:
        return False, "Unknown room."
    level = base.get("rooms", {}).get(room, 0)
    cost_data = BASE_ROOMS[room]["cost"]
    coin_cost = cost_data["coins"] * (level + 1)
    if coins < coin_cost:
        return False, f"Need {coin_cost} coins."
    missing = []
    for item, qty in cost_data["materials"].items():
        need = qty * (level + 1)
        if inventory.get(item, 0) < need:
            missing.append(f"{item} x{need - inventory.get(item, 0)}")
    if missing:
        return False, "Missing " + ", ".join(missing)
    return True, "Ready"


def upgrade_room(base, inventory, coins, room):
    ok, msg = can_upgrade_room(base, inventory, coins, room)
    if not ok:
        return False, coins, msg
    base.setdefault("rooms", {})
    level = base["rooms"].get(room, 0)
    cost_data = BASE_ROOMS[room]["cost"]
    coin_cost = cost_data["coins"] * (level + 1)
    for item, qty in cost_data["materials"].items():
        need = qty * (level + 1)
        inventory[item] -= need
        if inventory[item] <= 0:
            del inventory[item]
    base["rooms"][room] = level + 1
    base["upgrades"] = base.get("upgrades", 0) + 1
    return True, coins - coin_cost, f"{room} upgraded to Lv {level + 1}."


def add_reputation(reputation, faction, amount, base=None):
    if faction not in FACTIONS:
        return reputation
    bonus = get_base_bonus(base).get("rep_bonus", 0)
    reputation[faction] = int(reputation.get(faction, 0) + amount * (1 + bonus))
    return reputation


def reputation_title(reputation):
    if not reputation:
        return "New Trainer"
    faction, points = max(reputation.items(), key=lambda item: item[1])
    if points >= 500:
        rank = "Legend"
    elif points >= 250:
        rank = "Master"
    elif points >= 100:
        rank = "Adept"
    elif points >= 30:
        rank = "Initiate"
    else:
        rank = "New"
    return f"{rank} {faction}"


def get_active_seasonal_events(now=None):
    now = now or datetime.now()
    return [event for event in SEASONAL_EVENTS if event["condition"](now)]


def get_what_now_recommendations(state, limit=4):
    recs = []
    team = state.get("pokemon", {})
    if not team:
        recs.append("Choose or buy a starter Pokemon.")
    elif any(stats.get("hp", 0) <= 0 for stats in team.values()):
        recs.append("Visit the hospital and revive fainted Pokemon.")
    elif any(stats.get("hp", 0) < stats.get("maxhp", 1) * 0.35 for stats in team.values()):
        recs.append("Heal before taking another serious battle.")

    badges = state.get("badges", [])
    if len(badges) < 8 and team:
        avg_lvl = sum(stats.get("lvl", 1) for stats in team.values()) / max(1, len(team))
        if avg_lvl >= (len(badges) + 1) * 2:
            recs.append("Try the next Gym Challenge.")
        else:
            recs.append("Catch, train, or craft a TM before the next gym.")

    inventory = state.get("inventory", {})
    if inventory.get("TM Shard", 0) >= 2:
        recs.append("Open the TM Workshop and craft a coverage move.")
    if len(team) >= 2:
        recs.append("Preview a Fusion Lab 2.0 result before committing.")
    if state.get("daycare", {}).get("egg_waiting"):
        recs.insert(0, "Claim the waiting Daycare egg.")
    if state.get("daily_challenge", {}).get("daily_species"):
        recs.append(f"Catch daily target {state['daily_challenge']['daily_species'][0]}.")

    seen = set()
    unique = []
    for rec in recs:
        if rec not in seen:
            unique.append(rec)
            seen.add(rec)
    return unique[:limit]


def professor_advice(state, question=""):
    recs = get_what_now_recommendations(state, limit=3)
    title = reputation_title(state.get("reputation", {}))
    caught = len(state.get("pokedex_caught", []))
    team = state.get("pokemon", {})
    strongest = "none"
    if team:
        strongest = max(team.items(), key=lambda item: item[1].get("dm", 0))[0]
    lines = [
        f"Professor: Current trainer profile: {title}.",
        f"Professor: Pokedex caught count is {caught}; strongest attacker appears to be {strongest}.",
    ]
    if question:
        lines.append(f"Professor: On '{question}', I would inspect team health, coverage, and materials first.")
    lines.extend(f"Professor recommends: {rec}" for rec in recs)
    return lines


def generate_npc_trainer(player_level=5, region="Grasslands", seed=None):
    rng = random.Random(seed if seed is not None else time.time())
    arch = rng.choice(TRAINER_ARCHETYPES)
    first_names = ["Rhea", "Jax", "Mina", "Orion", "Selene", "Kai", "Nova", "Iris"]
    name = f"{arch['title']} {rng.choice(first_names)}"
    team_size = 2 + min(3, max(0, player_level // 12))
    team = []
    for idx in range(team_size):
        typ = rng.choice(arch["types"])
        lvl = max(1, player_level + rng.randint(-2, 4))
        team.append(
            {
                "name": f"{typ.lower()} specialist {idx + 1}",
                "type": typ,
                "hp": 45 + lvl * 8,
                "dm": 18 + lvl * 4,
                "speed": 35 + lvl * 3,
                "lvl": lvl,
                "moves": ["Tackle", "Quick Attack"],
            }
        )
    return {
        "name": name,
        "persona": arch["persona"],
        "region": region,
        "team": team,
        "history": {"wins": 0, "losses": 0},
    }


def build_codex_entry(name, stats=None, caught=False, seen=False):
    stats = stats or {}
    research = stats.get("research", {})
    grades = research.get("caught_grades", [])
    best_grade = max(grades, default="None", key=lambda g: ["D", "C", "B", "A", "S", "SS"].index(g) if g in ["D", "C", "B", "A", "S", "SS"] else -1)
    return {
        "name": name,
        "status": "Caught" if caught else ("Seen" if seen else "Unknown"),
        "type": stats.get("type", "Unknown"),
        "personality": stats.get("personality", "Unknown"),
        "bond": stats.get("bond", {}).get("title", "Unknown"),
        "best_catch_grade": best_grade,
        "fusion_history": stats.get("research", {}).get("fusions", 0),
        "note": f"{name.capitalize()} research grade: {best_grade}.",
    }

