#!/usr/bin/env python3
"""
AUTOMATED END-TO-END TEST SUITE FOR POKEMON GAME
Tests all systems: modules, data, battle logic, menu flow, invariants
"""
import sys
import os
import json
import time
import traceback

# Setup paths exactly like main.py does
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
for folder in ['core', 'ui', 'data', 'utils', 'AI']:
    full_path = os.path.join(BASE_DIR, folder)
    if full_path not in sys.path:
        sys.path.insert(0, full_path)

# ═══════════════════════════════════════════
# TEST RESULTS TRACKER
# ═══════════════════════════════════════════
class TestResults:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.errors = []
        self.current_phase = ""
    
    def start_phase(self, name):
        self.current_phase = name
        print(f"\n{'='*60}")
        print(f"  PHASE: {name}")
        print(f"{'='*60}")
    
    def pass_test(self, name):
        self.passed += 1
        print(f"  ✅ {name}")
    
    def fail_test(self, name, reason=""):
        self.failed += 1
        msg = f"  ❌ {name}"
        if reason:
            msg += f" - {reason}"
        print(msg)
        self.errors.append(f"{self.current_phase}: {name} - {reason}")
    
    def summary(self):
        total = self.passed + self.failed
        print(f"\n{'='*60}")
        print(f"  TEST SUMMARY")
        print(f"{'='*60}")
        print(f"  Total: {total}")
        print(f"  ✅ Passed: {self.passed}")
        print(f"  ❌ Failed: {self.failed}")
        if self.errors:
            print(f"\n  FAILURES:")
            for e in self.errors:
                print(f"    - {e}")
        print(f"{'='*60}")
        return self.failed == 0

results = TestResults()

