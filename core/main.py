import sys
import os

# Dynamic absolute path injection to allow all original imports to resolve cleanly from nested packages
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Check if we are running from inside core or root, and align BASE_DIR to root
if os.path.basename(BASE_DIR) == "core":
    BASE_DIR = os.path.dirname(BASE_DIR)

SUBFOLDERS = ["core", "ui", "data", "utils"]
for folder in SUBFOLDERS:
    full_path = os.path.join(BASE_DIR, folder)
    if full_path not in sys.path:
        sys.path.insert(0, full_path)

import random
import json
import subprocess
import time
import socket
import importlib.util

def check_and_install_packages():
    required = {"requests": "requests", "flask": "flask", "flask_bcrypt": "flask-bcrypt", "jwt": "pyjwt"}
    missing = {pkg: pip_name for pkg, pip_name in required.items() if importlib.util.find_spec(pkg) is None}
    if not missing:
        return True
    print(f"\n  ⚠️  Missing libraries: {', '.join(missing.values())}")
    print(f"  These are needed for cloud saves and online features.\n")
    ans = input("  Install them now? (y/n): ").strip().lower()
    if ans != "y":
        print(f"  {len(missing)} packages skipped. Cloud features will be disabled.\n")
        return False
    for pip_name in missing.values():
        print(f"  Installing {pip_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name, "--quiet"])
    print("\n  ✅ All packages installed!\n")
    return True

check_and_install_packages()

import requests

from pokemon_dex import weak_pokemon, moderately_strong_pokemon, strong_pokemon, ultra_strong_pokemon
from pokemon_shop_info import pokemonshop_starter, pokemonshop_competitive, pokemonshop_legends
from names import first_names, last_names
from game_functions import (
    get_wild_pokemon, get_arena_pokemon, calculate_move_damage, calculate_xp_gain,
    level_up_pokemon, heal_pokemon, train_pokemon, display_pokemon_stats,
    show_catch_animation, show_healing_animation, select_move_menu, use_item_menu,
    run_team_battle, get_max_pp, stage_multiplier, apply_stat_stage, reset_stages,
    has_pp, use_pp, struggle_damage, offer_to_learn_move, restore_all_pp, make_pokemon,
    get_eligible_learnset_moves, take_damage, clamp_hp,
    calculate_daycare_average_exp, calculate_breeding_compatibility, generate_egg_data, run_dungeon_raid
)
from weather_engine import get_random_weather, apply_weather_damage
from status_manager import apply_status_tick, can_attack
from gym_data import GYM_LEADERS, ELITE_FOUR
from world_map import REGIONS
from fusion_dex import FUSION_DEX
from moves_data import MOVES
from inventory import ITEMS
from ui_core import *
from save_manager import save_game
from quest_manager import quest_manager
from achievements import achievement_manager, AchievementManager, ACHIEVEMENTS
from settings import GAME_SETTINGS
from abilities import get_ability_for_pokemon, apply_ability_trigger
from held_items import HELD_ITEMS, BERRY_NAMES, TYPE_ITEMS, BATTLE_ITEMS, get_type_item
from time_system import (HOUR, get_period, get_time_name, advance_time,
                         get_time_icon, get_time_color, is_night, is_day,
                         time_spawn_modifier, get_time_spawns)
from game_functions import (
    apply_entry_abilities, apply_item_turn_trigger, apply_hp_threshold_items,
    apply_status_items, apply_ko_ability, apply_contact_abilities,
    apply_item_after_attack, format_type, get_shiny_rate
)
from daily_challenges import (
    get_daily_challenge, get_login_streak, get_streak_bonus,
    check_daily_species_catch, check_type_bonus
)
from battle_frontier import (
    BATTLE_FRONTIER, RENTAL_POKEMON, BATTLE_HALL_OPPONENTS,
    get_rental_team, get_pike_room, get_battle_hall_order,
    get_frontier_progress, update_frontier_progress, count_frontier_symbols
)
pokemon = {}
money = 500
pvp_rp = 1000
heal_tickets = 50
trophies = 0
inventory = {"Potion": 3, "Ultra Ball": 1} # Starter pack
location = "Grasslands"
badges = []
tower_record = 0
pokedex_seen = set()
pokedex_caught = set()
elite_four_defeated = []
cloud_token = None
cloud_username = None
SERVER_URL = "https://pokemon-game-jbjg.onrender.com/api"

# Shiny hunting system
shiny_chain = 0
last_encounter_species = None

# Daily challenge system
daily_challenge = get_daily_challenge()
login_streak = 0
last_login_date = None
daily_raid_completed = False
daily_species_caught = set()

# Battle Frontier progress
frontier_progress = {}

def robust_request(method, url, json_data=None, headers=None, timeout=30):
    """Make HTTP requests to the cloud server. No local fallback."""
    if method == "POST":
        return requests.post(url, json=json_data, headers=headers, timeout=timeout)
    elif method == "GET":
        return requests.get(url, headers=headers, timeout=timeout)

def is_server_running():
    try:
        r = requests.get(f"{SERVER_URL}/health", timeout=10)
        return r.status_code == 200
    except:
        return False

# ══════════════════════════════════════════════════
# CHECK CLOUD SERVER (Render)
# ══════════════════════════════════════════════════
print(f"  {DIM}☁️  Connecting to cloud server...{RESET}")
print(f"  {DIM}   (Free tier may take up to 60s to wake up){RESET}")
server_ready = False
for attempt in range(12):
    if is_server_running():
        server_ready = True
        break
    print(f"  {DIM}   Waiting... ({(attempt+1)*5}s){RESET}")
    time.sleep(5)

if not server_ready:
    print(f"  {BRIGHT_RED}❌ Cannot connect to cloud server. Exiting...{RESET}")
    time.sleep(2)
    sys.exit(0)
print(f"  {BRIGHT_GREEN}✅ Cloud server connected!{RESET}")
time.sleep(0.5)

# ══════════════════════════════════════════════════
# EPIC WELCOME SCREEN
# ══════════════════════════════════════════════════
print()
clear_screen()
matrix_rain(duration=1.5, width=55, density=0.2)
print()
print_title()
print_pokeball()
print()
fade_transition(lines=2, width=55)
crazy_box("⚡ Welcome to the Pokémon Game! ⚡", width=45)
print()
sparkle_burst(duration=0.5, width=40)
print()
typewriter("  Your journey begins now, Trainer...", delay=0.03, color=BRIGHT_CYAN)
typewriter("  Choose your first partner Pokémon!", delay=0.03, color=BRIGHT_YELLOW)
print()

# ══════════════════════════════════════════════════
# CLOUD ACCOUNT INTEGRATION AT STARTUP
# ══════════════════════════════════════════════════
clear_screen()
matrix_rain(duration=1.0, width=55, density=0.15)
fancy_header("POKÉMON CLOUD GATEWAY", emoji="☁️", width=50)

print(f"  {BOLD}{BRIGHT_CYAN}1.{RESET} 🔑 Login to Existing Cloud Account")
print(f"  {BOLD}{BRIGHT_YELLOW}2.{RESET} 📝 Register a New Cloud Account")
print()
theme_divider(50)
gateway_opt = crazy_input("Choose an option (1 or 2)").strip()

cloud_token = None
cloud_username = None
load_success = False
daycare = {"slots": [], "steps": 0, "egg_waiting": False}

if gateway_opt == "1":
    username = crazy_input("Username").strip()
    password = crazy_input("Password").strip()
    try:
        r = robust_request("POST", f"{SERVER_URL}/login", json_data={"username": username, "password": password}, timeout=30)
        if r.status_code == 200:
            cloud_token = r.json()["token"]
            cloud_username = r.json().get("username", username)
            print(f"\n  {BRIGHT_GREEN}✅ Logged in successfully as {cloud_username}!{RESET}")
            # Try to pull save data immediately
            pull_r = robust_request("GET", f"{SERVER_URL}/load", headers={"Authorization": f"Bearer {cloud_token}"}, timeout=30)
            if pull_r.status_code == 200:
                data = json.loads(pull_r.json()["save_data"])
                print(f"  {BOLD}{BRIGHT_YELLOW}💾 Cloud save file found for {cloud_username}!{RESET}")
                ans = crazy_input(f"Would you like to load your cloud save as {data.get('name', 'Trainer')}? (y/n)")
                if ans.lower() == 'y':
                    name = data.get("name", "Trainer")
                    pokemon = data.get("pokemon", {})
                    money = data.get("money", 500)
                    pvp_rp = data.get("pvp_rp", 1000)
                    trophies = data.get("trophies", 0)
                    inventory = data.get("inventory", {"Potion": 3})
                    location = data.get("location", "Grasslands")
                    badges = data.get("badges", [])
                    tower_record = data.get("tower_record", 0)
                    pokedex_seen = set(data.get("pokedex_seen", []))
                    pokedex_caught = set(data.get("pokedex_caught", []))
                    elite_four_defeated = data.get("elite_four_defeated", [])
                    ach_data = data.get("achievements", {"unlocked":[],"counters":{}})
                    achievement_manager.__dict__.update(AchievementManager.from_dict(ach_data).__dict__)
                    heal_tickets = data.get("heal_tickets", 50)
                    daycare = data.get("daycare", {"slots": [], "steps": 0, "egg_waiting": False})
                    shiny_chain = data.get("shiny_chain", 0)
                    last_encounter_species = data.get("last_encounter_species", None)
                    login_streak = data.get("login_streak", 0)
                    last_login_date = data.get("last_login_date", None)
                    daily_raid_completed = data.get("daily_raid_completed", False)
                    daily_species_caught = set(data.get("daily_species_caught", []))
                    frontier_progress = data.get("frontier_progress", {})
                    load_success = True
                    print(f"\n  {BOLD}{BRIGHT_GREEN}✅ Game Loaded Successfully from Cloud!{RESET}")
                    time.sleep(1)
            else:
                print(f"  {DIM}ℹ️  No cloud save found for this account. Starting fresh...{RESET}")
                time.sleep(1)
        else:
            print(f"  {BRIGHT_RED}❌ Login failed: {r.json().get('message', 'Error')}{RESET}")
            print(f"  {DIM}Please try again or register a new account.{RESET}")
            time.sleep(1.5)
            sys.exit(0)
    except Exception as e:
        print(f"  {BRIGHT_RED}❌ Server error: {e}{RESET}")
        print(f"  {DIM}Cannot connect to cloud server. Exiting...{RESET}")
        time.sleep(1.5)
        sys.exit(0)

elif gateway_opt == "2":
    username = crazy_input("Choose Username").strip()
    password = crazy_input("Choose Password").strip()
    try:
        r = robust_request("POST", f"{SERVER_URL}/register", json_data={"username": username, "password": password}, timeout=30)
        if r.status_code == 201:
            print(f"\n  {BRIGHT_GREEN}✅ Account created successfully!{RESET}")
            login_r = robust_request("POST", f"{SERVER_URL}/login", json_data={"username": username, "password": password}, timeout=30)
            if login_r.status_code == 200:
                cloud_token = login_r.json()["token"]
                cloud_username = login_r.json().get("username", username)
                print(f"  {BRIGHT_GREEN}✅ Automatically logged in as {cloud_username}!{RESET}")
            time.sleep(1)
        else:
            print(f"  {BRIGHT_RED}❌ Registration failed: {r.json().get('message', 'Error')}{RESET}")
            print(f"  {DIM}Please try again.{RESET}")
            time.sleep(1.5)
            sys.exit(0)
    except Exception as e:
        print(f"  {BRIGHT_RED}❌ Server error: {e}{RESET}")
        print(f"  {DIM}Cannot connect to cloud server. Exiting...{RESET}")
        time.sleep(1.5)
        sys.exit(0)

else:
    print(f"\n  {BRIGHT_RED}❌ Invalid option. You must login or register to play.{RESET}")
    time.sleep(1)
    sys.exit(0)

if not load_success:
    name = cloud_username
    print(f"  {BRIGHT_GREEN}👋 Welcome to the world of Pokémon, {name}!{RESET}")
    time.sleep(1)
    print()
    pokeball_loading("Creating new trainer profile", duration=1.0)
    print()

# Login streak handling
from datetime import datetime
today_str = datetime.now().strftime("%Y-%m-%d")
streak_result = get_login_streak(last_login_date)
if streak_result is not None:
    login_streak = streak_result
if last_login_date != today_str:
    login_streak += 1
    last_login_date = today_str
    # Show streak bonus
    bonus = get_streak_bonus(login_streak)
    if login_streak > 1:
        clear_screen()
        fancy_header("LOGIN STREAK!", emoji="🔥", width=50)
        print(f"  {BOLD}{BRIGHT_YELLOW}{bonus['desc']}{RESET}")
        print(f"  {BOLD}{BRIGHT_GREEN}+{bonus['coins']} coins{RESET}")
        print(f"  {BOLD}{BRIGHT_CYAN}+{bonus['tickets']} heal tickets{RESET}")
        if bonus['item']:
            print(f"  {BOLD}{BRIGHT_MAGENTA}+ {bonus['item']}{RESET}")
        money += bonus['coins']
        heal_tickets += bonus['tickets']
        if bonus['item']:
            inventory[bonus['item']] = inventory.get(bonus['item'], 0) + 1
        print()
        crazy_input("Press Enter to continue")
    
    # Reset daily raid on new day
    daily_raid_completed = False
    daily_species_caught = set()
    daily_challenge = get_daily_challenge()

    if name == "Ash":
        print_art(PIKACHU_ART, electric_text)
        explode_print("You got Pikachu! (HP: 60; DM: 40)")
        print(f"  {BOLD}{BRIGHT_YELLOW}⚡⚡⚡ PIKA PIKA! ⚡⚡⚡{RESET}")
        electric_storm(lines=3, width=40)
        pokemon["pikachu"] = make_pokemon(60, 40, "Electric", ["Thunder Shock", "Quick Attack"], speed=90)
        pokedex_seen.add("pikachu")
        pokedex_caught.add("pikachu")
    elif name == "Brock":
        print_art(ONIX_ART, lambda t: gradient_text(t, (150, 150, 150), (200, 200, 200)))
        explode_print("You got Onix!")
        print(f"  {BOLD}{BRIGHT_WHITE}🪨🪨🪨 ROCK SOLID! 🪨🪨🪨{RESET}")
        pokemon["onix"] = make_pokemon(80, 60, "Rock", ["Rock Throw", "Tackle"], speed=30)
        pokedex_seen.add("onix")
        pokedex_caught.add("onix")
    elif name == "Ohio sigma rizzler":
        print_art(TYRANITAR_ART, fire_text)
        matrix_text_reveal("ABSOLUTE SIGMA ENERGY DETECTED", delay=0.03)
        explode_print("You got Tyranitar!")
        fire_effect(lines=3, width=40)
        pokemon["tyranitar"] = make_pokemon(150, 200, "Rock", ["Bite", "Rock Slide"], speed=41)
        pokedex_seen.add("tyranitar")
        pokedex_caught.add("tyranitar")
    elif name == "Ting-wei Chang":
        print_art(LUCARIO_ART, lambda t: gradient_text(t, (0, 100, 255), (100, 200, 255)))
        explode_print("You got Lucario!")
        print(f"  {BOLD}{BRIGHT_BLUE}🌀🌀🌀 AURA POWER! 🌀🌀🌀{RESET}")
        pokemon["lucario"] = make_pokemon(100, 70, "Fighting", ["Close Combat", "Quick Attack"], speed=90)
        pokedex_seen.add("lucario")
        pokedex_caught.add("lucario")
    else:
        print()
        print_art(STARTER_SELECTION_ART, rainbow_text)
        print()
        print(f"  {BOLD}{BRIGHT_RED}1.{RESET} {fire_text('🔥 Charmander')} {DIM}(HP: 40; DM: 30){RESET}")
        print()
        print(f"  {BOLD}{BRIGHT_BLUE}2.{RESET} {gradient_text('💧 Squirtle', (0, 100, 255), (0, 200, 255))} {DIM}(HP: 50; DM: 25){RESET}")
        print()
        print(f"  {BOLD}{BRIGHT_GREEN}3.{RESET} {gradient_text('🌿 Bulbasaur', (0, 200, 0), (100, 255, 100))} {DIM}(HP: 60; DM: 15){RESET}")
        print()
        starter = crazy_int_input("Which one do you want")

        if starter == 1:
            pokeball_transition(width=40)
            print_art(CHARMANDER_ART, fire_text)
            explode_print("You got Charmander! 🔥")
            fire_effect(lines=3, width=40)
            pokemon["charmander"] = make_pokemon(40, 30, "Fire", ["Ember", "Scratch"], speed=65)
            pokedex_seen.add("charmander")
            pokedex_caught.add("charmander")
        elif starter == 2:
            pokeball_transition(width=40)
            print_art(SQUIRTLE_ART, lambda t: gradient_text(t, (0, 100, 255), (0, 200, 255)))
            explode_print("You got Squirtle! 💧")
            rain_effect(lines=3, width=40)
            pokemon["squirtle"] = make_pokemon(50, 25, "Water", ["Water Gun", "Tackle"], speed=43)
            pokedex_seen.add("squirtle")
            pokedex_caught.add("squirtle")
        elif starter == 3:
            pokeball_transition(width=40)
            print_art(BULBASAUR_ART, lambda t: gradient_text(t, (0, 200, 0), (100, 255, 100)))
            explode_print("You got Bulbasaur! 🌿")
            pokemon["bulbasaur"] = make_pokemon(60, 15, "Grass", ["Vine Whip", "Tackle"], speed=45)
            pokedex_seen.add("bulbasaur")
            pokedex_caught.add("bulbasaur")

print()
wipe_transition(width=50)
theme_print("⚡ Your adventure begins NOW! ⚡", delay=0.04)
print()

# ══════════════════════════════════════════════════
# SETTINGS MENU LOGIC
# ══════════════════════════════════════════════════
def run_settings_menu():
    """Run the massive interactive settings menu."""
    opt = 0
    while opt != 5:
        wipe_transition(width=50)
        fancy_header("UI SETTINGS", emoji="⚙️", width=50)
        
        print(f"  {BOLD}{BRIGHT_RED}1.{RESET} {theme_text('🎨 Theme Colors')}         {DIM}[{GAME_SETTINGS.get('theme').upper()}]{RESET}")
        print(f"  {BOLD}{BRIGHT_CYAN}2.{RESET} {theme_text('🎬 Animation Speed')}      {DIM}[{GAME_SETTINGS.get('animation_speed')}x]{RESET}")
        print(f"  {BOLD}{BRIGHT_YELLOW}3.{RESET} {theme_text('🖼️  UI Borders')}           {DIM}[{GAME_SETTINGS.get('border_style').upper()}]{RESET}")
        print(f"  {BOLD}{BRIGHT_GREEN}4.{RESET} {theme_text('📊 HUD & Bars')}           {DIM}[{GAME_SETTINGS.get('battle_hud_style').upper()}]{RESET}")
        print(f"  {BOLD}{DIM}5.{RESET} {DIM}🚪 Return to Game{RESET}")
        print()
        theme_divider(50)
        opt = crazy_int_input("Choose setting category")
        
        if opt == 1:
            themes = [
                "rainbow", "fire", "water", "grass", "electric", "psychic", "hacker", "vaporwave", 
                "gold", "blood", "ice", "retro", "dark", "cyberpunk", "synthwave", "sakura", 
                "obsidian", "steampunk", "aurora", "blizzard", "emerald", "ruby", "sapphire", 
                "crystal", "galaxy"
            ]
            print("\n  Available Themes:")
            for i, t in enumerate(themes, 1):
                print(f"  {i:2}. {t.capitalize()}")
            t_opt = crazy_int_input("Select theme number")
            if 1 <= t_opt <= len(themes):
                GAME_SETTINGS.set("theme", themes[t_opt-1])
                print(f"  {theme_text('Theme updated!')}")
                delay_sleep(1.0)
                
        elif opt == 2:
            print("\n  Animation Speeds:")
            print("  1. Instant (0.0x)")
            print("  2. Fast (0.5x)")
            print("  3. Normal (1.0x)")
            print("  4. Slow (2.0x)")
            s_opt = crazy_int_input("Select speed")
            speeds = {1: 0.0, 2: 0.5, 3: 1.0, 4: 2.0}
            if s_opt in speeds:
                GAME_SETTINGS.set("animation_speed", speeds[s_opt])
                print(f"  {theme_text('Speed updated!')}")
                time.sleep(1.0) # Always sleep 1s here to show feedback
                
        elif opt == 3:
            borders = [
                "crazy", "fire", "electric", "shadow", "double", "rounded", "dashed", "water", "grass",
                "box_0", "box_100", "box_250", "box_500", "box_750", "box_999"
            ]
            print("\n  Available Borders:")
            for i, b in enumerate(borders, 1):
                print(f"  {i:2}. {b.upper()}")
            b_opt = crazy_int_input("Select border style number")
            if 1 <= b_opt <= len(borders):
                GAME_SETTINGS.set("border_style", borders[b_opt-1])
                print(f"  {theme_text('Border updated!')}")
                delay_sleep(1.0)
                
        elif opt == 4:
            huds = ["classic", "modern", "minimal"]
            bars = ["blocks", "symbols", "emoji", "abstract"]
            print("\n  HUD Styles:")
            for i, h in enumerate(huds, 1): print(f"  {i}. {h.capitalize()}")
            h_opt = crazy_int_input("Select HUD style")
            if 1 <= h_opt <= len(huds): GAME_SETTINGS.set("battle_hud_style", huds[h_opt-1])
            
            print("\n  Bar Styles:")
            for i, b in enumerate(bars, 1): print(f"  {i}. {b.capitalize()}")
            b_opt = crazy_int_input("Select Bar style")
            if 1 <= b_opt <= len(bars): 
                GAME_SETTINGS.set("hp_bar_style", bars[b_opt-1])
                GAME_SETTINGS.set("xp_bar_style", bars[b_opt-1])
            
            print(f"  {theme_text('HUD & Bars updated!')}")
            delay_sleep(1.0)

# ══════════════════════════════════════════════════
# MAIN GAME LOOP
# ══════════════════════════════════════════════════
option = 0
try:
    while True:
        clear_screen()
        advance_time(1)
        
        # Badge count for Elite Four unlock
        gym_badges_check = [b for b in badges if any(b == g[1]["badge"] for g in GYM_LEADERS.items())]
        
        # ══════════════════════════════════════════════════
        # DAYCARE & EGG HATCHING UPDATES
        # ══════════════════════════════════════════════════
        daycare_slots = daycare.get("slots", [])
        if daycare_slots:
            daycare["steps"] += 1
            # 1. Passive EXP Gain for Daycare Pokémon
            for dp in daycare_slots:
                # EXP formula from foundation: calculate_daycare_average_exp
                exp_gain = calculate_daycare_average_exp(dp)
                dp["xp"] = dp.get("xp", 0) + exp_gain
                dp["maxxp"] = dp.get("maxxp", dp.get("lvl", 1) * 50)
                
                # Check for passive Level Up
                while dp["xp"] >= dp["maxxp"]:
                    dp["xp"] -= dp["maxxp"]
                    dp["lvl"] = dp.get("lvl", 1) + 1
                    dp["maxxp"] = dp["lvl"] * 50
                    dp["pending_level_ups"] = dp.get("pending_level_ups", 0) + 1
            
            # 2. Egg Generation Check
            if len(daycare_slots) == 2 and not daycare.get("egg_waiting"):
                # Calculate Compatibility using foundation
                compatibility, _ = calculate_breeding_compatibility(daycare_slots[0], daycare_slots[1])
                
                # Breed Rate Check
                breed_chance = 0.0
                if compatibility > 80:
                    breed_chance = 0.15
                elif compatibility > 50:
                    breed_chance = 0.08
                elif compatibility > 25:
                    breed_chance = 0.04
                
                if random.random() < breed_chance:
                    daycare["egg_waiting"] = True

        # 3. Active Party Egg Incubation & Hatching Ticks
        hatched_keys = []
        for pk_key, pk_stats in list(pokemon.items()):
            if pk_stats.get("is_egg"):
                pk_stats["steps_left"] = pk_stats.get("steps_left", 20) - 1
                if pk_stats["steps_left"] <= 0:
                    hatched_keys.append(pk_key)
        
        for hk in hatched_keys:
            # Trigger hatching sequence!
            egg_stats = pokemon.pop(hk)
            p1_name = egg_stats.get("parent1", "bulbasaur")
            p2_name = egg_stats.get("parent2", "bulbasaur")
            
            # Determine species
            roll = random.random()
            is_fusion = False
            
            # Masuda method: different species parents = tripled shiny rate
            is_masuda = (p1_clean != p2_clean)
            has_shiny_charm = inventory.get("Shiny Charm", 0) > 0
            shiny_rate = get_shiny_rate(chain=0, has_shiny_charm=has_shiny_charm, is_masuda=is_masuda, is_egg=True)
            shiny_roll = random.random() < shiny_rate
            
            # Helper to strip numbers for species lookup
            def clean_species_name(nm):
                return nm.lower().rstrip("0123456789")
                
            p1_clean = clean_species_name(p1_name)
            p2_clean = clean_species_name(p2_name)
            
            if roll < 0.40:
                baby_species = p1_clean
            elif roll < 0.80:
                baby_species = p2_clean
            else:
                is_fusion = True
                baby_species = f"{p1_clean}-{p2_clean}"
            
            # Setup Stats
            baby_hp = 45 if not is_fusion else 65
            baby_dm = 20 if not is_fusion else 30
            baby_spd = 50
            baby_type = "Normal"
            baby_moves = ["Tackle"]
            
            # Lookup baby base stats in pokedexes if natural
            from pokemon_dex import weak_pokemon, moderately_strong_pokemon, strong_pokemon, ultra_strong_pokemon
            for dex in [weak_pokemon, moderately_strong_pokemon, strong_pokemon, ultra_strong_pokemon]:
                if baby_species in dex:
                    baby_hp = dex[baby_species]["hp"]
                    baby_dm = dex[baby_species]["dm"]
                    baby_type = dex[baby_species].get("type", "Normal")
                    baby_moves = dex[baby_species].get("moves", ["Tackle"])
                    baby_spd = dex[baby_species].get("speed", 50)
                    break
            
            if is_fusion:
                # Blended types
                from fusion_manager import get_fusion_type
                baby_type = get_fusion_type(p1_clean, p2_clean)
                baby_moves = ["Tackle", "Quick Attack"]
            
            baby_stats = make_pokemon(baby_hp, baby_dm, baby_type, baby_moves, speed=baby_spd, shiny=shiny_roll, generation=1 if is_fusion else 0)
            baby_name = baby_species
            
            # Generate unique key in party
            suffix = 2
            final_key = baby_name
            while final_key in pokemon:
                final_key = f"{baby_name}{suffix}"
                suffix += 1
            
            # Hatching Screen!
            clear_screen()
            sparkle_burst(duration=1.0, width=50)
            fancy_header("🐣 EGG HATCHING! 🐣", emoji="💖", width=50)
            print()
            print(f"  {BOLD}{BRIGHT_YELLOW}Oh? The Egg is hatching!{RESET}")
            print()
            spinner_animation("Hatching", duration=2.0)
            sparkle_burst(duration=1.5, width=55)
            
            shiny_tag = f" {BRIGHT_YELLOW}✨SHINY✨{RESET}" if shiny_roll else ""
            fusion_tag = f" {BRIGHT_CYAN}[FUSION]{RESET}" if is_fusion else ""
            masuda_tag = f" {BRIGHT_MAGENTA}[Masuda]{RESET}" if is_masuda else ""
            print(f"\n  🎉 {BOLD}{BRIGHT_GREEN}Congratulations! A {rainbow_text(baby_name.upper())}{shiny_tag}{fusion_tag}{masuda_tag} hatched from the Egg!{RESET}")
            if is_masuda:
                print(f"  {DIM}🌍 Masuda Method bonus applied! (3x shiny rate){RESET}")
            if has_shiny_charm:
                print(f"  {DIM}🍀 Shiny Charm bonus applied! (2x shiny rate){RESET}")
            print()
            stat_card(final_key, baby_stats["hp"], baby_stats["maxhp"], baby_stats["dm"], baby_stats["xp"], baby_stats["maxxp"], baby_stats["lvl"], speed=baby_stats.get("speed", 50))
            print()
            pokemon[final_key] = baby_stats
            pokedex_seen.add(baby_name.lower())
            pokedex_caught.add(baby_name.lower())
            crazy_input("Press Enter to continue")

        # PASSIVE BACKGROUND HEALING: All pokemon heal 5% max HP per action
        for pn, st in pokemon.items():
            if st.get("hp", 0) > 0 and st.get("hp", 0) < st.get("maxhp", 1):
                heal_amt = max(1, int(st["maxhp"] * 0.05))
                st["hp"] = min(st["maxhp"], st["hp"] + heal_amt)
        period = get_period()
        time_icon = get_time_icon()
        time_name = get_time_name()
        print()
        fancy_header("MAIN MENU", emoji="🎮", width=50)
        
        # Build side-by-side panel grid dashboard
        p_left = (
            f"📍 REGION: {location.upper()}\n"
            f"⏰ TIME: {time_icon} {time_name} ({period})\n"
            f"⛈️  WEATHER: {get_random_weather().upper()}"
        )
        p_right = (
            f"💰 WALLET: {money:>5} coins\n"
            f"🎫 TICKETS: {heal_tickets:>3} tickets\n"
            f"🏆 TROPHIES: {trophies:>4} trophies"
        )
        p_daily = (
            f"🔥 STREAK: {login_streak} days\n"
            f"🎯 DAILY: {daily_challenge['daily_species'][0]}\n"
            f"👑 RAID: {'✅' if daily_raid_completed else '⬜'} {daily_challenge['daily_raid']['name']}"
        )
        render_panel_grid([p_left, p_right, p_daily], width=56)
        print()
        print(f"  {BOLD}{BRIGHT_RED}A.{RESET}  ⚔️  Adventure           {DIM}[Explore & battle]{RESET}")
        print(f"  {BOLD}{BRIGHT_CYAN}B.{RESET}  🏆 Competitive        {DIM}[Towers, raids & PvP]{RESET}")
        print(f"  {BOLD}{BRIGHT_GREEN}C.{RESET}  🎒 Management         {DIM}[Items, shop & fusion]{RESET}")
        print(f"  {BOLD}{BRIGHT_MAGENTA}D.{RESET}  📊 Info & Social      {DIM}[Stats, pokedex & cloud]{RESET}")
        print(f"  {BOLD}{BRIGHT_YELLOW}E.{RESET}  🗺️  World              {DIM}[Travel & daycare]{RESET}")
        print()
        print(f"  {BOLD}{DIM}S.{RESET} 💾 Save & Leave")
        print()
        theme_divider(50)
        category = crazy_input("Select category").strip().upper()
        
        # ══════════════════════════════════════
        # CATEGORY A: ADVENTURE
        # ══════════════════════════════════════
        if category == "A":
            clear_screen()
            fancy_header("ADVENTURE", emoji="⚔️", width=50)
            print(f"  {BOLD}{BRIGHT_RED}1.{RESET}  🌿 Catch Pokemon      {DIM}[Wild encounters]{RESET}")
            print(f"  {BOLD}{BRIGHT_YELLOW}2.{RESET}  🏅 Gym Challenge      {DIM}[Badges: {len(badges)}/8]{RESET}")
            print(f"  {BOLD}{BRIGHT_RED}3.{RESET}  🐛 Bug Hunt           {DIM}[Corrupted gauntlet]{RESET}")
            print(f"  {BOLD}{BRIGHT_BLUE}4.{RESET}  🗺️  Travel              {DIM}[Change regions]{RESET}")
            raid_status = "✅ Done" if daily_raid_completed else "Available"
            print(f"  {BOLD}{BRIGHT_MAGENTA}5.{RESET}  📅 Daily Challenge    {DIM}[{raid_status}]{RESET}")
            gym_badges_check_a = [b for b in badges if any(b == g[1]["badge"] for g in GYM_LEADERS.items())]
            if len(gym_badges_check_a) >= len(GYM_LEADERS):
                ef_status = f"{len(elite_four_defeated)}/5 beaten"
                print(f"  {BOLD}{BRIGHT_YELLOW}6.{RESET}  👑 Elite Four         {DIM}[{ef_status}]{RESET}")
            print()
            print(f"  {BOLD}{DIM}Q.{RESET} Back")
            adv_opt = crazy_input("Choose").strip()
            if adv_opt == "1":
                option = 1
            elif adv_opt == "2":
                option = 10
            elif adv_opt == "3":
                option = 12
            elif adv_opt == "4":
                option = 7
            elif adv_opt == "5":
                option = 23  # Daily challenge
            elif adv_opt == "6" and len(gym_badges_check_a) >= len(GYM_LEADERS):
                option = 20  # Elite Four
            else:
                option = 0
                
        # ══════════════════════════════════════
        # CATEGORY B: COMPETITIVE
        # ══════════════════════════════════════
        elif category == "B":
            clear_screen()
            fancy_header("COMPETITIVE", emoji="🏆", width=50)
            print(f"  {BOLD}{BRIGHT_YELLOW}1.{RESET}  🏟️  Arena               {DIM}[Battle trainers]{RESET}")
            print(f"  {BOLD}{BRIGHT_CYAN}2.{RESET}  🗼 Battle Tower        {DIM}[Record: {tower_record}]{RESET}")
            print(f"  {BOLD}{BRIGHT_RED}3.{RESET}  👑 Boss Raids          {DIM}[Legendary battles]{RESET}")
            print(f"  {BOLD}{BRIGHT_MAGENTA}4.{RESET}  🏰 Dungeon Gauntlets  {DIM}[Endurance gauntlet]{RESET}")
            print(f"  {BOLD}{BRIGHT_BLUE}5.{RESET}  📶 GTS & Ranked PvP   {DIM}[Online station]{RESET}")
            symbols = count_frontier_symbols({"frontier_progress": frontier_progress})
            print(f"  {BOLD}{BRIGHT_YELLOW}6.{RESET}  🎪 Battle Frontier    {DIM}[{symbols}/7 Symbols]{RESET}")
            print()
            print(f"  {BOLD}{DIM}Q.{RESET} Back")
            comp_opt = crazy_input("Choose").strip()
            if comp_opt == "1":
                option = 3
            elif comp_opt == "2":
                option = 11
            elif comp_opt == "3":
                option = 19
            elif comp_opt == "4":
                option = 18
            elif comp_opt == "5":
                option = 17
            elif comp_opt == "6":
                option = 24  # Battle Frontier
            else:
                option = 0
                
        # ══════════════════════════════════════
        # CATEGORY C: MANAGEMENT
        # ══════════════════════════════════════
        elif category == "C":
            clear_screen()
            fancy_header("MANAGEMENT", emoji="🎒", width=50)
            print(f"  {BOLD}{BRIGHT_GREEN}1.{RESET}  🏪 Shop               {DIM}[Buy items & tickets]{RESET}")
            print(f"  {BOLD}{BRIGHT_MAGENTA}2.{RESET}  🏥 Hospital           {DIM}[Heal with tickets]{RESET}")
            print(f"  {BOLD}{BRIGHT_BLUE}3.{RESET}  🎒 Bag                {DIM}[Use items]{RESET}")
            print(f"  {BOLD}{BRIGHT_MAGENTA}4.{RESET}  🧬 Fusion Lab         {DIM}[Fuse Pokemon]{RESET}")
            egg_notif = f" {BOLD}{BRIGHT_YELLOW}[☁️ Egg Ready!]{RESET}" if daycare.get("egg_waiting") else ""
            print(f"  {BOLD}{BRIGHT_YELLOW}5.{RESET}  🏡 Daycare & Breeding {DIM}[Level & Breed]{RESET}{egg_notif}")
            print(f"  {BOLD}{BRIGHT_WHITE}6.{RESET}  ⚙️  Settings            {DIM}[Customize UI]{RESET}")
            print()
            print(f"  {BOLD}{DIM}Q.{RESET} Back")
            mgmt_opt = crazy_input("Choose").strip()
            if mgmt_opt == "1":
                option = 4
            elif mgmt_opt == "2":
                option = 5
            elif mgmt_opt == "3":
                option = 6
            elif mgmt_opt == "4":
                option = 12
            elif mgmt_opt == "5":
                option = 16
            elif mgmt_opt == "6":
                option = 8
            else:
                option = 0
                
        # ══════════════════════════════════════
        # CATEGORY D: INFO & SOCIAL
        # ══════════════════════════════════════
        elif category == "D":
            clear_screen()
            fancy_header("INFO & SOCIAL", emoji="📊", width=50)
            print(f"  {BOLD}{BRIGHT_CYAN}1.{RESET}  📊 Stats              {DIM}[View team]{RESET}")
            print(f"  {BOLD}{BRIGHT_GREEN}2.{RESET}  📖 Pokedex            {DIM}[{len(pokedex_caught)} caught]{RESET}")
            print(f"  {BOLD}{BRIGHT_GREEN}3.{RESET}  📋 Quest Board        {DIM}[{len(quest_manager.active)} active]{RESET}")
            print(f"  {BOLD}{BRIGHT_CYAN}4.{RESET}  ☁️  Cloud Account       {DIM}[{cloud_username if cloud_token else 'Not logged in'}]{RESET}")
            print(f"  {BOLD}{BRIGHT_MAGENTA}5.{RESET}  🤖 AI Chatbot         {DIM}[Ask questions]{RESET}")
            print()
            print(f"  {BOLD}{DIM}Q.{RESET} Back")
            info_opt = crazy_input("Choose").strip()
            if info_opt == "1":
                option = 2
            elif info_opt == "2":
                option = 13
            elif info_opt == "3":
                option = 14
            elif info_opt == "4":
                option = 9
            elif info_opt == "5":
                option = 21
            else:
                option = 0
                
        # ══════════════════════════════════════
        # CATEGORY E: WORLD
        # ══════════════════════════════════════
        elif category == "E":
            clear_screen()
            fancy_header("WORLD", emoji="🗺️", width=50)
            print(f"  {BOLD}{BRIGHT_WHITE}1.{RESET}  🗺️  Travel              {DIM}[Change regions]{RESET}")
            egg_notif_e = f" {BOLD}{BRIGHT_YELLOW}[☁️ Egg Ready!]{RESET}" if daycare.get("egg_waiting") else ""
            print(f"  {BOLD}{BRIGHT_YELLOW}2.{RESET}  🏡 Daycare & Breeding {DIM}[Level & Breed]{RESET}{egg_notif_e}")
            print()
            print(f"  {BOLD}{DIM}Q.{RESET} Back")
            world_opt = crazy_input("Choose").strip()
            if world_opt == "1":
                option = 7
            elif world_opt == "2":
                option = 16
            else:
                option = 0
                
        # ══════════════════════════════════════
        # SAVE & LEAVE
        # ══════════════════════════════════════
        elif category == "S":
            option = 22  # Will be mapped to save & quit
        else:
            option = 0

        # ══════════════════════════════════════
        # OPTION 1: CATCH POKEMON
        # ══════════════════════════════════════
        if option == 1:
            clear_screen()
            hit = 0
            level = random.randint(1, 40)
            
            # Check for Shiny Charm
            has_shiny_charm = inventory.get("Shiny Charm", 0) > 0
            
            # Get wild pokemon with chain and shiny charm bonuses
            result = get_wild_pokemon(level, location, chain=shiny_chain, has_shiny_charm=has_shiny_charm)
            wild, enemyhp, enemydm, enemytype, enemymoves, is_shiny, enemyspeed, shiny_rate = result
            pokedex_seen.add(wild.lower())
            original_enemyhp = enemyhp
            enemy_status = None
            
            # Update chain tracking
            if wild.lower() == last_encounter_species:
                shiny_chain += 1
            else:
                shiny_chain = 1
                last_encounter_species = wild.lower()
            battle_weather = get_random_weather()

            wipe_transition(width=50)
            print_art(REGIONS[location]["art"], theme_text)
            print_art(WILD_ENCOUNTER_ART, fire_text)

            # ✨ SHINY CHECK
            if is_shiny:
                sparkle_burst(duration=1.0, width=50)
                print(f"  {BOLD}{BRIGHT_YELLOW}✨✨✨ A SHINY {rainbow_text(wild.upper())} APPEARED! ✨✨✨{RESET}")
                sparkle_burst(duration=0.5, width=50)
                enemyhp = int(enemyhp * 1.3)
                enemydm = int(enemydm * 1.3)
                original_enemyhp = enemyhp
            else:
                matrix_text_reveal(f"A wild {wild.upper()} ({enemytype}) appeared in {location}!", delay=0.03)

            print()
            shiny_tag = f" {BRIGHT_YELLOW}✨SHINY✨{RESET}" if is_shiny else ""
            electric_box(f"{wild.upper()}{shiny_tag} — HP: {enemyhp} | DM: {enemydm} | Type: {format_type(enemytype)}", width=50)
            if battle_weather != "Clear":
                print(f"  {BOLD}{BRIGHT_CYAN}🌤️  Weather: {battle_weather}{RESET}")
            
            # Show shiny chain and odds
            chain_bonus = min(shiny_chain // 5, 20)
            base_odds = "1/100"
            charm_tag = f" {BRIGHT_MAGENTA}🍀Shiny Charm{RESET}" if has_shiny_charm else ""
            print(f"  {BOLD}{BRIGHT_YELLOW}🔗 Chain: {shiny_chain}{RESET}{charm_tag}  {DIM}Odds: ~1/{int(1/shiny_rate)}{RESET}")
            if shiny_chain >= 10:
                print(f"  {DIM}Chain bonus: +{chain_bonus}% shiny rate{RESET}")
            print()
            coption = crazy_input("Battle/catch this pokémon? (yes or no)")
            print()

            if coption == "yes":
                hphits = 0
                battle_loading()
                print_art(BATTLE_ART, fire_text)
                print(f"  {BOLD}{BRIGHT_CYAN}Your team:{RESET} {rainbow_text(', '.join(pokemon.keys()))}")
                print()
                poke_choice = crazy_input("Who do you want to battle with")
                print()

                if poke_choice in pokemon:
                    if pokemon[poke_choice]["hp"] <= 0:
                        print(f"  {BOLD}{BRIGHT_RED}💀 This pokemon fainted!{RESET}")
                        continue

                    your_status = pokemon[poke_choice].get("status", None)
                    countdown(3)
                    battle_log.clear()
                    battle_state = {
                        "mega_evolved": False,
                        "z_move_used": False,
                        "gigantamax_active": False,
                        "gigantamax_turns": 0,
                        "z_power_active": False
                    }
                    battle_hud(poke_choice, pokemon[poke_choice]["hp"], pokemon[poke_choice]["maxhp"],
                               pokemon[poke_choice]["dm"], wild, enemyhp, original_enemyhp, enemydm,
                               your_status=your_status, enemy_status=enemy_status, weather=battle_weather,
                               your_stages=pokemon[poke_choice].get("stages"),
                               your_ability=pokemon[poke_choice].get("ability"),
                               your_item=pokemon[poke_choice].get("hold_item"),
                               battle_mode="Wild Encounter")

                    boption = 0
                    while boption != 4:
                        battle_log.next_turn()
                        for pn, ps in [(poke_choice, pokemon[poke_choice])]:
                            if ps.get("hp", 0) > 0:
                                tm = apply_item_turn_trigger(ps)
                                for m in tm:
                                    if m: battle_log.log(f"{pn}: {m}", BRIGHT_GREEN)
                                hm = apply_hp_threshold_items(ps)
                                for m in hm:
                                    if m: battle_log.log(f"{pn}: {m}", BRIGHT_GREEN)
                                sm = apply_status_items(ps)
                                for m in sm:
                                    if m: battle_log.log(f"{pn}: {m}", BRIGHT_GREEN)
                        # STATUS TICK — your pokemon
                        your_status = pokemon[poke_choice].get("status", None)
                        if your_status:
                            s_dmg, s_msg = apply_status_tick(pokemon[poke_choice])
                            if s_dmg > 0:
                                battle_log.log(f"{poke_choice} takes {s_dmg} {your_status} damage!", BRIGHT_MAGENTA)
                            if pokemon[poke_choice]["hp"] <= 0:
                                print_art(DEFEAT_ART, lambda t: gradient_text(t, (255, 0, 0), (80, 0, 0)))
                                defeat_rain(lines=3, width=35)
                                break

                        # WEATHER TICK — your pokemon
                        w_dmg, w_msg = apply_weather_damage(battle_weather, pokemon[poke_choice])
                        if w_dmg > 0:
                            battle_log.log(w_msg, BRIGHT_CYAN)

                        print()
                        menu_divider(38)
                        print(f"  {BOLD}{BRIGHT_RED}1.{RESET} {fire_text('⚔️  Attack')}")
                        print(f"  {BOLD}{BRIGHT_GREEN}2.{RESET} {gradient_text('🎯 Catch', (0, 255, 0), (0, 150, 255))}")
                        print(f"  {BOLD}{BRIGHT_BLUE}3.{RESET} {theme_text('🎒 Bag')}")
                        print(f"  {BOLD}{BRIGHT_MAGENTA}L.{RESET} {theme_text('📋 Log')}")
                        print(f"  {BOLD}{DIM}4.{RESET} {DIM}🏃 Flee{RESET}")
                        menu_divider(38)
                        boption_input = crazy_input("Action")
                        if boption_input.lower() == "l":
                            battle_log.show_history()
                            continue
                        try:
                            boption = int(boption_input)
                        except ValueError:
                            boption = 0

                        # PARALYSIS / SLEEP CHECK
                        can_act, status_msg = can_attack(pokemon[poke_choice])
                        if not can_act and boption == 1:
                            print(f"  {BRIGHT_YELLOW}⚠️  {poke_choice} {status_msg}{RESET}")
                            time.sleep(0.5)
                            enemy_move = random.choice(enemymoves)
                            edmg, _ = calculate_move_damage(enemy_move, {"dm": enemydm, "type": enemytype, "stages": {"dm": 0, "speed": 0}}, pokemon[poke_choice].get("type", "Normal"), battle_weather)
                            animate_enemy_attack_sequence(wild, poke_choice, edmg)
                            take_damage(pokemon[poke_choice], edmg)
                            battle_hud(poke_choice, pokemon[poke_choice]["hp"], pokemon[poke_choice]["maxhp"],
                                       pokemon[poke_choice]["dm"], wild, max(0, enemyhp), original_enemyhp, enemydm,
                                       your_status=pokemon[poke_choice].get("status"), enemy_status=enemy_status, weather=battle_weather,
                                       your_stages=pokemon[poke_choice].get("stages"),
                                       your_ability=pokemon[poke_choice].get("ability"),
                                       battle_mode="Wild Encounter")
                            if pokemon[poke_choice]["hp"] <= 0:
                                print_art(DEFEAT_ART, lambda t: gradient_text(t, (255, 0, 0), (80, 0, 0)))
                                defeat_rain(lines=3, width=35)
                                break
                            continue

                        if boption == 1:
                            move = select_move_menu(poke_choice, pokemon[poke_choice], inventory, battle_state)
                            if not move: continue
                            if pokemon[poke_choice].get("name"):
                                poke_choice = pokemon[poke_choice]["name"]
                            if not has_pp(pokemon[poke_choice], move):
                                print(f"  {BOLD}{BRIGHT_RED}❌ No PP left for {move}!{RESET}")
                                continue
                            use_pp(pokemon[poke_choice], move)
                            
                            hit += 1
                            hphits += 1
                            crit = random.randint(1, 10)
                            is_crit = crit == 10
                            damage, eff = calculate_move_damage(move, pokemon[poke_choice], enemytype, battle_weather, is_crit)
                            
                            animate_attack_sequence(poke_choice, wild, damage, is_crit)
                            if eff > 1.0: print(f"  {BOLD}{BRIGHT_YELLOW}💥 It's super effective!{RESET}")
                            elif eff < 1.0 and eff > 0: print(f"  {DIM}It's not very effective...{RESET}")
                            elif eff == 0: print(f"  {BOLD}{BRIGHT_RED}🚫 It had no effect!{RESET}")
                            
                            # STATUS INFLICTION (10% chance)
                            move_data = MOVES.get(move, {})
                            if move_data.get("type") == "Fire" and random.random() < 0.1 and not enemy_status:
                                enemy_status = "Burn"
                                print(f"  {BRIGHT_RED}🔥 {wild} was burned!{RESET}")
                            elif move_data.get("type") == "Poison" and random.random() < 0.15 and not enemy_status:
                                enemy_status = "Poison"
                                print(f"  {BRIGHT_MAGENTA}☠️  {wild} was poisoned!{RESET}")
                            elif move_data.get("type") == "Electric" and random.random() < 0.1 and not enemy_status:
                                enemy_status = "Paralyze"
                                print(f"  {BRIGHT_YELLOW}⚡ {wild} was paralyzed!{RESET}")

                            item = pokemon[poke_choice].get("hold_item")
                            if item:
                                ir = apply_held_item_trigger(item, "damage_calc", pokemon[poke_choice], move_type=move_data.get("type","Normal") if move_data else "Normal")
                                recoil = ir.get("recoil", 0)
                                if recoil > 0:
                                    take_damage(pokemon[poke_choice], recoil)
                                    print(f"  {BRIGHT_RED}Life Orb: {poke_choice} took {recoil} recoil damage!{RESET}")
                                    recoil_flash(poke_choice, recoil)

                            enemyhp -= damage
                            if enemyhp <= 0:
                                km = apply_ko_ability(pokemon[poke_choice])
                                for m in km:
                                    print(f"  {BRIGHT_CYAN}{m}{RESET}")
                                for qid, q in quest_manager.hook_defeat(enemytype, wild):
                                    print(f"  {BRIGHT_YELLOW}🎉 Quest #{qid} complete! {q['reward_desc']}!{RESET}")
                                for a in achievement_manager.hook_defeat():
                                    part = a["reward"]
                                    print(f"  {BRIGHT_GREEN}🏅 Achievement: {a['name']}! +{part['value']} {part['type']}!{RESET}")
                                print_art(VICTORY_ROYALE_ART, rainbow_text)
                                victory_celebration(lines=3, width=35)
                                explode_print(f"You defeated {wild}!")
                                xp_gain = calculate_xp_gain(max(0, original_enemyhp), pokemon[poke_choice]["dm"], hit, enemydm)
                                if is_shiny: xp_gain = int(xp_gain * 2)
                                # Daily species bonus
                                daily_xp_mult = check_daily_species_catch(wild, daily_challenge['daily_species'])
                                if daily_xp_mult > 1.0:
                                    xp_gain = int(xp_gain * daily_xp_mult)
                                    print(f"  {BOLD}{BRIGHT_MAGENTA}🎯 Daily species bonus! {daily_xp_mult}x XP!{RESET}")
                                pokemon[poke_choice]["xp"] += xp_gain
                                print(f"  {BOLD}{BRIGHT_CYAN}⭐ +{xp_gain} XP!{RESET}")
                                trophies += 150 if is_shiny else 100
                                daily_species_caught.add(wild.lower())
                                if pokemon[poke_choice]["xp"] >= pokemon[poke_choice]["maxxp"]:
                                    poke_choice = level_up_pokemon(pokemon, poke_choice)
                                break

                            print()
                            print(f"  {BOLD}{BRIGHT_RED}👊 {wild.upper()}'s Turn!{RESET}")
                            dramatic_pause(0.5)
                            enemy_move = random.choice(enemymoves)
                            edmg, _ = calculate_move_damage(enemy_move, {"dm": enemydm, "type": enemytype, "stages": {"dm": 0, "speed": 0}}, pokemon[poke_choice].get("type", "Normal"), battle_weather)
                            
                            animate_enemy_attack_sequence(wild, poke_choice, edmg)
                            take_damage(pokemon[poke_choice], edmg)
                            
                            battle_hud(poke_choice, pokemon[poke_choice]["hp"], pokemon[poke_choice]["maxhp"],
                                       pokemon[poke_choice]["dm"], wild, max(0, enemyhp), original_enemyhp, enemydm,
                                       your_status=pokemon[poke_choice].get("status"), enemy_status=enemy_status, weather=battle_weather,
                                       your_stages=pokemon[poke_choice].get("stages"),
                                       your_ability=pokemon[poke_choice].get("ability"),
                                       battle_mode="Wild Encounter")
                                        
                            # Gigantamax turns decrement
                            if battle_state.get("gigantamax_active"):
                                battle_state["gigantamax_turns"] -= 1
                                if battle_state["gigantamax_turns"] <= 0:
                                    battle_state["gigantamax_active"] = False
                                    pokemon[poke_choice]["maxhp"] //= 2
                                    pokemon[poke_choice]["hp"] = min(pokemon[poke_choice]["maxhp"], pokemon[poke_choice]["hp"] // 2)
                                    print(f"\n  {BOLD}{BRIGHT_RED}👹 {poke_choice}'s Gigantamax wore off!{RESET}")

                            if pokemon[poke_choice]["hp"] <= 0:
                                print_art(DEFEAT_ART, lambda t: gradient_text(t, (255, 0, 0), (80, 0, 0)))
                                defeat_rain(lines=3, width=35)
                                break

                        elif boption == 2:
                            # Catch logic
                            prob = 40
                            if is_shiny: prob -= 15
                            if "Ultra Ball" in inventory and inventory["Ultra Ball"] > 0: prob += 25
                            if "Master Ball" in inventory and inventory["Master Ball"] > 0: prob = 100
                            
                            if prob < 100:
                                # Enhanced Tactical Throw Minigame
                                hp_ratio = max(0, enemyhp / original_enemyhp) if original_enemyhp > 0 else 1
                                
                                # Difficulty scales with remaining HP
                                if hp_ratio > 0.7:
                                    time_limit = 1.5
                                    difficulty = "HARD"
                                    diff_color = BRIGHT_RED
                                    words = ["CAPTURE", "POKEBALL", "GOTCHA"]
                                elif hp_ratio > 0.4:
                                    time_limit = 2.0
                                    difficulty = "MEDIUM"
                                    diff_color = BRIGHT_YELLOW
                                    words = ["CATCH", "THROW", "NICE"]
                                else:
                                    time_limit = 3.0
                                    difficulty = "EASY"
                                    diff_color = BRIGHT_GREEN
                                    words = ["CATCH", "OK", "GO"]
                                
                                challenge_word = random.choice(words)
                                
                                print(f"\n  {BOLD}{BRIGHT_MAGENTA}⚡ TACTICAL THROW INITIATED! ⚡{RESET}")
                                print(f"  {DIM}Difficulty: {diff_color}{difficulty}{RESET} | Time Limit: {BOLD}{time_limit:.1f}s{RESET}")
                                print(f"  {DIM}Type the word as fast as you can!{RESET}")
                                time.sleep(0.8)
                                
                                # Visual countdown
                                print(f"  {BOLD}{BRIGHT_YELLOW}READY...{RESET}")
                                time.sleep(0.4)
                                print(f"  {BOLD}{BRIGHT_YELLOW}SET...{RESET}")
                                time.sleep(0.4)
                                print(f"  {BOLD}{BRIGHT_GREEN}GO! → {BOLD}{BRIGHT_CYAN}{challenge_word}{RESET}")
                                
                                start_time = time.time()
                                user_type = input(f"  > ").strip().upper()
                                elapsed = time.time() - start_time
                                
                                # Calculate bonus based on performance
                                if user_type == challenge_word.upper() and elapsed <= time_limit:
                                    speed_ratio = elapsed / time_limit
                                    if speed_ratio <= 0.5:
                                        # Perfect: under 50% of time limit
                                        bonus_mult = 2.5
                                        rating = "⭐ PERFECT! ⭐"
                                        rating_color = BRIGHT_CYAN
                                    elif speed_ratio <= 0.75:
                                        # Great: under 75% of time limit
                                        bonus_mult = 2.0
                                        rating = " GREAT!"
                                        rating_color = BRIGHT_GREEN
                                    else:
                                        # Good: within time limit
                                        bonus_mult = 1.5
                                        rating = "👍 GOOD!"
                                        rating_color = BRIGHT_YELLOW
                                    
                                    prob = min(100, int(prob * bonus_mult))
                                    print(f"  {rating_color}{BOLD}{rating} ({elapsed:.2f}s){RESET}")
                                    print(f"  {BRIGHT_GREEN}Catch rate boosted to {prob}%!{RESET}")
                                elif user_type == challenge_word.upper():
                                    print(f"  {DIM}Too slow! ({elapsed:.2f}s > {time_limit:.1f}s) No bonus.{RESET}")
                                else:
                                    print(f"  {DIM}Wrong word! Expected '{challenge_word}', got '{user_type}'. No bonus.{RESET}")
                            
                            spinner_animation("Throwing ball", duration=1.0)
                            catch_roll = random.randint(1, 100)
                            show_catch_animation(wild, catch_roll <= prob)
                            if catch_roll <= prob:
                                if "Master Ball" in inventory and inventory["Master Ball"] > 0:
                                    inventory["Master Ball"] -= 1
                                elif "Ultra Ball" in inventory and inventory["Ultra Ball"] > 0:
                                    inventory["Ultra Ball"] -= 1
                                
                                pokemon[wild.lower()] = make_pokemon(original_enemyhp, enemydm, enemytype, enemymoves, enemyspeed, shiny=is_shiny)
                                pokedex_caught.add(wild.lower())
                                for qid, q in quest_manager.hook_catch(enemytype, wild):
                                    print(f"  {BRIGHT_YELLOW}🎉 Quest #{qid} complete! {q['reward_desc']}!{RESET}")
                                for a in achievement_manager.hook_catch(is_shiny):
                                    part = a["reward"]
                                    print(f"  {BRIGHT_GREEN}🏅 Achievement: {a['name']}! +{part['value']} {part['type']}!{RESET}")
                                if is_shiny:
                                    print(f"  {BOLD}{rainbow_text('✨✨✨ YOU CAUGHT A SHINY!!! ✨✨✨')}{RESET}")
                                    sparkle_burst(duration=1.0, width=50)
                                break
                            else:
                                print(f"  {BOLD}{BRIGHT_RED}❌ It broke free!{RESET}")

                        elif boption == 3:
                            _, new_name = use_item_menu(inventory, pokemon[poke_choice], pokemon, poke_choice)
                            if new_name: poke_choice = new_name
                            battle_hud(poke_choice, pokemon[poke_choice]["hp"], pokemon[poke_choice]["maxhp"],
                                       pokemon[poke_choice]["dm"], wild, max(0, enemyhp), original_enemyhp, enemydm,
                                       your_status=pokemon[poke_choice].get("status"), enemy_status=enemy_status, weather=battle_weather,
                                       your_stages=pokemon[poke_choice].get("stages"),
                                       your_ability=pokemon[poke_choice].get("ability"),
                                       battle_mode="Wild Encounter")
                                        
                        elif boption == 4:
                            print(f"  {DIM}🏃 Retreating...{RESET}")
                            break
                else:
                    print(f"  {BOLD}{BRIGHT_RED}❌ {poke_choice} not in your index.{RESET}")

            elif coption == "no":
                print(f"  {BOLD}{BRIGHT_RED}😢 You must release one pokemon.{RESET}")
                print(f"  {BOLD}{BRIGHT_CYAN}Team:{RESET} {rainbow_text(', '.join(pokemon.keys()))}")
                while True:
                    removedpoke = crazy_input("Which pokemon to release")
                    if removedpoke in pokemon:
                        del pokemon[removedpoke]
                        print(f"\n  {DIM}👋 Released {removedpoke}...{RESET}")
                        print(f"  {BOLD}{BRIGHT_CYAN}Remaining:{RESET} {rainbow_text(', '.join(pokemon.keys()))}")
                        break
                    else:
                        print(f"  {BOLD}{BRIGHT_RED}❌ Not found. Try again.{RESET}")

        # ══════════════════════════════════════
        # OPTION 2: STATS
        # ══════════════════════════════════════
        if option == 2:
            while True:
                clear_screen()
                print(f"  {BOLD}{BRIGHT_CYAN}1.{RESET} {theme_text('📊 Team Stats')}")
                print(f"  {BOLD}{BRIGHT_YELLOW}2.{RESET} {theme_text('🏅 Achievements')}           {DIM}{len(achievement_manager.unlocked)}/{len(ACHIEVEMENTS)}{RESET}")
                print(f"  {BOLD}{DIM}Q.{RESET} Back")
                r = crazy_input("Choose")
                if r == "1":
                    clear_screen()
                    display_pokemon_stats(pokemon, name, money, trophies)
                    crazy_input("Press Enter to continue")
                elif r == "2":
                    achievement_manager.show_menu()
                elif r.lower() == "q":
                    break

        # ══════════════════════════════════════
        # OPTION 3: ARENA
        # ══════════════════════════════════════
        if option == 3:
            clear_screen()
            if not pokemon:
                print(f"\n  {BOLD}{BRIGHT_RED}You need Pokemon first!{RESET}")
                time.sleep(1)
                continue
            first = random.choice(first_names)
            last = random.choice(last_names)
            wipe_transition(width=50)
            print_art(ARENA_ENTRANCE_ART, electric_text)
            print()
            fancy_header("ARENA CHALLENGE", emoji="🏟️", width=50)
            print(f"  {BOLD}{BRIGHT_RED}Opponent: {first} {last}{RESET}")
            print(f"  {BOLD}{BRIGHT_WHITE}Reward: {BRIGHT_GREEN}+250 coins, +200 trophies{RESET}")
            print()
            ans = crazy_input("Accept the challenge? (y/n)")
            if ans.lower() != 'y':
                continue

            arena_weather = get_random_weather()
            arena_team = {}
            max_player_lvl = max(s.get("lvl", 1) for s in pokemon.values())
            for i in range(2):
                lvl = random.randint(1, max(5, max_player_lvl))
                arena, hp, dm, typ, moves, shiny, spd = get_wild_pokemon(lvl, location)
                arena_team[arena] = {"hp": hp, "maxhp": hp, "dm": dm, "speed": spd, "type": typ, "moves": moves, "lvl": lvl // 10 + 1}
            
            print(f"  {BOLD}{BRIGHT_CYAN}Enemy team:{RESET}")
            for pn, st in arena_team.items():
                print(f"    {BRIGHT_RED}{pn}{RESET}  Lvl {st['lvl']}  {st['type']}  HP:{st['hp']} DM:{st['dm']}")
            print()
            print(f"  {BOLD}{BRIGHT_GREEN}Your team:{RESET}")
            for pn, st in pokemon.items():
                hp_pct = int((st['hp'] / st['maxhp']) * 100) if st['maxhp'] > 0 else 0
                bar_color = BRIGHT_GREEN if hp_pct > 60 else (BRIGHT_YELLOW if hp_pct > 30 else BRIGHT_RED)
                bar = f"{bar_color}{'█' * (hp_pct // 5)}{DIM}{'░' * (20 - hp_pct // 5)}{RESET}"
                print(f"    {pn}  {bar} {st['hp']}/{st['maxhp']}")
            print()
            
            battle_context = {"mode": "Arena", "inventory": inventory, "player_team": pokemon}
            won, xp_dict, money_gained = run_team_battle(pokemon, arena_team, arena_weather, battle_context)
            if won:
                money += 250 + money_gained
                trophies += 200
                print_art(VICTORY_ROYALE_ART, rainbow_text)
                victory_celebration(lines=3, width=35)
                print(f"  {BOLD}{BRIGHT_GREEN}🏆 You beat {first} {last}!{RESET}")
                print(f"  {BRIGHT_YELLOW}+{250 + money_gained} coins, +200 trophies{RESET}")
                for qid, q in quest_manager.hook_battle_win("arena"):
                    print(f"  {BRIGHT_YELLOW}🎉 Quest #{qid} complete! {q['reward_desc']}!{RESET}")
                achievement_manager.hook_badge(len(badges))
            else:
                print_art(DEFEAT_ART, lambda t: gradient_text(t, (255, 0, 0), (80, 0, 0)))
                defeat_rain(lines=3, width=35)
                print(f"  {BOLD}{BRIGHT_RED}💀 Lost to {first} {last}...{RESET}")
            crazy_input("Press Enter to continue")

        # ══════════════════════════════════════
        # OPTION 4: SHOP
        # ══════════════════════════════════════
        if option == 4:
            clear_screen()
            wipe_transition(width=50)
            print_art(SHOP_ENTRANCE_ART, rainbow_text)
            typewriter("  Welcome to the Poké Mart!", delay=0.02, color=BRIGHT_GREEN)
            print(f"  {money_display(money)}")
            print()
            print()
            menu_divider(38)
            print(f"  {BOLD}{BRIGHT_GREEN}1.{RESET} {gradient_text('🛒 Buy Pokemon', (0, 255, 0), (0, 200, 100))}")
            print(f"  {BOLD}{BRIGHT_BLUE}2.{RESET} {theme_text('🎒 Buy Items')}")
            print(f"  {BOLD}{BRIGHT_CYAN}3.{RESET} {theme_text('🎫 Buy Heal Tickets')}  {DIM}10 for 200 coins{RESET}")
            print(f"  {BOLD}{BRIGHT_RED}4.{RESET} {fire_text('💪 Train Pokemon')}")
            print(f"  {BOLD}{BRIGHT_YELLOW}5.{RESET} {electric_text('🔨 Craft Items')}")
            print(f"  {BOLD}{BRIGHT_MAGENTA}6.{RESET} {psychic_text('🧠 Move Relearner')}")
            menu_divider(38)
            shopoption = crazy_int_input("What do you want to do")
            print()

            if shopoption == 1:
                fancy_header("POKÉMON SHOP", emoji="🛒", width=45)
                pokeoption = 0
                while pokeoption != 4:
                    print()
                    menu_divider(42)
                    print(f"  {BOLD}{BRIGHT_GREEN}1.{RESET} {gradient_text('🌱 Starter', (0, 200, 0), (100, 255, 100))}")
                    print(f"  {BOLD}{BRIGHT_YELLOW}2.{RESET} {electric_text('⚡ Competitive')}")
                    print(f"  {BOLD}{BRIGHT_MAGENTA}3.{RESET} {psychic_text('🌟 Legendary/Mythic')}")
                    print(f"  {BOLD}{DIM}4.{RESET} {DIM}🚪 Leave{RESET}")
                    menu_divider(42)
                    pokeoption = crazy_int_input("What do you want")

                    if pokeoption in [1, 2, 3]:
                        shops = {1: (pokemonshop_starter, "STARTER"), 2: (pokemonshop_competitive, "COMPETITIVE"), 3: (pokemonshop_legends, "LEGENDARY")}
                        shop, shop_name = shops[pokeoption]
                        fancy_header(f"{shop_name} SHOP", emoji="🏪", width=45)
                        for i, (pn, st) in enumerate(shop.items(), 1):
                            shop_item_card(pn, st['cost'], st['hp'], st['dm'], i)
                        print()
                        buy_choice = crazy_input("Which pokemon do you want")
                        if buy_choice in shop:
                            st = shop[buy_choice]
                            if money >= st['cost']:
                                pokeball_loading(f"Purchasing {buy_choice}", duration=1.0)
                                pokeball_transition(width=35)
                                pokemon[buy_choice.lower()] = make_pokemon(st['hp'], st['dm'], st.get("type", "Normal"), st.get("moves", ["Tackle"]), speed=st.get("speed", 50))
                                pokedex_seen.add(buy_choice.lower())
                                pokedex_caught.add(buy_choice.lower())
                                explode_print(f"You bought {buy_choice}!")
                                money -= st['cost']
                                print(f"  {money_display(money)}")
                                crazy_input("Press Enter to continue")
                                break
                            else:
                                print(f"  {BOLD}{BRIGHT_RED}❌ Not enough coins!{RESET}")
                        else:
                            print(f"  {BOLD}{BRIGHT_RED}❌ Not found in shop.{RESET}")

            elif shopoption == 2:
                fancy_header("ITEM SHOP", emoji="🎒", width=45)
                print(f"  {BOLD}{BRIGHT_WHITE}1.{RESET} {BRIGHT_CYAN}Consumables{RESET}")
                print(f"  {BOLD}{BRIGHT_WHITE}2.{RESET} {BRIGHT_YELLOW}Held Items{RESET}")
                print(f"  {BOLD}{BRIGHT_WHITE}3.{RESET} {RED}Back{RESET}")
                item_cat = crazy_int_input("Choose category")
                if item_cat == 1:
                    fancy_header("CONSUMABLES", emoji="🎒", width=45)
                    item_list = list(ITEMS.keys())
                    consumable_keys = [k for k in item_list if ITEMS[k].get("effect",{}).get("type") != "held_item"]
                    for i, item_name in enumerate(consumable_keys, 1):
                        data = ITEMS[item_name]
                        print(f"  {BOLD}{BRIGHT_WHITE}{i:2}.{RESET} {BRIGHT_CYAN}{item_name:15}{RESET} [Cost: {data['price']:4} | {data['description']}]")
                    print(f"  {BOLD}{BRIGHT_WHITE}{len(consumable_keys)+1:2}.{RESET} {RED}Back{RESET}")
                    i_choice = crazy_int_input("What do you want to buy")
                    if 1 <= i_choice <= len(consumable_keys):
                        item_name = consumable_keys[i_choice-1]
                        item_data = ITEMS[item_name]
                        if money >= item_data["price"]:
                            money -= item_data["price"]
                            inventory[item_name] = inventory.get(item_name, 0) + 1
                            print(f"\n  {BOLD}{BRIGHT_GREEN}✨ Bought {item_name}!{RESET}")
                            crazy_input("Press Enter to continue")
                        else:
                            print(f"\n  {BOLD}{BRIGHT_RED}❌ Not enough money!{RESET}")
                elif item_cat == 2:
                    fancy_header("HELD ITEMS", emoji="🎒", width=45)
                    held_list = ["Leftovers","Choice Band","Choice Scarf","Life Orb","Expert Belt","Focus Sash",
                                 "Rocky Helmet","Shell Bell","Oran Berry","Sitrus Berry","Lum Berry",
                                 "Charcoal","Mystic Water","Miracle Seed","Magnet",
                                 "Charizardite X","Charizardite Y","Venusaurite","Blastoisinite","Mewtwonite Y","Gengarite","Alakazite",
                                 "Pikashunium Z","Firium Z","Electrium Z","Waterium Z","Grassium Z","Normalium Z"]
                    for i, item_name in enumerate(held_list, 1):
                        held_data = HELD_ITEMS.get(item_name, {})
                        price = held_data.get("price", 500)
                        desc = held_data.get("desc", "")
                        print(f"  {BOLD}{BRIGHT_WHITE}{i:2}.{RESET} {BRIGHT_YELLOW}{item_name:15}{RESET} [Cost: {price:4} | {desc[:35]}]")
                    print(f"  {BOLD}{BRIGHT_WHITE}{len(held_list)+1:2}.{RESET} {RED}Back{RESET}")
                    i_choice = crazy_int_input("What held item do you want")
                    if 1 <= i_choice <= len(held_list):
                        item_name = held_list[i_choice-1]
                        held_data = HELD_ITEMS.get(item_name, {})
                        price = held_data.get("price", 500)
                        if money >= price:
                            money -= price
                            inventory[item_name] = inventory.get(item_name, 0) + 1
                            print(f"\n  {BOLD}{BRIGHT_GREEN}✨ Bought {item_name}!{RESET}")
                            crazy_input("Press Enter to continue")
                        else:
                            print(f"\n  {BOLD}{BRIGHT_RED}❌ Not enough money!{RESET}")

            elif shopoption == 3:
                clear_screen()
                fancy_header("HEAL TICKETS", emoji="🎫", width=45)
                print(f"  {BOLD}{BRIGHT_WHITE}💰 Coins: {money}{RESET}  |  {BRIGHT_CYAN}🎫 Tickets: {heal_tickets}{RESET}")
                print()
                print(f"  {BOLD}{BRIGHT_GREEN}1.{RESET} Buy 10 tickets  {DIM}(200 coins){RESET}")
                print(f"  {BOLD}{BRIGHT_YELLOW}2.{RESET} Buy 50 tickets  {DIM}(900 coins){RESET}")
                print(f"  {BOLD}{BRIGHT_MAGENTA}3.{RESET} Buy 100 tickets {DIM}(1600 coins){RESET}")
                print(f"  {BOLD}{DIM}4.{RESET} Back")
                print()
                tk_opt = crazy_int_input("Choose")
                if tk_opt == 1:
                    if money >= 200:
                        money -= 200
                        heal_tickets += 10
                        print(f"  {BRIGHT_GREEN}✨ Bought 10 heal tickets!{RESET}")
                    else:
                        print(f"  {BRIGHT_RED}❌ Need 200 coins!{RESET}")
                elif tk_opt == 2:
                    if money >= 900:
                        money -= 900
                        heal_tickets += 50
                        print(f"  {BRIGHT_GREEN}✨ Bought 50 heal tickets!{RESET}")
                    else:
                        print(f"  {BRIGHT_RED}❌ Need 900 coins!{RESET}")
                elif tk_opt == 3:
                    if money >= 1600:
                        money -= 1600
                        heal_tickets += 100
                        print(f"  {BRIGHT_GREEN}✨ Bought 100 heal tickets!{RESET}")
                    else:
                        print(f"  {BRIGHT_RED}❌ Need 1600 coins!{RESET}")
                crazy_input("Press Enter to continue")

            elif shopoption == 4:
                display_pokemon_stats(pokemon, name, money, trophies)
                poke_to_train = crazy_input("Which pokemon do you want to train")
                if poke_to_train in pokemon:
                    print(f"  {BOLD}{BRIGHT_GREEN}1.{RESET} Train Health")
                    print(f"  {BOLD}{BRIGHT_RED}2.{RESET} Train Damage")
                    stat_choice = crazy_int_input("What to train")
                    s_type = "hp" if stat_choice == 1 else "dm"
                    money = train_pokemon(pokemon, poke_to_train, money, s_type)
                else:
                    print(f"  {BOLD}{BRIGHT_RED}❌ Pokemon not found!{RESET}")
                crazy_input("Press Enter to continue")

            elif shopoption == 5:
                fancy_header("ITEM CRAFTING", emoji="🔨", width=45)
                print(f"  {DIM}Combine items from your bag to craft new ones!{RESET}")
                print()
                if len(inventory) < 2:
                    print(f"  {BOLD}{BRIGHT_RED}❌ Need at least 2 different item types to craft!{RESET}")
                    crazy_input("Press Enter to continue")
                else:
                    # Generate random recipe from inventory items
                    bag_items = list(inventory.keys())
                    num_ingredients = min(random.randint(2, 4), len(bag_items))
                    recipe_ing = random.sample(bag_items, num_ingredients)
                    recipe_qtys = {}
                    for ing in recipe_ing:
                        max_qty = min(inventory[ing], random.randint(1, 5))
                        recipe_qtys[ing] = max(1, max_qty)
                    
                    # Pick result from available items
                    all_items = list(ITEMS.keys())
                    result_item = random.choice(all_items)
                    result_qty = random.randint(1, 3)
                    
                    print(f"  {BOLD}{BRIGHT_YELLOW}🔨 Recipe Found!{RESET}")
                    print()
                    print(f"  {BOLD}{BRIGHT_WHITE}Ingredients:{RESET}")
                    for ing, qty in recipe_qtys.items():
                        have = inventory.get(ing, 0)
                        color = BRIGHT_GREEN if have >= qty else BRIGHT_RED
                        print(f"    {color}{ing} x{qty}{RESET} {DIM}(you have {have}){RESET}")
                    print()
                    print(f"  {BOLD}{BRIGHT_GREEN}Result:{RESET} {result_item} x{result_qty}")
                    success_rate = 75
                    print(f"  {DIM}Success rate: {success_rate}%{RESET}")
                    print()
                    ans = crazy_input("Attempt to craft? (y/n)")
                    if ans.lower() == 'y':
                        can_craft = all(inventory.get(ing, 0) >= qty for ing, qty in recipe_qtys.items())
                        if not can_craft:
                            print(f"  {BOLD}{BRIGHT_RED}❌ Not enough ingredients!{RESET}")
                        else:
                            spinner_animation("Crafting", duration=2.0)
                            if random.random() * 100 < success_rate:
                                for ing, qty in recipe_qtys.items():
                                    inventory[ing] -= qty
                                    if inventory[ing] <= 0:
                                        del inventory[ing]
                                inventory[result_item] = inventory.get(result_item, 0) + result_qty
                                print(f"  {BOLD}{BRIGHT_GREEN}✅ Crafted {result_qty}x {result_item}!{RESET}")
                                print(f"  {BOLD}{BRIGHT_YELLOW}💰 +50 coins (savings){RESET}")
                                money += 50
                            else:
                                for ing, qty in recipe_qtys.items():
                                    inventory[ing] -= qty
                                    if inventory[ing] <= 0:
                                        del inventory[ing]
                                print(f"  {BOLD}{BRIGHT_RED}💥 Crafting failed! Lost the ingredients!{RESET}")
                    crazy_input("Press Enter to continue")

            elif shopoption == 6:
                fancy_header("MOVE RELEARNER", emoji="🧠", width=45)
                if not pokemon:
                    print(f"  {BOLD}{BRIGHT_RED}❌ You need Pokemon first!{RESET}")
                    crazy_input("Press Enter to continue")
                else:
                    display_pokemon_stats(pokemon, name, money, trophies)
                    relearn_choice = crazy_input("Which pokemon should remember a move")
                    if relearn_choice not in pokemon:
                        print(f"  {BOLD}{BRIGHT_RED}❌ Pokemon not found!{RESET}")
                        crazy_input("Press Enter to continue")
                    else:
                        stats = pokemon[relearn_choice]
                        relearnable_moves = get_eligible_learnset_moves(
                            relearn_choice,
                            stats.get("lvl", 1),
                            stats.get("moves", [])
                        )
                        if not relearnable_moves:
                            print(f"  {BOLD}{BRIGHT_GREEN}✅ {relearn_choice.capitalize()} has no forgotten moves to relearn.{RESET}")
                            crazy_input("Press Enter to continue")
                        else:
                            cost = 250 + stats.get("lvl", 1) * 25
                            print(f"  {BOLD}{BRIGHT_YELLOW}Cost:{RESET} {cost} coins")
                            print(f"  {money_display(money)}")
                            print()
                            for i, move_name in enumerate(relearnable_moves, 1):
                                move_data = MOVES.get(move_name, {"type": "Normal", "power": 0, "pp": 15, "category": "Status"})
                                print(f"  {BOLD}{BRIGHT_WHITE}{i}.{RESET} {BRIGHT_CYAN}{move_name:15}{RESET} "
                                      f"[{move_data['type']}/{move_data['category']}/{move_data['power']}] "
                                      f"PP: {get_max_pp(move_name)}")
                            print(f"  {BOLD}{BRIGHT_WHITE}{len(relearnable_moves)+1}.{RESET} {RED}Back{RESET}")
                            move_choice = crazy_int_input("Which move should be remembered")
                            if 1 <= move_choice <= len(relearnable_moves):
                                if money < cost:
                                    print(f"  {BOLD}{BRIGHT_RED}❌ Not enough coins! Need {cost}, have {money}{RESET}")
                                else:
                                    learned = offer_to_learn_move(stats, relearnable_moves[move_choice-1])
                                    if learned:
                                        money -= cost
                                        print(f"  {BOLD}{BRIGHT_GREEN}✨ Move relearned!{RESET}")
                                        print(f"  {money_display(money)}")
                                    else:
                                        print(f"  {DIM}No coins spent.{RESET}")
                            crazy_input("Press Enter to continue")

        # ══════════════════════════════════════
        # OPTION 5: HOSPITAL
        # ══════════════════════════════════════
        if option == 5:
            clear_screen()
            wipe_transition(width=50)
            print_art(HOSPITAL_ENTRANCE_ART, lambda t: gradient_text(t, (0, 200, 100), (0, 255, 200)))
            typewriter("  Welcome to the Pokémon Center!", delay=0.02, color=BRIGHT_GREEN)
            print()
            print(f"  {BOLD}{BRIGHT_WHITE}💰 Coins: {money}{RESET}  |  {BRIGHT_CYAN}🎫 Heal Tickets: {heal_tickets}{RESET}")
            print()
            menu_divider(40)
            print(f"  {BOLD}{BRIGHT_GREEN}1.{RESET} {gradient_text('❤️  Heal HP', (0, 255, 0), (0, 200, 100))}  {DIM}Cost: 1 ticket{RESET}")
            print(f"  {BOLD}{BRIGHT_MAGENTA}2.{RESET} {psychic_text('💊 Full Heal')}  {DIM}Cost: 2 tickets{RESET}")
            print(f"  {BOLD}{BRIGHT_YELLOW}3.{RESET} {theme_text('🌟 Heal All')}  {DIM}Cost: 5 tickets{RESET}")
            print(f"  {BOLD}{DIM}4.{RESET} {DIM}🚪 Leave{RESET}")
            menu_divider(40)
            hosp_option = crazy_int_input("Choose service")
            if hosp_option == 1:
                clear_screen()
                print(f"  {BOLD}{BRIGHT_WHITE}🎫 Tickets: {heal_tickets}{RESET}\n")
                for pn, st in pokemon.items():
                    hp_pct = int((st['hp'] / st['maxhp']) * 100) if st['maxhp'] > 0 else 0
                    status = st.get('status', None)
                    status_tag = f" {BRIGHT_RED}[{status}]{RESET}" if status else ""
                    bar_color = BRIGHT_GREEN if hp_pct > 60 else (BRIGHT_YELLOW if hp_pct > 30 else BRIGHT_RED)
                    bar = f"{bar_color}{'█' * (hp_pct // 5)}{DIM}{'░' * (20 - hp_pct // 5)}{RESET}"
                    print(f"  {BOLD}{pn}{status_tag}  {bar} {st['hp']}/{st['maxhp']} ({hp_pct}%){RESET}")
                print()
                if heal_tickets < 1:
                    print(f"  {BRIGHT_RED}❌ Not enough tickets! Buy more at the shop.{RESET}")
                    crazy_input("Press Enter to continue")
                else:
                    poke_to_heal = crazy_input("Who do you want to heal (or 'all')")
                    if poke_to_heal.lower() == 'all':
                        healed = 0
                        for pn, st in pokemon.items():
                            if st['hp'] < st['maxhp'] or st.get('status'):
                                st['hp'] = st['maxhp']
                                st['status'] = None
                                restore_all_pp(st)
                                healed += 1
                        heal_tickets -= 1
                        print(f"  {BRIGHT_GREEN}✨ Healed {healed} Pokemon! (-1 ticket){RESET}")
                    elif poke_to_heal in pokemon:
                        if pokemon[poke_to_heal]['hp'] >= pokemon[poke_to_heal]['maxhp'] and not pokemon[poke_to_heal].get('status'):
                            print(f"  {BRIGHT_YELLOW}{poke_to_heal} is already at full health!{RESET}")
                        else:
                            spinner_animation(f"Healing {poke_to_heal}", duration=0.8)
                            pokemon[poke_to_heal]['hp'] = pokemon[poke_to_heal]['maxhp']
                            pokemon[poke_to_heal]['status'] = None
                            restore_all_pp(pokemon[poke_to_heal])
                            heal_tickets -= 1
                            print(f"  {BRIGHT_GREEN}✨ {poke_to_heal} fully healed! (-1 ticket){RESET}")
                    else:
                        print(f"  {BRIGHT_RED}❌ Pokemon not found{RESET}")
                    crazy_input("Press Enter to continue")
            elif hosp_option == 2:
                clear_screen()
                print(f"  {BOLD}{BRIGHT_WHITE}🎫 Tickets: {heal_tickets}{RESET}\n")
                for pn, st in pokemon.items():
                    has_status = st.get("status") is not None
                    status_tag = f" [{BRIGHT_RED}{st['status']}{RESET}]" if has_status else f" [{BRIGHT_GREEN}Healthy{RESET}]"
                    print(f"  {BOLD}{BRIGHT_CYAN}- {pn}{status_tag}{RESET}")
                print()
                if heal_tickets < 2:
                    print(f"  {BRIGHT_RED}❌ Need 2 tickets!{RESET}")
                    crazy_input("Press Enter to continue")
                else:
                    poke_to_heal = crazy_input("Which pokemon to cure")
                    if poke_to_heal in pokemon and pokemon[poke_to_heal].get("status"):
                        spinner_animation(f"Curing {poke_to_heal}", duration=0.8)
                        pokemon[poke_to_heal]["status"] = None
                        heal_tickets -= 2
                        print(f"  {BRIGHT_GREEN}✨ {poke_to_heal} is fully cured! (-2 tickets){RESET}")
                    elif poke_to_heal not in pokemon:
                        print(f"  {BRIGHT_RED}❌ Pokemon not found{RESET}")
                    else:
                        print(f"  {BRIGHT_YELLOW}{poke_to_heal} has no status condition{RESET}")
                    crazy_input("Press Enter to continue")
            elif hosp_option == 3:
                clear_screen()
                if heal_tickets < 5:
                    print(f"  {BRIGHT_RED}❌ Need 5 tickets to heal all!{RESET}")
                    crazy_input("Press Enter to continue")
                else:
                    print(f"  {BOLD}{BRIGHT_YELLOW}🌟 Healing all Pokemon...{RESET}")
                    spinner_animation("Healing", duration=1.5)
                    for pn, st in pokemon.items():
                        st['hp'] = st['maxhp']
                        st['status'] = None
                        restore_all_pp(st)
                    heal_tickets -= 5
                    print(f"  {BRIGHT_GREEN}✨ All Pokemon fully healed! (-5 tickets){RESET}")
                    crazy_input("Press Enter to continue")

        # ══════════════════════════════════════
        # OPTION 6: BAG
        # ══════════════════════════════════════
        if option == 6:
            clear_screen()
            if not pokemon:
                print(f"\n  {BOLD}{BRIGHT_RED}You have no Pokemon to use items on!{RESET}")
                time.sleep(1)
            else:
                fancy_header("BAG", emoji="🎒", width=45)
                print(f"  {BOLD}{BRIGHT_WHITE}💰 Coins: {money}{RESET}  |  {BRIGHT_CYAN}🎫 Tickets: {heal_tickets}{RESET}")
                print()
                print(f"  {BOLD}{BRIGHT_WHITE}1.{RESET} Use consumable item")
                print(f"  {BOLD}{BRIGHT_YELLOW}2.{RESET} Equip/Unequip held item")
                print(f"  {BOLD}{BRIGHT_GREEN}3.{RESET} View team status")
                print(f"  {BOLD}{DIM}4.{RESET} Back")
                bag_opt = crazy_int_input("Choose")
                if bag_opt == 1:
                    clear_screen()
                    fancy_header("USE ITEM", emoji="🎒", width=45)
                    print(f"  {BOLD}{BRIGHT_CYAN}Your Pokemon:{RESET}")
                    for i, (pn, st) in enumerate(pokemon.items(), 1):
                        hp_pct = int((st['hp'] / st['maxhp']) * 100) if st['maxhp'] > 0 else 0
                        status = st.get('status', None)
                        status_tag = f" {BRIGHT_RED}[{status}]{RESET}" if status else ""
                        bar_color = BRIGHT_GREEN if hp_pct > 60 else (BRIGHT_YELLOW if hp_pct > 30 else BRIGHT_RED)
                        bar = f"{bar_color}{'█' * (hp_pct // 5)}{DIM}{'░' * (20 - hp_pct // 5)}{RESET}"
                        print(f"  {BOLD}{i}.{RESET} {pn}{status_tag}  {bar} {st['hp']}/{st['maxhp']}")
                    print()
                    p_idx = crazy_int_input("Select Pokemon")
                    poke_list = list(pokemon.keys())
                    if 1 <= p_idx <= len(poke_list):
                        p_choice = poke_list[p_idx - 1]
                        use_item_menu(inventory, pokemon[p_choice], pokemon, p_choice)
                    else:
                        print(f"\n  {BRIGHT_RED}❌ Invalid selection!{RESET}")
                        time.sleep(1)
                elif bag_opt == 2:
                    held_inv = [k for k in inventory if k in HELD_ITEMS]
                    if not held_inv:
                        print(f"\n  {BOLD}{BRIGHT_RED}No held items in bag! Buy them at the shop.{RESET}")
                        crazy_input("Press Enter to continue")
                    else:
                        print(f"  {BOLD}{BRIGHT_CYAN}Your Held Items:{RESET}")
                        for i, hi in enumerate(held_inv, 1):
                            print(f"  {BOLD}{BRIGHT_WHITE}{i}.{RESET} {hi} x{inventory[hi]}")
                        print(f"  {BOLD}{BRIGHT_WHITE}{len(held_inv)+1}.{RESET} {RED}Cancel{RESET}")
                        hi_choice = crazy_int_input("Select item to equip")
                        if 1 <= hi_choice <= len(held_inv):
                            chosen_item = held_inv[hi_choice - 1]
                            print(f"  {BOLD}{BRIGHT_CYAN}Equip {chosen_item} to which Pokemon?{RESET}")
                            for pn, ps in pokemon.items():
                                cur_item = ps.get("hold_item") or "none"
                                print(f"  {BOLD}{BRIGHT_WHITE}- {pn}{RESET} {DIM}[holding: {cur_item}]{RESET}")
                            eq_choice = crazy_input("Pokemon name")
                            if eq_choice in pokemon:
                                old_item = pokemon[eq_choice].get("hold_item")
                                if old_item:
                                    inventory[old_item] = inventory.get(old_item, 0) + 1
                                pokemon[eq_choice]["hold_item"] = chosen_item
                                inventory[chosen_item] -= 1
                                if inventory[chosen_item] <= 0:
                                    del inventory[chosen_item]
                                print(f"  {BOLD}{BRIGHT_GREEN}✨ {eq_choice} now holds {chosen_item}!{RESET}")
                                crazy_input("Press Enter to continue")
                            else:
                                print(f"\n  {BOLD}{BRIGHT_RED}Pokemon not found!{RESET}")
                                time.sleep(1)
                elif bag_opt == 3:
                    clear_screen()
                    fancy_header("TEAM STATUS", emoji="📊", width=45)
                    for pn, st in pokemon.items():
                        hp_pct = int((st['hp'] / st['maxhp']) * 100) if st['maxhp'] > 0 else 0
                        status = st.get('status', None)
                        ability = st.get('ability', 'None')
                        hold = st.get('hold_item', 'None')
                        status_tag = f" {BRIGHT_RED}[{status}]{RESET}" if status else f" {BRIGHT_GREEN}[OK]{RESET}"
                        bar_color = BRIGHT_GREEN if hp_pct > 60 else (BRIGHT_YELLOW if hp_pct > 30 else BRIGHT_RED)
                        bar = f"{bar_color}{'█' * (hp_pct // 5)}{DIM}{'░' * (20 - hp_pct // 5)}{RESET}"
                        print(f"  {BOLD}{pn}{status_tag}")
                        print(f"    {bar} {st['hp']}/{st['maxhp']}  Lvl {st['lvl']}")
                        print(f"    {DIM}Ability: {ability} | Item: {hold}{RESET}")
                        print()
                    crazy_input("Press Enter to continue")

        # ══════════════════════════════════════
        # OPTION 7: TRAVEL
        # ══════════════════════════════════════
        if option == 7:
            clear_screen()
            wipe_transition(width=50)
            fancy_header("WORLD TRAVEL", emoji="🗺️", width=50)
            print(f"  {BOLD}{BRIGHT_WHITE}Current: {BRIGHT_GREEN}{location}{RESET}")
            print()
            region_list = list(REGIONS.keys())
            for i, r_name in enumerate(region_list):
                marker = " 📍" if r_name == location else ""
                print(f"  {BOLD}{BRIGHT_WHITE}{i+1}.{RESET} {r_name:15}{marker}  {DIM}{REGIONS[r_name]['description'][:40]}{RESET}")
            print()
            t_choice = crazy_int_input("Where do you want to go")
            if 1 <= t_choice <= len(region_list):
                new_location = region_list[t_choice-1]
                if new_location == location:
                    print(f"  {BRIGHT_YELLOW}Already in {location}!{RESET}")
                else:
                    pokeball_transition(width=35)
                    location = new_location
                    print_art(REGIONS[location]["art"], theme_text)
                    print(f"  {BOLD}{BRIGHT_GREEN}🚀 Arrived in {location}!{RESET}")
                    for qid, q in quest_manager.hook_explore(location):
                        print(f"  {BRIGHT_YELLOW}🎉 Quest #{qid} complete! {q['reward_desc']}!{RESET}")
                    achievement_manager.hook_explore(len(set([location] + [location])))
                    
                    # 20% chance to trigger a Procedural World Event during Travel!
                    if random.random() < 0.20:
                        time.sleep(1)
                        clear_screen()
                        print_art(RANDOM_EVENT_ART, lambda t: gradient_text(t, (255, 100, 100), (255, 200, 50)))
                        time.sleep(1.5)
                        
                        event_roll = random.randint(1, 5)
                        if event_roll == 1:
                            fancy_header("TREASURE CACHE", emoji="🎒", width=50)
                            print(f"  {BOLD}You discovered a hidden metal chest in the tall grass!{RESET}")
                            chest_items = ["Master Ball", "Rare Candy", "Ultra Ball", "Max Potion", "Dusk Stone", "Charizardite Y"]
                            reward_item = random.choice(chest_items)
                            inventory[reward_item] = inventory.get(reward_item, 0) + 1
                            print(f"  {BOLD}{BRIGHT_GREEN}🎁 Obtained: 1x {reward_item}!{RESET}")
                            
                        elif event_roll == 2:
                            fancy_header("WILD RESCUE", emoji="🐾", width=50)
                            print(f"  {BOLD}You hear a faint whimper and spot an injured EEVEE cornered by a large boulder!{RESET}")
                            print()
                            print(f"  {BOLD}{BRIGHT_CYAN}1.{RESET} Offer Potion from your Bag")
                            print(f"  {BOLD}{BRIGHT_YELLOW}2.{RESET} Shoo away wild threats and help it escape")
                            choice = crazy_input("Choose action").strip()
                            if choice == "1" and inventory.get("Potion", 0) > 0:
                                inventory["Potion"] -= 1
                                print(f"\n  {BOLD}{BRIGHT_GREEN}💖 The Eevee drinks the potion and feels restored!{RESET}")
                                print(f"  {BOLD}It rubs against your leg gratefully and decides to join your active team!{RESET}")
                                pokemon["eevee"] = make_pokemon(100, 45, "Normal", ["Tackle", "Swift"], speed=60)
                                pokedex_seen.add("eevee")
                                pokedex_caught.add("eevee")
                            else:
                                print(f"\n  {BOLD}You safely shoo away wild threats. The Eevee runs off happily!{RESET}")
                                
                        elif event_roll == 3:
                            fancy_header("LEGENDARY SIGHTING", emoji="🌟", width=50)
                            print(f"  {BOLD}{BRIGHT_MAGENTA}An imposing presence appears! The sky turns crimson...{RESET}")
                            roamer_names = ["arceus", "mew", "celebi", "giratina"]
                            roamer = random.choice(roamer_names)
                            print(f"  {BOLD}{BRIGHT_YELLOW}⚡ A legendary wild {roamer.upper()} appeared! ⚡{RESET}")
                            print()
                            ans = crazy_input("Engage in legendary battle? (y/n)")
                            if ans.lower() == 'y':
                                avg_lvl = sum(m.get("lvl", 5) for m in pokemon.values()) // len(pokemon)
                                enemy_mon = {roamer: make_pokemon(int(avg_lvl * 15), int(avg_lvl * 8), "Psychic", ["Confusion", "Swift"], speed=100)}
                                enemy_mon[roamer]["lvl"] = avg_lvl + 5
                                
                                pvp_battle_context = {"mode": "Wild Encounter", "inventory": inventory, "player_team": pokemon}
                                run_team_battle(pokemon, enemy_mon, "Fog", pvp_battle_context)
                                
                        elif event_roll == 4:
                            fancy_header("TRAVELING MERCHANT", emoji="🏪", width=50)
                            print(f"  {BOLD}A shady traveling merchant calls out to you...{RESET}")
                            print(f"  \"Psst! Hey kid, I have a rare item at a special price...\"")
                            print(f"  Offers: {BOLD}{BRIGHT_YELLOW}Mystic Z-Crystal{RESET} for {BOLD}600 coins{RESET}.")
                            print()
                            merchant_ans = crazy_input("Purchase the mystery crystal? (y/n)")
                            if merchant_ans.lower() == 'y':
                                if money >= 600:
                                    money -= 600
                                    crystal = random.choice(["Grassium Z", "Firium Z", "Waterium Z", "Electrium Z"])
                                    inventory[crystal] = inventory.get(crystal, 0) + 1
                                    print(f"\n  {BOLD}{BRIGHT_GREEN}🛍️ Purchased 1x {crystal}!{RESET}")
                                else:
                                    print(f"\n  {BOLD}{BRIGHT_RED}❌ Not enough coins!{RESET}")
                                    
                        elif event_roll == 5:
                            fancy_header("TRAINER AMBUSH!", emoji="⚔️", width=50)
                            print(f"  {BOLD}{BRIGHT_RED}An elite trainer jumps out from the shadows!{RESET}")
                            print(f"  \"No traveler passes my path without a battle!\"{RESET}")
                            print()
                            crazy_input("Prepare for battle! Press Enter")
                            avg_lvl = sum(m.get("lvl", 5) for m in pokemon.values()) // len(pokemon)
                            opp_team = {
                                "garchomp": make_pokemon(int(avg_lvl * 12), int(avg_lvl * 6), "Dragon", ["Tackle"], speed=80),
                                "lucario": make_pokemon(int(avg_lvl * 10), int(avg_lvl * 7), "Steel", ["Tackle"], speed=75)
                            }
                            opp_team["garchomp"]["lvl"] = avg_lvl
                            opp_team["lucario"]["lvl"] = avg_lvl
                            
                            pvp_battle_context = {"mode": "Trainer Battle", "inventory": inventory, "player_team": pokemon}
                            won, pvp_xp, pvp_money = run_team_battle(pokemon, opp_team, "Clear", pvp_battle_context)
                            if won:
                                reward_coins = avg_lvl * 100
                                money += reward_coins
                                print(f"\n  {BOLD}{BRIGHT_GREEN}🎉 You defeated the ambush! Gained {reward_coins} coins!{RESET}")
                                
                        crazy_input("\nPress Enter to complete travel")
                time.sleep(1)

        # ══════════════════════════════════════
        # OPTION 8: SETTINGS
        # ══════════════════════════════════════
        if option == 8:
            clear_screen()
            run_settings_menu()

        # ══════════════════════════════════════
        # OPTION 9: CLOUD ACCOUNT
        # ══════════════════════════════════════
        if option == 9:
            clear_screen()
            fancy_header("CLOUD ACCOUNT", emoji="☁️", width=50)
            status = f"{BRIGHT_GREEN}{cloud_username}{RESET}" if cloud_token else f"{DIM}Not logged in{RESET}"
            print(f"  {BOLD}Status: {status}{RESET}")
            print()
            print(f"  {BOLD}{BRIGHT_WHITE}1.{RESET} Register new account")
            print(f"  {BOLD}{BRIGHT_WHITE}2.{RESET} Login")
            print(f"  {BOLD}{BRIGHT_WHITE}3.{RESET} Push save to cloud")
            print(f"  {BOLD}{BRIGHT_WHITE}4.{RESET} Pull save from cloud")
            print(f"  {BOLD}{BRIGHT_WHITE}5.{RESET} View registered accounts")
            print(f"  {BOLD}{BRIGHT_WHITE}6.{RESET} Logout")
            print(f"  {BOLD}{DIM}Q.{RESET} Back")
            cloud_opt = crazy_input("Choose")
            if cloud_opt == "1":
                username = crazy_input("Username").strip()
                password = crazy_input("Password").strip()
                try:
                    r = robust_request("POST", f"{SERVER_URL}/register", json_data={"username": username, "password": password}, timeout=30)
                    if r.status_code == 201:
                        print(f"  {BRIGHT_GREEN}✅ {r.json().get('message', 'Account created!')}{RESET}")
                    else:
                        print(f"  {BRIGHT_RED}❌ {r.json().get('message', 'Error')}{RESET}")
                except Exception as e:
                    print(f"  {BRIGHT_RED}❌ Server error: {e}{RESET}")
                crazy_input("Press Enter to continue")
            elif cloud_opt == "2":
                username = crazy_input("Username").strip()
                password = crazy_input("Password").strip()
                try:
        r = robust_request("POST", f"{SERVER_URL}/login", json_data={"username": username, "password": password}, timeout=30)
                    if r.status_code == 200:
                        cloud_token = r.json()["token"]
                        cloud_username = r.json().get("username", username)
                        print(f"  {BRIGHT_GREEN}✅ Logged in as {cloud_username}!{RESET}")
                    else:
                        print(f"  {BRIGHT_RED}❌ {r.json().get('message', 'Error')}{RESET}")
                except Exception as e:
                    print(f"  {BRIGHT_RED}❌ Server error: {e}{RESET}")
                crazy_input("Press Enter to continue")
            elif cloud_opt == "3" and cloud_token:
                try:
                    save_data = json.dumps({"name": name, "pokemon": pokemon, "money": money, "trophies": trophies, "inventory": inventory, "location": location, "badges": badges, "tower_record": tower_record, "pokedex_seen": list(pokedex_seen), "pokedex_caught": list(pokedex_caught), "elite_four_defeated": elite_four_defeated, "achievements": achievement_manager.to_dict(), "heal_tickets": heal_tickets, "daycare": daycare, "pvp_rp": pvp_rp, "shiny_chain": shiny_chain, "last_encounter_species": last_encounter_species, "login_streak": login_streak, "last_login_date": last_login_date, "daily_raid_completed": daily_raid_completed, "daily_species_caught": list(daily_species_caught), "frontier_progress": frontier_progress})
                    r = robust_request("POST", f"{SERVER_URL}/save", json_data={"save_data": save_data}, headers={"Authorization": f"Bearer {cloud_token}"}, timeout=30)
                    if r.status_code == 200:
                        print(f"  {BRIGHT_GREEN}✅ {r.json().get('message', 'Save pushed to cloud!')}{RESET}")
                    else:
                        print(f"  {BRIGHT_RED}❌ {r.json().get('message', 'Error')}{RESET}")
                except Exception as e:
                    print(f"  {BRIGHT_RED}❌ Server error: {e}{RESET}")
                crazy_input("Press Enter to continue")
            elif cloud_opt == "4" and cloud_token:
                try:
                    r = robust_request("GET", f"{SERVER_URL}/load", headers={"Authorization": f"Bearer {cloud_token}"}, timeout=30)
                    if r.status_code == 200:
                        data = json.loads(r.json()["save_data"])
                        name = data.get("name", name)
                        pokemon = data.get("pokemon", pokemon)
                        money = data.get("money", money)
                        trophies = data.get("trophies", trophies)
                        inventory = data.get("inventory", inventory)
                        location = data.get("location", location)
                        badges = data.get("badges", badges)
                        tower_record = data.get("tower_record", tower_record)
                        pokedex_seen = set(data.get("pokedex_seen", []))
                        pokedex_caught = set(data.get("pokedex_caught", []))
                        elite_four_defeated = data.get("elite_four_defeated", [])
                        ach_data = data.get("achievements", {"unlocked":[],"counters":{}})
                        achievement_manager.__dict__.update(AchievementManager.from_dict(ach_data).__dict__)
                        heal_tickets = data.get("heal_tickets", heal_tickets)
                        daycare = data.get("daycare", daycare)
                        pvp_rp = data.get("pvp_rp", pvp_rp)
                        print(f"  {BRIGHT_GREEN}✅ Save loaded from cloud!{RESET}")
                    else:
                        print(f"  {BRIGHT_RED}❌ {r.json().get('message', 'Error')}{RESET}")
                except Exception as e:
                    print(f"  {BRIGHT_RED}❌ Server error: {e}{RESET}")
                crazy_input("Press Enter to continue")
            elif cloud_opt == "5":
                clear_screen()
                fancy_header("REGISTERED ACCOUNTS", emoji="👥", width=50)
                try:
                    r = robust_request("GET", f"{SERVER_URL}/accounts", timeout=30)
                    if r.status_code == 200:
                        accounts = r.json().get("accounts", [])
                        total = r.json().get("total", 0)
                        print(f"  {BOLD}{BRIGHT_CYAN}Total accounts: {total}{RESET}")
                        print()
                        if accounts:
                            for i, acc in enumerate(accounts, 1):
                                created = acc.get("created", "unknown")
                                print(f"  {BOLD}{BRIGHT_WHITE}{i}.{RESET} {BRIGHT_GREEN}{acc['username']}{RESET} {DIM}(since {created}){RESET}")
                        else:
                            print(f"  {DIM}No accounts registered yet.{RESET}")
                    else:
                        print(f"  {BRIGHT_RED}❌ {r.json().get('message', 'Error')}{RESET}")
                except Exception as e:
                    print(f"  {BRIGHT_RED}❌ Server error: {e}{RESET}")
                crazy_input("Press Enter to continue")
            elif cloud_opt == "6":
                cloud_token = None
                cloud_username = None
                print(f"  {BRIGHT_YELLOW}Logged out.{RESET}")
                crazy_input("Press Enter to continue")

        # ══════════════════════════════════════
        # OPTION 10: GYM CHALLENGE
        # ══════════════════════════════════════
        if option == 11:
            clear_screen()
            gym_badges = [b for b in badges if any(b == g[1]["badge"] for g in GYM_LEADERS.items())]
            if len(gym_badges) >= len(GYM_LEADERS):
                print(f"\n  {BOLD}{BRIGHT_YELLOW}🏆 You already have all badges!{RESET}")
                time.sleep(1)
                continue
            gym_list = list(GYM_LEADERS.items())
            next_gym_idx = len(gym_badges)
            if next_gym_idx >= len(gym_list):
                print(f"\n  {BOLD}{BRIGHT_YELLOW}🏆 All gyms completed!{RESET}")
                time.sleep(1)
                continue
            gl_name, gl_data = gym_list[next_gym_idx]
            wipe_transition(width=50)
            fancy_header(f"{gl_name}'s GYM", emoji="🏅", width=50)
            print(f"  {BOLD}{BRIGHT_WHITE}Type: {gl_data['type']}  |  Badge: {gl_data['badge']}{RESET}")
            print(f"  {DIM}\"{gl_data['message']}\"{RESET}")
            print()
            print(f"  {BOLD}{BRIGHT_RED}Leader's team:{RESET}")
            for pn, st in gl_data["team"].items():
                print(f"    {pn}  Lvl {st.get('lvl','?')}  {format_type(st.get('type','?'))}  HP:{st.get('hp','?')} DM:{st.get('dm','?')}")
            print()
            print(f"  {BOLD}{BRIGHT_GREEN}Your team:{RESET}")
            for pn, st in pokemon.items():
                hp_pct = int((st['hp'] / st['maxhp']) * 100) if st['maxhp'] > 0 else 0
                bar_color = BRIGHT_GREEN if hp_pct > 60 else (BRIGHT_YELLOW if hp_pct > 30 else BRIGHT_RED)
                bar = f"{bar_color}{'█' * (hp_pct // 5)}{DIM}{'░' * (20 - hp_pct // 5)}{RESET}"
                print(f"    {pn}  {bar} {st['hp']}/{st['maxhp']}")
            print()
            ans = crazy_input("Challenge this gym leader? (y/n)")
            if ans.lower() != 'y': continue
            arena_weather = get_random_weather()
            battle_context = {"mode": "Gym", "inventory": inventory, "player_team": pokemon}
            gym_won, xp_dict, money_gained = run_team_battle(pokemon, gl_data["team"], arena_weather, battle_context)
            if gym_won:
                print_art(VICTORY_ROYALE_ART, rainbow_text)
                victory_celebration(lines=3, width=35)
                explode_print(f"You defeated Gym Leader {gl_name}!")
                badges.append(gl_data["badge"])
                for a in achievement_manager.hook_badge(len(badges)):
                    part = a["reward"]
                    print(f"  {BRIGHT_GREEN}🏅 Achievement: {a['name']}! +{part['value']} {part['type']}!{RESET}")
                reward = 500 + len(badges) * 200
                money += reward + money_gained
                trophies += 300
                print(f"  {BOLD}{BRIGHT_YELLOW}🏅 Earned: {gl_data['badge']}!{RESET}")
                print(f"  {BRIGHT_YELLOW}+{reward} coins, +300 trophies{RESET}")
            else:
                print_art(DEFEAT_ART, lambda t: gradient_text(t, (255, 0, 0), (80, 0, 0)))
                defeat_rain(lines=3, width=35)
                print(f"  {BOLD}{BRIGHT_RED}💀 Gym challenge failed!{RESET}")
            crazy_input("Press Enter to continue")

        # ══════════════════════════════════════
        # OPTION 10: BATTLE TOWER
        # ══════════════════════════════════════
        if option == 10:
            clear_screen()
            if not pokemon:
                print(f"\n  {BOLD}{BRIGHT_RED}You need Pokemon first!{RESET}")
                time.sleep(1)
                continue
            wipe_transition(width=50)
            fancy_header("BATTLE TOWER", emoji="🗼", width=50)
            print(f"  {DIM}Endless gauntlet — how far can you go?{RESET}")
            print(f"  {BOLD}{BRIGHT_YELLOW}🏆 Current Record: {tower_record}{RESET}")
            print()
            print(f"  {BOLD}{BRIGHT_GREEN}Your team:{RESET}")
            for pn, st in pokemon.items():
                hp_pct = int((st['hp'] / st['maxhp']) * 100) if st['maxhp'] > 0 else 0
                bar_color = BRIGHT_GREEN if hp_pct > 60 else (BRIGHT_YELLOW if hp_pct > 30 else BRIGHT_RED)
                bar = f"{bar_color}{'█' * (hp_pct // 5)}{DIM}{'░' * (20 - hp_pct // 5)}{RESET}"
                print(f"    {pn}  {bar} {st['hp']}/{st['maxhp']}")
            print()
            ans = crazy_input("Enter the tower? (y/n)")
            if ans.lower() != 'y':
                continue
                
            # Enhanced Battle Tower with expanded rules and wager system
            print(f"  {DIM}You currently have {money} PokéCoins.{RESET}")
            print(f"  {BOLD}{BRIGHT_WHITE}Wager Options:{RESET}")
            print(f"  {BOLD}{BRIGHT_GREEN}1.{RESET} No Wager  {DIM}[Play for trophies only]{RESET}")
            print(f"  {BOLD}{BRIGHT_YELLOW}2.{RESET} Small Wager  {DIM}[100 coins → 200 every 5 rounds]{RESET}")
            print(f"  {BOLD}{BRIGHT_RED}3.{RESET} Big Wager  {DIM}[500 coins → 1000 every 5 rounds]{RESET}")
            print(f"  {BOLD}{BRIGHT_MAGENTA}4.{RESET} Custom Wager  {DIM}[Enter your amount]{RESET}")
            wager_choice = crazy_int_input("Choose wager level")
            
            wager = 0
            wager_mult = 2
            if wager_choice == 1:
                wager = 0
            elif wager_choice == 2:
                if money >= 100:
                    wager = 100
                    money -= wager
                else:
                    print(f"  {DIM}Not enough coins! Wager set to 0.{RESET}")
            elif wager_choice == 3:
                if money >= 500:
                    wager = 500
                    money -= wager
                else:
                    print(f"  {DIM}Not enough coins! Wager set to 0.{RESET}")
            elif wager_choice == 4:
                wager_str = crazy_input("Enter wager amount").strip()
                if wager_str.isdigit():
                    wager = int(wager_str)
                    if wager > money:
                        print(f"  {DIM}You don't have that much! Wager set to 0.{RESET}")
                        wager = 0
                    else:
                        money -= wager
            
            if wager > 0:
                print(f"  {BOLD}{BRIGHT_YELLOW}🎰 Wager locked: {wager} PokéCoins!{RESET}")
                time.sleep(0.5)
            
            tower_round = 0
            win_streak = 0
            
            # Expanded environmental rules
            env_rules = {
                "Normal": {"desc": "No special rules.", "icon": "⚪"},
                "Gravity Surge": {"desc": "Flying-types are grounded and take 5% HP per turn.", "icon": "🌍", "effect": "gravity"},
                "Overdrive": {"desc": "Electric-type moves deal 1.5x damage.", "icon": "⚡", "effect": "overdrive"},
                "Trick Room": {"desc": "Slower Pokémon move first.", "icon": "🔄", "effect": "trickroom"},
                "Vampiric Field": {"desc": "All attacks drain 10% of damage dealt as HP.", "icon": "🩸", "effect": "vampiric"},
                "Solar Flare": {"desc": "Fire-type moves deal 2x damage. Water-types take 5% HP per turn.", "icon": "☀️", "effect": "solarflare"},
                "Misty Terrain": {"desc": "Status moves have 50% accuracy. Dragon-type moves deal 0.5x damage.", "icon": "🌸", "effect": "misty"},
                "Psychic Terrain": {"desc": "Priority moves fail. Psychic-type moves deal 1.3x damage.", "icon": "🔮", "effect": "psychic"},
                "Electric Terrain": {"desc": "All Pokémon cannot fall asleep. Electric moves deal 1.3x damage.", "icon": "⚡", "effect": "electric"},
                "Grassy Terrain": {"desc": "Grounded Pokémon heal 5% HP per turn. Grass moves deal 1.3x damage.", "icon": "🌿", "effect": "grassy"},
                "Hailstorm": {"desc": "Ice-type moves deal 1.5x damage. Non-Ice types take 5% HP per turn.", "icon": "❄️", "effect": "hailstorm"},
                "Sandstorm": {"desc": "Rock/Ground/Steel types take no sandstorm damage. Others take 5% HP per turn.", "icon": "🌪️", "effect": "sandstorm"},
            }
            
            while True:
                tower_round += 1
                
                # Special round modifiers
                is_boss_round = (tower_round % 10 == 0)
                is_checkpoint = (tower_round % 5 == 0)
                
                num_enemy = min(3, 1 + tower_round // 3)
                if is_boss_round:
                    num_enemy = 1  # Boss round = single powerful enemy
                
                enemy_team = {}
                for i in range(num_enemy):
                    level = tower_round * 5 + random.randint(1, 10)
                    if is_boss_round:
                        level = int(level * 1.5)  # Boss is 50% stronger
                    
                    ename, ehp, edm, etyp, emoves, eshiny, espd = get_wild_pokemon(level, location)
                    if eshiny:
                        ehp, edm = int(ehp * 1.3), int(edm * 1.3)
                    
                    # Scale with round number
                    scale = 1 + tower_round * 0.05
                    if is_boss_round:
                        scale *= 1.5
                    
                    ehp = int(ehp * scale)
                    edm = int(edm * scale)
                    espd = int(espd * scale)
                    
                    enemy_team[ename] = {"hp": ehp, "maxhp": ehp, "dm": edm, "speed": espd, "type": etyp, "moves": emoves, "lvl": level // 10 + 1}
                
                # Pick environmental rule (boss rounds always have a rule)
                if is_boss_round:
                    rule_keys = [k for k in env_rules if k != "Normal"]
                    current_rule = random.choice(rule_keys)
                else:
                    current_rule = random.choice(list(env_rules.keys()))
                
                rule_data = env_rules[current_rule]
                
                # Display round info
                print(f"\n  {BOLD}{BRIGHT_YELLOW}{'═' * 40}{RESET}")
                if is_boss_round:
                    print(f"  {BOLD}{BRIGHT_RED}👑 BOSS ROUND {tower_round} 👑{RESET}")
                else:
                    print(f"  {BOLD}{BRIGHT_YELLOW}═══ TOWER ROUND {tower_round} ═══{RESET}")
                
                if current_rule != "Normal":
                    print(f"  {rule_data['icon']} {BOLD}{BRIGHT_MAGENTA}RULE: {current_rule}{RESET}")
                    print(f"  {DIM}{rule_data['desc']}{RESET}")
                
                if is_checkpoint and wager > 0:
                    print(f"  {BOLD}{BRIGHT_GREEN}💰 Checkpoint: Wager doubles on victory!{RESET}")
                
                print(f"  {BOLD}{BRIGHT_RED}Enemy team:{RESET}")
                for pn, st in enemy_team.items():
                    boss_tag = " 👑" if is_boss_round else ""
                    print(f"    {pn}{boss_tag}  Lvl {st['lvl']}  {st['type']}  HP:{st['hp']} DM:{st['dm']}")
                print()
                
                tower_weather = get_random_weather()
                battle_context = {"mode": "Tower", "inventory": inventory, "player_team": pokemon, "env_rule": current_rule}
                won, xp_dict, money_gained = run_team_battle(pokemon, enemy_team, tower_weather, battle_context)
                
                if not won:
                    print_art(DEFEAT_ART, lambda t: gradient_text(t, (255, 0, 0), (80, 0, 0)))
                    defeat_rain(lines=3, width=35)
                    print(f"  {BOLD}{BRIGHT_RED}💀 Tower run ended at Round {tower_round}!{RESET}")
                    print(f"  {BOLD}Win Streak: {win_streak}{RESET}")
                    if wager > 0:
                        print(f"  {DIM}Lost wager of {wager} PokéCoins.{RESET}")
                    
                    # Streak bonus consolation
                    if win_streak >= 5:
                        streak_bonus = win_streak * 20
                        trophies += streak_bonus
                        print(f"  {BRIGHT_YELLOW}🔥 Streak bonus: +{streak_bonus} trophies!{RESET}")
                    break
                
                win_streak += 1
                
                # Checkpoint wager payout
                if is_checkpoint and wager > 0:
                    payout = wager * wager_mult
                    money += payout
                    print(f"\n  {BOLD}{BRIGHT_YELLOW}🎰 CHECKPOINT REACHED! 🎰{RESET}")
                    print(f"  {BOLD}{BRIGHT_GREEN}Wager payout: +{payout} PokéCoins!{RESET}")
                    wager = payout
                
                # Streak bonuses
                if win_streak == 5:
                    print(f"  {BOLD}{BRIGHT_CYAN}🔥 5 Win Streak! +100 trophies!{RESET}")
                    trophies += 100
                elif win_streak == 10:
                    print(f"  {BOLD}{BRIGHT_MAGENTA}🔥🔥 10 Win Streak! +300 trophies!{RESET}")
                    trophies += 300
                elif win_streak == 20:
                    print(f"  {BOLD}{BRIGHT_RED}🔥🔥🔥 20 Win Streak! +1000 trophies!{RESET}")
                    trophies += 1000
                
                trophies += 50 * tower_round
                if tower_round > tower_record:
                    tower_record = tower_round
                
                print(f"  {BOLD}{BRIGHT_GREEN}✅ Round {tower_round} cleared!  Record: {tower_record}  Streak: {win_streak}{RESET}")
                for qid, q in quest_manager.hook_tower(tower_round):
                    print(f"  {BRIGHT_YELLOW}🎉 Quest #{qid} complete! {q['reward_desc']}!{RESET}")
                
                ans = crazy_input("Continue to next round? (y/n)")
                if ans.lower() != 'y': break
            
            print(f"\n  {BOLD}{BRIGHT_YELLOW}🗼 Tower Run ended at Round {tower_round}{RESET}")
            print(f"  {BOLD}{BRIGHT_CYAN}🏆 Record: {tower_record}  |  Win Streak: {win_streak}{RESET}")
            crazy_input("Press Enter to continue")

        # ══════════════════════════════════════
        # OPTION 11: FUSION LAB
        # ══════════════════════════════════════
        if option == 12:
            clear_screen()
            if len(pokemon) < 2:
                print(f"\n  {BOLD}{BRIGHT_RED}❌ Need at least 2 Pokemon to fuse!{RESET}")
                time.sleep(1)
                continue
            wipe_transition(width=50)
            fancy_header("POKÉMON FUSION LAB", emoji="🧬", width=50)
            print(f"  {DIM}Select two Pokemon to fuse into one!{RESET}")
            print(f"  {DIM}Fusion depth limit: 5 generations{RESET}")
            print()
            for i, (pn, st) in enumerate(pokemon.items(), 1):
                gen = st.get('generation', 0)
                gen_tag = f" {DIM}Gen{gen}{RESET}" if gen > 0 else ""
                shiny_tag = f" {BRIGHT_YELLOW}✨{RESET}" if st.get('shiny') else ""
                hp_pct = int((st['hp'] / st['maxhp']) * 100) if st['maxhp'] > 0 else 0
                bar_color = BRIGHT_GREEN if hp_pct > 60 else (BRIGHT_YELLOW if hp_pct > 30 else BRIGHT_RED)
                bar = f"{bar_color}{'█' * (hp_pct // 5)}{DIM}{'░' * (20 - hp_pct // 5)}{RESET}"
                print(f"  {BOLD}{i}.{RESET} {pn}{gen_tag}{shiny_tag}  {bar} {st['hp']}/{st['maxhp']}  {format_type(st.get('type','?'))}  DM:{st['dm']}")
            print()
            print(f"  {BOLD}{BRIGHT_CYAN}Your Team:{RESET} {rainbow_text(', '.join(pokemon.keys()))}")
            p1 = crazy_input("First Pokemon")
            if p1 not in pokemon:
                print(f"  {BOLD}{BRIGHT_RED}❌ Not found!{RESET}")
                time.sleep(1)
                continue
            gen1 = pokemon[p1].get("generation", 0)
            p2 = crazy_input("Second Pokemon")
            if p2 not in pokemon or p2 == p1:
                print(f"  {BOLD}{BRIGHT_RED}❌ Invalid or same Pokemon!{RESET}")
                time.sleep(1)
                continue
            gen2 = pokemon[p2].get("generation", 0)
            new_gen = max(gen1, gen2) + 1
            if new_gen > 5:
                print(f"  {BOLD}{BRIGHT_RED}❌ Fusion would be generation {new_gen}, max is 5!{RESET}")
                time.sleep(1)
                continue

            spinner_animation("Initializing fusion reactor", duration=1.5)

            # Generate fusion name
            name1 = p1.lower()
            name2 = p2.lower()
            part1 = name1[:len(name1)//2]
            part2 = name2[len(name2)//2:]
            f_name = (part1 + part2).capitalize()

            # Calculate average stats
            avg_hp = (pokemon[p1]["maxhp"] + pokemon[p2]["maxhp"]) // 2
            avg_dm = (pokemon[p1]["dm"] + pokemon[p2]["dm"]) // 2
            avg_spd = (pokemon[p1].get("speed", 50) + pokemon[p2].get("speed", 50)) // 2

            # Look up expected fusion stats from the 233K-entry FUSION_DEX
            dex_fusion = FUSION_DEX.get(f_name.lower())
            if dex_fusion:
                dex_hp = dex_fusion["hp"]
                dex_dm = dex_fusion["dm"]
                dex_speed = dex_fusion.get("speed", avg_spd)
                dex_type = dex_fusion.get("type", "Normal")
                dex_moves = dex_fusion.get("moves", ["Tackle"])
            else:
                dex_hp, dex_dm, dex_speed = avg_hp, avg_dm, avg_spd
                dex_type, dex_moves = pokemon[p1].get("type", "Normal"), list(set(pokemon[p1].get("moves", ["Tackle"]) + pokemon[p2].get("moves", ["Tackle"])))[:4]

            # Show expected base from fusion database
            print(f"  {BOLD}{BRIGHT_CYAN}📊 Fusion Database entry found!{RESET}")
            print(f"  {DIM}Expected base stats: HP {dex_hp} | DM {dex_dm} | SPD {dex_speed}{RESET}")
            print()

            # Determine outcome tier
            outcome_roll = random.random()
            if outcome_roll < 0.04:  # 4% - CRAZY
                hp_mult = random.uniform(2.5, 4.0)
                dm_mult = random.uniform(2.5, 4.0)
                spd_mult = random.uniform(2.0, 3.5)
                tier_name = "CRAZY"
                tier_color = BRIGHT_MAGENTA
                tier_emoji = "💥💎🔥"
            elif outcome_roll < 0.10:  # 6% - SHIT
                hp_mult = random.uniform(0.6, 0.9)
                dm_mult = random.uniform(0.6, 0.9)
                spd_mult = random.uniform(0.6, 0.9)
                tier_name = "SHIT"
                tier_color = BRIGHT_RED
                tier_emoji = "💩💩💩"
            else:  # 90% - Decent
                hp_mult = random.uniform(1.0, 1.3)
                dm_mult = random.uniform(1.0, 1.3)
                spd_mult = random.uniform(1.0, 1.3)
                tier_name = "DECENT"
                tier_color = BRIGHT_GREEN
                tier_emoji = "✨"

            f_hp = int(dex_hp * hp_mult)
            f_dm = int(dex_dm * dm_mult)
            f_spd = int(dex_speed * spd_mult)

            f_type = dex_type
            f_moves = dex_moves

            # Show result
            print_art(VICTORY_ROYALE_ART, rainbow_text)
            sparkle_burst(duration=1.0, width=50)
            print(f"  {tier_color}{BOLD}{tier_emoji} FUSION RESULT: {tier_name} {tier_emoji}{RESET}")
            explode_print(f"{p1} + {p2} = {f_name}!")

            print(f"  {BOLD}{BRIGHT_CYAN}HP: {dex_hp} × {hp_mult:.2f} = {f_hp}{RESET}")
            print(f"  {BOLD}{BRIGHT_RED}DM: {dex_dm} × {dm_mult:.2f} = {f_dm}{RESET}")
            print(f"  {BOLD}{BRIGHT_YELLOW}SPD: {dex_speed} × {spd_mult:.2f} = {f_spd}{RESET}")
            print(f"  {BOLD}{BRIGHT_WHITE}Generation: {new_gen}/5{RESET}")
            print()

            # Parent types for secret move check
            t1 = pokemon[p1].get("type", "Normal")
            t2 = pokemon[p2].get("type", "Normal")
            
            secret_map = {
                frozenset(["Fire", "Water"]): "Steam Overload",
                frozenset(["Fire", "Grass"]): "Chloroflame",
                frozenset(["Electric", "Water"]): "Hydro-Shock",
                frozenset(["Grass", "Water"]): "Swamp Entrap",
                frozenset(["Dragon", "Psychic"]): "Cosmic Rage",
                frozenset(["Ghost", "Dark"]): "Shadow Void",
                frozenset(["Rock", "Ground"]): "Earth Shatter",
                frozenset(["Ice", "Water"]): "Glacial Avalanche",
                frozenset(["Electric", "Fire"]): "Plasma Bolt",
                frozenset(["Fighting", "Steel"]): "Iron Fist"
            }
            
            secret_move = secret_map.get(frozenset([t1, t2]), "Core Fusion")
            print(f"  {BOLD}{BRIGHT_MAGENTA}✨ RESONANCE DETECTED! ✨{RESET}")
            print(f"  Parent types {t1} + {t2} have unlocked a Secret Hybrid Move: {BOLD}{BRIGHT_GREEN}{secret_move}{RESET}!")
            print()
            teach_ans = crazy_input(f"Would you like to teach {f_name} the custom move '{secret_move}'? (y/n)")
            if teach_ans.lower() == 'y':
                if secret_move not in f_moves:
                    if len(f_moves) < 4:
                        f_moves.append(secret_move)
                    else:
                        print(f"\n  {BOLD}Choose a move to replace:{RESET}")
                        for idx, mv in enumerate(f_moves, 1):
                            print(f"  {BOLD}{idx}.{RESET} {mv}")
                        replace_idx = crazy_int_input("Select move index")
                        if 1 <= replace_idx <= len(f_moves):
                            print(f"  {BOLD}{BRIGHT_GREEN}Forgotten {f_moves[replace_idx-1]} and learned {secret_move}!{RESET}")
                            f_moves[replace_idx-1] = secret_move

            # Create the fused pokemon
            del pokemon[p1]
            del pokemon[p2]
            pokemon[f_name.lower()] = make_pokemon(f_hp, f_dm, f_type, f_moves, speed=f_spd, generation=new_gen)

            for qid, q in quest_manager.hook_fuse():
                print(f"  {BRIGHT_YELLOW}🎉 Quest #{qid} complete! {q['reward_desc']}!{RESET}")
            for a in achievement_manager.hook_fusion():
                part = a["reward"]
                print(f"  {BRIGHT_GREEN}🏅 Achievement: {a['name']}! +{part['value']} {part['type']}!{RESET}")

            stat_card(f_name, f_hp, f_hp, f_dm, 0, 50, 1, speed=f_spd)
            crazy_input("Press Enter to continue")

        # ══════════════════════════════════════
        # OPTION 12: POKEDEX + COSMETICS SHOP
        # ══════════════════════════════════════
        if option == 13:
            while True:
                clear_screen()
                wipe_transition(width=50)
                fancy_header("POKÉDEX & SHOP", emoji="📖", width=55)
                total = len(pokedex_seen) if pokedex_seen else 1
                caught_pct = int((len(pokedex_caught) / total) * 100) if total > 0 else 0
                pct_bar = f"{BRIGHT_GREEN}{'█' * (caught_pct // 2)}{DIM}{'░' * (50 - caught_pct // 2)}{RESET}"
                print(f"  {BOLD}{BRIGHT_WHITE}Progress: {pct_bar} {caught_pct}%{RESET}")
                print(f"  {BRIGHT_CYAN}📖 Seen: {len(pokedex_seen)}  |  🎯 Caught: {len(pokedex_caught)}{RESET}")
                print()
                print(f"  {BOLD}{BRIGHT_GREEN}1.{RESET} 📖 View Pokédex")
                print(f"  {BOLD}{BRIGHT_YELLOW}2.{RESET} 📊 Type Effectiveness Table")
                print(f"  {BOLD}{BRIGHT_MAGENTA}3.{RESET} 🎨 Cosmetics Shop")
                print(f"  {BOLD}{BRIGHT_CYAN}4.{RESET} 🔍 Search Pokémon")
                print(f"  {BOLD}{DIM}Q.{RESET} Back")
                print()
                theme_divider(50)
                pdx_opt = crazy_input("Choose").strip().lower()
                
                if pdx_opt == "1":
                    clear_screen()
                    fancy_header("POKÉDEX", emoji="📖", width=55)
                    if pokedex_caught:
                        print(f"  {BOLD}{BRIGHT_GREEN}═══ CAUGHT ({len(pokedex_caught)}) ═══{RESET}")
                        caught_list = sorted(pokedex_caught)
                        for i in range(0, len(caught_list), 3):
                            row = caught_list[i:i+3]
                            row_str = "  ".join([f"{BRIGHT_GREEN}✅{RESET} {p.capitalize()}" for p in row])
                            print(f"  {row_str}")
                    if pokedex_seen - pokedex_caught:
                        print(f"\n  {BOLD}{BRIGHT_YELLOW}═══ SEEN ONLY ({len(pokedex_seen - pokedex_caught)}) ═══{RESET}")
                        seen_list = sorted(pokedex_seen - pokedex_caught)
                        for i in range(0, len(seen_list), 3):
                            row = seen_list[i:i+3]
                            row_str = "  ".join([f"{BRIGHT_YELLOW}👁️{RESET} {p.capitalize()}" for p in row])
                            print(f"  {row_str}")
                    if len(pokedex_caught) >= 10 and "Pokedex Pro" not in badges:
                        print(f"\n  {BOLD}{BRIGHT_YELLOW}🏅 Milestone: Caught 10 Pokemon! +200 coins{RESET}")
                        money += 200
                        badges.append("Pokedex Pro")
                    if len(pokedex_caught) >= 30 and "Pokemon Master" not in badges:
                        print(f"\n  {BOLD}{BRIGHT_YELLOW}🏅 Milestone: Caught 30 Pokemon! +500 coins{RESET}")
                        money += 500
                        badges.append("Pokemon Master")
                    crazy_input("Press Enter to continue")
                
                elif pdx_opt == "2":
                    clear_screen()
                    fancy_header("TYPE EFFECTIVENESS TABLE", emoji="📊", width=55)
                    print(f"  {DIM}Shows damage multipliers for each attacking type vs defending type{RESET}")
                    print(f"  {BRIGHT_GREEN}2.0x{RESET} = Super Effective | {BRIGHT_RED}0.5x{RESET} = Not Very Effective | {DIM}0x{RESET} = Immune")
                    print()
                    
                    types = ["Normal", "Fire", "Water", "Grass", "Electric", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
                    
                    # Header row
                    header = f"  {'':10}"
                    for t in types[:9]:
                        header += f"{t[:4]:5}"
                    print(header)
                    print(f"  {'─' * 55}")
                    
                    # Data rows (first half)
                    for atk_type in types[:9]:
                        row = f"  {atk_type[:8]:10}"
                        for def_type in types[:9]:
                            eff = get_effectiveness(atk_type, def_type)
                            if eff == 2.0: cell = f"{BRIGHT_GREEN}2.0 {RESET}"
                            elif eff == 0.5: cell = f"{BRIGHT_RED}0.5 {RESET}"
                            elif eff == 0.0: cell = f"{DIM}0.0 {RESET}"
                            elif eff == 4.0: cell = f"{BRIGHT_GREEN}4.0 {RESET}"
                            elif eff == 0.25: cell = f"{BRIGHT_RED}0.25{RESET}"
                            else: cell = f"1.0 "
                            row += f"{cell}"
                        print(row)
                    
                    print()
                    print(f"  {'─' * 55}")
                    # Header row for second half
                    header2 = f"  {'':10}"
                    for t in types[9:]:
                        header2 += f"{t[:4]:5}"
                    print(header2)
                    print(f"  {'─' * 55}")
                    
                    # Data rows (second half)
                    for atk_type in types[:9]:
                        row = f"  {atk_type[:8]:10}"
                        for def_type in types[9:]:
                            eff = get_effectiveness(atk_type, def_type)
                            if eff == 2.0: cell = f"{BRIGHT_GREEN}2.0 {RESET}"
                            elif eff == 0.5: cell = f"{BRIGHT_RED}0.5 {RESET}"
                            elif eff == 0.0: cell = f"{DIM}0.0 {RESET}"
                            elif eff == 4.0: cell = f"{BRIGHT_GREEN}4.0 {RESET}"
                            elif eff == 0.25: cell = f"{BRIGHT_RED}0.25{RESET}"
                            else: cell = f"1.0 "
                            row += f"{cell}"
                        print(row)
                    
                    print()
                    crazy_input("Press Enter to continue")
                
                elif pdx_opt == "3":
                    while True:
                        clear_screen()
                        fancy_header("COSMETICS SHOP", emoji="🎨", width=55)
                        print(f"  {BOLD}{BRIGHT_WHITE}💰 Coins: {money}{RESET}")
                        print()
                        cosmetics = [
                            {"name": "Golden Border", "desc": "Gold ANSI borders for all menus", "price": 1000, "id": "golden_border"},
                            {"name": "Neon Glow", "desc": "Neon-colored text effects", "price": 1500, "id": "neon_glow"},
                            {"name": "Matrix Theme", "desc": "Green-on-black terminal theme", "price": 2000, "id": "matrix_theme"},
                            {"name": "Rainbow HP Bars", "desc": "HP bars cycle through rainbow colors", "price": 800, "id": "rainbow_hp"},
                            {"name": "Shiny Badge", "desc": "Display a ✨ badge next to your name", "price": 500, "id": "shiny_badge"},
                            {"name": "Champion Title", "desc": "Title 'Champion' displayed in menus", "price": 5000, "id": "champion_title"},
                            {"name": "Animated Background", "desc": "Subtle animated particles in menus", "price": 3000, "id": "anim_bg"},
                            {"name": "Retro CRT", "desc": "CRT scanline effect on all screens", "price": 1200, "id": "retro_crt"},
                        ]
                        
                        for i, c in enumerate(cosmetics, 1):
                            owned = " ✅" if c["id"] in badges else ""
                            print(f"  {BOLD}{BRIGHT_WHITE}{i}.{RESET} {BRIGHT_CYAN}{c['name']}{RESET} {DIM}- {c['desc']}{RESET}")
                            print(f"     {BRIGHT_YELLOW}{c['price']} coins{RESET}{owned}")
                        print(f"  {BOLD}{BRIGHT_WHITE}{len(cosmetics)+1}.{RESET} {RED}Back{RESET}")
                        print()
                        
                        shop_choice = crazy_int_input("Select item")
                        if 1 <= shop_choice <= len(cosmetics):
                            item = cosmetics[shop_choice - 1]
                            if item["id"] in badges:
                                print(f"  {BRIGHT_YELLOW}You already own this!{RESET}")
                            elif money >= item["price"]:
                                money -= item["price"]
                                badges.append(item["id"])
                                print(f"  {BRIGHT_GREEN}✅ Purchased {item['name']}!{RESET}")
                            else:
                                print(f"  {BRIGHT_RED}❌ Not enough coins! Need {item['price']}, have {money}{RESET}")
                            crazy_input("Press Enter to continue")
                        else:
                            break
                
                elif pdx_opt == "4":
                    clear_screen()
                    fancy_header("POKÉMON SEARCH", emoji="🔍", width=55)
                    query = crazy_input("Search term (name or type)").strip().lower()
                    if not query:
                        continue
                    
                    results = []
                    all_dex = {}
                    for dex in [weak_pokemon, moderately_strong_pokemon, strong_pokemon, ultra_strong_pokemon]:
                        all_dex.update(dex)
                    
                    for name, data in all_dex.items():
                        if query in name.lower() or query in data.get("type", "").lower():
                            results.append((name, data))
                    
                    if results:
                        print(f"\n  {BOLD}{BRIGHT_GREEN}Found {len(results)} results:{RESET}")
                        for name, data in results[:20]:
                            caught = "✅" if name in pokedex_caught else ("👁️" if name in pokedex_seen else "❓")
                            print(f"  {caught} {BOLD}{name.capitalize():15}{RESET} {format_type(data.get('type','?')):12} HP:{data.get('hp','?'):3} DM:{data.get('dm','?'):3}")
                        if len(results) > 20:
                            print(f"  {DIM}...and {len(results) - 20} more{RESET}")
                    else:
                        print(f"  {BRIGHT_RED}No results found for '{query}'{RESET}")
                    crazy_input("Press Enter to continue")
                
                elif pdx_opt == "q":
                    break

        # ══════════════════════════════════════
        # OPTION 13: BUG HUNT
        # ══════════════════════════════════════
        # ══════════════════════════════════════
        # OPTION 13: QUEST BOARD
        # ══════════════════════════════════════
        if option == 14:
            clear_screen()
            quest_manager.show_menu(money, trophies)
            continue


        # ══════════════════════════════════════
        # OPTION 14: BUG HUNT
        # ══════════════════════════════════════
        if option == 15:
            clear_screen()
            if not pokemon:
                print(f"\n  {BOLD}{BRIGHT_RED}You need Pokemon first!{RESET}")
                time.sleep(1)
                continue
            wipe_transition(width=50)
            print_art(DEFEAT_ART, lambda t: glitch_text(t))
            fancy_header("BUG HUNT", emoji="🐛", width=50)
            print(f"  {BOLD}{BRIGHT_RED}{glitch_text('⚠️  CORRUPTED DATA DETECTED! ⚠️')}{RESET}")
            print(f"  {DIM}Squash the bugs to restore stability!{RESET}")
            print()
            print(f"  {BOLD}{BRIGHT_GREEN}Your team:{RESET}")
            for pn, st in pokemon.items():
                hp_pct = int((st['hp'] / st['maxhp']) * 100) if st['maxhp'] > 0 else 0
                bar_color = BRIGHT_GREEN if hp_pct > 60 else (BRIGHT_YELLOW if hp_pct > 30 else BRIGHT_RED)
                bar = f"{bar_color}{'█' * (hp_pct // 5)}{DIM}{'░' * (20 - hp_pct // 5)}{RESET}"
                print(f"    {pn}  {bar} {st['hp']}/{st['maxhp']}")
            print()
            ans = crazy_input("Enter the Bug Hunt? (y/n)")
            if ans.lower() != 'y': continue
            bug_round = 0
            bug_poke = None
            while True:
                if bug_round > 0:
                    ans = crazy_input("Continue Bug Hunt? (y/n)")
                    if ans.lower() != 'y': break
                bug_round += 1
                level = random.randint(bug_round * 3, bug_round * 3 + 10)
                bwild, benemyhp, benemydm, benemytype, benemymoves, _, benemyspeed = get_wild_pokemon(level, location)
                benemyhp = int(benemyhp * 1.5)
                benemydm = int(benemydm * 1.3)
                glitch_name = glitch_text(bwild.upper())
                print(f"\n  {BOLD}{BRIGHT_RED}═══ BUG HUNT ROUND {bug_round} ═══{RESET}")
                print(f"  {glitch_name} {BRIGHT_MAGENTA}[CORRUPTED]{RESET}")
                print(f"  {DIM}HP: {benemyhp} | DM: {benemydm} | Type: {benemytype}{RESET}")
                print()
                print(f"  {BOLD}{BRIGHT_GREEN}Your team:{RESET}")
                for pn, st in pokemon.items():
                    hp_pct = int((st['hp'] / st['maxhp']) * 100) if st['maxhp'] > 0 else 0
                    bar_color = BRIGHT_GREEN if hp_pct > 60 else (BRIGHT_YELLOW if hp_pct > 30 else BRIGHT_RED)
                    bar = f"{bar_color}{'█' * (hp_pct // 5)}{DIM}{'░' * (20 - hp_pct // 5)}{RESET}"
                    print(f"    {pn}  {bar} {st['hp']}/{st['maxhp']}")
                if not bug_poke or (bug_poke not in pokemon) or pokemon[bug_poke]["hp"] <= 0:
                    while True:
                        can_fight = [p for p, s in pokemon.items() if s["hp"] > 0]
                        if not can_fight:
                            defeat_rain(lines=3, width=35)
                            break
                        bug_poke = crazy_input("Choose your Pokemon")
                        if bug_poke in pokemon and pokemon[bug_poke]["hp"] > 0:
                            break
                        print(f"  {BOLD}{BRIGHT_RED}❌ Invalid!{RESET}")
                    if not can_fight: break
                bcur_hp = benemyhp
                while bcur_hp > 0:
                    if pokemon[bug_poke]["hp"] <= 0:
                        while True:
                            can_fight = [p for p, s in pokemon.items() if s["hp"] > 0]
                            if not can_fight: break
                            bug_poke = crazy_input("Switch to")
                            if bug_poke in pokemon and pokemon[bug_poke]["hp"] > 0:
                                break
                            print(f"  {BOLD}{BRIGHT_RED}❌ Invalid!{RESET}")
                        if not can_fight: break
                    bug_move = random.choice(pokemon[bug_poke].get("moves", ["Tackle"]))
                    if random.random() < 0.2:
                        bug_move = random.choice(list(MOVES.keys()))
                    damage, eff = calculate_move_damage(bug_move, pokemon[bug_poke], benemytype, "Clear", random.random() < 0.2)
                    damage = int(damage * random.uniform(0.5, 2.0))
                    animate_attack_sequence(bug_poke, bwild, damage, random.random() < 0.2)
                    bcur_hp -= damage
                    if bcur_hp <= 0:
                        xp_gain = calculate_xp_gain(benemyhp, pokemon[bug_poke]["dm"], 3, benemydm) * 2
                        pokemon[bug_poke]["xp"] += xp_gain
                        if pokemon[bug_poke]["xp"] >= pokemon[bug_poke]["maxxp"]:
                            bug_poke = level_up_pokemon(pokemon, bug_poke)
                        print(f"  {BOLD}{BRIGHT_GREEN}🐛 Bug squashed! +{xp_gain} XP{RESET}")
                        trophies += 100 * bug_round
                        break
                    edmg = int(benemydm * random.uniform(0.5, 1.5))
                    animate_enemy_attack_sequence(bwild, bug_poke, edmg)
                    take_damage(pokemon[bug_poke], edmg)
            print(f"\n  {BOLD}{BRIGHT_CYAN}🐛 Bug Hunt ended at Round {bug_round}{RESET}")
            print(f"  {BOLD}{BRIGHT_YELLOW}🏆 +{trophies} total trophies{RESET}")
            crazy_input("Press Enter to continue")

        # ══════════════════════════════════════
        # OPTION 16: DAYCARE & BREEDING CENTER
        # ══════════════════════════════════════
        if option == 16:
            while True:
                clear_screen()
                fancy_header("🏡 POKÉMON DAYCARE CENTER", emoji="🏡", width=55)
                print(f"  {DIM}Leave your Pokémon to gain passive experience and find Eggs!{RESET}")
                print()
                
                daycare_slots = daycare.get("slots", [])
                
                # Render slots status
                print(f"  {BOLD}{BRIGHT_WHITE}Daycare Status:{RESET}")
                if not daycare_slots:
                    print(f"    {DIM}Empty (0/2 slots occupied){RESET}")
                else:
                    for idx, dp in enumerate(daycare_slots, 1):
                        shiny_tag = f" {BRIGHT_YELLOW}✨SHINY✨{RESET}" if dp.get("shiny") else ""
                        pending_text = f" {BRIGHT_GREEN}[{dp.get('pending_level_ups', 0)} Level Up ready!]{RESET}" if dp.get("pending_level_ups", 0) > 0 else ""
                        avg_gain = calculate_daycare_average_exp(dp)
                        print(f"    {BOLD}{idx}.{RESET} {dp.get('name', 'Pokemon').upper()}{shiny_tag} (LVL: {dp.get('lvl')} | XP: {dp.get('xp')}/{dp.get('maxxp')})")
                        print(f"       {DIM}Passive Rate: +{avg_gain} EXP per step{RESET}{pending_text}")
                print()
                
                # Breeding Status
                if len(daycare_slots) == 2:
                    p1, p2 = daycare_slots[0], daycare_slots[1]
                    score, desc = calculate_breeding_compatibility(p1, p2)
                    print(f"  {BOLD}{BRIGHT_CYAN}Breeding Compatibility:{RESET} {score}%")
                    print(f"  {DIM}{desc}{RESET}")
                    print()
                    
                if daycare.get("egg_waiting"):
                    print(f"  {BOLD}{BRIGHT_YELLOW}🎁 The Daycare Man has found an Egg!{RESET}")
                    print()
                
                # Menu choices
                print(f"  {BOLD}{BRIGHT_GREEN}1.{RESET} Deposit a Pokémon")
                print(f"  {BOLD}{BRIGHT_RED}2.{RESET} Withdraw a Pokémon")
                if daycare.get("egg_waiting"):
                    print(f"  {BOLD}{BRIGHT_YELLOW}3.{RESET} Claim Pokémon Egg")
                print(f"  {BOLD}{DIM}Q.{RESET} Back")
                print()
                theme_divider(50)
                dc_opt = crazy_input("Choose")
                
                if dc_opt == "1":
                    # Deposit
                    if len(daycare_slots) >= 2:
                        print(f"\n  {BOLD}{BRIGHT_RED}❌ Daycare is full! Max 2 Pokémon.{RESET}")
                        time.sleep(1.5)
                        continue
                    non_eggs = [p for p, s in pokemon.items() if not s.get("is_egg")]
                    if len(non_eggs) <= 1:
                        print(f"\n  {BOLD}{BRIGHT_RED}❌ You must keep at least 1 battle-ready Pokémon on your active team!{RESET}")
                        time.sleep(1.5)
                        continue
                        
                    clear_screen()
                    fancy_header("DEPOSIT POKÉMON", emoji="📥", width=50)
                    print(f"  {DIM}Select a Pokémon to leave in Daycare:{RESET}")
                    print()
                    
                    team_list = list(pokemon.keys())
                    # Skip any eggs in team list
                    team_list = [t for t in team_list if not pokemon[t].get("is_egg")]
                    
                    if not team_list:
                        print(f"  {DIM}No Pokémon available to deposit.{RESET}")
                        crazy_input("Press Enter to continue")
                        continue
                        
                    for i, tname in enumerate(team_list, 1):
                        pdata = pokemon[tname]
                        print(f"  {BOLD}{i}.{RESET} {tname.upper()} (LVL: {pdata['lvl']})")
                    print(f"  {BOLD}{len(team_list)+1}.{RESET} {RED}Cancel{RESET}")
                    print()
                    
                    dep_choice = crazy_int_input("Select Pokémon")
                    if 1 <= dep_choice <= len(team_list):
                        dep_name = team_list[dep_choice - 1]
                        
                        # Preview compatibility if another pokemon is already there
                        if len(daycare_slots) == 1:
                            exist_poke = daycare_slots[0]
                            cand_poke = pokemon[dep_name]
                            score, desc = calculate_breeding_compatibility(exist_poke, cand_poke)
                            avg_exp = calculate_daycare_average_exp(cand_poke)
                            
                            clear_screen()
                            fancy_header("COMPATIBILITY PREVIEW", emoji="📊", width=50)
                            print(f"  {BOLD}Depositing:{RESET} {dep_name.upper()}")
                            print(f"  {BOLD}Daycare Partner:{RESET} {exist_poke.get('name', 'Pokemon').upper()}")
                            print()
                            theme_divider(45)
                            print(f"  📈 {BOLD}Compatibility Affinity:{RESET} {score}%")
                            print(f"  💬 {DIM}{desc}{RESET}")
                            print(f"  🔥 {BOLD}Expected EXP gain:{RESET} +{avg_exp} per step")
                            print()
                            ans = crazy_input("Confirm deposit? (y/n)")
                            if ans.lower() != 'y':
                                continue
                        
                        # Perform deposit
                        poke_stats = pokemon.pop(dep_name)
                        poke_stats["name"] = dep_name
                        poke_stats["pending_level_ups"] = 0
                        daycare_slots.append(poke_stats)
                        daycare["slots"] = daycare_slots
                        
                        print(f"\n  {BOLD}{BRIGHT_GREEN}✅ Successfully deposited {dep_name.upper()}!{RESET}")
                        time.sleep(1.5)
                        
                elif dc_opt == "2":
                    # Withdraw
                    if not daycare_slots:
                        print(f"\n  {BOLD}{BRIGHT_RED}❌ No Pokémon in Daycare!{RESET}")
                        time.sleep(1.5)
                        continue
                        
                    clear_screen()
                    fancy_header("WITHDRAW POKÉMON", emoji="📤", width=50)
                    print(f"  {DIM}Select a Pokémon to take back to your team:{RESET}")
                    print()
                    for i, dp in enumerate(daycare_slots, 1):
                        print(f"  {BOLD}{i}.{RESET} {dp.get('name', 'Pokemon').upper()} (LVL: {dp.get('lvl')})")
                    print(f"  {BOLD}{len(daycare_slots)+1}.{RESET} {RED}Cancel{RESET}")
                    print()
                    
                    wd_choice = crazy_int_input("Select Pokémon")
                    if 1 <= wd_choice <= len(daycare_slots):
                        wp = daycare_slots.pop(wd_choice - 1)
                        daycare["slots"] = daycare_slots
                        
                        wname = wp.pop("name")
                        pending_lvl = wp.pop("pending_level_ups", 0)
                        
                        # Restore to party
                        pokemon[wname] = wp
                        
                        print(f"\n  {BOLD}{BRIGHT_GREEN}✅ Withdrew {wname.upper()} from Daycare!{RESET}")
                        time.sleep(1.0)
                        
                        # Apply pending level ups
                        for _ in range(pending_lvl):
                            wname = level_up_pokemon(pokemon, wname)
                            
                elif dc_opt == "3" and daycare.get("egg_waiting"):
                    # Claim Pokémon Egg
                    clear_screen()
                    fancy_header("CLAIM POKÉMON EGG", emoji="🥚", width=50)
                    print(f"  {DIM}The Daycare Man carefully hands you a warm, patterned Pokémon Egg.{RESET}")
                    print()
                    
                    egg_key = f"egg_{random.randint(1000, 9999)}"
                    p1_name = daycare_slots[0].get("name", "bulbasaur")
                    p2_name = daycare_slots[1].get("name", "bulbasaur")
                    
                    egg_stats = generate_egg_data(p1_name, p2_name, daycare_slots[0], daycare_slots[1])
                    pokemon[egg_key] = egg_stats
                    daycare["egg_waiting"] = False
                    
                    pokeball_loading("Receiving Egg", duration=1.0)
                    sparkle_burst(duration=0.5, width=40)
                    print(f"\n  {BOLD}{BRIGHT_YELLOW}🥚 Pokémon Egg added to your active team! Keep taking steps to hatch it!{RESET}")
                    print()
                    crazy_input("Press Enter to continue")
                    
                elif dc_opt.lower() == "q":
                    break


        # ══════════════════════════════════════
        # OPTION 17: GTS & RANKED PVP ARENA
        # ══════════════════════════════════════
        if option == 17:
            while True:
                clear_screen()
                fancy_header("GTS & RANKED PVP STATION", emoji="📶", width=55)
                tier = "Bronze"
                tier_color = BRIGHT_RED
                if pvp_rp >= 2500:
                    tier = "Champion"
                    tier_color = BRIGHT_YELLOW
                elif pvp_rp >= 2200:
                    tier = "Master"
                    tier_color = BRIGHT_CYAN
                elif pvp_rp >= 1800:
                    tier = "Gold"
                    tier_color = YELLOW
                elif pvp_rp >= 1400:
                    tier = "Silver"
                    tier_color = WHITE
                
                print(f"  {BOLD}🏆 RANK TIER:{RESET} {tier_color}{tier.upper()}{RESET}  |  {BOLD}⭐ RP POINTS:{RESET} {BRIGHT_GREEN}{pvp_rp}{RESET}")
                print()
                print(f"  {BOLD}{BRIGHT_CYAN}1.{RESET} 🏟️  Ranked PvP Matchmaking   {DIM}[Standard 6v6 tier battle]{RESET}")
                print(f"  {BOLD}{BRIGHT_YELLOW}2.{RESET} 📶 GTS Global Trade Station {DIM}[Trade active team Pokemon]{RESET}")
                print(f"  {BOLD}{BRIGHT_MAGENTA}3.{RESET} 📋 Ranked Leaderboard        {DIM}[View global ladder tiers]{RESET}")
                print(f"  {BOLD}{DIM}4.{RESET} 🚪 Exit Station")
                print()
                theme_divider(50)
                station_choice = crazy_input("Enter your choice").strip()
                
                if station_choice == "1":
                    clear_screen()
                    fancy_header("RANKED MATCHMAKING", emoji="🏟️", width=55)
                    print(f"  {DIM}Broadcasting battle request to GTS servers...{RESET}")
                    
                    # Dynamic queue time based on RP (higher RP = longer queue)
                    queue_time = 2.0 + (pvp_rp - 1000) / 1000.0
                    queue_time = min(queue_time, 6.0)
                    spinner_animation("Searching for online opponents...", duration=queue_time)
                    
                    # Simulate matchmaking phases
                    print(f"  {DIM}Checking player pool...{RESET}")
                    time.sleep(0.5)
                    print(f"  {DIM}Analyzing skill brackets...{RESET}")
                    time.sleep(0.5)
                    
                    # Expanded Ghost AI trainer database with proper teams
                    ghost_trainers = [
                        # BRONZE TIER (1000-1399 RP)
                        {"name": "Youngster Joey", "tier": "Bronze", "rp_range": (1000, 1199), "persona": "Hyper-Offense",
                         "mons": [{"name": "rattata", "type": "Normal", "moves": ["Quick Attack", "Tackle", "Hyper Fang"]},
                                  {"name": "raticate", "type": "Normal", "moves": ["Hyper Fang", "Quick Attack", "Pursuit"]},
                                  {"name": "furret", "type": "Normal", "moves": ["Quick Attack", "Slam", "Hyper Fang"]}]},
                        {"name": "Lass Carrie", "tier": "Bronze", "rp_range": (1000, 1299), "persona": "Support",
                         "mons": [{"name": "clefairy", "type": "Fairy", "moves": ["Pound", "Double Slap", "Metronome"]},
                                  {"name": "jigglypuff", "type": "Normal", "moves": ["Pound", "Sing", "Double Slap"]},
                                  {"name": "skitty", "type": "Normal", "moves": ["Tackle", "Growl", "Assist"]}]},
                        {"name": "Bug Catcher Don", "tier": "Bronze", "rp_range": (1000, 1199), "persona": "Trickster",
                         "mons": [{"name": "caterpie", "type": "Bug", "moves": ["Tackle", "Bug Bite", "String Shot"]},
                                  {"name": "weedle", "type": "Bug", "moves": ["Poison Sting", "Bug Bite", "String Shot"]},
                                  {"name": "paras", "type": "Bug", "moves": ["Scratch", "Bug Bite", "Spore"]}]},
                        
                        # SILVER TIER (1400-1799 RP)
                        {"name": "Cooltrainer Nick", "tier": "Silver", "rp_range": (1400, 1699), "persona": "Tactical",
                         "mons": [{"name": "pidgeot", "type": "Flying", "moves": ["Wing Attack", "Quick Attack", "Steel Wing"]},
                                  {"name": "alakazam", "type": "Psychic", "moves": ["Psychic", "Shadow Ball", "Recover"]},
                                  {"name": "arcanine", "type": "Fire", "moves": ["Flamethrower", "Extreme Speed", "Crunch"]},
                                  {"name": "gyarados", "type": "Water", "moves": ["Waterfall", "Crunch", "Earthquake"]}]},
                        {"name": "Beauty Victoria", "tier": "Silver", "rp_range": (1400, 1699), "persona": "Staller",
                         "mons": [{"name": "milotic", "type": "Water", "moves": ["Surf", "Ice Beam", "Recover"]},
                                  {"name": "gardevoir", "type": "Psychic", "moves": ["Psychic", "Thunderbolt", "Calm Mind"]},
                                  {"name": "roselia", "type": "Grass", "moves": ["Giga Drain", "Sludge Bomb", "Sleep Powder"]}]},
                        {"name": "Ace Trainer Jake", "tier": "Silver", "rp_range": (1500, 1799), "persona": "Hyper-Offense",
                         "mons": [{"name": "salamence", "type": "Dragon", "moves": ["Dragon Claw", "Flamethrower", "Earthquake"]},
                                  {"name": "metagross", "type": "Steel", "moves": ["Meteor Mash", "Earthquake", "Bullet Punch"]},
                                  {"name": "tyranitar", "type": "Rock", "moves": ["Stone Edge", "Earthquake", "Crunch"]}]},
                        
                        # GOLD TIER (1800-2199 RP)
                        {"name": "Veteran Edgar", "tier": "Gold", "rp_range": (1800, 2099), "persona": "Tactical",
                         "mons": [{"name": "garchomp", "type": "Dragon", "moves": ["Dragon Claw", "Earthquake", "Stone Edge", "Fire Fang"]},
                                  {"name": "lucario", "type": "Fighting", "moves": ["Close Combat", "Extreme Speed", "Shadow Ball"]},
                                  {"name": "togekiss", "type": "Fairy", "moves": ["Air Slash", "Flamethrower", "Aura Sphere"]},
                                  {"name": "roserade", "type": "Grass", "moves": ["Sludge Bomb", "Giga Drain", "Sleep Powder"]}]},
                        {"name": "Pokémon Breeder Lydia", "tier": "Gold", "rp_range": (1800, 2099), "persona": "Support",
                         "mons": [{"name": "blissey", "type": "Normal", "moves": ["Seismic Toss", "Softboiled", "Thunder Wave"]},
                                  {"name": "chansey", "type": "Normal", "moves": ["Seismic Toss", "Softboiled", "Heal Bell"]},
                                  {"name": "clefable", "type": "Fairy", "moves": ["Moonblast", "Thunder Wave", "Softboiled"]}]},
                        {"name": "Ace Trainer Maya", "tier": "Gold", "rp_range": (1900, 2199), "persona": "Bully",
                         "mons": [{"name": "dragonite", "type": "Dragon", "moves": ["Outrage", "Hurricane", "Fire Punch"]},
                                  {"name": "hydreigon", "type": "Dark", "moves": ["Dragon Pulse", "Dark Pulse", "Flamethrower"]},
                                  {"name": "goodra", "type": "Dragon", "moves": ["Dragon Pulse", "Sludge Wave", "Thunderbolt"]}]},
                        
                        # MASTER TIER (2200-2499 RP)
                        {"name": "Cynthia", "tier": "Master", "rp_range": (2200, 2399), "persona": "Tactical",
                         "mons": [{"name": "garchomp", "type": "Dragon", "moves": ["Dragon Claw", "Earthquake", "Stone Edge", "Fire Fang"]},
                                  {"name": "milotic", "type": "Water", "moves": ["Surf", "Ice Beam", "Recover", "Mirror Coat"]},
                                  {"name": "lucario", "type": "Fighting", "moves": ["Close Combat", "Extreme Speed", "Shadow Ball", "Swords Dance"]},
                                  {"name": "togekiss", "type": "Fairy", "moves": ["Air Slash", "Flamethrower", "Aura Sphere", "Nasty Plot"]},
                                  {"name": "roserade", "type": "Grass", "moves": ["Sludge Bomb", "Giga Drain", "Sleep Powder", "Spikes"]},
                                  {"name": "spiritomb", "type": "Ghost", "moves": ["Shadow Ball", "Dark Pulse", "Will-O-Wisp", "Pain Split"]}]},
                        {"name": "Steven Stone", "tier": "Master", "rp_range": (2200, 2499), "persona": "Staller",
                         "mons": [{"name": "metagross", "type": "Steel", "moves": ["Meteor Mash", "Earthquake", "Bullet Punch", "Agility"]},
                                  {"name": "aggron", "type": "Steel", "moves": ["Iron Head", "Earthquake", "Stone Edge", "Stealth Rock"]},
                                  {"name": "skarmory", "type": "Steel", "moves": ["Brave Bird", "Roost", "Spikes", "Whirlwind"]},
                                  {"name": "cradily", "type": "Rock", "moves": ["Giga Drain", "Stone Edge", "Recover", "Stealth Rock"]},
                                  {"name": "armaldo", "type": "Rock", "moves": ["X-Scissor", "Stone Edge", "Earthquake", "Swords Dance"]}]},
                        
                        # CHAMPION TIER (2500+ RP)
                        {"name": "Red", "tier": "Champion", "rp_range": (2500, 9999), "persona": "Hyper-Offense",
                         "mons": [{"name": "charizard", "type": "Fire", "moves": ["Flamethrower", "Air Slash", "Dragon Pulse", "Solar Beam"]},
                                  {"name": "pikachu", "type": "Electric", "moves": ["Thunderbolt", "Quick Attack", "Iron Tail", "Volt Tackle"]},
                                  {"name": "snorlax", "type": "Normal", "moves": ["Body Slam", "Earthquake", "Crunch", "Rest"]},
                                  {"name": "venusaur", "type": "Grass", "moves": ["Giga Drain", "Sludge Bomb", "Sleep Powder", "Swords Dance"]},
                                  {"name": "blastoise", "type": "Water", "moves": ["Surf", "Ice Beam", "Dark Pulse", "Rapid Spin"]},
                                  {"name": "mewtwo", "type": "Psychic", "moves": ["Psychic", "Shadow Ball", "Ice Beam", "Recover"]}]},
                        {"name": "Blue Oak", "tier": "Champion", "rp_range": (2500, 9999), "persona": "Bully",
                         "mons": [{"name": "alakazam", "type": "Psychic", "moves": ["Psychic", "Shadow Ball", "Focus Blast", "Calm Mind"]},
                                  {"name": "gyarados", "type": "Water", "moves": ["Waterfall", "Earthquake", "Dragon Dance", "Ice Fang"]},
                                  {"name": "arcanine", "type": "Fire", "moves": ["Flare Blitz", "Extreme Speed", "Crunch", "Morning Sun"]},
                                  {"name": "exeggutor", "type": "Grass", "moves": ["Psychic", "Giga Drain", "Sleep Powder", "Trick Room"]},
                                  {"name": "rhydon", "type": "Ground", "moves": ["Earthquake", "Stone Edge", "Megahorn", "Swords Dance"]},
                                  {"name": "pidgeot", "type": "Flying", "moves": ["Hurricane", "Heat Wave", "U-turn", "Roost"]}]},
                    ]
                    
                    # Find opponents in player's RP range
                    eligible = [t for t in ghost_trainers if t["rp_range"][0] <= pvp_rp <= t["rp_range"][1]]
                    if not eligible:
                        # Fallback to closest tier
                        if pvp_rp < 1400:
                            eligible = [t for t in ghost_trainers if t["tier"] == "Bronze"]
                        elif pvp_rp < 1800:
                            eligible = [t for t in ghost_trainers if t["tier"] == "Silver"]
                        elif pvp_rp < 2200:
                            eligible = [t for t in ghost_trainers if t["tier"] == "Gold"]
                        elif pvp_rp < 2500:
                            eligible = [t for t in ghost_trainers if t["tier"] == "Master"]
                        else:
                            eligible = [t for t in ghost_trainers if t["tier"] == "Champion"]
                    
                    opp_data = random.choice(eligible)
                    opp_name = opp_data["name"]
                    opp_tier = opp_data["tier"]
                    opp_persona = opp_data["persona"]
                    
                    print(f"  {BOLD}{BRIGHT_GREEN}⚔️ Match Found! ⚔️{RESET}")
                    print(f"  {BOLD}Opponent:{RESET} {BRIGHT_CYAN}{opp_name}{RESET} ({BRIGHT_RED}{opp_tier} Tier{RESET})")
                    print(f"  {DIM}AI Persona: {opp_persona}{RESET}")
                    print()
                    ans = crazy_input("Accept ranked match? (y/n)")
                    if ans.lower() != 'y': continue
                    
                    # Calculate enemy level based on RP
                    enemy_lvl = int(max(5, (pvp_rp - 500) // 15))
                    
                    # Build opponent team with proper types and moves
                    opp_team = {}
                    for mon_data in opp_data["mons"]:
                        mon_name = mon_data["name"]
                        mon_type = mon_data["type"]
                        mon_moves = mon_data["moves"]
                        
                        # Scale stats based on level and tier
                        tier_mult = {"Bronze": 0.6, "Silver": 0.8, "Gold": 1.0, "Master": 1.2, "Champion": 1.5}
                        mult = tier_mult.get(opp_tier, 1.0)
                        
                        base_hp = int(enemy_lvl * 10 * mult)
                        base_dm = int(enemy_lvl * 6 * mult)
                        base_spd = int(enemy_lvl * 1.2 * mult)
                        
                        opp_team[mon_name] = make_pokemon(base_hp, base_dm, mon_type, mon_moves, speed=base_spd)
                        opp_team[mon_name]["lvl"] = enemy_lvl
                    
                    # Show opponent team preview
                    print(f"\n  {BOLD}{BRIGHT_RED}═══ Opponent Team ═══{RESET}")
                    for mon_name, mon_stats in opp_team.items():
                        print(f"    {BRIGHT_CYAN}{mon_name.upper()}{RESET}  Lvl {mon_stats['lvl']}  {mon_stats['type']}  HP:{mon_stats['hp']} DM:{mon_stats['dm']}")
                    print()
                    
                    pvp_battle_context = {
                        "mode": "Ranked PvP", 
                        "inventory": inventory, 
                        "player_team": pokemon,
                        "ai_persona": opp_persona,
                        "enemy_trainer_name": opp_name
                    }
                    pvp_weather = get_random_weather()
                    
                    pvp_won, pvp_xp, pvp_money = run_team_battle(pokemon, opp_team, pvp_weather, pvp_battle_context)
                    
                    # RP calculation with streak bonus
                    if pvp_won:
                        base_rp = 25
                        # Bonus for beating higher tier
                        tier_bonus = {"Bronze": 0, "Silver": 5, "Gold": 10, "Master": 15, "Champion": 25}
                        rp_gain = base_rp + tier_bonus.get(opp_tier, 0)
                        pvp_rp += rp_gain
                        coins_reward = enemy_lvl * 50 + tier_bonus.get(opp_tier, 0) * 20
                        money += coins_reward
                        print()
                        fancy_header("RANKED VICTORY", emoji="🏆", width=55)
                        print(f"  {BOLD}{BRIGHT_GREEN}🎉 You defeated {opp_name}!{RESET}")
                        print(f"  {BOLD}RP Gain:{RESET} {BRIGHT_GREEN}+{rp_gain} RP{RESET} (New RP: {pvp_rp})")
                        print(f"  {BOLD}Bonus Reward:{RESET} {BRIGHT_YELLOW}+{coins_reward} coins!{RESET}")
                    else:
                        base_loss = 15
                        rp_loss = base_loss
                        pvp_rp = max(1000, pvp_rp - rp_loss)
                        print()
                        fancy_header("RANKED DEFEAT", emoji="💀", width=55)
                        print(f"  {BOLD}{BRIGHT_RED}❌ You fainted against {opp_name}...{RESET}")
                        print(f"  {BOLD}RP Loss:{RESET} {BRIGHT_RED}-{rp_loss} RP{RESET} (New RP: {pvp_rp})")
                        
                    print()
                    crazy_input("Press Enter to continue")
                    
                elif station_choice == "2":
                    while True:
                        clear_screen()
                        fancy_header("GLOBAL TRADE STATION (GTS)", emoji="📶", width=55)
                        print(f"  {BOLD}{BRIGHT_CYAN}1.{RESET} 📤 Upload Pokémon to GTS      {DIM}[List one of your team]{RESET}")
                        print(f"  {BOLD}{BRIGHT_YELLOW}2.{RESET} 🔍 Search GTS Postings       {DIM}[Browse global offers]{RESET}")
                        print(f"  {BOLD}{DIM}3.{RESET} 🚪 Return to Lobby")
                        print()
                        theme_divider(50)
                        gts_choice = crazy_input("Enter choice").strip()
                        
                        if gts_choice == "1":
                            clear_screen()
                            fancy_header("UPLOAD POKÉMON", emoji="📤", width=55)
                            if len(pokemon) <= 1:
                                print(f"\n  {BOLD}{BRIGHT_RED}❌ You must keep at least 1 Pokémon on your active team!{RESET}")
                                crazy_input("\nPress Enter to continue")
                                continue
                                
                            print(f"  {BOLD}{BRIGHT_CYAN}Choose a Pokémon to deposit:{RESET}")
                            mon_list = list(pokemon.keys())
                            for idx, mon in enumerate(mon_list):
                                print(f"  {BOLD}{idx+1}.{RESET} {mon.upper()} (LVL {pokemon[mon]['lvl']})")
                            print(f"  {BOLD}{len(mon_list)+1}.{RESET} Back")
                            print()
                            
                            upload_idx = crazy_int_input("Select a index")
                            if 1 <= upload_idx <= len(mon_list):
                                upload_mon = mon_list[upload_idx-1]
                                wanted = crazy_input("What species do you want in exchange? (e.g. Charizard, Mewtwo)").strip().lower()
                                
                                print()
                                pokeball_loading(f"Uploading {upload_mon.upper()} to GTS", duration=1.0)
                                print(f"\n  {BOLD}{BRIGHT_GREEN}🚀 {upload_mon.upper()} uploaded! Searching cloud for matching trades...{RESET}")
                                time.sleep(1.5)
                                
                                if wanted in ["charizard", "mewtwo", "garchomp", "pikachu", "arceus", "venusaur", "blastoise", "gengar"]:
                                    print(f"  {BOLD}{BRIGHT_YELLOW}✨ Matching Offer Found!{RESET}")
                                    print(f"  Another trainer has deposited a level 50 {wanted.upper()} in exchange for a {upload_mon.upper()}!")
                                    confirm_trade = crazy_input("Confirm GTS trade? (y/n)")
                                    if confirm_trade.lower() == 'y':
                                        del pokemon[upload_mon]
                                        pokemon[wanted] = make_pokemon(300, 150, "Dragon" if wanted=="garchomp" else "Psychic" if wanted=="mewtwo" else "Normal", ["Tackle", "Swift"], speed=95)
                                        pokemon[wanted]["lvl"] = 50
                                        
                                        pokedex_seen.add(wanted)
                                        pokedex_caught.add(wanted)
                                        
                                        clear_screen()
                                        pokeball_loading("GTS Trade in Progress", duration=2.0)
                                        sparkle_burst(duration=1.0, width=50)
                                        print(f"\n  {BOLD}{rainbow_text('🎉 GTS TRADE COMPLETED SUCCESSFULLY! 🎉')}{RESET}")
                                        print(f"  Traded away: {upload_mon.upper()} | Received: {wanted.upper()}!")
                                else:
                                    print(f"\n  {DIM}No matches found immediately. Your {upload_mon.upper()} remains listed.{RESET}")
                                    
                            crazy_input("\nPress Enter to continue")
                            
                        elif gts_choice == "2":
                            clear_screen()
                            fancy_header("SEARCH POSTINGS", emoji="🔍", width=55)
                            postings = [
                                {"offer": "Charizard", "lvl": 60, "wanted": "onix", "ability": "Blaze"},
                                {"offer": "Mewtwo", "lvl": 70, "wanted": "pikachu", "ability": "Pressure"},
                                {"offer": "Garchomp", "lvl": 55, "wanted": "gyarados", "ability": "Sand Veil"},
                                {"offer": "Pikachu", "lvl": 45, "wanted": "pidgeot", "ability": "Static"}
                            ]
                            
                            for idx, post in enumerate(postings):
                                print(f"  {BOLD}{idx+1}.{RESET} Trainer wants: {BRIGHT_YELLOW}{post['wanted'].upper()}{RESET}  |  Offers: {BRIGHT_GREEN}{post['offer']} (LVL {post['lvl']}){RESET}")
                            print(f"  {BOLD}{len(postings)+1}.{RESET} Back")
                            print()
                            
                            search_idx = crazy_int_input("Select a trade offer")
                            if 1 <= search_idx <= len(postings):
                                chosen_post = postings[search_idx-1]
                                wanted_mon = chosen_post["wanted"]
                                offer_mon = chosen_post["offer"]
                                
                                if wanted_mon in pokemon:
                                    if len(pokemon) <= 1:
                                        print(f"\n  {BOLD}{BRIGHT_RED}❌ You must keep at least 1 Pokémon on your active team!{RESET}")
                                    else:
                                        confirm = crazy_input(f"Trade your {wanted_mon.upper()} for level {chosen_post['lvl']} {offer_mon}? (y/n)")
                                        if confirm.lower() == 'y':
                                            del pokemon[wanted_mon]
                                            pokemon[offer_mon.lower()] = make_pokemon(int(chosen_post['lvl'] * 6), int(chosen_post['lvl'] * 4), "Fire" if offer_mon=="Charizard" else "Dragon", ["Tackle", "Swift"], speed=85)
                                            pokemon[offer_mon.lower()]["lvl"] = chosen_post["lvl"]
                                            pokemon[offer_mon.lower()]["ability"] = chosen_post["ability"]
                                            
                                            pokedex_seen.add(offer_mon.lower())
                                            pokedex_caught.add(offer_mon.lower())
                                            
                                            clear_screen()
                                            pokeball_loading("GTS Trade in Progress", duration=2.0)
                                            sparkle_burst(duration=1.0, width=50)
                                            print(f"\n  {BOLD}{rainbow_text('🎉 GTS TRADE COMPLETED SUCCESSFULLY! 🎉')}{RESET}")
                                            print(f"  Traded away: {wanted_mon.upper()} | Received: {offer_mon}!{RESET}")
                                else:
                                    print(f"\n  {BOLD}{BRIGHT_RED}❌ You don't have a {wanted_mon.upper()} to trade!{RESET}")
                                    
                            crazy_input("\nPress Enter to continue")
                            
                        elif gts_choice == "3":
                            break
                            
                elif station_choice == "3":
                    clear_screen()
                    fancy_header("RANKED PVP LEADERBOARD", emoji="📋", width=55)
                    print(f"  {BOLD}{UNDERLINE}{'Rank':<8}{'Trainer Name':<20}{'RP Points':<15}{'Tier':<12}{RESET}")
                    
                    sim_leaders = [
                        {"rank": 1, "name": "Red", "rp": 3150, "tier": "Champion"},
                        {"rank": 2, "name": "Cynthia", "rp": 2980, "tier": "Champion"},
                        {"rank": 3, "name": "Steven", "rp": 2720, "tier": "Master"},
                        {"rank": 4, "name": "Blue", "rp": 2450, "tier": "Master"},
                        {"rank": 5, "name": name, "rp": pvp_rp, "tier": tier},
                        {"rank": 6, "name": "Lance", "rp": 2180, "tier": "Gold"},
                        {"rank": 7, "name": "Joey", "rp": 1050, "tier": "Bronze"}
                    ]
                    sim_leaders.sort(key=lambda x: x["rp"], reverse=True)
                    
                    for idx, l in enumerate(sim_leaders):
                        style = BOLD + BRIGHT_GREEN if l["name"] == name else ""
                        print(f"  {style}{idx+1:<8}{l['name']:<20}{l['rp']:<15}{l['tier']:<12}{RESET}")
                        
                    print()
                    crazy_input("Press Enter to return to lobby")
                    
                elif station_choice == "4":
                    break

        exit_option = 21 if len(gym_badges_check) >= len(GYM_LEADERS) else 20
        if option == exit_option:
            break

        # ══════════════════════════════════════
        # OPTION 18: DUNGEON GAUNTLETS
        # ══════════════════════════════════════
        if option == 18:
            clear_screen()
            if not pokemon:
                print(f"\n  {BOLD}{BRIGHT_RED}❌ You need Pokemon first!{RESET}")
                time.sleep(1)
                continue
                
            fancy_header("DUNGEON GAUNTLETS", emoji="🏰", width=55)
            print(f"  {DIM}High-difficulty sequential raids. Healing items are disabled!{RESET}")
            print(f"  {DIM}Your team does NOT recover between battles!{RESET}")
            print()
            print(f"  {BOLD}{BRIGHT_GREEN}1.{RESET} Viridian Forest   {DIM}[Easy - Lv 20 | Rewards: Leaf Stone & 2k coins]{RESET}")
            print(f"  {BOLD}{BRIGHT_YELLOW}2.{RESET} Mt. Chimney      {DIM}[Medium - Lv 50 | Sunny weather | Rewards: Firium Z & 5k coins]{RESET}")
            print(f"  {BOLD}{BRIGHT_RED}3.{RESET} Cerulean Cave     {DIM}[Hard - Lv 80 | Boss: Fused Mewtwo | Mewtwonite Y]{RESET}")
            print(f"  {BOLD}{DIM}Q. Back{RESET}")
            print()
            d_choice = crazy_input("Select Dungeon").strip()
            if d_choice.lower() == 'q':
                continue
                
            if d_choice in ["1", "2", "3"]:
                won_raid = run_dungeon_raid(pokemon, d_choice, inventory)
                if won_raid:
                    if d_choice == "1":
                        money += 2000
                        inventory["Leaf Stone"] = inventory.get("Leaf Stone", 0) + 1
                        print(f"\n  {BOLD}{BRIGHT_GREEN}🎉 Dungeon Beaten! Received Leaf Stone & 2000 coins!{RESET}")
                    elif d_choice == "2":
                        money += 5000
                        inventory["Firium Z"] = inventory.get("Firium Z", 0) + 1
                        print(f"\n  {BOLD}{BRIGHT_GREEN}🎉 Dungeon Beaten! Received Firium Z & 5000 coins!{RESET}")
                    elif d_choice == "3":
                        money += 15000
                        inventory["Mewtwonite Y"] = inventory.get("Mewtwonite Y", 0) + 1
                        print(f"\n  {BOLD}{BRIGHT_GREEN}🎉 Cerulean Cave Conqueror! Received Mewtwonite Y & 15000 coins!{RESET}")
                    crazy_input("Press Enter to continue")
                continue

        # ══════════════════════════════════════
        # OPTION 19: BOSS RAIDS
        # ══════════════════════════════════════
        if option == 19:
            clear_screen()
            if not pokemon:
                print(f"\n  {BOLD}{BRIGHT_RED}❌ You need Pokemon first!{RESET}")
                time.sleep(1)
                continue
            
            fancy_header("LEGENDARY BOSS RAIDS", emoji="👑", width=55)
            print(f"  {DIM}Challenge legendary bosses for massive rewards!{RESET}")
            print(f"  {BOLD}{BRIGHT_RED}⚠️ Bosses have 10x+ HP and Elemental Shields!{RESET}")
            print()
            
            from game_functions import LEGENDARY_BOSSES
            boss_list = list(LEGENDARY_BOSSES.keys())
            for i, bkey in enumerate(boss_list, 1):
                boss = LEGENDARY_BOSSES[bkey]
                reward = boss["reward"]
                print(f"  {BOLD}{BRIGHT_WHITE}{i}.{RESET} {BRIGHT_MAGENTA}{boss['name']}{RESET} {DIM}({boss['type']}){RESET}")
                print(f"     {DIM}Reward: {reward['coins']} coins, {reward['trophies']} trophies, {reward['item']}{RESET}")
            print(f"  {BOLD}{BRIGHT_WHITE}{len(boss_list)+1}.{RESET} {RED}Back{RESET}")
            print()
            
            boss_choice = crazy_int_input("Select a boss to challenge")
            if 1 <= boss_choice <= len(boss_list):
                selected_boss = boss_list[boss_choice - 1]
                from game_functions import run_boss_raid
                run_boss_raid(pokemon, selected_boss, inventory)
            continue

        # ══════════════════════════════════════
        # OPTION 20: ELITE FOUR
        # ══════════════════════════════════════
        ef_option_number = 20 if len(gym_badges_check) >= len(GYM_LEADERS) else -1
        if option == ef_option_number:
            clear_screen()
            if not pokemon:
                print(f"\n  {BOLD}{BRIGHT_RED}You need Pokemon first!{RESET}")
                time.sleep(1)
                continue

            fancy_header("POKEMON LEAGUE CHALLENGE", emoji="👑", width=55)
            print(f"  {DIM}Defeat all 5 members to become Champion!{RESET}")
            print(f"  {BOLD}{BRIGHT_YELLOW}Progress: {len(elite_four_defeated)}/5{RESET}")
            print()
            ans = crazy_input("Enter the Pokemon League? (y/n)")
            if ans.lower() != 'y': continue

            for ef_idx, ef_member in enumerate(ELITE_FOUR):
                if ef_idx < len(elite_four_defeated):
                    continue

                ef_name = ef_member["name"]
                ef_type = ef_member["type"]
                ef_msg = ef_member["message"]
                ef_team = ef_member["team"]

                print()
                fancy_header(f"{ef_name} — {ef_type} Specialist", emoji="⚔️", width=55)
                print(f"  {DIM}\"{ef_msg}\"{RESET}")
                print()

                pre_heal_ans = crazy_input("Heal your team before battle? (y/n, costs 500 coins)")
                if pre_heal_ans.lower() == 'y' and money >= 500:
                    money -= 500
                    for pn, ps in pokemon.items():
                        ps["hp"] = ps["maxhp"]
                        ps["status"] = None
                        restore_all_pp(ps)
                    print(f"  {BRIGHT_GREEN}Team fully restored!{RESET}")

                ef_battle_context = {"mode": "Elite Four", "inventory": inventory, "player_team": pokemon}
                ef_weather = get_random_weather()
                ef_won, ef_xp, ef_money = run_team_battle(pokemon, ef_team, ef_weather, ef_battle_context)

                if ef_won:
                    elite_four_defeated.append(ef_name)
                    for a in achievement_manager.hook_elite_four(len(elite_four_defeated)):
                        part = a["reward"]
                        print(f"  {BRIGHT_GREEN}🏅 Achievement: {a['name']}! +{part['value']} {part['type']}!{RESET}")
                    reward = 2000 + (ef_idx * 500)
                    money += reward + ef_money
                    trophies += 500
                    print()
                    print_art(VICTORY_ROYALE_ART, rainbow_text)
                    victory_celebration(lines=5, width=45)
                    explode_print(f"You defeated {ef_name}!")
                    print(f"  {BOLD}{BRIGHT_YELLOW}💰 +{reward} coins!{RESET}")
                    print(f"  {BOLD}{BRIGHT_GREEN}👑 Elite Four Progress: {len(elite_four_defeated)}/5{RESET}")

                    if ef_idx == 4:
                        print()
                        fancy_header("🎉 YOU ARE THE CHAMPION! 🎉", emoji="🏆", width=55)
                        sparkle_burst(duration=2.0, width=55)
                        explode_print("CONGRATULATIONS! You've beaten the Pokemon League!")
                        trophies += 5000
                        money += 10000
                        if "Champion" not in badges:
                            badges.append("Champion")
                        print(f"  {BOLD}{BRIGHT_YELLOW}🏆 +5000 Trophies!{RESET}")
                        print(f"  {BOLD}{BRIGHT_YELLOW}💰 +10000 Coins!{RESET}")
                        animate_money_earned(10000)
                else:
                    print()
                    print_art(DEFEAT_ART, lambda t: gradient_text(t, (255,0,0), (80,0,0)))
                    defeat_rain(lines=5, width=40)
                    print(f"  {BOLD}{BRIGHT_RED}Your Pokemon League run has ended.{RESET}")
                    print(f"  {DIM}Defeated by {ef_name}.{RESET}")
                    break

                crazy_input("Press Enter to continue")

                if ef_idx < 4 and ef_idx + 1 < len(ELITE_FOUR):
                    ans = crazy_input("Continue to the next member? (y/n)")
                    if ans.lower() != 'y': break

            crazy_input("Press Enter to continue")

        # ══════════════════════════════════════
        # OPTION 21: AI CHATBOT
        # ══════════════════════════════════════
        if option == 21:
            clear_screen()
            try:
                from AI.chatbot import PokemonChatbot
                chatbot = PokemonChatbot()
                fancy_header("AI POKEMON CHATBOT", emoji="🤖", width=50)
                print(f"  {DIM}Ask me anything about Pokemon, math, science, or game tips!{RESET}")
                print(f"  {DIM}Type 'quit' or 'exit' to leave.{RESET}")
                print()
                print(f"  {BRIGHT_GREEN}{chatbot.greet()}{RESET}")
                print()
                while True:
                    user_msg = crazy_input("You").strip()
                    if user_msg.lower() in ("quit", "exit", "q", "bye"):
                        print(f"  {BRIGHT_YELLOW}{chatbot.say_goodbye()}{RESET}")
                        break
                    if not user_msg:
                        continue
                    response = chatbot.respond(user_msg)
                    print(f"  {BRIGHT_CYAN}🤖 {response}{RESET}")
                    print()
            except ImportError:
                fancy_header("AI CHATBOT", emoji="🤖", width=50)
                print(f"  {BRIGHT_RED}⚠️  Chatbot module not found.{RESET}")
                print(f"  {DIM}Make sure the AI/ folder exists with chatbot.py{RESET}")
            except Exception as e:
                fancy_header("AI CHATBOT", emoji="🤖", width=50)
                print(f"  {BRIGHT_RED}❌ Chatbot error: {e}{RESET}")
            crazy_input("Press Enter to continue")

        # ══════════════════════════════════════
        # OPTION 23: DAILY CHALLENGES
        # ══════════════════════════════════════
        if option == 23:
            clear_screen()
            fancy_header("DAILY CHALLENGES", emoji="📅", width=50)
            print(f"  {DIM}Date: {daily_challenge['date']}{RESET}")
            print()
            print(f"  {BOLD}{BRIGHT_YELLOW}🎯 Daily Species (2x XP):{RESET}")
            for i, sp in enumerate(daily_challenge['daily_species'], 1):
                caught_tag = " ✅" if sp.lower() in [p.lower() for p in daily_species_caught] else ""
                print(f"    {i}. {sp}{caught_tag}")
            print()
            print(f"  {BOLD}{BRIGHT_MAGENTA}💰 Bonus Type (1.5x Coins): {daily_challenge['daily_bonus_type']}{RESET}")
            print()
            print(f"  {BOLD}{BRIGHT_RED}👑 Daily Raid Boss:{RESET}")
            rb = daily_challenge['daily_raid']
            raid_status = "✅ COMPLETED" if daily_raid_completed else "⬜ AVAILABLE"
            print(f"    {rb['name']} (Lvl {rb['level']}) {rb['type']} — {raid_status}")
            if not daily_raid_completed:
                print(f"    {DIM}Rewards: {rb['reward']['coins']} coins, {rb['reward']['trophies']} trophies, {rb['reward']['item']}{RESET}")
            print()
            print(f"  {BOLD}{BRIGHT_WHITE}1.{RESET} Challenge Daily Raid Boss")
            print(f"  {BOLD}{DIM}Q.{RESET} Back")
            print()
            daily_opt = crazy_input("Choose").strip()
            if daily_opt == "1" and not daily_raid_completed:
                if not pokemon:
                    print(f"\n  {BOLD}{BRIGHT_RED}❌ You need Pokemon first!{RESET}")
                    time.sleep(1)
                else:
                    clear_screen()
                    rb = daily_challenge['daily_raid']
                    fancy_header(f"RAID: {rb['name'].upper()}", emoji="👑", width=50)
                    print(f"  {BOLD}{BRIGHT_RED}Level: {rb['level']} | Type: {rb['type']}{RESET}")
                    print(f"  {BOLD}{BRIGHT_YELLOW}HP Multiplier: {rb['hp_mult']}x | DM Multiplier: {rb['dm_mult']}x{RESET}")
                    print()
                    print(f"  {BOLD}{BRIGHT_GREEN}Your team:{RESET}")
                    for pn, st in pokemon.items():
                        hp_pct = int((st['hp'] / st['maxhp']) * 100) if st['maxhp'] > 0 else 0
                        bar_color = BRIGHT_GREEN if hp_pct > 60 else (BRIGHT_YELLOW if hp_pct > 30 else BRIGHT_RED)
                        bar = f"{bar_color}{'█' * (hp_pct // 5)}{DIM}{'░' * (20 - hp_pct // 5)}{RESET}"
                        print(f"    {pn} {bar} {st['hp']}/{st['maxhp']}")
                    print()
                    ans = crazy_input("Start raid? (y/n)").strip().lower()
                    if ans == 'y':
                        # Create raid boss stats
                        from game_functions import make_pokemon
                        boss_hp = int(rb['hp_mult'] * 50)
                        boss_dm = int(rb['dm_mult'] * 30)
                        boss = make_pokemon(boss_hp, boss_dm, rb['type'], ['Hyper Beam', 'Dragon Pulse', 'Earthquake', 'Psychic'], speed=80, lvl=rb['level'], name=rb['name'])
                        boss['maxhp'] = boss_hp
                        
                        # Run raid battle
                        clear_screen()
                        fancy_header(f"VS {rb['name'].upper()}", emoji="⚔️", width=50)
                        print(f"  {BOLD}{BRIGHT_RED}{rb['name']} (Lvl {rb['level']}) — HP: {boss['hp']}/{boss['maxhp']} | DM: {boss['dm']}{RESET}")
                        print()
                        
                        raid_won = True
                        while boss['hp'] > 0:
                            # Player turn
                            print(f"  {BOLD}{BRIGHT_CYAN}Your turn! Choose a Pokemon:{RESET}")
                            for i, (pn, st) in enumerate(pokemon.items(), 1):
                                print(f"    {i}. {pn} HP: {st['hp']}/{st['maxhp']}")
                            poke_idx = crazy_input("Pokemon #").strip()
                            try:
                                poke_idx = int(poke_idx)
                                poke_keys = list(pokemon.keys())
                                if 1 <= poke_idx <= len(poke_keys):
                                    poke_key = poke_keys[poke_idx - 1]
                                    player = pokemon[poke_key]
                                    if player['hp'] <= 0:
                                        print(f"  {BRIGHT_RED}{poke_key} is fainted!{RESET}")
                                        time.sleep(1)
                                        continue
                                    
                                    print(f"  {BOLD}{BRIGHT_CYAN}Choose a move:{RESET}")
                                    for i, m in enumerate(player['moves'], 1):
                                        print(f"    {i}. {m}")
                                    move_idx = crazy_input("Move #").strip()
                                    try:
                                        move_idx = int(move_idx)
                                        if 1 <= move_idx <= len(player['moves']):
                                            move_name = player['moves'][move_idx - 1]
                                            from game_functions import calculate_move_damage
                                            dmg, eff = calculate_move_damage(move_name, player, boss['type'])
                                            boss['hp'] = max(0, boss['hp'] - dmg)
                                            eff_msg = ""
                                            if eff > 1.0: eff_msg = f" {BRIGHT_GREEN}Super effective!{RESET}"
                                            elif eff < 1.0 and eff > 0: eff_msg = f" {BRIGHT_RED}Not very effective...{RESET}"
                                            elif eff == 0: eff_msg = f" {DIM}No effect!{RESET}"
                                            print(f"  {BRIGHT_YELLOW}{poke_key} used {move_name}! {dmg} damage!{eff_msg}{RESET}")
                                            print(f"  {BRIGHT_RED}{rb['name']} HP: {boss['hp']}/{boss['maxhp']}{RESET}")
                                            print()
                                    except:
                                        pass
                                else:
                                    print(f"  {BRIGHT_RED}Invalid selection!{RESET}")
                                    time.sleep(1)
                                    continue
                            except:
                                pass
                            
                            if boss['hp'] <= 0:
                                break
                            
                            # Boss turn
                            boss_dmg = max(1, boss['dm'] // 3)
                            player['hp'] = max(0, player['hp'] - boss_dmg)
                            print(f"  {BRIGHT_RED}{rb['name']} attacks! {boss_dmg} damage to {poke_key}!{RESET}")
                            print(f"  {BRIGHT_YELLOW}{poke_key} HP: {player['hp']}/{player['maxhp']}{RESET}")
                            print()
                            
                            if player['hp'] <= 0:
                                print(f"  {BRIGHT_RED}{poke_key} fainted!{RESET}")
                                # Check if any pokemon left
                                alive = sum(1 for p in pokemon.values() if p['hp'] > 0)
                                if alive == 0:
                                    raid_won = False
                                    print(f"  {BRIGHT_RED}All Pokemon fainted! Raid failed!{RESET}")
                                    break
                        
                        if raid_won:
                            daily_raid_completed = True
                            money += rb['reward']['coins']
                            trophies += rb['reward']['trophies']
                            inventory[rb['reward']['item']] = inventory.get(rb['reward']['item'], 0) + 1
                            print(f"\n  {BOLD}{BRIGHT_GREEN}🎉 RAID COMPLETE!{RESET}")
                            print(f"  {BOLD}{BRIGHT_GREEN}+{rb['reward']['coins']} coins{RESET}")
                            print(f"  {BOLD}{BRIGHT_GREEN}+{rb['reward']['trophies']} trophies{RESET}")
                            print(f"  {BOLD}{BRIGHT_MAGENTA}+ {rb['reward']['item']}{RESET}")
                        else:
                            print(f"\n  {BOLD}{BRIGHT_RED}💀 Raid failed! Heal your team and try again.{RESET}")
                        crazy_input("Press Enter to continue")
            elif daily_opt == "1" and daily_raid_completed:
                print(f"\n  {BOLD}{BRIGHT_YELLOW}Daily raid already completed! Come back tomorrow.{RESET}")
                crazy_input("Press Enter to continue")

        # ══════════════════════════════════════
        # OPTION 24: BATTLE FRONTIER
        # ══════════════════════════════════════
        if option == 24:
            clear_screen()
            fancy_header("BATTLE FRONTIER", emoji="🎪", width=50)
            print(f"  {DIM}Post-game facilities. Earn Frontier Symbols!{RESET}")
            symbols = count_frontier_symbols({"frontier_progress": frontier_progress})
            print(f"  {BOLD}{BRIGHT_YELLOW}Frontier Symbols: {symbols}/7{RESET}")
            print()
            for i, (key, fac) in enumerate(BATTLE_FRONTIER.items(), 1):
                prog = get_frontier_progress({"frontier_progress": frontier_progress}, key)
                status = "✅" if prog.get("completed") else f"Best: {prog.get('best_streak', 0)}"
                print(f"  {BOLD}{BRIGHT_WHITE}{i}.{RESET} {fac['emoji']} {fac['name']} {DIM}[{status}]{RESET}")
            print()
            print(f"  {BOLD}{DIM}Q.{RESET} Back")
            bf_opt = crazy_input("Choose").strip()
            bf_keys = list(BATTLE_FRONTIER.keys())
            if bf_opt.isdigit() and 1 <= int(bf_opt) <= len(bf_keys):
                selected_fac = bf_keys[int(bf_opt) - 1]
                fac = BATTLE_FRONTIER[selected_fac]
                clear_screen()
                fancy_header(fac['name'], emoji=fac['emoji'], width=50)
                print(f"  {BOLD}{BRIGHT_CYAN}{fac['description']}{RESET}")
                print(f"  {DIM}Rules: {fac['rules']}{RESET}")
                print(f"  {BOLD}{BRIGHT_MAGENTA}Reward: {fac['symbol']}{RESET}")
                print()
                print(f"  {BOLD}{BRIGHT_WHITE}1.{RESET} Start Challenge")
                print(f"  {BOLD}{DIM}Q.{RESET} Back")
                bf_start = crazy_input("Choose").strip()
                if bf_start == "1":
                    if not pokemon:
                        print(f"\n  {BOLD}{BRIGHT_RED}❌ You need Pokemon first!{RESET}")
                        time.sleep(1)
                    else:
                        # Run the selected facility
                        if selected_fac == "factory":
                            # Battle Factory - rental Pokemon
                            clear_screen()
                            fancy_header("BATTLE FACTORY", emoji="🏭", width=50)
                            print(f"  {DIM}You receive 3 random rental Pokemon!{RESET}")
                            print()
                            rental_team = get_rental_team(3)
                            for i, rp in enumerate(rental_team, 1):
                                print(f"  {BOLD}{BRIGHT_WHITE}{i}.{RESET} {rp['name']} {DIM}[{rp['type'][0]}]{RESET} HP:{rp['hp']} DM:{rp['dm']} SPD:{rp['speed']}")
                                print(f"     {DIM}Moves: {', '.join(rp['moves'][:3])}...{RESET}")
                            print()
                            print(f"  {BOLD}{BRIGHT_YELLOW}Win 7 battles to earn the Knowledge Symbol!{RESET}")
                            print()
                            ans = crazy_input("Accept rental team? (y/n)").strip().lower()
                            if ans == 'y':
                                # Simulate factory battles
                                wins = 0
                                for round_num in range(1, 8):
                                    clear_screen()
                                    fancy_header(f"FACTORY ROUND {round_num}/7", emoji="🏭", width=50)
                                    opponent = random.choice(RENTAL_POKEMON)
                                    print(f"  {BOLD}{BRIGHT_RED}Opponent: {opponent['name']} ({opponent['type'][0]}){RESET}")
                                    print(f"  {DIM}HP: {opponent['hp']} | DM: {opponent['dm']} | SPD: {opponent['speed']}{RESET}")
                                    print()
                                    # Simple battle simulation
                                    player_power = sum(r['dm'] for r in rental_team)
                                    enemy_power = opponent['dm']
                                    if player_power > enemy_power * 0.8:
                                        wins += 1
                                        print(f"  {BRIGHT_GREEN}✅ Round {round_num} won!{RESET}")
                                    else:
                                        print(f"  {BRIGHT_RED}❌ Round {round_num} lost!{RESET}")
                                        break
                                    time.sleep(0.5)
                                    crazy_input("Press Enter")
                                
                                if wins >= 7:
                                    money += 5000
                                    trophies += 3000
                                    inventory["Choice Band"] = inventory.get("Choice Band", 0) + 1
                                    frontier_progress = update_frontier_progress({"frontier_progress": frontier_progress}, "factory", streak=7, completed=True, symbol="Knowledge Symbol")
                                    print(f"\n  {BOLD}{BRIGHT_GREEN}🎉 FACTORY COMPLETE! Knowledge Symbol earned!{RESET}")
                                    print(f"  {BOLD}{BRIGHT_GREEN}+5000 coins, +3000 trophies, +Choice Band{RESET}")
                                else:
                                    frontier_progress = update_frontier_progress({"frontier_progress": frontier_progress}, "factory", streak=wins)
                                    print(f"\n  {BOLD}{BRIGHT_RED}💀 Factory run ended at {wins}/7 wins.{RESET}")
                                crazy_input("Press Enter to continue")
                        
                        elif selected_fac == "hall":
                            # Battle Hall - face all 18 types
                            clear_screen()
                            fancy_header("BATTLE HALL", emoji="🏰", width=50)
                            print(f"  {DIM}Face all 18 types in succession!{RESET}")
                            print()
                            hall_order = get_battle_hall_order()
                            print(f"  {BOLD}{BRIGHT_YELLOW}Type order:{RESET}")
                            for i, t in enumerate(hall_order, 1):
                                opp = BATTLE_HALL_OPPONENTS[t]
                                print(f"  {i:2}. {t:8} - {opp['name']} (HP:{opp['hp']} DM:{opp['dm']})")
                            print()
                            ans = crazy_input("Start Battle Hall? (y/n)").strip().lower()
                            if ans == 'y':
                                # Clone team for hall (no healing between battles)
                                hall_team = {}
                                for k, v in pokemon.items():
                                    hall_team[k] = dict(v)
                                
                                wins = 0
                                for i, ptype in enumerate(hall_order):
                                    opp = BATTLE_HALL_OPPONENTS[ptype]
                                    clear_screen()
                                    fancy_header(f"HALL BATTLE {i+1}/18: {ptype.upper()}", emoji="⚔️", width=50)
                                    print(f"  {BOLD}{BRIGHT_RED}Opponent: {opp['name']} ({ptype}){RESET}")
                                    print(f"  {DIM}HP: {opp['hp']} | DM: {opp['dm']} | SPD: {opp['speed']}{RESET}")
                                    print()
                                    # Show team status
                                    alive = {k: v for k, v in hall_team.items() if v['hp'] > 0}
                                    if not alive:
                                        print(f"  {BRIGHT_RED}All Pokemon fainted!{RESET}")
                                        break
                                    print(f"  {BOLD}{BRIGHT_GREEN}Your team:{RESET}")
                                    for k, v in alive.items():
                                        print(f"    {k} HP: {v['hp']}/{v['maxhp']}")
                                    print()
                                    # Simple simulation
                                    team_power = sum(v['dm'] for v in alive.values())
                                    if team_power > opp['dm'] * 0.7:
                                        wins += 1
                                        # Take some damage
                                        for k in list(alive.keys())[:1]:
                                            dmg = max(1, opp['dm'] // 4)
                                            hall_team[k]['hp'] = max(0, hall_team[k]['hp'] - dmg)
                                        print(f"  {BRIGHT_GREEN}✅ {ptype} type defeated!{RESET}")
                                    else:
                                        # Lose a pokemon
                                        if alive:
                                            loser = random.choice(list(alive.keys()))
                                            hall_team[loser]['hp'] = 0
                                            print(f"  {BRIGHT_RED}❌ {loser} fainted!{RESET}")
                                        # Check if still have pokemon
                                        alive_check = {k: v for k, v in hall_team.items() if v['hp'] > 0}
                                        if not alive_check:
                                            print(f"  {BRIGHT_RED}All Pokemon fainted!{RESET}")
                                            break
                                        wins += 0.5  # Partial win
                                    time.sleep(0.5)
                                    crazy_input("Press Enter")
                                
                                final_wins = int(wins)
                                if final_wins >= 18:
                                    money += 30000
                                    trophies += 15000
                                    inventory["Expert Belt"] = inventory.get("Expert Belt", 0) + 1
                                    frontier_progress = update_frontier_progress({"frontier_progress": frontier_progress}, "hall", streak=18, completed=True, symbol="Print Symbol")
                                    print(f"\n  {BOLD}{BRIGHT_GREEN}🎉 HALL COMPLETE! Print Symbol earned!{RESET}")
                                    print(f"  {BOLD}{BRIGHT_GREEN}+30000 coins, +15000 trophies, +Expert Belt{RESET}")
                                else:
                                    frontier_progress = update_frontier_progress({"frontier_progress": frontier_progress}, "hall", streak=final_wins)
                                    print(f"\n  {BOLD}{BRIGHT_RED}💀 Hall run ended at {final_wins}/18 types.{RESET}")
                                crazy_input("Press Enter to continue")
                        
                        else:
                            # Generic facility handler for other facilities
                            clear_screen()
                            fancy_header(fac['name'], emoji=fac['emoji'], width=50)
                            print(f"  {DIM}Challenge in progress...{RESET}")
                            print()
                            # Simple simulation for other facilities
                            rounds = fac.get('rounds', fac.get('rooms', fac.get('max_streak', 7)))
                            wins = 0
                            for r in range(1, rounds + 1):
                                print(f"  {BOLD}{BRIGHT_WHITE}Round {r}/{rounds}...{RESET}")
                                if random.random() < 0.7:  # 70% win rate
                                    wins += 1
                                    print(f"  {BRIGHT_GREEN}✅ Won!{RESET}")
                                else:
                                    print(f"  {BRIGHT_RED}❌ Lost!{RESET}")
                                    break
                                time.sleep(0.3)
                            
                            if wins >= rounds:
                                reward_key = "complete"
                                reward = fac['rewards'].get(reward_key, {"coins": 5000, "trophies": 3000, "item": "Rare Candy"})
                                money += reward['coins']
                                trophies += reward['trophies']
                                if reward.get('item'):
                                    inventory[reward['item']] = inventory.get(reward['item'], 0) + 1
                                frontier_progress = update_frontier_progress({"frontier_progress": frontier_progress}, selected_fac, streak=wins, completed=True, symbol=fac['symbol'])
                                print(f"\n  {BOLD}{BRIGHT_GREEN}🎉 {fac['name']} COMPLETE! {fac['symbol']} earned!{RESET}")
                                print(f"  {BOLD}{BRIGHT_GREEN}+{reward['coins']} coins, +{reward['trophies']} trophies{RESET}")
                                if reward.get('item'):
                                    print(f"  {BOLD}{BRIGHT_MAGENTA}+ {reward['item']}{RESET}")
                            else:
                                frontier_progress = update_frontier_progress({"frontier_progress": frontier_progress}, selected_fac, streak=wins)
                                print(f"\n  {BOLD}{BRIGHT_RED}💀 Run ended at {wins}/{rounds}.{RESET}")
                            crazy_input("Press Enter to continue")

        # ══════════════════════════════════════
        # OPTION 22: SAVE & LEAVE
        # ══════════════════════════════════════
        if option == 22:
            # Push save to cloud before leaving
            if cloud_token:
                try:
                    print(f"  {DIM}☁️  Saving to cloud...{RESET}")
                    save_data = json.dumps({"name": name, "pokemon": pokemon, "money": money, "pvp_rp": pvp_rp, "trophies": trophies, "inventory": inventory, "location": location, "badges": badges, "tower_record": tower_record, "pokedex_seen": list(pokedex_seen), "pokedex_caught": list(pokedex_caught), "elite_four_defeated": elite_four_defeated, "achievements": achievement_manager.to_dict(), "heal_tickets": heal_tickets, "daycare": daycare})
                    r = robust_request("POST", f"{SERVER_URL}/save", json_data={"save_data": save_data}, headers={"Authorization": f"Bearer {cloud_token}"}, timeout=30)
                    if r.status_code == 200:
                        print(f"  {BRIGHT_GREEN}✅ Game saved to cloud!{RESET}")
                    else:
                        print(f"  {BRIGHT_RED}❌ Cloud save failed: {r.json().get('message', 'Error')}{RESET}")
                except Exception as e:
                    print(f"  {BRIGHT_RED}❌ Cloud save error: {e}{RESET}")
            time.sleep(1)
            break

except Exception as e:
    print()
    print_art(SAVING_ART, lambda t: glitch_text(t))
    print(f"  {BOLD}{BRIGHT_RED}⚠️ CRASH DETECTED! ⚠️{RESET}")
    print(f"  {DIM}Error: {e}{RESET}")
    print()
    import traceback
    traceback.print_exc()
    print()
    if cloud_token:
        try:
            print(f"  {DIM}☁️  Emergency cloud save...{RESET}")
            save_data = json.dumps({"name": name, "pokemon": pokemon, "money": money, "pvp_rp": pvp_rp, "trophies": trophies, "inventory": inventory, "location": location, "badges": badges, "tower_record": tower_record, "pokedex_seen": list(pokedex_seen), "pokedex_caught": list(pokedex_caught), "elite_four_defeated": elite_four_defeated, "achievements": achievement_manager.to_dict(), "heal_tickets": heal_tickets, "daycare": daycare})
            r = robust_request("POST", f"{SERVER_URL}/save", json_data={"save_data": save_data}, headers={"Authorization": f"Bearer {cloud_token}"}, timeout=30)
            if r.status_code == 200:
                print(f"  {BRIGHT_GREEN}✅ Emergency cloud save successful!{RESET}")
            else:
                print(f"  {BRIGHT_RED}❌ Emergency cloud save failed!{RESET}")
        except:
            print(f"  {BRIGHT_RED}❌ Could not save to cloud!{RESET}")
    time.sleep(1)

# ══════════════════════════════════════
# CLOUD SAVE ON EXIT
# ══════════════════════════════════════
if cloud_token:
    try:
        print(f"  {DIM}☁️  Auto-saving to cloud...{RESET}")
        save_data = json.dumps({"name": name, "pokemon": pokemon, "money": money, "pvp_rp": pvp_rp, "trophies": trophies, "inventory": inventory, "location": location, "badges": badges, "tower_record": tower_record, "pokedex_seen": list(pokedex_seen), "pokedex_caught": list(pokedex_caught), "elite_four_defeated": elite_four_defeated, "achievements": achievement_manager.to_dict(), "heal_tickets": heal_tickets, "daycare": daycare})
        r = robust_request("POST", f"{SERVER_URL}/save", json_data={"save_data": save_data}, headers={"Authorization": f"Bearer {cloud_token}"}, timeout=30)
        if r.status_code == 200:
            print(f"  {BRIGHT_GREEN}✅ Cloud save updated!{RESET}")
        else:
            print(f"  {BRIGHT_RED}❌ Cloud save failed: {r.json().get('message', 'Error')}{RESET}")
    except Exception as e:
        print(f"  {BRIGHT_RED}❌ Cloud auto-save error: {e}{RESET}")
time.sleep(1)

print()
clear_screen()
wipe_transition(width=50)
print_art(GAME_OVER_ART, theme_text)
theme_print(f"Thanks for playing, {name}! See you next time! 👋", delay=0.04)
sparkle_burst(duration=0.5, width=35)
theme_divider(50)
crazy_input("Press Enter to exit")
