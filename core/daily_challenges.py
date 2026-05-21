"""
Daily Challenge System
- Rotating daily spawns with bonus XP
- Daily raid boss with escalating rewards
- Login streak bonuses
"""
import random
import time
from datetime import datetime, timedelta

# Seed daily challenges based on date so they rotate daily
def get_daily_seed():
    """Get a seed based on the current date for consistent daily challenges."""
    today = datetime.now().strftime("%Y-%m-%d")
    return hash(today) % (2**32)

def get_daily_challenge():
    """Get today's daily challenge. Returns consistent results for the same day."""
    seed = get_daily_seed()
    rng = random.Random(seed)
    
    # Daily spawn rotation - bonus XP for catching specific species
    all_species = [
        "Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Eevee",
        "Gengar", "Dragonite", "Snorlax", "Lapras", "Mewtwo",
        "Lucario", "Garchomp", "Salamence", "Tyranitar", "Metagross",
        "Rayquaza", "Gardevoir", "Blaziken", "Swampert", "Aggron",
        "Gyarados", "Alakazam", "Machamp", "Golem", "Arcanine",
        "Ninetales", "Scizor", "Heracross", "Houndoom", "Ursaring"
    ]
    
    # Pick 3 daily species
    daily_species = rng.sample(all_species, 3)
    
    # Daily raid boss
    raid_bosses = [
        {"name": "Mewtwo", "type": "Psychic", "level": 80, "hp_mult": 15, "dm_mult": 4,
         "reward": {"coins": 10000, "trophies": 5000, "item": "Mewtwonite Y"}},
        {"name": "Rayquaza", "type": "Dragon", "level": 85, "hp_mult": 18, "dm_mult": 4.5,
         "reward": {"coins": 12000, "trophies": 6000, "item": "Meteorite"}},
        {"name": "Groudon", "type": "Ground", "level": 80, "hp_mult": 20, "dm_mult": 3.5,
         "reward": {"coins": 10000, "trophies": 5000, "item": "Red Orb"}},
        {"name": "Kyogre", "type": "Water", "level": 80, "hp_mult": 20, "dm_mult": 3.5,
         "reward": {"coins": 10000, "trophies": 5000, "item": "Blue Orb"}},
        {"name": "Dialga", "type": "Steel", "level": 85, "hp_mult": 16, "dm_mult": 4,
         "reward": {"coins": 11000, "trophies": 5500, "item": "Adamant Orb"}},
        {"name": "Palkia", "type": "Water", "level": 85, "hp_mult": 16, "dm_mult": 4,
         "reward": {"coins": 11000, "trophies": 5500, "item": "Lustrous Orb"}},
        {"name": "Giratina", "type": "Ghost", "level": 90, "hp_mult": 22, "dm_mult": 5,
         "reward": {"coins": 15000, "trophies": 7000, "item": "Griseous Orb"}},
        {"name": "Arceus", "type": "Normal", "level": 100, "hp_mult": 25, "dm_mult": 5,
         "reward": {"coins": 20000, "trophies": 10000, "item": "Legend Plate"}},
    ]
    
    # Pick 1 daily raid boss
    daily_raid = rng.choice(raid_bosses)
    
    # Daily bonus type (bonus coins for using this type)
    all_types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting",
                 "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost",
                 "Dragon", "Dark", "Steel", "Fairy"]
    daily_bonus_type = rng.choice(all_types)
    
    return {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "daily_species": daily_species,
        "daily_raid": daily_raid,
        "daily_bonus_type": daily_bonus_type,
        "xp_bonus": 2.0,  # 2x XP for daily species
        "coin_bonus": 1.5,  # 1.5x coins for bonus type
    }

def get_login_streak(last_login_date):
    """Calculate login streak based on last login date."""
    if not last_login_date:
        return 1  # First login
    
    try:
        last = datetime.strptime(last_login_date, "%Y-%m-%d").date()
        today = datetime.now().date()
        diff = (today - last).days
        
        if diff == 1:
            # Consecutive day - streak continues
            return None  # Will be incremented by caller
        elif diff == 0:
            # Same day - streak unchanged
            return None
        else:
            # Missed days - streak resets
            return 1
    except:
        return 1

def get_streak_bonus(streak):
    """Get bonus rewards based on login streak."""
    if streak >= 30:
        return {"coins": 5000, "tickets": 20, "item": "Master Ball", "desc": "30-Day Streak!"}
    elif streak >= 21:
        return {"coins": 3000, "tickets": 15, "item": "Ultra Ball x5", "desc": "21-Day Streak!"}
    elif streak >= 14:
        return {"coins": 2000, "tickets": 10, "item": "Shiny Charm", "desc": "14-Day Streak!"}
    elif streak >= 7:
        return {"coins": 1000, "tickets": 5, "item": "Rare Candy", "desc": "7-Day Streak!"}
    elif streak >= 3:
        return {"coins": 500, "tickets": 3, "item": "Potion x3", "desc": "3-Day Streak!"}
    else:
        return {"coins": 100, "tickets": 1, "item": None, "desc": "Daily Login!"}

def check_daily_species_catch(species_name, daily_species):
    """Check if caught species is a daily species. Returns XP multiplier."""
    for ds in daily_species:
        if ds.lower() in species_name.lower():
            return 2.0  # 2x XP bonus
    return 1.0

def check_type_bonus(move_type, daily_bonus_type):
    """Check if move type matches daily bonus type. Returns coin multiplier."""
    if move_type == daily_bonus_type:
        return 1.5  # 1.5x coin bonus
    return 1.0