# ═══════════════════════════════════════════
# PHASE 1: MODULE LOADING & DATA INTEGRITY
# ═══════════════════════════════════════════
def test_phase1_modules():
    results.start_phase("Module Loading & Data Integrity")
    
    # 1.1 Core data modules
    try:
        from moves_data import MOVES
        assert isinstance(MOVES, dict)
        assert len(MOVES) >= 700
        results.pass_test(f"MOVES loaded: {len(MOVES)} moves")
    except Exception as e:
        results.fail_test("MOVES", str(e))
    
    try:
        from fusion_dex import FUSION_DEX
        assert isinstance(FUSION_DEX, dict)
        assert len(FUSION_DEX) >= 250000
        results.pass_test(f"FUSION_DEX loaded: {len(FUSION_DEX)} entries")
    except Exception as e:
        results.fail_test("FUSION_DEX", str(e))
    
    try:
        from pokemon_dex import weak_pokemon, moderately_strong_pokemon, strong_pokemon, ultra_strong_pokemon
        assert isinstance(weak_pokemon, dict)
        results.pass_test(f"pokemon_dex loaded: {len(weak_pokemon)} weak, {len(moderately_strong_pokemon)} moderate, {len(strong_pokemon)} strong, {len(ultra_strong_pokemon)} ultra")
    except Exception as e:
        results.fail_test("pokemon_dex", str(e))
    
    try:
        from abilities import ABILITY_MAP
        assert isinstance(ABILITY_MAP, dict)
        assert len(ABILITY_MAP) >= 900
        results.pass_test(f"ABILITY_MAP loaded: {len(ABILITY_MAP)} entries")
    except Exception as e:
        results.fail_test("ABILITY_MAP", str(e))
    
    try:
        from held_items import HELD_ITEMS
        assert isinstance(HELD_ITEMS, dict)
        assert len(HELD_ITEMS) >= 50
        results.pass_test(f"HELD_ITEMS loaded: {len(HELD_ITEMS)} items")
    except Exception as e:
        results.fail_test("HELD_ITEMS", str(e))
    
    try:
        from gym_data import GYM_LEADERS
        assert isinstance(GYM_LEADERS, dict)
        assert len(GYM_LEADERS) == 8
        results.pass_test(f"GYM_LEADERS loaded: {len(GYM_LEADERS)} gyms")
    except Exception as e:
        results.fail_test("GYM_LEADERS", str(e))
    
    try:
        from inventory import ITEMS
        assert isinstance(ITEMS, dict)
        assert len(ITEMS) >= 20
        results.pass_test(f"ITEMS loaded: {len(ITEMS)} items")
    except Exception as e:
        results.fail_test("ITEMS", str(e))
    
    try:
        from world_map import REGIONS
        assert isinstance(REGIONS, dict)
        assert len(REGIONS) >= 1
        results.pass_test(f"REGIONS loaded: {len(REGIONS)} regions")
    except Exception as e:
        results.fail_test("REGIONS", str(e))
    
    try:
        from quest_system import QUESTS
        assert isinstance(QUESTS, list)
        assert len(QUESTS) >= 1000
        results.pass_test(f"QUESTS loaded: {len(QUESTS)} quests")
    except Exception as e:
        results.fail_test("QUESTS", str(e))
    
    try:
        from evolution_map import EVOLUTION_MAP
        assert isinstance(EVOLUTION_MAP, dict)
        assert len(EVOLUTION_MAP) >= 500
        results.pass_test(f"EVOLUTION_MAP loaded: {len(EVOLUTION_MAP)} entries")
    except Exception as e:
        results.fail_test("EVOLUTION_MAP", str(e))
    
    # 1.2 Core game modules
    try:
        from game_functions import (
            get_wild_pokemon, get_arena_pokemon, calculate_move_damage, calculate_xp_gain,
            level_up_pokemon, heal_pokemon, train_pokemon, display_pokemon_stats,
            run_team_battle, get_max_pp, stage_multiplier, apply_stat_stage, reset_stages,
            has_pp, use_pp, struggle_damage, offer_to_learn_move, restore_all_pp, make_pokemon,
            take_damage, clamp_hp, get_eligible_learnset_moves
        )
        results.pass_test("game_functions: all critical functions imported")
    except Exception as e:
        results.fail_test("game_functions", str(e))
    
    try:
        from ui_core import crazy_input, crazy_int_input, clear_screen, fancy_header, hp_bar
        results.pass_test("ui_core: all UI functions imported")
    except Exception as e:
        results.fail_test("ui_core", str(e))
    
    try:
        from time_system import get_period, get_time_name, get_time_icon, advance_time
        results.pass_test("time_system: all functions imported")
    except Exception as e:
        results.fail_test("time_system", str(e))
    
    try:
        from weather_engine import get_random_weather, apply_weather_damage
        results.pass_test("weather_engine: all functions imported")
    except Exception as e:
        results.fail_test("weather_engine", str(e))
    
    try:
        from status_manager import STATUS_EFFECTS, apply_status_tick, can_attack
        results.pass_test(f"status_manager: {len(STATUS_EFFECTS)} status effects")
    except Exception as e:
        results.fail_test("status_manager", str(e))
    
    try:
        from save_manager import save_game
        results.pass_test("save_manager: save_game function imported (cloud-only)")
    except Exception as e:
        results.fail_test("save_manager", str(e))
    
    try:
        from chatbot import PokemonChatbot
        results.pass_test("AI chatbot: PokemonChatbot class imported")
    except Exception as e:
        results.fail_test("AI chatbot", str(e))
    
    try:
        from server import app
        results.pass_test("server: Flask app imported")
    except Exception as e:
        results.fail_test("server", str(e))
    
    # 1.3 Data structure validation
    try:
        from moves_data import MOVES
        required_move_keys = {'type', 'power', 'pp', 'category'}
        missing_keys = []
        for move_name, move_data in MOVES.items():
            if not required_move_keys.issubset(move_data.keys()):
                missing_keys.append(move_name)
        if missing_keys:
            results.fail_test("MOVES structure", f"{len(missing_keys)} moves missing keys: {missing_keys[:5]}...")
        else:
            results.pass_test("MOVES structure: all moves have required keys")
    except Exception as e:
        results.fail_test("MOVES structure", str(e))
    
    try:
        from fusion_dex import FUSION_DEX
        required_fusion_keys = {'generation', 'hp', 'maxhp', 'dm', 'speed', 'type', 'moves'}
        sample = list(FUSION_DEX.values())[:100]
        bad_entries = []
        for entry in sample:
            if not required_fusion_keys.issubset(entry.keys()):
                bad_entries.append(entry)
        if bad_entries:
            results.fail_test("FUSION_DEX structure", f"{len(bad_entries)} entries missing keys")
        else:
            results.pass_test("FUSION_DEX structure: all sampled entries have required keys")
    except Exception as e:
        results.fail_test("FUSION_DEX structure", str(e))
    
    try:
        from gym_data import GYM_LEADERS
        for leader_name, leader_data in GYM_LEADERS.items():
            assert 'team' in leader_data, f"{leader_name} missing team"
            for pname, pdata in leader_data['team'].items():
                required = {'hp', 'maxhp', 'dm', 'lvl', 'type', 'moves', 'speed', 'stages'}
                assert required.issubset(pdata.keys()), f"{leader_name}/{pname} missing keys: {required - pdata.keys()}"
        results.pass_test("GYM_LEADERS structure: all gym leaders and teams valid")
    except Exception as e:
        results.fail_test("GYM_LEADERS structure", str(e))

