import random
from pokemon_dex import weak_pokemon, moderately_strong_pokemon, strong_pokemon, ultra_strong_pokemon
from evolution_map import EVOLUTION_MAP
from abilities import get_ability_for_pokemon, pick_ability_by_type, apply_ability_trigger
from held_items import apply_held_item_trigger, HELD_ITEMS
from time_system import advance_time, time_spawn_modifier, get_time_spawns
from crazy_style import (
    RESET, BOLD, DIM, ITALIC, UNDERLINE, REVERSE,
    RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE,
    BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_BLUE,
    BRIGHT_MAGENTA, BRIGHT_CYAN, BRIGHT_WHITE,
    BG_RED, BG_GREEN, BG_YELLOW,
    rgb, bg_rgb,
    rainbow_text, fire_text, electric_text, gradient_text, crazy_text,
    glitch_text, sparkle_text, neon_glow, psychic_text, random_color_text,
    crazy_box, fire_box, electric_box, hp_bar, xp_bar,
    crazy_divider, menu_divider,
    typewriter, dramatic_print, explode_print, dramatic_pause, slow_reveal,
    stat_label, money_display, trophy_display,
    pokemon_name_style, enemy_name_style, player_name_style,
    print_art, LEVEL_UP_ART, WIN_ART, LOSE_ART, CATCH_ART, CRIT_ART,
    BATTLE_ART, SHOP_ART, HOSPITAL_ART,
    crazy_input, crazy_int_input,
    ALL_COLORS, FIRE_COLORS
)
from animations import (
    pokeball_loading, progress_bar_animated, spinner_animation, battle_loading,
    matrix_text_reveal, explosion_effect, sparkle_burst, damage_shake,
    rain_effect, fire_effect, electric_storm,
    wipe_transition, fade_transition, pokeball_transition,
    animate_attack_sequence, animate_enemy_attack_sequence, animate_catch_attempt, animate_heal, animate_level_up,
    animate_money_earned, dna_evolution_sequence,
    stat_card, battle_hud, shop_item_card, fancy_header,
    countdown, victory_celebration, defeat_rain,
    ability_activation, item_flash, type_effectiveness_flash,
    recoil_flash, healing_flash, stage_change_flash
)
from battle_log import battle_log
from quest_manager import quest_manager
from world_map import REGIONS
from moves_data import MOVES, get_effectiveness
from inventory import ITEMS, apply_item_effect
from status_manager import STATUS_EFFECTS, apply_status_tick, can_attack
from weather_engine import WEATHER_EFFECTS, apply_weather_damage
from ascii_art import (
    get_pokemon_sprite, POKEMON_SPRITES,
    WILD_ENCOUNTER_ART, ARENA_ENTRANCE_ART, SHOP_ENTRANCE_ART,
    HOSPITAL_ENTRANCE_ART, VICTORY_ROYALE_ART, DEFEAT_ART,
    CAUGHT_POKEMON_ART, MEGA_CRIT_ART, LEVEL_UP_MEGA_ART,
    TRAINING_ART, HEALING_FRAMES, STARTER_SELECTION_ART,
    MONEY_EARNED_ART, TROPHY_ART,
    POKEBALL_THROW_FRAMES, POKEBALL_FAIL_FRAMES,
    ATTACK_FRAMES, ENEMY_ATTACK_FRAMES
)
import time
import sys