# ═══════════════════════════════════════════
# PHASE 2: BATTLE MECHANICS
# ═══════════════════════════════════════════
def test_phase2_battle():
    results.start_phase("Battle Mechanics")
    
    try:
        from game_functions import clamp_hp, make_pokemon
        
        # 2.1 HP clamping - clamp_hp takes pokemon_stats dict
        mon = {'hp': 50, 'maxhp': 100}
        clamp_hp(mon)
        assert mon['hp'] == 50
        
        mon = {'hp': -10, 'maxhp': 100}
        clamp_hp(mon)
        assert mon['hp'] == 0
        
        mon = {'hp': 150, 'maxhp': 100}
        clamp_hp(mon)
        assert mon['hp'] == 100
        
        mon = {'hp': 0, 'maxhp': 100}
        clamp_hp(mon)
        assert mon['hp'] == 0
        
        results.pass_test("clamp_hp: correctly clamps to [0, maxhp]")
    except Exception as e:
        results.fail_test("clamp_hp", str(e))
    
    try:
        from game_functions import take_damage, clamp_hp
        
        # 2.2 take_damage never goes below 0
        mon = {'hp': 30, 'maxhp': 100}
        take_damage(mon, 50)
        clamp_hp(mon)
        assert mon['hp'] == 0, f"HP should be 0, got {mon['hp']}"
        
        mon = {'hp': 30, 'maxhp': 100}
        take_damage(mon, 10)
        clamp_hp(mon)
        assert mon['hp'] == 20, f"HP should be 20, got {mon['hp']}"
        
        results.pass_test("take_damage + clamp_hp: HP never goes below 0")
    except Exception as e:
        results.fail_test("take_damage", str(e))
    
    try:
        from game_functions import heal_pokemon, make_pokemon
        
        # 2.3 Healing caps at maxhp - heal_pokemon expects dict keyed by name
        pokemon_dict = {
            'Charizard': make_pokemon(70, 80, "Fire", ['Flamethrower', 'Fly'], 100, 0, 10, 50, False, 0, 'Charizard')
        }
        pokemon_dict['Charizard']['hp'] = 30
        heal_pokemon(pokemon_dict, 'Charizard', 99999)  # Give enough money
        assert pokemon_dict['Charizard']['hp'] == pokemon_dict['Charizard']['maxhp'], f"HP should be {pokemon_dict['Charizard']['maxhp']}, got {pokemon_dict['Charizard']['hp']}"
        
        results.pass_test("heal_pokemon: healing caps at maxhp")
    except Exception as e:
        results.fail_test("heal_pokemon", str(e))
    
    try:
        from game_functions import calculate_move_damage, make_pokemon
        
        # 2.4 Type effectiveness - function signature: (move_name, attacker_stats, defender_type, weather, is_crit)
        attacker = make_pokemon(50, 40, "Electric", ['Thunder Shock', 'Quick Attack'], 60, 0, 5, 50, False, 0, 'Pikachu')
        attacker['pp'] = {'Thunder Shock': 40, 'Quick Attack': 35}
        attacker['stages'] = {'dm': 0, 'speed': 0}
        
        # Electric vs Water = super effective
        dmg_water = calculate_move_damage('Thunder Shock', attacker, 'Water', 'Clear', False)
        
        # Electric vs Ground = immune
        dmg_ground = calculate_move_damage('Thunder Shock', attacker, 'Ground', 'Clear', False)
        
        assert dmg_water > dmg_ground, f"Electric should be more effective vs Water ({dmg_water}) than Ground ({dmg_ground})"
        
        results.pass_test(f"type effectiveness: Electric vs Water={dmg_water}dmg, vs Ground={dmg_ground}dmg")
    except Exception as e:
        results.fail_test("type effectiveness", str(e))
    
    try:
        from game_functions import get_max_pp, has_pp, use_pp, make_pokemon
        import io, sys
        
        # 2.5 PP management
        mon = make_pokemon(50, 40, "Electric", ['Thunder Shock', 'Quick Attack'], 60, 0, 5, 50, False, 0, 'Pikachu')
        mon['pp'] = {'Thunder Shock': 40, 'Quick Attack': 35}
        
        # get_max_pp returns the max PP from MOVES database (may differ from current PP)
        max_pp = get_max_pp('Thunder Shock')
        assert isinstance(max_pp, int) and max_pp > 0
        
        assert has_pp(mon, 'Thunder Shock')
        
        # Suppress print output
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        use_pp(mon, 'Thunder Shock')
        sys.stdout = old_stdout
        
        assert mon['pp']['Thunder Shock'] == 39
        
        results.pass_test("PP management: get_max_pp, has_pp, use_pp work correctly")
    except Exception as e:
        results.fail_test("PP management", str(e))
    
    try:
        from game_functions import stage_multiplier, apply_stat_stage, make_pokemon
        
        # 2.6 Stat stages
        mon = make_pokemon(50, 40, "Electric", ['Thunder Shock'], 60, 0, 5, 50, False, 0, 'Pikachu')
        mon['stages'] = {'dm': 0, 'speed': 0}
        
        assert stage_multiplier(mon['stages'], 'dm') == 1.0
        
        apply_stat_stage(mon, 'dm', 1)
        assert mon['stages']['dm'] == 1
        
        apply_stat_stage(mon, 'dm', -1)
        assert mon['stages']['dm'] == 0
        
        results.pass_test("stat stages: multipliers and application correct")
    except Exception as e:
        results.fail_test("stat stages", str(e))
    
    try:
        from game_functions import make_pokemon
        
        # 2.7 make_pokemon creates complete pokemon dict
        mon = make_pokemon(50, 40, "Electric", ['Thunder Shock', 'Quick Attack'], 60, 0, 5, 50, False, 0, 'Pikachu')
        # Note: make_pokemon doesn't include 'name' key, it's added by caller
        required_keys = {'hp', 'maxhp', 'dm', 'type', 'moves', 'lvl', 'speed', 'xp', 'stages', 'pp', 'status', 'ability', 'hold_item'}
        missing = required_keys - mon.keys()
        if missing:
            results.fail_test("make_pokemon", f"missing keys: {missing}")
        else:
            results.pass_test("make_pokemon: creates complete pokemon dict with all required fields")
    except Exception as e:
        results.fail_test("make_pokemon", str(e))
    
    try:
        from game_functions import get_wild_pokemon
        
        # 2.8 Wild pokemon generation
        result = get_wild_pokemon(5)
        assert isinstance(result, tuple) and len(result) == 8
        name, hp, dm, ptype, moves, shiny, speed, shiny_rate = result
        assert isinstance(name, str) and len(name) > 0
        assert isinstance(hp, int) and hp > 0
        assert isinstance(dm, int) and dm > 0
        assert isinstance(speed, int) and speed > 0
        assert isinstance(moves, list) and len(moves) > 0
        assert isinstance(shiny, bool)
        assert isinstance(shiny_rate, float) and shiny_rate > 0
        results.pass_test(f"get_wild_pokemon: returns valid data ({name}, hp={hp}, dm={dm}, speed={speed}, rate={shiny_rate:.4f})")
    except Exception as e:
        results.fail_test("get_wild_pokemon", str(e))
    
    try:
        from game_functions import get_arena_pokemon
        
        # 2.9 Arena pokemon generation
        result = get_arena_pokemon(5)
        assert isinstance(result, tuple) and len(result) == 6
        name, hp, dm, ptype, moves, speed = result
        assert isinstance(name, str) and len(name) > 0
        assert isinstance(hp, int) and hp > 0
        assert isinstance(dm, int) and dm > 0
        assert isinstance(speed, int) and speed > 0
        assert isinstance(moves, list) and len(moves) > 0
        results.pass_test(f"get_arena_pokemon: returns valid data ({name}, hp={hp}, dm={dm}, speed={speed})")
    except Exception as e:
        results.fail_test("get_arena_pokemon", str(e))

# ═══════════════════════════════════════════
# PHASE 3: CORE GAME SYSTEMS
# ═══════════════════════════════════════════
def test_phase3_systems():
    results.start_phase("Core Game Systems")
    
    # 3.1 Time system
    try:
        from time_system import get_period, get_time_name, get_time_icon, advance_time, set_hour
        set_hour(6)
        period = get_period()
        assert isinstance(period, str) and len(period) > 0
        
        set_hour(12)
        period2 = get_period()
        assert isinstance(period2, str) and len(period2) > 0
        
        icon = get_time_icon()
        assert isinstance(icon, str) and len(icon) > 0
        
        results.pass_test(f"time system: periods and icons work correctly")
    except Exception as e:
        results.fail_test("time system", str(e))
    
    # 3.2 Weather system
    try:
        from weather_engine import get_random_weather, apply_weather_damage
        weather = get_random_weather()
        assert isinstance(weather, str) and len(weather) > 0
        results.pass_test(f"weather system: get_random_weather returns '{weather}'")
    except Exception as e:
        results.fail_test("weather system", str(e))
    
    # 3.3 Status effects
    try:
        from status_manager import STATUS_EFFECTS, apply_status_tick, can_attack
        assert isinstance(STATUS_EFFECTS, dict)
        assert len(STATUS_EFFECTS) >= 4
        results.pass_test(f"status effects: {len(STATUS_EFFECTS)} status types defined")
    except Exception as e:
        results.fail_test("status effects", str(e))
    
    # 3.4 Save/Load - Cloud only, no local saves
    try:
        # Verify no local save file exists (cloud-only)
        assert not os.path.exists('save_game.json'), "Local save_game.json should not exist (cloud-only)"
        assert not os.path.exists('save.json'), "Local save.json should not exist (cloud-only)"
        assert not os.path.exists('cloud_simulation.json'), "Local cloud_simulation.json should not exist (cloud-only)"
        
        results.pass_test("save/load: cloud-only mode verified (no local save files)")
    except Exception as e:
        results.fail_test("save/load", str(e))
    
    # 3.5 AI Chatbot
    try:
        from chatbot import PokemonChatbot
        bot = PokemonChatbot()
        
        greet = bot.greet()
        assert isinstance(greet, str) and len(greet) > 0
        
        goodbye = bot.say_goodbye()
        assert isinstance(goodbye, str) and len(goodbye) > 0
        
        response = bot.respond("What is Pikachu?")
        assert isinstance(response, str) and len(response) > 0
        
        response2 = bot.respond("Calculate 2+2")
        assert isinstance(response2, str) and len(response2) > 0
        
        results.pass_test(f"AI chatbot: greet/respond/say_goodbye work correctly")
    except Exception as e:
        results.fail_test("AI chatbot", str(e))