def get_wild_pokemon(level, region="Grasslands"):
    """Get a random wild pokemon and its stats based on level and region."""
    region_data = REGIONS.get(region, REGIONS["Grasslands"])
    possible_spawns = region_data["spawns"]
    possible_spawns = get_time_spawns(list(possible_spawns))
    wild = random.choice(possible_spawns)
    
    # Find in any dex
    dex_entry = None
    for dex in [weak_pokemon, moderately_strong_pokemon, strong_pokemon, ultra_strong_pokemon]:
        if wild in dex:
            dex_entry = dex[wild]
            break
    
    if not dex_entry:
        dex_entry = {"hp": 50, "dm": 20, "type": "Normal", "speed": 50}
        
    enemyhp = dex_entry["hp"] + random.randint(0, level)
    enemydm = dex_entry["dm"] + (level // 2)
    enemytype = dex_entry.get("type", "Normal")
    enemymoves = dex_entry.get("moves", ["Tackle"])
    enemyspeed = dex_entry.get("speed", 50) + (level // 4)
    
    # SHINY CHECK (1/100)
    is_shiny = random.random() < 0.01
    
    return wild, enemyhp, enemydm, enemytype, enemymoves, is_shiny, enemyspeed


def get_arena_pokemon(level):
    """Get a random arena pokemon and its stats based on level."""
    # Arena can pick from any dex
    all_dex = list(weak_pokemon.keys()) + list(moderately_strong_pokemon.keys()) + list(strong_pokemon.keys()) + list(ultra_strong_pokemon.keys())
    arena = random.choice(all_dex)
    
    dex_entry = None
    for dex in [weak_pokemon, moderately_strong_pokemon, strong_pokemon, ultra_strong_pokemon]:
        if arena in dex:
            dex_entry = dex[arena]
            break
            
    arenaenemyhp = dex_entry["hp"] + (level // 2)
    arenaenemydm = dex_entry["dm"] + (level // 4)
    arenatype = dex_entry.get("type", "Normal")
    arenamoves = dex_entry.get("moves", ["Tackle"])
    arenaspeed = dex_entry.get("speed", 50) + (level // 4)

    return arena, arenaenemyhp, arenaenemydm, arenatype, arenamoves, arenaspeed


def calculate_move_damage(move_name, attacker_stats, defender_type, weather="Clear", is_crit=False):
    """Calculate damage based on move power, category, type effectiveness, status, and weather."""
    move = MOVES.get(move_name, {"type": "Normal", "power": 40, "category": "Physical"})
    effectiveness = get_effectiveness(move["type"], defender_type)
    
    atk_mult = 1.0
    status = attacker_stats.get("status")
    if status == "Burn":
        atk_mult = 0.5

    ability = attacker_stats.get("ability")
    ab_result = apply_ability_trigger(ability, "damage_calc", attacker_stats, weather=weather, move_type=move["type"])
    atk_mult *= ab_result.get("damage_mult", 1.0)
    
    item = attacker_stats.get("hold_item")
    item_result = apply_held_item_trigger(item, "damage_calc", attacker_stats, move_type=move["type"])
    item_dm = item_result.get("damage_mult", 1.0)
    atk_mult *= item_dm
        
    weather_data = WEATHER_EFFECTS.get(weather, WEATHER_EFFECTS["Clear"])
    if weather_data["boost_type"] == move["type"]:
        atk_mult *= 1.5
    if weather == "Solar Flare" and move["type"] == "Fire":
        atk_mult *= 2.0

    low_hp_trig = apply_ability_trigger(ability, "low_hp", attacker_stats, move_type=move["type"])
    atk_mult *= low_hp_trig.get("damage_mult", 1.0)
    
    stages = attacker_stats.get("stages", {})
    if move["category"] == "Physical":
        atk_stat = attacker_stats["dm"]
        atk_stage = stages.get("dm", 0)
    else:
        atk_stat = attacker_stats["dm"]
        atk_stage = stages.get("dm", 0)
    
    atk_mult *= stage_multiplier(stages, "dm")
    
    base_damage = atk_stat * (move["power"] / 40.0) * atk_mult
    final_damage = base_damage * effectiveness

    if move.get("effect") and move["effect"].get("status") and ability == "Serene Grace":
        pass
    
    if is_crit:
        final_damage *= 1.5
        
    return int(final_damage), effectiveness


def calculate_xp_gain(enemy_hp, attacker_dm, hit_count, enemy_dm):
    """Calculate XP gained from battle."""
    return ((enemy_hp + (attacker_dm * hit_count)) + enemy_dm) // 2


def show_pokemon_sprite(name):
    """Show a pokemon's ASCII art sprite with styling."""
    sprite = get_pokemon_sprite(name)
    for line in sprite.strip().split('\n'):
        print(gradient_text(line, (100, 200, 255), (255, 100, 200)))


def animate_attack_sequence(attacker, defender, damage, is_crit=False):
    """Full attack animation with ASCII art frames."""
    print()
    for frame in ATTACK_FRAMES:
        frame_text = frame.replace("YOUR POKEMON", attacker.upper()).replace("ENEMY", defender.upper())
        sys.stdout.write(f"\r  {BOLD}{BRIGHT_RED}{frame_text}{RESET}{' ' * 10}")
        sys.stdout.flush()
        time.sleep(0.2)
    print()

    if is_crit:
        print_art(MEGA_CRIT_ART, fire_text)
        damage_shake(f"💥💥💥 {damage} MEGA DAMAGE! 💥💥💥", shakes=10)
    else:
        damage_shake(f"💥 {damage} damage! 💥", shakes=5)
    print()


def animate_enemy_attack_sequence(attacker, defender, damage):
    """Full enemy attack animation."""
    print()
    for frame in ENEMY_ATTACK_FRAMES:
        frame_text = frame.replace("YOUR POKEMON", defender.upper()).replace("ENEMY", attacker.upper())
        sys.stdout.write(f"\r  {BOLD}{RED}{frame_text}{RESET}{' ' * 10}")
        sys.stdout.flush()
        time.sleep(0.2)
    print()
    damage_shake(f"💥 -{damage} to {defender}!", shakes=5)
    print()


def show_catch_animation(pokemon_name, success):
    """Full catch attempt animation with pokeball throw."""
    print()
    for frame in POKEBALL_THROW_FRAMES:
        for line in frame.strip().split('\n'):
            line_text = line.replace("🐾", pokemon_name.upper())
            print(f"  {BRIGHT_YELLOW}{line_text}{RESET}")
        time.sleep(0.3)
        line_count = len(frame.strip().split('\n'))
        sys.stdout.write(f"\033[{line_count}A")
        sys.stdout.flush()

    if success:
        print_art(CAUGHT_POKEMON_ART, rainbow_text)
        sparkle_burst(duration=0.5, width=30)
    else:
        for frame in POKEBALL_FAIL_FRAMES:
            for line in frame.strip().split('\n'):
                print(f"  {BRIGHT_RED}{line}{RESET}")
            time.sleep(0.4)


def show_healing_animation(pokemon_name, heal_amount):
    """Full healing animation with frames."""
    print()
    for frame in HEALING_FRAMES:
        for line in frame.strip().split('\n'):
            print(f"  {BRIGHT_GREEN}{line}{RESET}")
        time.sleep(0.4)
        line_count = len(frame.strip().split('\n'))
        sys.stdout.write(f"\033[{line_count}A")
        sys.stdout.flush()

    for line in HEALING_FRAMES[-1].strip().split('\n'):
        print(f"  {BOLD}{BRIGHT_GREEN}{line}{RESET}")
    print(f"  {BOLD}{BRIGHT_GREEN}✨ {pokemon_name} healed for +{heal_amount} HP!{RESET}")


def _evolution_lookup_key(pokemon_name):
    key = pokemon_name.lower()
    if key in EVOLUTION_MAP:
        return key

    base_key = key.rstrip("0123456789")
    if base_key in EVOLUTION_MAP:
        return base_key
    return key


def get_eligible_learnset_moves(pokemon_name, level, current_moves):
    """Return learnset moves for this form up to level that are not currently known."""
    evo_data = EVOLUTION_MAP.get(_evolution_lookup_key(pokemon_name))
    if not evo_data:
        return []

    known_moves = set(current_moves or [])
    eligible_moves = []
    seen_moves = set()
    for learn_level, moves in sorted(evo_data.get("learns", {}).items()):
        if learn_level > level:
            continue
        for move_name in moves:
            if move_name in known_moves or move_name in seen_moves:
                continue
            eligible_moves.append(move_name)
            seen_moves.add(move_name)
    return eligible_moves


def learn_level_up_moves(pokemon_stats, pokemon_name):
    """Offer every eligible level-up move for the pokemon's current form."""
    level = pokemon_stats.get("lvl", 1)
    moves_to_learn = get_eligible_learnset_moves(
        pokemon_name,
        level,
        pokemon_stats.get("moves", [])
    )
    for move_name in moves_to_learn:
        offer_to_learn_move(pokemon_stats, move_name)


def _unique_pokemon_key(pokemon_dict, desired_name, old_name):
    base_key = desired_name.lower()
    if base_key == old_name or base_key not in pokemon_dict:
        return base_key

    suffix = 2
    while f"{base_key}{suffix}" in pokemon_dict:
        suffix += 1
    return f"{base_key}{suffix}"


def try_evolve_pokemon(pokemon_dict, poke_name):
    """Prompt to evolve an eligible pokemon and return its current team key."""
    if poke_name not in pokemon_dict:
        return poke_name

    stats = pokemon_dict[poke_name]
    evo_data = EVOLUTION_MAP.get(_evolution_lookup_key(poke_name))
    if not evo_data or not evo_data.get("evolves_to"):
        return poke_name
    if stats.get("lvl", 1) < evo_data.get("level", 999):
        return poke_name

    evolved_name = evo_data["evolves_to"]
    print()
    fancy_header("EVOLUTION READY", emoji="🧬", width=45)
    print(f"  {BOLD}{BRIGHT_WHITE}{poke_name.capitalize()}{RESET} can evolve into {BOLD}{BRIGHT_GREEN}{evolved_name}{RESET}!")
    ans = crazy_input("Evolve now? (y/n)")
    if ans.lower() != "y":
        print(f"  {DIM}{poke_name.capitalize()} did not evolve yet.{RESET}")
        time.sleep(1)
        return poke_name

    new_key = _unique_pokemon_key(pokemon_dict, evolved_name, poke_name)
    dna_evolution_sequence(poke_name, evolved_name)

    for stat_name, stat_gain in evo_data.get("stats", {}).items():
        stats[stat_name] = stats.get(stat_name, 0) + stat_gain

    if stats.get("hp", 0) > stats.get("maxhp", stats.get("hp", 0)):
        stats["hp"] = stats.get("maxhp", stats["hp"])
    if stats.get("name"):
        stats["name"] = new_key

    pokemon_dict[new_key] = pokemon_dict.pop(poke_name)
    if new_key != evolved_name.lower():
        print(f"  {DIM}Stored as {new_key} because {evolved_name.lower()} is already on your team.{RESET}")

    stat_card(new_key, stats["hp"], stats["maxhp"], stats["dm"],
              stats["xp"], stats["maxxp"], stats["lvl"], speed=stats.get("speed", 50))
    print()
    learn_level_up_moves(stats, new_key)
    return new_key


def level_up_pokemon(pokemon_dict, poke_name):
    """Handle pokemon leveling up and stat upgrades — MEGA VERSION."""
    stats = pokemon_dict[poke_name]
    stats["lvl"] += 1
    stats["maxxp"] = stats["lvl"] * 50
    stats["xp"] = 0

    print()
    wipe_transition(width=45)
    print_art(LEVEL_UP_MEGA_ART, rainbow_text)
    animate_level_up(poke_name, stats["lvl"])
    sparkle_burst(duration=0.5, width=35)
    print()

    stat_card(poke_name, stats["hp"], stats["maxhp"], stats["dm"],
              stats["xp"], stats["maxxp"], stats["lvl"], speed=stats.get("speed", 50))
    print()

    print(f"  {BOLD}{BRIGHT_CYAN}Choose an upgrade:{RESET}")
    print()
    print(f"  {BOLD}{BRIGHT_GREEN}1.{RESET} {gradient_text('❤️  HEALTH BOOST', (0, 255, 0), (0, 200, 100))}")
    increase_hp = stats["lvl"] * 5
    print(f"     {DIM}+{increase_hp} HP{RESET}")
    print()
    print(f"  {BOLD}{BRIGHT_RED}2.{RESET} {gradient_text('⚔️  POWER SURGE', (255, 0, 0), (255, 100, 0))}")
    increase_dm = stats["lvl"] * 2
    print(f"     {DIM}+{increase_dm} DM{RESET}")
    print()
    avr = crazy_input("What do you want")

    if avr == "health" or avr == "1":
        print()
        fancy_header("HEALTH BOOST", emoji="❤️", width=40)
        progress_bar_animated(label="Upgrading HP", total=15, duration=1.0)
        stats["hp"] += increase_hp
        stats["maxhp"] += increase_hp
        print(f"  {BOLD}{BRIGHT_GREEN}⬆️  +{increase_hp} HP!{RESET}")
        hp_bar(stats['hp'], stats['maxhp'], name=poke_name)
    elif avr == "damage" or avr == "2":
        print()
        fancy_header("POWER SURGE", emoji="⚔️", width=40)
        progress_bar_animated(label="Upgrading DM", total=15, duration=1.0)
        stats["dm"] += increase_dm
        print(f"  {BOLD}{BRIGHT_RED}⬆️  +{increase_dm} DM!{RESET}")

    print(f"  {BOLD}{BRIGHT_CYAN}Current LVL: {stats['lvl']} | XP: {stats['xp']}/{stats['maxxp']}{RESET}")

    learn_level_up_moves(stats, poke_name)
    current_name = try_evolve_pokemon(pokemon_dict, poke_name)
    return current_name


def select_move_menu(pokemon_name, stats):
    """Interactive menu to select a move showing PP and priority."""
    moves = stats.get("moves", ["Tackle"])
    fancy_header(f"{pokemon_name.upper()}'S MOVES", emoji="⚔️", width=40)
    
    pp_data = stats.get("pp", {})

    for i, move_name in enumerate(moves):
        move = MOVES.get(move_name, {"type": "Normal", "power": 40, "category": "Physical", "priority": 0})
        move_color = YELLOW
        type_colors = {
            "Fire": RED, "Water": BLUE, "Grass": GREEN, "Electric": BRIGHT_YELLOW,
            "Psychic": MAGENTA, "Ice": BRIGHT_CYAN, "Fighting": BRIGHT_RED,
            "Ghost": BRIGHT_MAGENTA, "Dragon": BRIGHT_BLUE, "Steel": WHITE
        }
        move_color = type_colors.get(move["type"], YELLOW)

        current_pp = pp_data.get(move_name, get_max_pp(move_name))
        max_pp = get_max_pp(move_name)
        priority_mark = f" {BOLD}{BRIGHT_YELLOW}★Priority{RESET}" if move.get("priority", 0) != 0 else ""

        print(f"  {BOLD}{BRIGHT_WHITE}{i+1}.{RESET} {move_color}{move_name:15}{RESET} [{move['type']}/{move['category']}/{move['power']}]  PP: {current_pp}/{max_pp}{priority_mark}")
    
    print(f"  {BOLD}{BRIGHT_WHITE}{len(moves)+1}.{RESET} {RED}Back{RESET}")
    
    choice = crazy_int_input("Select a move")
    if 1 <= choice <= len(moves):
        return moves[choice-1]
    return None


def use_item_menu(inventory, pokemon_stats, pokemon_dict=None, current_name=None):
    """Interactive menu to use an item from the bag."""
    if not inventory:
        print(f"\n  {BOLD}{BRIGHT_RED}Your bag is empty!{RESET}")
        time.sleep(1)
        return False, None
        
    fancy_header("YOUR BAG", emoji="🎒", width=40)
    bag_items = list(inventory.keys())
    for i, item_name in enumerate(bag_items):
        print(f"  {BOLD}{BRIGHT_WHITE}{i+1}.{RESET} {BRIGHT_CYAN}{item_name:15}{RESET} [Qty: {inventory[item_name]}]")
    
    print(f"  {BOLD}{BRIGHT_WHITE}{len(bag_items)+1}.{RESET} {RED}Back{RESET}")
    
    choice = crazy_int_input("Select an item")
    if 1 <= choice <= len(bag_items):
        item_name = bag_items[choice-1]
        success, msg = apply_item_effect(pokemon_stats, item_name)
        if success:
            inventory[item_name] -= 1
            if inventory[item_name] <= 0:
                del inventory[item_name]
            if msg == "rare_candy_level_up" and pokemon_dict and current_name:
                pokemon_stats["xp"] = pokemon_stats.get("maxxp", 50)
                new_name = level_up_pokemon(pokemon_dict, current_name)
                print(f"\n  {BOLD}{BRIGHT_GREEN}✨ Rare Candy caused a level up!{RESET}")
                time.sleep(1)
                return True, new_name
            elif msg.startswith("pp_restore"):
                parts = msg.split(":")
                move_name = parts[1] if len(parts) > 1 else None
                amount = int(parts[2]) if len(parts) > 2 else None
                if move_name:
                    restore_move_pp(pokemon_stats, move_name, amount)
                else:
                    restore_all_pp(pokemon_stats)
                print(f"\n  {BOLD}{BRIGHT_GREEN}✨ PP restored!{RESET}")
                time.sleep(1)
                return True, None
            elif msg.startswith("cure_status"):
                pokemon_stats["status"] = None
                print(f"\n  {BOLD}{BRIGHT_GREEN}✨ Status cured!{RESET}")
                time.sleep(1)
                return True, None
            elif msg.startswith("revive"):
                if pokemon_stats.get("hp", 0) <= 0:
                    pokemon_stats["hp"] = pokemon_stats["maxhp"] // 2
                print(f"\n  {BOLD}{BRIGHT_GREEN}✨ Revived!{RESET}")
                time.sleep(1)
                return True, None
            print(f"\n  {BOLD}{BRIGHT_GREEN}✨ {msg}{RESET}")
            time.sleep(1)
            return True, None
        else:
            print(f"\n  {BOLD}{BRIGHT_RED}❌ {msg}{RESET}")
            time.sleep(1)
    return False, None


def heal_pokemon(pokemon_dict, poke_name, money):
    """Heal a pokemon — MEGA VERSION."""
    if poke_name not in pokemon_dict:
        print(f"\n  {BOLD}{BRIGHT_RED}❌ {poke_name} is not found in your index{RESET}")
        return money

    stats = pokemon_dict[poke_name]
    clamp_hp(stats)
    print()
    fancy_header(f"HEALING {poke_name.upper()}", emoji="💊", width=40)
    spinner_animation(f"Preparing medicine for {poke_name}", duration=1.0)

    if stats["hp"] < 0:
        heal_amount = abs(stats["hp"]) + stats["maxhp"]
    else:
        heal_amount = max(0, stats["maxhp"] - stats["hp"])

    cost = heal_amount * 10

    show_healing_animation(poke_name, heal_amount)
    print()
    print(f"  {BOLD}{BRIGHT_YELLOW}💰 Cost: {cost} coins{RESET}")

    if money < cost:
        print(f"  {BOLD}{BRIGHT_RED}❌ Not enough coins! Need {cost}, have {money}{RESET}")
        return money

    money -= cost
    stats["hp"] += heal_amount
    stats["hp"] = min(stats["maxhp"], stats["hp"])
    restore_all_pp(stats)
    print()
    stat_card(poke_name, stats["hp"], stats["maxhp"], stats["dm"],
              stats["xp"], stats["maxxp"], stats["lvl"], speed=stats.get("speed", 50))
    print(f"  {money_display(money)}")
    return money


def train_pokemon(pokemon_dict, poke_name, money, stat_type):
    """Train a pokemon — MEGA VERSION."""
    if poke_name not in pokemon_dict:
        print(f"\n  {BOLD}{BRIGHT_RED}❌ {poke_name} not found in your pokemon.{RESET}")
        return money

    if money < 250:
        print(f"\n  {BOLD}{BRIGHT_RED}❌ Not enough coins to train! Need 250, have {money}{RESET}")
        return money

    stats = pokemon_dict[poke_name]

    print()
    print_art(TRAINING_ART, rainbow_text)

    if stat_type.lower() in ["health", "hp"]:
        fancy_header(f"TRAINING {poke_name.upper()}'s HEALTH", emoji="💪", width=45)
        countdown(3)
        progress_bar_animated(label="Training HP", total=20, duration=1.5)
        stats["hp"] += 20
        print(f"  {BOLD}{BRIGHT_GREEN}⬆️  +20 Health!{RESET}")
        hp_bar(stats["hp"], stats["maxhp"], name=poke_name)
        print(f"  {BOLD}{BRIGHT_YELLOW}💰 -250 coins{RESET}")
        animate_money_earned(-250)
        return money - 250
    elif stat_type.lower() in ["damage", "dm"]:
        fancy_header(f"TRAINING {poke_name.upper()}'s DAMAGE", emoji="💪", width=45)
        countdown(3)
        progress_bar_animated(label="Training DM", total=20, duration=1.5)
        stats["dm"] += 10
        print(f"  {BOLD}{BRIGHT_RED}⬆️  +10 Damage!{RESET}")
        print(f"  {BOLD}{BRIGHT_RED}⚔️  Total DM: {stats['dm']}{RESET}")
        print(f"  {BOLD}{BRIGHT_YELLOW}💰 -250 coins{RESET}")
        animate_money_earned(-250)
        return money - 250

    return money


def display_pokemon_stats(pokemon_dict, player_name, money, trophies):
    """Display all player pokemon stats — MODERN VERSION."""
    clear_screen()
    wipe_transition(width=50)
    fancy_header(f"{player_name}'s POKÉMON TEAM", emoji="📊", width=50)
    print()
    
    if not pokemon_dict:
        print(f"  {BRIGHT_RED}You have no Pokemon yet! Go catch some!{RESET}")
        print()
    else:
        for poke_name, stats in pokemon_dict.items():
            clamp_hp(stats)
            hp_pct = int((stats['hp'] / stats['maxhp']) * 100) if stats['maxhp'] > 0 else 0
            xp_pct = int((stats['xp'] / stats['maxxp']) * 100) if stats['maxxp'] > 0 else 0
            status = stats.get('status', None)
            ability = stats.get('ability', 'None')
            hold = stats.get('hold_item', 'None')
            shiny_tag = f" {BRIGHT_YELLOW}✨SHINY{RESET}" if stats.get('shiny') else ""
            gen_tag = f" {DIM}Gen{stats.get('generation', 0)}{RESET}" if stats.get('generation', 0) > 0 else ""
            status_tag = f" {BRIGHT_RED}[{status}]{RESET}" if status else f" {BRIGHT_GREEN}[OK]{RESET}"
            
            bar_color = BRIGHT_GREEN if hp_pct > 60 else (BRIGHT_YELLOW if hp_pct > 30 else BRIGHT_RED)
            hp_bar = f"{bar_color}{'█' * (hp_pct // 2)}{DIM}{'░' * (50 - hp_pct // 2)}{RESET}"
            xp_bar = f"{BRIGHT_CYAN}{'█' * (xp_pct // 2)}{DIM}{'░' * (50 - xp_pct // 2)}{RESET}"
            
            print(f"  {BOLD}{BRIGHT_WHITE}┌─ {poke_name.upper()}{shiny_tag}{gen_tag}{status_tag}{RESET}")
            print(f"  {BOLD}{BRIGHT_WHITE}│{RESET} {BRIGHT_WHITE}Level: {stats['lvl']}  |  Type: {stats.get('type', '?')}  |  Speed: {stats.get('speed', 50)}{RESET}")
            print(f"  {BOLD}{BRIGHT_WHITE}│{RESET} HP:    {hp_bar} {stats['hp']}/{stats['maxhp']}")
            print(f"  {BOLD}{BRIGHT_WHITE}│{RESET} XP:    {xp_bar} {stats['xp']}/{stats['maxxp']}")
            print(f"  {BOLD}{BRIGHT_WHITE}│{RESET} DM: {stats['dm']}  |  Stages: DM+{stats.get('stages',{}).get('dm',0)} SPD+{stats.get('stages',{}).get('speed',0)}")
            print(f"  {BOLD}{BRIGHT_WHITE}│{RESET} {DIM}Ability: {ability} | Item: {hold}{RESET}")
            moves = stats.get('moves', [])
            pp_data = stats.get('pp', {})
            moves_str = " | ".join([f"{m} ({pp_data.get(m, '?')})" for m in moves])
            print(f"  {BOLD}{BRIGHT_WHITE}│{RESET} Moves: {moves_str}")
            print(f"  {BOLD}{BRIGHT_WHITE}└{'─' * 48}{RESET}")
            print()

    print(f"  {BOLD}{BRIGHT_WHITE}💰 Coins: {money}  |  🏆 Trophies: {trophies}{RESET}")
    print()
    crazy_divider(50)


# ============================================================
# POKEMON CREATION HELPER
# ============================================================

def make_pokemon(hp, dm, type_name, moves_list, speed=50, xp=0, lvl=1, maxxp=50, shiny=False, generation=0, name=None, ability=None, hold_item=None):
    """Create a properly-formed pokemon stats dict with all required fields."""
    pp = {}
    for move in moves_list:
        pp[move] = get_max_pp(move)
    if ability is None and name:
        ability = get_ability_for_pokemon(name)
    if ability is None:
        ability = pick_ability_by_type(type_name)
    return {
        "hp": hp, "maxhp": hp, "dm": dm, "speed": speed,
        "xp": xp, "lvl": lvl, "maxxp": maxxp,
        "type": type_name, "moves": list(moves_list),
        "pp": pp, "stages": {"dm": 0, "speed": 0},
        "status": None, "shiny": shiny, "generation": generation,
        "ability": ability, "hold_item": hold_item
    }

# ============================================================
# NEW SYSTEM: Stage Multipliers & Stat Stage Management
# ============================================================

def stage_multiplier(stages, stat_name):
    stage = stages.get(stat_name, 0)
    if stage >= 0:
        return (2 + stage) / 2
    else:
        return 2 / (2 - stage)


def apply_stat_stage(pokemon_stats, stat_name, delta):
    if "stages" not in pokemon_stats:
        pokemon_stats["stages"] = {}
    current = pokemon_stats["stages"].get(stat_name, 0)
    new_stage = max(-6, min(6, current + delta))
    pokemon_stats["stages"][stat_name] = new_stage
    if delta != 0:
        direction = "rose" if delta > 0 else "fell"
        stage_change_flash(pokemon_stats.get("name", "Pokemon"), stat_name, direction, abs(delta))
    return new_stage


def reset_stages(pokemon_stats):
    pokemon_stats["stages"] = {"dm": 0, "speed": 0}


def take_damage(pokemon_stats, amount):
    """Apply damage to a pokemon, clamping HP at 0 so it never goes negative."""
    pokemon_stats["hp"] = max(0, pokemon_stats["hp"] - amount)
    return pokemon_stats["hp"]


def clamp_hp(pokemon_stats):
    """Ensure HP is within valid bounds [0, maxhp]."""
    pokemon_stats["hp"] = max(0, min(pokemon_stats["maxhp"], pokemon_stats["hp"]))


def get_fusion_generation(pokemon_stats):
    """Get the fusion generation of a pokemon (0 = base/natural)."""
    return pokemon_stats.get("generation", 0)


# ============================================================
# PP System
# ============================================================

def get_max_pp(move_name):
    move = MOVES.get(move_name, {"pp": 15})
    return int(move.get("pp", 15) * 1.6)


def has_pp(pokemon_stats, move_name):
    pp_data = pokemon_stats.get("pp", {})
    current = pp_data.get(move_name, 0)
    return current > 0


def use_pp(pokemon_stats, move_name):
    pp_data = pokemon_stats.get("pp", {})
    current = pp_data.get(move_name, 0)
    if current <= 0:
        return False
    pp_data[move_name] = current - 1
    pokemon_stats["pp"] = pp_data
    return True


def restore_move_pp(pokemon_stats, move_name, amount=None):
    max_pp = get_max_pp(move_name)
    pp_data = pokemon_stats.get("pp", {})
    current = pp_data.get(move_name, 0)
    if amount is None:
        pp_data[move_name] = max_pp
    else:
        pp_data[move_name] = min(max_pp, current + amount)
    pokemon_stats["pp"] = pp_data


def restore_all_pp(pokemon_stats):
    pp_data = {}
    for move_name in pokemon_stats.get("moves", []):
        pp_data[move_name] = get_max_pp(move_name)
    pokemon_stats["pp"] = pp_data


def struggle_damage(pokemon_stats):
    return max(1, pokemon_stats["maxhp"] // 4)


# ============================================================
# Learning Moves
# ============================================================

def offer_to_learn_move(pokemon_stats, new_move_name):
    """Offer a move and return True only if the pokemon learned it."""
    move = MOVES.get(new_move_name, {"type": "Normal", "power": 0, "pp": 15})
    print()
    fancy_header("NEW MOVE!", emoji="⭐", width=40)
    print(f"  {BOLD}{BRIGHT_CYAN}Your pokemon can learn {BRIGHT_YELLOW}{new_move_name}{BRIGHT_CYAN}!{RESET}")
    print(f"  {DIM}Type: {move['type']} | Power: {move['power']} | PP: {get_max_pp(new_move_name)}{RESET}")
    print()

    current_moves = pokemon_stats.get("moves", [])
    if len(current_moves) < 4:
        current_moves.append(new_move_name)
        pokemon_stats["moves"] = current_moves
        pptmp = pokemon_stats.get("pp", {})
        pptmp[new_move_name] = get_max_pp(new_move_name)
        pokemon_stats["pp"] = pptmp
        print(f"  {BOLD}{BRIGHT_GREEN}✓ {new_move_name} was learned!{RESET}")
        time.sleep(1)
        return True

    print(f"  {BOLD}{BRIGHT_WHITE}Current moves:{RESET}")
    for i, m in enumerate(current_moves):
        print(f"  {BOLD}{BRIGHT_WHITE}{i+1}.{RESET} {m}")
    print(f"  {BOLD}{BRIGHT_WHITE}{len(current_moves)+1}.{RESET} {RED}Don't learn{RESET}")
    print()

    choice = crazy_int_input("Replace which move")
    if 1 <= choice <= len(current_moves):
        old_move = current_moves[choice - 1]
        current_moves[choice - 1] = new_move_name
        pokemon_stats["moves"] = current_moves
        pptmp = pokemon_stats.get("pp", {})
        if old_move in pptmp:
            del pptmp[old_move]
        pptmp[new_move_name] = get_max_pp(new_move_name)
        pokemon_stats["pp"] = pptmp
        print(f"  {BOLD}{BRIGHT_GREEN}✓ {new_move_name} learned! Forgot {old_move}.{RESET}")
        time.sleep(1)
        return True

    print(f"  {DIM}{new_move_name} was not learned.{RESET}")
    time.sleep(1)
    return False


# ============================================================
# Move Effects Application
# ============================================================

def apply_move_effects(move_name, attacker, defender):
    move = MOVES.get(move_name)
    if not move:
        return ""
    effect = move.get("effect")
    if not effect:
        return ""
    messages = []
    if effect.get("status") and not defender.get("status"):
        if random.random() < effect.get("chance", 1.0):
            defender["status"] = effect["status"]
            messages.append(f"{defender.get('name','Enemy')} was {effect['status']}ed!")
    if effect.get("self"):
        for stat, stages in effect["self"].items():
            apply_stat_stage(attacker, stat, stages)
            direction = "rose" if stages > 0 else "fell"
            messages.append(f"{attacker.get('name','User')}'s {stat} {direction}!")
    if effect.get("target"):
        for stat, stages in effect["target"].items():
            apply_stat_stage(defender, stat, stages)
            direction = "rose" if stages > 0 else "fell"
            messages.append(f"{defender.get('name','Enemy')}'s {stat} {direction}!")
    if effect.get("heal"):
        heal = int(attacker["maxhp"] * effect["heal"])
        attacker["hp"] = min(attacker["maxhp"], attacker["hp"] + heal)
        messages.append(f"{attacker.get('name','User')} restored {heal} HP!")
        healing_flash(attacker.get("name", "User"), heal)
    if effect.get("recoil"):
        recoil = int(attacker["maxhp"] * effect["recoil"])
        take_damage(attacker, recoil)
        messages.append(f"{attacker.get('name','User')} took {recoil} recoil damage!")
        recoil_flash(attacker.get("name", "User"), recoil)
    if effect.get("protect"):
        pass
    return ", ".join(messages)


# ============================================================
# Ability & Held Item Battle Hooks
# ============================================================

def apply_entry_abilities(player_active, enemy_active, weather):
    messages = []
    weather_change = None
    for poke, label in [(player_active, "Your"), (enemy_active, "Foe")]:
        ab = poke.get("ability")
        if not ab: continue
        defender = enemy_active if label == "Your" else player_active
        res = apply_ability_trigger(ab, "on_entry", poke, defender=defender, weather=weather)
        messages.extend(res.get("messages", []))
        if res.get("weather_change"):
            weather_change = res["weather_change"]
            messages.append(f"{ab} changed the weather to {weather_change}!")
    return messages, weather_change

def apply_item_turn_trigger(pokemon):
    messages = []
    item = pokemon.get("hold_item")
    if item:
        res = apply_held_item_trigger(item, "on_turn", pokemon)
        if res.get("heal"):
            messages.append(res["messages"][0] if res["messages"] else "")
        if res.get("consumed"):
            pokemon["hold_item"] = None
    ab = pokemon.get("ability")
    if ab:
        res = apply_ability_trigger(ab, "passive_turn", pokemon)
        messages.extend(res.get("messages", []))
    return messages

def apply_hp_threshold_items(pokemon):
    messages = []
    item = pokemon.get("hold_item")
    if item:
        res = apply_held_item_trigger(item, "on_hp_threshold", pokemon)
        if res.get("heal"):
            messages.extend(res.get("messages", []))
        if res.get("consumed"):
            pokemon["hold_item"] = None
    ab = pokemon.get("ability")
    if ab:
        res = apply_ability_trigger(ab, "passive_turn", pokemon)
        messages.extend(res.get("messages", []))
    return messages

def apply_status_items(pokemon):
    messages = []
    item = pokemon.get("hold_item")
    if item and pokemon.get("status"):
        res = apply_held_item_trigger(item, "on_status", pokemon)
        if res.get("consumed"):
            pokemon["hold_item"] = None
        messages.extend(res.get("messages", []))
    return messages

def apply_ko_ability(pokemon):
    messages = []
    ab = pokemon.get("ability")
    if ab:
        res = apply_ability_trigger(ab, "on_ko", pokemon)
        stages = res.get("stage_changes", {})
        for stat, val in stages.items():
            apply_stat_stage(pokemon, stat, val)
        messages.extend(res.get("messages", []))
    return messages

def apply_contact_abilities(defender, attacker):
    messages = []
    ab = defender.get("ability")
    if ab:
        res = apply_ability_trigger(ab, "on_contact", defender, attacker=attacker)
        messages.extend(res.get("messages", []))
    item = defender.get("hold_item")
    if item:
        res = apply_held_item_trigger(item, "on_contact", defender, attacker=attacker)
        messages.extend(res.get("messages", []))
    if res and res.get("consumed"):
        defender["hold_item"] = None
    return messages

def apply_item_after_attack(attacker, defender, damage_dealt):
    messages = []
    item = attacker.get("hold_item")
    if item:
        res = apply_held_item_trigger(item, "after_attack", attacker, defender=defender)
        heal = int(damage_dealt * 1/8) if item == "Shell Bell" else 0
        if heal:
            attacker["hp"] = min(attacker.get("maxhp", 1), attacker.get("hp", 0) + heal)
            messages.append(f"Shell Bell restored {heal} HP!")
            healing_flash(attacker.get("name", "Pokemon"), heal)
    return messages

# ============================================================
# Enemy AI
# ============================================================

def choose_enemy_action(enemy_stats, ally_stats, enemy_team_available):
    moves = enemy_stats.get("moves", ["Tackle"])
    move_data = []
    status_move = None
    for m in moves:
        data = MOVES.get(m, {"type": "Normal", "power": 40, "category": "Physical", "effect": None})
        eff = get_effectiveness(data["type"], ally_stats.get("type", "Normal"))
        is_status = data.get("category") == "Status" and data.get("effect", {}).get("status")
        move_data.append((m, data, eff, is_status))
        if is_status:
            status_move = m

    if enemy_stats.get("hp", 0) < enemy_stats.get("maxhp", 1) * 0.25 and enemy_team_available:
        if random.random() < 0.4:
            return ("switch", random.choice(enemy_team_available))

    if status_move and not ally_stats.get("status"):
        if random.random() < 0.25:
            return ("attack", status_move)

    for m, data, eff, _ in move_data:
        if eff > 1.0 and random.random() < 0.6:
            return ("attack", m)

    attack_moves = [m for m, data, _, _ in move_data if MOVES.get(m, {}).get("power", 0) > 0]
    if not attack_moves:
        attack_moves = moves
    return ("attack", random.choice(attack_moves))


# ============================================================
# Full Team Battle Engine
# ============================================================

def run_team_battle(player_team, enemy_team, weather, battle_context):
    player_won = False
    xp_dict = {}
    money_gained = 0
    if not isinstance(battle_context, dict):
        battle_context = {"mode": str(battle_context)}
    battle_context.setdefault("player_team", player_team)
    battle_context.setdefault("inventory", {})

    py_index = {}
    for name, s in player_team.items():
        if s.get("hp", 0) > 0:
            py_index[name] = s
    ey_index = {}
    for name, s in enemy_team.items():
        if s.get("hp", 0) > 0:
            ey_index[name] = s

    if not py_index or not ey_index:
        return False, {}, 0

    print()
    fancy_header("TEAM BATTLE PREVIEW", emoji="⚔️", width=50)
    print(f"  {BOLD}{BRIGHT_GREEN}Your team:{RESET}")
    for name in py_index:
        s = py_index[name]
        hp_str = f"HP: {s.get('hp',0)}/{s.get('maxhp',1)}"
        print(f"    {pokemon_name_style(name)}  {hp_str}")
    print(f"  {BOLD}{BRIGHT_RED}Enemy team:{RESET}")
    for name in ey_index:
        s = ey_index[name]
        hp_str = f"HP: {s.get('hp',0)}/{s.get('maxhp',1)}"
        print(f"    {enemy_name_style(name)}  {hp_str}")
    print()

    player_active_name = crazy_input("Choose your lead pokemon")
    while player_active_name not in py_index:
        player_active_name = crazy_input("Invalid. Choose your lead pokemon")
    player_active = py_index[player_active_name]
    player_active["name"] = player_active_name

    enemy_active_name = list(ey_index.keys())[0]
    enemy_active = ey_index[enemy_active_name]
    enemy_active["name"] = enemy_active_name

    entry_msgs, weather_change = apply_entry_abilities(player_active, enemy_active, weather)
    if weather_change:
        weather = weather_change
    for m in entry_msgs:
        battle_log.log(m, BRIGHT_CYAN)
    apply_status_items(player_active)
    apply_status_items(enemy_active)

    participants = {player_active_name}
    turn_count = 0
    from collections import Counter

    while True:
        turn_count += 1
        battle_log.next_turn()
        print()
        battle_hud(player_active_name, player_active.get("hp", 0), player_active.get("maxhp", 1), player_active.get("dm", 0),
                   enemy_active_name, enemy_active.get("hp", 0), enemy_active.get("maxhp", 1), enemy_active.get("dm", 0),
                   your_status=player_active.get("status"), enemy_status=enemy_active.get("status"), weather=weather,
                   your_stages=player_active.get("stages"), enemy_stages=enemy_active.get("stages"),
                   turn=turn_count, messages=battle_log.get_recent(),
                   your_ability=player_active.get("ability"), your_item=player_active.get("hold_item"),
                   enemy_ability=enemy_active.get("ability"))

        weather_msg = apply_weather_damage(weather, player_active)
        if weather_msg[0] > 0:
            battle_log.log(weather_msg[1], BRIGHT_YELLOW)
        weather_msg2 = apply_weather_damage(weather, enemy_active)
        if weather_msg2[0] > 0:
            battle_log.log(weather_msg2[1], BRIGHT_YELLOW)

        p_speed = player_active.get("speed", 50) * stage_multiplier(player_active.get("stages", {}), "speed")
        e_speed = enemy_active.get("speed", 50) * stage_multiplier(enemy_active.get("stages", {}), "speed")

        first_name, first_stats, second_name, second_stats = (
            (player_active_name, player_active, enemy_active_name, enemy_active)
            if p_speed >= e_speed
            else (enemy_active_name, enemy_active, player_active_name, player_active)
        )
        is_player_first = (first_name == player_active_name)

        for turn_phase in range(2):
            if turn_phase == 0:
                cur_name, cur_stats, opp_name, opp_stats = first_name, first_stats, second_name, second_stats
                is_player = (cur_name == player_active_name)
            else:
                cur_name, cur_stats, opp_name, opp_stats = second_name, second_stats, first_name, first_stats
                is_player = (cur_name == player_active_name)
                if cur_stats.get("hp", 0) <= 0:
                    continue

            if cur_stats.get("hp", 0) <= 0:
                continue

            can_attack_result = can_attack(cur_stats)
            if not can_attack_result[0]:
                msg = can_attack_result[1]
                battle_log.log(f"{cur_name} {msg}! Can't move!", BRIGHT_RED)
                time.sleep(0.8)
                continue

            if not is_player:
                available = [n for n in ey_index if n != cur_name and ey_index[n].get("hp", 0) > 0]
                action_type, action_target = choose_enemy_action(cur_stats, opp_stats, available)
                if action_type == "switch":
                    old_name = cur_name
                    battle_log.log(f"Enemy switched {cur_name} for {action_target}!", BRIGHT_RED)
                    enemy_active_name = action_target
                    enemy_active = ey_index[action_target]
                    enemy_active["name"] = action_target
                    reset_stages(enemy_active)
                    cur_name = enemy_active_name
                    cur_stats = enemy_active
                    em, wc = apply_entry_abilities(player_active, enemy_active, weather)
                    if wc: weather = wc
                    for m in em:
                        battle_log.log(m, BRIGHT_CYAN)
                    apply_status_items(enemy_active)
                    time.sleep(0.8)
                    continue
                chosen_move = action_target
                battle_log.log(f"Enemy {cur_name} used {chosen_move}!", BRIGHT_RED)

            else:
                print()
                print(f"  {BOLD}{BRIGHT_GREEN}{cur_name}'s turn:{RESET}")
                print(f"  {BOLD}{BRIGHT_WHITE}1.{RESET} {BRIGHT_CYAN}Fight{RESET}")
                print(f"  {BOLD}{BRIGHT_WHITE}2.{RESET} {BRIGHT_MAGENTA}Bag{RESET}")
                print(f"  {BOLD}{BRIGHT_WHITE}3.{RESET} {BRIGHT_YELLOW}Switch{RESET}")
                print(f"  {BOLD}{BRIGHT_MAGENTA}L.{RESET} {DIM}Log{RESET}")
                action = crazy_input("Action")

                if action.lower() == "l":
                    battle_log.show_history()
                    continue
                elif action == "2":
                    from inventory import ITEMS as _
                    item_success, item_result = use_item_menu(battle_context.get("inventory", {}), cur_stats, battle_context.get("player_team"), cur_name)
                    if item_success and item_result is not None:
                        cur_name = item_result
                        cur_stats = battle_context.get("player_team", {}).get(cur_name, cur_stats)
                        player_active = cur_stats
                        player_active_name = cur_name
                        player_active["name"] = cur_name
                    time.sleep(0.5)
                    continue
                elif action == "3":
                    print(f"  {BOLD}{BRIGHT_YELLOW}Switch to which?{RESET}")
                    available = [n for n in py_index if n != cur_name and py_index[n].get("hp", 0) > 0]
                    if not available:
                        print(f"  {BOLD}{BRIGHT_RED}No available pokemon to switch!{RESET}")
                        time.sleep(0.5)
                        continue
                    for i, n in enumerate(available):
                        s = py_index[n]
                        print(f"  {BOLD}{BRIGHT_WHITE}{i+1}.{RESET} {pokemon_name_style(n)}  HP: {s.get('hp',0)}/{s.get('maxhp',1)}")
                    print(f"  {BOLD}{BRIGHT_WHITE}{len(available)+1}.{RESET} {RED}Cancel{RESET}")
                    sw_choice = crazy_int_input("Select")
                    if 1 <= sw_choice <= len(available):
                        old_name = cur_name
                        new_name = available[sw_choice - 1]
                        print(f"  {BRIGHT_GREEN}Come back, {old_name}!{RESET}")
                        reset_stages(cur_stats)
                        player_active_name = new_name
                        player_active = py_index[new_name]
                        player_active["name"] = new_name
                        cur_name = new_name
                        cur_stats = player_active
                        participants.add(new_name)
                        print(f"  {BRIGHT_GREEN}Go, {new_name}!{RESET}")
                        em, wc = apply_entry_abilities(player_active, enemy_active, weather)
                        if wc: weather = wc
                        for m in em:
                            print(f"  {BRIGHT_CYAN}{m}{RESET}")
                        apply_status_items(player_active)
                        time.sleep(0.8)
                    continue
                else:
                    chosen_move = select_move_menu(cur_name, cur_stats)
                    if not chosen_move:
                        continue

            move = MOVES.get(chosen_move, {"type": "Normal", "power": 40, "category": "Physical", "priority": 0})
            if not has_pp(cur_stats, chosen_move):
                battle_log.log(f"No PP left! {cur_name} used Struggle!", BRIGHT_RED)
                sd = struggle_damage(cur_stats)
                final_damage = int(cur_stats["dm"] * 0.25)
                take_damage(opp_stats, final_damage)
                take_damage(cur_stats, sd)
                animate_attack_sequence(cur_name, opp_name, final_damage)
                battle_log.log(f"{opp_name} took {final_damage} damage (Struggle)!", BRIGHT_MAGENTA)
                battle_log.log(f"{cur_name} took {sd} recoil damage!", BRIGHT_RED)
                recoil_flash(cur_name, sd)
            else:
                use_pp(cur_stats, chosen_move)
                is_crit = random.random() < 0.0625
                final_damage, effectiveness = calculate_move_damage(chosen_move, cur_stats, opp_stats.get("type", "Normal"), weather, is_crit)
                eff_msg = ""
                if effectiveness > 1.0:
                    eff_msg = f"  {BRIGHT_GREEN}It's super effective!{RESET}"
                    type_effectiveness_flash(effectiveness)
                elif effectiveness < 1.0 and effectiveness > 0.0:
                    eff_msg = f"  {DIM}It's not very effective...{RESET}"
                    type_effectiveness_flash(effectiveness)
                elif effectiveness == 0.0:
                    eff_msg = f"  {DIM}It doesn't affect {opp_name}...{RESET}"
                    type_effectiveness_flash(effectiveness)

                take_damage(opp_stats, final_damage)
                if is_player:
                    animate_attack_sequence(cur_name, opp_name, final_damage, is_crit)
                else:
                    animate_enemy_attack_sequence(cur_name, opp_name, final_damage)
                if is_crit:
                    battle_log.log("Critical hit!", BRIGHT_YELLOW)
                battle_log.log(f"-{final_damage} HP to {opp_name}!", BRIGHT_RED)
                if eff_msg:
                    print(eff_msg)

                effects_msg = apply_move_effects(chosen_move, cur_stats, opp_stats)
                if effects_msg:
                    battle_log.log(effects_msg, BRIGHT_CYAN)

                item = cur_stats.get("hold_item")
                if item:
                    ir = apply_held_item_trigger(item, "damage_calc", cur_stats, move_type=move.get("type","Normal"))
                    recoil = ir.get("recoil", 0)
                    if recoil > 0:
                        take_damage(cur_stats, recoil)
                        battle_log.log(f"Life Orb: {cur_name} took {recoil} recoil damage!", BRIGHT_RED)
                        recoil_flash(cur_name, recoil)

                if opp_stats.get("hp", 0) > 0:
                    cm = apply_contact_abilities(opp_stats, cur_stats)
                    for m in cm:
                        battle_log.log(m, BRIGHT_MAGENTA)

            time.sleep(0.8)

            if opp_stats.get("hp", 0) <= 0:
                battle_log.log(f"{opp_name} fainted!", BRIGHT_RED)
                km = apply_ko_ability(cur_stats)
                for m in km:
                    battle_log.log(m, BRIGHT_CYAN)
                time.sleep(0.8)

                if is_player and opp_name == enemy_active_name:
                    del ey_index[enemy_active_name]
                    if ey_index:
                        enemy_active_name = list(ey_index.keys())[0]
                        enemy_active = ey_index[enemy_active_name]
                        enemy_active["name"] = enemy_active_name
                        battle_log.log(f"Enemy sent out {enemy_active_name}!", BRIGHT_RED)
                        reset_stages(enemy_active)
                        time.sleep(0.8)
                    else:
                        player_won = True
                        for qid, q in quest_manager.hook_battle_win():
                            battle_log.log(f"Quest #{qid} complete! {q['reward_desc']}!", BRIGHT_YELLOW)
                        break
                elif not is_player and opp_name == player_active_name:
                    del py_index[player_active_name]
                    if py_index:
                        print(f"  {BOLD}{BRIGHT_YELLOW}Choose next pokemon:{RESET}")
                        available = [n for n in py_index if py_index[n].get("hp", 0) > 0]
                        if not available:
                            break
                        for i, n in enumerate(available):
                            s = py_index[n]
                            print(f"  {BOLD}{BRIGHT_WHITE}{i+1}.{RESET} {pokemon_name_style(n)}  HP: {s.get('hp',0)}/{s.get('maxhp',1)}")
                        sw_choice = crazy_int_input("Select")
                        if 1 <= sw_choice <= len(available):
                            new_name = available[sw_choice - 1]
                            player_active_name = new_name
                            player_active = py_index[new_name]
                            player_active["name"] = new_name
                            participants.add(new_name)
                            reset_stages(player_active)
                            battle_log.log(f"Go, {new_name}!", BRIGHT_GREEN)
                            time.sleep(0.8)
                    else:
                        break

        if player_won or not py_index or not ey_index:
            break

        status_dmg, status_msg = apply_status_tick(player_active)
        if status_dmg > 0:
            battle_log.log(f"{player_active_name} {status_msg}", BRIGHT_MAGENTA)
        status_dmg2, status_msg2 = apply_status_tick(enemy_active)
        if status_dmg2 > 0:
            battle_log.log(f"{enemy_active_name} {status_msg2}", BRIGHT_MAGENTA)

        for pn, ps in [(player_active_name, player_active), (enemy_active_name, enemy_active)]:
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

        advance_time(2)

    if player_won:
        print()
        print_art(WIN_ART, rainbow_text)
        victory_celebration(lines=5, width=40)
        all_enemy_hp = sum(s.get("maxhp", 50) for s in enemy_team.values())
        all_enemy_dm = sum(s.get("dm", 20) for s in enemy_team.values())
        for pname in participants:
            if pname in player_team:
                ps = player_team[pname]
                xp_gain = calculate_xp_gain(all_enemy_hp, ps.get("dm", 20), len(enemy_team), all_enemy_dm)
                xp_dict[pname] = xp_gain
                ps["xp"] = ps.get("xp", 0) + xp_gain
                print(f"  {pokemon_name_style(pname)} gained {xp_gain} XP!")
                while ps.get("xp", 0) >= ps.get("maxxp", 50):
                    pname = level_up_pokemon(player_team, pname)
                    ps = player_team[pname]
        money_gained = sum(s.get("lvl", 5) * 15 for s in enemy_team.values())
        print(f"  {BRIGHT_YELLOW}💰 Won {money_gained} coins!{RESET}")
    else:
        print()
        print_art(LOSE_ART, fire_text)
        defeat_rain(lines=5, width=40)
        print(f"  {BOLD}{BRIGHT_RED}All your pokemon fainted...{RESET}")

    return player_won, xp_dict, money_gained


# ============================================================
# FOUNDATION: DAYCARE & BREEDING ENGINE FUNCTIONS
# ============================================================

def calculate_daycare_average_exp(pokemon_stats):
    """Calculate expected average EXP gained per action in Daycare."""
    return pokemon_stats.get("lvl", 1) * 3 + 10


def calculate_breeding_compatibility(p1, p2):
    """
    Calculate breeding compatibility score (0-100%) and return the score
    along with a descriptive textual assessment.
    """
    # Type similarity bonus
    type_bonus = 35 if p1.get("type") == p2.get("type") else 0
    
    # Level synergy bonus (closer levels breed more harmoniously)
    lvl_diff = abs(p1.get("lvl", 1) - p2.get("lvl", 1))
    lvl_bonus = max(0, 25 - lvl_diff)
    
    # Fusion generation match bonus
    gen1 = p1.get("generation", 0)
    gen2 = p2.get("generation", 0)
    gen_bonus = 20 if (gen1 > 0 and gen2 > 0) or (gen1 == 0 and gen2 == 0) else 0
    
    # Hash name chemistry (deterministic pseudo-random chemistry based on names)
    n1 = p1.get("name", "bulbasaur") or ""
    n2 = p2.get("name", "bulbasaur") or ""
    char_sum = sum(ord(c) for c in n1 + n2)
    hash_bonus = char_sum % 21  # 0 to 20
    
    score = min(100, type_bonus + lvl_bonus + gen_bonus + hash_bonus)
    
    if score > 80:
        desc = "They are head over heels in love! (High egg rate! ✨)"
    elif score > 50:
        desc = "They seem to get along nicely! (Normal egg rate)"
    elif score > 25:
        desc = "They are indifferent to each other. (Low egg rate)"
    else:
        desc = "They don't seem to like each other at all... (No eggs will be produced)"
        
    return score, desc


def generate_egg_data(p1_name, p2_name, p1_stats, p2_stats):
    """Generate a waiting egg statistics dictionary based on parent genes."""
    return {
        "name": "Pokémon Egg",
        "is_egg": True,
        "steps_left": 20,
        "hp": 0,
        "maxhp": 0,
        "parent1": p1_name,
        "parent2": p2_name,
        "lvl": 1,
        "species": "egg",
        "shiny": False,
        "is_fusion": False
    }