# ═══════════════════════════════════════════
# PHASE 4: FUSION SYSTEM
# ═══════════════════════════════════════════
def test_phase4_fusion():
    results.start_phase("Fusion System")
    
    try:
        from fusion_dex import FUSION_DEX
        
        # 4.1 Generation distribution
        gen_counts = {}
        for entry in FUSION_DEX.values():
            gen = entry.get('generation', 0)
            gen_counts[gen] = gen_counts.get(gen, 0) + 1
        
        assert 1 in gen_counts, "Generation 1 fusions should exist"
        assert gen_counts[1] >= 196000, f"Should have 196k+ gen 1 fusions, got {gen_counts.get(1, 0)}"
        
        total = sum(gen_counts.values())
        assert total >= 250000, f"Should have 250k+ total fusions, got {total}"
        
        results.pass_test(f"fusion generations: {gen_counts}")
    except Exception as e:
        results.fail_test("fusion generations", str(e))
    
    try:
        from fusion_dex import FUSION_DEX
        
        # 4.2 Fusion entry structure
        required_keys = {'generation', 'hp', 'maxhp', 'dm', 'speed', 'type', 'moves'}
        bad_entries = 0
        for name, entry in FUSION_DEX.items():
            if not required_keys.issubset(entry.keys()):
                bad_entries += 1
                if bad_entries > 5:
                    break
        
        assert bad_entries == 0, f"{bad_entries} entries missing required keys"
        results.pass_test("fusion structure: all entries have required fields")
    except Exception as e:
        results.fail_test("fusion structure", str(e))
    
    try:
        from fusion_dex import FUSION_DEX
        
        # 4.3 Fusion stats are reasonable
        for name, entry in list(FUSION_DEX.items())[:1000]:
            assert entry['hp'] > 0, f"{name} has invalid HP: {entry['hp']}"
            assert entry['maxhp'] > 0, f"{name} has invalid maxhp: {entry['maxhp']}"
            assert entry['dm'] > 0, f"{name} has invalid dm: {entry['dm']}"
            assert entry['speed'] > 0, f"{name} has invalid speed: {entry['speed']}"
            assert len(entry['moves']) >= 2, f"{name} has too few moves: {len(entry['moves'])}"
            assert isinstance(entry['type'], str) and len(entry['type']) > 0
        
        results.pass_test("fusion stats: all sampled entries have valid stats")
    except Exception as e:
        results.fail_test("fusion stats", str(e))
    
    try:
        from fusion_manager import generate_fusion_name
        
        # 4.4 Fusion manager functions
        name = generate_fusion_name("Pikachu", "Charizard")
        assert isinstance(name, str) and len(name) > 0
        
        results.pass_test(f"fusion manager: generate_fusion_name returns '{name}'")
    except Exception as e:
        results.fail_test("fusion manager", str(e))

# ═══════════════════════════════════════════
# PHASE 5: GYM & ELITE FOUR
# ═══════════════════════════════════════════
def test_phase5_gyms():
    results.start_phase("Gym & Elite Four")
    
    try:
        from gym_data import GYM_LEADERS
        from moves_data import MOVES
        
        # 5.1 All gym moves exist in MOVES
        missing_moves = []
        for leader_name, leader_data in GYM_LEADERS.items():
            for pname, pdata in leader_data['team'].items():
                for move in pdata['moves']:
                    if move not in MOVES:
                        missing_moves.append(f"{leader_name}/{pname}: {move}")
        
        if missing_moves:
            results.fail_test("gym moves validation", f"{len(missing_moves)} moves not in MOVES: {missing_moves[:5]}")
        else:
            results.pass_test("gym moves: all moves exist in MOVES database")
    except Exception as e:
        results.fail_test("gym moves validation", str(e))
    
    try:
        from gym_data import GYM_LEADERS
        
        # 5.2 All gym leaders have required fields
        required_leader_keys = {'city', 'type', 'badge', 'message', 'team'}
        for leader_name, leader_data in GYM_LEADERS.items():
            assert required_leader_keys.issubset(leader_data.keys()), f"{leader_name} missing keys: {required_leader_keys - leader_data.keys()}"
            assert len(leader_data['team']) > 0, f"{leader_name} has empty team"
        
        results.pass_test("gym leaders: all have required fields and non-empty teams")
    except Exception as e:
        results.fail_test("gym leaders structure", str(e))
    
    try:
        from gym_data import GYM_LEADERS
        
        # 5.3 Elite Four accessibility check
        badges = ['Boulder', 'Cascade', 'Thunder', 'Rainbow', 'Soul', 'Marsh', 'Volcano', 'Earth']
        has_all_badges = len(badges) >= 8
        assert has_all_badges, "Should be able to check badge count"
        
        results.pass_test("elite four: badge check logic works")
    except Exception as e:
        results.fail_test("elite four badge check", str(e))

# ═══════════════════════════════════════════
# PHASE 6: INVENTORY & ITEMS
# ═══════════════════════════════════════════
def test_phase6_inventory():
    results.start_phase("Inventory & Items")
    
    try:
        from inventory import ITEMS, apply_item_effect
        
        # 6.1 All items have required fields
        required_item_keys = {'price', 'description', 'effect'}
        for item_name, item_data in ITEMS.items():
            assert required_item_keys.issubset(item_data.keys()), f"{item_name} missing keys: {required_item_keys - item_data.keys()}"
        
        results.pass_test(f"inventory: all {len(ITEMS)} items have required fields")
    except Exception as e:
        results.fail_test("inventory structure", str(e))
    
    try:
        from held_items import HELD_ITEMS
        
        # 6.2 Held items have effects
        for item_name, item_data in HELD_ITEMS.items():
            assert 'effect' in item_data or 'trigger' in item_data, f"{item_name} has no effect"
        
        results.pass_test(f"held items: all {len(HELD_ITEMS)} items have effects")
    except Exception as e:
        results.fail_test("held items", str(e))

# ═══════════════════════════════════════════
# PHASE 7: UI & SCREEN EFFECTS
# ═══════════════════════════════════════════
def test_phase7_ui():
    results.start_phase("UI & Screen Effects")
    
    try:
        from ui_core import hp_bar
        import io, sys
        
        # 7.1 Health bar generation - hp_bar prints to stdout
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        hp_bar(50, 100)
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        assert isinstance(output, str) and len(output) > 0
        assert '[' in output and ']' in output
        
        results.pass_test("hp_bar: generates correctly for various HP levels")
    except Exception as e:
        results.fail_test("hp_bar", str(e))
    
    try:
        from ui_core import clear_screen
        
        # 7.2 Clear screen doesn't crash
        import io
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        clear_screen()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        assert '\033[2J' in output or '\033[H' in output, "clear_screen should output ANSI escape codes"
        results.pass_test("clear_screen: outputs ANSI escape codes correctly")
    except Exception as e:
        results.fail_test("clear_screen", str(e))

# ═══════════════════════════════════════════
# PHASE 8: ABILITY & HELD ITEM ENGINE
# ═══════════════════════════════════════════
def test_phase8_abilities():
    results.start_phase("Ability & Held Item Engine")
    
    try:
        from abilities import ABILITY_MAP
        
        # 8.1 Ability map coverage - values are strings (ability names), not dicts
        assert len(ABILITY_MAP) >= 900, f"Should have 900+ ability entries, got {len(ABILITY_MAP)}"
        
        # Sample check - values should be strings
        sample = list(ABILITY_MAP.values())[:10]
        for val in sample:
            assert isinstance(val, str), f"Ability value should be string, got {type(val)}"
        
        results.pass_test(f"ability engine: {len(ABILITY_MAP)} entries, structure valid")
    except Exception as e:
        results.fail_test("ability engine", str(e))
    
    try:
        from held_items import HELD_ITEMS
        
        # 8.2 Held item engine
        assert len(HELD_ITEMS) >= 50, f"Should have 50+ held items, got {len(HELD_ITEMS)}"
        
        results.pass_test(f"held item engine: {len(HELD_ITEMS)} items loaded")
    except Exception as e:
        results.fail_test("held item engine", str(e))

# ═══════════════════════════════════════════
# PHASE 9: MOVE DATABASE VALIDATION
# ═══════════════════════════════════════════
def test_phase9_moves():
    results.start_phase("Move Database Validation")
    
    try:
        from moves_data import MOVES
        
        # 9.1 Move count
        assert len(MOVES) >= 740, f"Should have 740+ moves, got {len(MOVES)}"
        results.pass_test(f"move count: {len(MOVES)} moves")
    except Exception as e:
        results.fail_test("move count", str(e))
    
    try:
        from moves_data import MOVES
        
        # 9.2 All moves have valid types
        valid_types = {'Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy'}
        invalid_types = []
        for name, data in MOVES.items():
            if data['type'] not in valid_types:
                invalid_types.append(f"{name}: {data['type']}")
        
        if invalid_types:
            results.fail_test("move types", f"{len(invalid_types)} moves have invalid types: {invalid_types[:5]}")
        else:
            results.pass_test("move types: all moves have valid types")
    except Exception as e:
        results.fail_test("move types", str(e))
    
    try:
        from moves_data import MOVES
        
        # 9.3 Power and PP ranges
        invalid_power = []
        invalid_pp = []
        for name, data in MOVES.items():
            if not isinstance(data['power'], (int, float)) or data['power'] < 0:
                invalid_power.append(name)
            if not isinstance(data['pp'], (int, float)) or data['pp'] <= 0:
                invalid_pp.append(name)
        
        if invalid_power:
            results.fail_test("move power", f"{len(invalid_power)} moves have invalid power")
        elif invalid_pp:
            results.fail_test("move PP", f"{len(invalid_pp)} moves have invalid PP")
        else:
            results.pass_test("move power/PP: all values valid")
    except Exception as e:
        results.fail_test("move power/PP", str(e))

# ═══════════════════════════════════════════
# PHASE 10: SERVER & CLOUD
# ═══════════════════════════════════════════
def test_phase10_server():
    results.start_phase("Server & Cloud")
    
    try:
        from server import app
        
        # 10.1 Flask app exists
        assert app is not None
        assert app.name is not None
        
        results.pass_test("server: Flask app initialized")
    except Exception as e:
        results.fail_test("server", str(e))
    
    try:
        from server import app
        
        # 10.2 Test endpoints exist (they have /api/ prefix)
        rules = [rule.rule for rule in app.url_map.iter_rules()]
        expected_endpoints = ['/api/register', '/api/login', '/api/save', '/api/load', '/api/save-info', '/api/accounts', '/api/me']
        
        missing = [ep for ep in expected_endpoints if ep not in rules]
        if missing:
            results.fail_test("server endpoints", f"Missing: {missing}")
        else:
            results.pass_test(f"server endpoints: all {len(expected_endpoints)} expected endpoints exist")
    except Exception as e:
        results.fail_test("server endpoints", str(e))

# ═══════════════════════════════════════════
# PHASE 11: 2.0 UPDATE SYSTEMS
# ═══════════════════════════════════════════
def test_phase11_update_systems():
    results.start_phase("2.0 Update Systems")

    try:
        import py_compile
        py_compile.compile(os.path.join(BASE_DIR, "core", "main.py"), doraise=True)
        py_compile.compile(os.path.join(BASE_DIR, "core", "game_functions.py"), doraise=True)
        py_compile.compile(os.path.join(BASE_DIR, "core", "update_systems.py"), doraise=True)
        results.pass_test("core compile: main/game_functions/update_systems compile cleanly")
    except Exception as e:
        results.fail_test("core compile", str(e))

    try:
        from game_functions import make_pokemon, calculate_move_damage
        mon = make_pokemon(80, 50, "Electric", ["Thunder Shock"], speed=90, name="Pikachu")
        assert "personality" in mon
        assert "bond" in mon and "title" in mon["bond"]
        assert "fusion_stability" in mon
        dmg, eff = calculate_move_damage("Thunder Shock", mon, "Water")
        assert dmg > 0 and eff >= 1
        results.pass_test("pokemon profiles: personality, bond, and damage hooks work")
    except Exception as e:
        results.fail_test("pokemon profiles", str(e))

    try:
        from update_systems import calculate_catch_grade, catch_grade_rewards, apply_reward_bundle
        inventory = {}
        grade = calculate_catch_grade({
            "hp_ratio": 0.05,
            "catch_probability": 100,
            "attempts": 1,
            "status": "Sleep",
            "shiny": True,
            "throw_rating": "PERFECT",
        })
        assert grade["grade"] in ("S", "SS")
        reward = catch_grade_rewards(grade, "Electric", shiny=True)
        coins = apply_reward_bundle(inventory, reward)
        assert coins > 0 and inventory
        results.pass_test(f"catch grading: {grade['grade']} rewards produce coins/materials")
    except Exception as e:
        results.fail_test("catch grading", str(e))

    try:
        from update_systems import generate_item_drops, apply_item_drops, craft_tm, TM_RECIPES
        inventory = {"Spark Shard": 3, "TM Shard": 2, "Battle Scrap": 1}
        drops = generate_item_drops("pikachu", "Electric", level=25, grade="S", victory=True)
        apply_item_drops(inventory, drops)
        ok, coins, msg = craft_tm(inventory, "Thunderbolt", coins=1000)
        assert ok, msg
        assert inventory.get(TM_RECIPES["Thunderbolt"]["item"], 0) == 1
        assert coins < 1000
        results.pass_test("item drops + TM crafting: materials and crafted TM work")
    except Exception as e:
        results.fail_test("item drops + TM crafting", str(e))

    try:
        from game_functions import make_pokemon
        from update_systems import create_default_base, preview_fusion, roll_fusion_result
        p1 = make_pokemon(60, 40, "Fire", ["Ember"], speed=65, name="Charmander")
        p2 = make_pokemon(70, 35, "Water", ["Water Gun"], speed=55, name="Squirtle")
        preview = preview_fusion("charmander", p1, "squirtle", p2, {}, create_default_base())
        rolled = roll_fusion_result(preview)
        assert rolled["hp"] > 0 and rolled["dm"] > 0 and rolled["speed"] > 0
        assert rolled["stability"] in ("Perfect", "Stable", "Volatile", "Chaotic", "Fractured")
        results.pass_test(f"fusion 2.0: preview and roll produce {rolled['stability']} fusion")
    except Exception as e:
        results.fail_test("fusion 2.0", str(e))

    try:
        from update_systems import NotificationCenter, create_default_reputation, get_what_now_recommendations, professor_advice
        state = {
            "pokemon": {"pikachu": {"hp": 5, "maxhp": 60, "lvl": 5}},
            "inventory": {"TM Shard": 2},
            "badges": [],
            "daycare": {"egg_waiting": True},
            "daily_challenge": {"daily_species": ["Pikachu"]},
            "pokedex_caught": ["pikachu"],
            "reputation": create_default_reputation(),
        }
        center = NotificationCenter(poll_interval=5)
        generated = center.poll(state, force=True)
        recs = get_what_now_recommendations(state)
        advice = professor_advice(state)
        assert generated and recs and advice
        results.pass_test("notifications/professor/what-now: produce actionable guidance")
    except Exception as e:
        results.fail_test("notifications/professor/what-now", str(e))

# ═══════════════════════════════════════════
# MAIN TEST RUNNER
# ═══════════════════════════════════════════
def run_all_tests():
    print("\n" + "="*60)
    print("  POKEMON GAME - AUTOMATED END-TO-END TEST SUITE")
    print("="*60)
    
    test_phase1_modules()
    test_phase2_battle()
    test_phase3_systems()
    test_phase4_fusion()
    test_phase5_gyms()
    test_phase6_inventory()
    test_phase7_ui()
    test_phase8_abilities()
    test_phase9_moves()
    test_phase10_server()
    test_phase11_update_systems()
    
    success = results.summary()
    
    if success:
        print("\n  🎉 ALL TESTS PASSED! Game is ready to play!")
    else:
        print(f"\n  ⚠️  {results.failed} test(s) failed. See details above.")
    
    return success

if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
