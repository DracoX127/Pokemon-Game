"""
Tactical Move System: Types and Move Data
==========================================
Comprehensive database with ALL official Gen 1-9 moves + custom fusion moves
Consolidated from across the entire codebase into this single source of truth.

Total Moves: 744 moves (450+ official + Z-Moves + G-Max + custom fusion)
Categories: Physical, Special, Status
Types: Normal, Fire, Water, Grass, Electric, Ice, Fighting, Poison, Ground,
       Flying, Psychic, Bug, Rock, Ghost, Dragon, Dark, Steel, Fairy

Move Effect Types:
- status: Inflicts status condition (Burn, Paralyze, Poison, Sleep, Freeze, Confuse, Flinch)
- recoil: User takes percentage of damage dealt as recoil damage
- heal: Restores percentage of user's max HP
- trap: Prevents target from switching for 4-5 turns
- charge: Requires turn to charge before executing
- recharge: User must rest on turn after using
- multi_hit: Hits 2-5 times in one turn
- ohko: One-hit KO move (accuracy-based)
- protect: Blocks incoming attacks
- force_switch: Forces target to switch out
- stat changes: self/target/ally stat modifications
"""

# ═══════════════════════════════════════════════════════════════════
# TYPE CHART - Effectiveness multipliers (Gen 6+)
# ═══════════════════════════════════════════════════════════════════
TYPE_CHART = {
    "Normal": {'Rock': 0.5, 'Ghost': 0.0, 'Steel': 0.5},
    "Fire": {'Fire': 0.5, 'Water': 0.5, 'Grass': 2.0, 'Ice': 2.0, 'Bug': 2.0, 'Rock': 0.5, 'Dragon': 0.5, 'Steel': 2.0},
    "Water": {'Fire': 2.0, 'Water': 0.5, 'Grass': 0.5, 'Ground': 2.0, 'Rock': 2.0, 'Dragon': 0.5},
    "Grass": {'Fire': 0.5, 'Water': 2.0, 'Grass': 0.5, 'Poison': 0.5, 'Ground': 2.0, 'Flying': 0.5, 'Bug': 0.5, 'Rock': 2.0, 'Dragon': 0.5, 'Steel': 0.5},
    "Electric": {'Water': 2.0, 'Grass': 0.5, 'Electric': 0.5, 'Ground': 0.0, 'Flying': 2.0, 'Dragon': 0.5},
    "Ice": {'Fire': 0.5, 'Water': 0.5, 'Grass': 2.0, 'Ice': 0.5, 'Ground': 2.0, 'Flying': 2.0, 'Dragon': 2.0, 'Steel': 0.5},
    "Fighting": {'Normal': 2.0, 'Ice': 2.0, 'Rock': 2.0, 'Dark': 2.0, 'Steel': 2.0, 'Poison': 0.5, 'Flying': 0.5, 'Psychic': 0.5, 'Bug': 0.5, 'Ghost': 0.0, 'Fairy': 0.5},
    "Poison": {'Grass': 2.0, 'Poison': 0.5, 'Ground': 0.5, 'Rock': 0.5, 'Ghost': 0.5, 'Steel': 0.0, 'Fairy': 2.0},
    "Ground": {'Fire': 2.0, 'Electric': 2.0, 'Grass': 0.5, 'Poison': 2.0, 'Flying': 0.0, 'Bug': 0.5, 'Rock': 2.0, 'Steel': 2.0},
    "Flying": {'Grass': 2.0, 'Electric': 0.5, 'Fighting': 2.0, 'Bug': 2.0, 'Rock': 0.5, 'Steel': 0.5},
    "Psychic": {'Fighting': 2.0, 'Poison': 2.0, 'Psychic': 0.5, 'Dark': 0.0, 'Steel': 0.5},
    "Bug": {'Fire': 0.5, 'Grass': 2.0, 'Fighting': 0.5, 'Poison': 0.5, 'Flying': 0.5, 'Psychic': 2.0, 'Ghost': 0.5, 'Dark': 2.0, 'Steel': 0.5, 'Fairy': 0.5},
    "Rock": {'Fire': 2.0, 'Ice': 2.0, 'Fighting': 0.5, 'Ground': 0.5, 'Flying': 2.0, 'Bug': 2.0, 'Steel': 0.5},
    "Ghost": {'Normal': 0.0, 'Psychic': 2.0, 'Ghost': 2.0, 'Dark': 0.5},
    "Dragon": {'Dragon': 2.0, 'Steel': 0.5, 'Fairy': 0.0},
    "Dark": {'Fighting': 0.5, 'Psychic': 2.0, 'Ghost': 2.0, 'Dark': 0.5, 'Fairy': 0.5},
    "Steel": {'Fire': 0.5, 'Water': 0.5, 'Electric': 0.5, 'Ice': 2.0, 'Rock': 2.0, 'Steel': 0.5, 'Fairy': 2.0},
    "Fairy": {'Fire': 0.5, 'Fighting': 2.0, 'Poison': 0.5, 'Dragon': 2.0, 'Dark': 2.0, 'Steel': 0.5},
}

# ═══════════════════════════════════════════════════════════════════
# MOVES DATABASE
# ═══════════════════════════════════════════════════════════════════
MOVES = {

    # ═════════════════════════════════════════════════════════════
    # NORMAL TYPE MOVES
    # Normal-type moves are versatile and have no type advantages or disadvantages.
    # They are effective against no types but are resisted by Rock and Steel,
    # and have no effect on Ghost-type Pokemon.
    # Many Normal moves focus on raw power, stat manipulation, or utility effects.
    # Key strategies: High-power recoil moves, stat boosting, and status infliction.
    # ═════════════════════════════════════════════════════════════

    # Lowers target's Attack and Defense
    "Battle Cry": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status",
        "priority": 0,
        "effect": {'target': {'dm': -1, 'def': -1}},
    },

    # Traps target for 4-5 turns, dealing damage each turn
    "Bind": {
        "type": "Normal",
        "power": 35,
        "acc": 85,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'trap': True},
    },

    # High-power special attack
    "Blood Moon": {
        "type": "Normal",
        "power": 140,
        "acc": 100,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": None,
    },

    # Physical attack with 30% paralysis chance
    "Body Slam": {
        "type": "Normal",
        "power": 85,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Paralyze', 'chance': 0.3},
    },

    # Fusion-powered special attack
    "Core Fusion": {
        "type": "Normal",
        "power": 120,
        "acc": 100,
        "pp": 10,
        "category": "Special",
        "priority": 0,
        "effect": None,
    },

    # Steals target's held item
    "Covet": {
        "type": "Normal",
        "power": 60,
        "acc": 100,
        "pp": 25,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # 50% chance to lower target's Defense
    "Crush Claw": {
        "type": "Normal",
        "power": 75,
        "acc": 95,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'target': {'def': -1}, 'chance': 0.5},
    },

    # Raises user's Defense
    "Defense Curl": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 40,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'def': 1}},
    },

    # 20% chance to confuse target
    "Dizzy Punch": {
        "type": "Normal",
        "power": 70,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Confuse', 'chance': 0.2},
    },

    # Copies target's ability
    "Doodle": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status",
        "priority": 0,
        "effect": {'ability_copy': True},
    },

    # Strikes twice in one turn
    "Double Hit": {
        "type": "Normal",
        "power": 35,
        "acc": 90,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'multi_hit': 2},
    },

    # Very high-power physical attack with 33% recoil
    "Double-Edge": {
        "type": "Normal",
        "power": 120,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'recoil': 0.33},
    },

    # Power increases with each consecutive use
    "Echoed Voice": {
        "type": "Normal",
        "power": 40,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    # High-power physical attack
    "Egg Bomb": {
        "type": "Normal",
        "power": 100,
        "acc": 75,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Reduces target's HP to match user's HP
    "Endeavor": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'level_damage': True},
    },

    # Massive damage, user faints
    "Explosion": {
        "type": "Normal",
        "power": 250,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'recoil': 1.0},
    },

    # Priority +2 physical attack
    "Extreme Speed": {
        "type": "Normal",
        "power": 80,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 2,
        "effect": None,
    },

    # Power doubles if user is statused
    "Facade": {
        "type": "Normal",
        "power": 70,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Priority +3, only works first turn, causes flinch
    "Fake Out": {
        "type": "Normal",
        "power": 40,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 3,
        "effect": {'status': 'Flinch', 'chance': 1.0},
    },

    # Sharply raises Attack, Sp. Atk, Speed; costs 50% HP
    "Fillet Away": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status",
        "priority": 0,
        "effect": {'self': {'dm': 2, 'sp_atk': 2, 'speed': 2}},
    },

    # Power increases as user's HP decreases
    "Flail": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'desperation': True},
    },

    # Power based on low friendship with trainer
    "Frustration": {
        "type": "Normal",
        "power": 102,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Multi-hit physical attack (2-5 hits)
    "Fury Swipes": {
        "type": "Normal",
        "power": 18,
        "acc": 80,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Lowers target's Attack
    "Growl": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 40,
        "category": "Status  ",
        "priority": 0,
        "effect": {'target': {'dm': -1}},
    },

    # Raises Attack and Special Attack
    "Growth": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'dm': 1, 'sp_atk': 1}},
    },

    # Raises user's Defense
    "Harden": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 30,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'def': 1}},
    },

    # High-power attack with 25% recoil
    "Head Charge": {
        "type": "Normal",
        "power": 120,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'recoil': 0.25},
    },

    # Physical attack with 30% flinch chance
    "Headbutt": {
        "type": "Normal",
        "power": 70,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.3},
    },

    # Boosts ally's move power by 50%
    "Helping Hand": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 5,
        "effect": {'ally_boost': True},
    },

    # Type and power vary based on Pokemon's IVs
    "Hidden Power": {
        "type": "Normal",
        "power": 60,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    # Leaves target with at least 1 HP
    "Hold Back": {
        "type": "Normal",
        "power": 40,
        "acc": 100,
        "pp": 40,
        "category": "Physical",
        "priority": 0,
        "effect": {'no_ko': True},
    },

    # One-hit KO move with 30% accuracy
    "Horn Drill": {
        "type": "Normal",
        "power": 120,
        "acc": 30,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Maximum power special attack, requires recharge turn
    "Hyper Beam": {
        "type": "Normal",
        "power": 150,
        "acc": 90,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'recharge': True},
    },

    # Physical attack with 10% flinch chance
    "Hyper Fang": {
        "type": "Normal",
        "power": 80,
        "acc": 90,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.1},
    },

    # Sound-based special attack
    "Hyper Voice": {
        "type": "Normal",
        "power": 90,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    # Type changes based on held Plate
    "Judgment": {
        "type": "Normal",
        "power": 100,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    # Can only be used after all other moves
    "Last Resort": {
        "type": "Normal",
        "power": 140,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Lowers target's Defense
    "Leer": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 30,
        "category": "Status  ",
        "priority": 0,
        "effect": {'target': {'dm': -1}},
    },

    # Max Move: Blocks attacks
    "Max Guard": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status",
        "priority": 4,
        "effect": {'max_protect': True},
    },

    # High-power physical attack
    "Mega Kick": {
        "type": "Normal",
        "power": 120,
        "acc": 75,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Strong physical attack
    "Mega Punch": {
        "type": "Normal",
        "power": 80,
        "acc": 85,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Randomly uses any move in the game
    "Metronome": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'random_move': True},
    },

    # Restores 50% of user's max HP
    "Milk Drink": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'heal': 0.5},
    },

    # Type and power based on held Berry
    "Natural Gift": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Lowers target's Attack and Special Attack
    "Noble Roar": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 30,
        "category": "Status  ",
        "priority": 0,
        "effect": {'target': {'dm': -1, 'sp_atk': -1}},
    },

    # Ultimate move with recharge
    "Omega Destroyer": {
        "type": "Normal",
        "power": 200,
        "acc": 75,
        "pp": 1,
        "category": "Special",
        "priority": 0,
        "effect": {'recharge': True},
    },

    # Averages user and target's HP
    "Pain Split": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'pain_split': True},
    },

    # Scatters coins after battle
    "Pay Day": {
        "type": "Normal",
        "power": 40,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'money': True},
    },

    # Basic physical attack with no additional effects
    "Pound": {
        "type": "Normal",
        "power": 40,
        "acc": 100,
        "pp": 35,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Damages or heals target randomly
    "Present": {
        "type": "Normal",
        "power": 0,
        "acc": 90,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'present': True},
    },

    # Blocks all attacks this turn
    "Protect": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 4,
        "effect": {'protect': True},
    },

    # Priority +1 physical attack
    "Quick Attack": {
        "type": "Normal",
        "power": 40,
        "acc": 100,
        "pp": 30,
        "category": "Physical",
        "priority": 1,
        "effect": None,
    },

    # Attack increases each time user is hit
    "Rage": {
        "type": "Normal",
        "power": 20,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'rage': True},
    },

    # Breaks through barriers
    "Raging Bull": {
        "type": "Normal",
        "power": 90,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Removes hazards and trapping effects
    "Rapid Spin": {
        "type": "Normal",
        "power": 50,
        "acc": 100,
        "pp": 40,
        "category": "Physical",
        "priority": 0,
        "effect": {'remove_hazards': True},
    },

    # Charges turn 1, attacks turn 2
    "Razor Wind": {
        "type": "Normal",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'charge': True},
    },

    # Restores 50% of user's max HP
    "Recover": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'heal': 0.5},
    },

    # Cures user's status condition
    "Refresh": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'cure_status': True},
    },

    "Relic Song": {
        "type": "Normal",
        "power": 75,
        "acc": 100,
        "pp": 10,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Sleep', 'chance': 0.1},
    },

    # Power doubles if ally fainted last turn
    "Retaliate": {
        "type": "Normal",
        "power": 70,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Power based on friendship with trainer
    "Return": {
        "type": "Normal",
        "power": 102,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Power increases as user's HP decreases
    "Reversal": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'desperation': True},
    },

    # Revives fainted Pokemon with 50% HP
    "Revival Blessing": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 1,
        "category": "Status",
        "priority": 0,
        "effect": {'revival_blessing': True},
    },

    # 20% chance to confuse target
    "Rock Climb": {
        "type": "Normal",
        "power": 90,
        "acc": 85,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Confuse', 'chance': 0.2},
    },

    # Power doubles if other Pokemon used it same turn
    "Round": {
        "type": "Normal",
        "power": 60,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    # Prevents status conditions for 5 turns
    "Safeguard": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 25,
        "category": "Status  ",
        "priority": 0,
        "effect": {'safeguard': True},
    },

    # Basic physical attack with no additional effects
    "Scratch": {
        "type": "Normal",
        "power": 40,
        "acc": 100,
        "pp": 35,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Sharply lowers target's Defense
    "Screech": {
        "type": "Normal",
        "power": 0,
        "acc": 85,
        "pp": 40,
        "category": "Status  ",
        "priority": 0,
        "effect": {'target': {'def': -2}},
    },

    # Effect varies based on terrain
    "Secret Power": {
        "type": "Normal",
        "power": 70,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'terrain_effect': True},
    },

    # Massive damage attack, user faints
    "Self-Destruct": {
        "type": "Normal",
        "power": 200,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'recoil': 1.0},
    },

    # Raises user's Attack
    "Sharpen": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 30,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'dm': 1}},
    },

    # Creates substitute, then switches out
    "Shed Tail": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status",
        "priority": 0,
        "effect": {'substitute': 0.5, 'switch_user': True},
    },

    # Sharply raises Attack, Sp. Atk, Speed; lowers Defense, Sp. Def
    "Shell Smash": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'dm': 2, 'sp_atk': 2, 'speed': 2, 'def': -1, 'sp_def': -1}},
    },

    # Charges turn 1, attacks turn 2 with high power
    "Skull Bash": {
        "type": "Normal",
        "power": 130,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'charge': True},
    },

    # Standard physical attack
    "Slam": {
        "type": "Normal",
        "power": 80,
        "acc": 75,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Physical attack with high critical hit ratio
    "Slash": {
        "type": "Normal",
        "power": 70,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Randomly uses a move while asleep
    "Sleep Talk": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'sleep_talk': True},
    },

    # Lowers target's accuracy
    "Smokescreen": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'target': {'acc': -1}},
    },

    # Can only be used while asleep, 30% flinch
    "Snore": {
        "type": "Normal",
        "power": 50,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.3},
    },

    # Restores 50% of user's max HP
    "Soft-Boiled": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'heal': 0.5},
    },

    # Deals fixed 40 damage regardless of stats
    "Sonic Boom": {
        "type": "Normal",
        "power": 40,
        "acc": 90,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    # Releases stored Stockpile power
    "Spit Up": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'stockpile_damage': True},
    },

    # Stores energy to power up Spit Up/Swallow
    "Stockpile": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'stockpile': True},
    },

    # Physical attack with 30% flinch chance
    "Stomp": {
        "type": "Normal",
        "power": 65,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.3},
    },

    # Standard physical attack
    "Strength": {
        "type": "Normal",
        "power": 80,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Lowers target's Attack, heals user
    "Strength Sap": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'strength_sap': True},
    },

    # Used when no PP remains, causes recoil
    "Struggle": {
        "type": "Normal",
        "power": 50,
        "acc": 100,
        "pp": 999,
        "category": "Physical",
        "priority": 0,
        "effect": {'recoil': 0.25},
    },

    # Consumes held Berry
    "Stuff Cheeks": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'eat_berry': True},
    },

    # Creates decoy with 25% of max HP
    "Substitute": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'substitute': 0.25},
    },

    # Cuts target's HP in half
    "Super Fang": {
        "type": "Normal",
        "power": 0,
        "acc": 90,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'half_hp': True},
    },

    # Heals based on Stockpile count
    "Swallow": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'stockpile_heal': True},
    },

    # Lowers target's evasion
    "Sweet Scent": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'target': {'evasion': -1}},
    },

    # Special attack that never misses
    "Swift": {
        "type": "Normal",
        "power": 60,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    # Sharply raises user's Attack by 2 stages
    "Swords Dance": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'dm': 2}},
    },

    # Basic physical attack with no additional effects
    "Tackle": {
        "type": "Normal",
        "power": 40,
        "acc": 100,
        "pp": 35,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Sharply raises Special Attack by 3 stages
    "Tail Glow": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'sp_atk': 3}},
    },

    # Lowers target's Defense
    "Tail Whip": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 30,
        "category": "Status  ",
        "priority": 0,
        "effect": {'target': {'dm': -1}},
    },

    # High-power physical attack with 25% recoil
    "Take Down": {
        "type": "Normal",
        "power": 90,
        "acc": 85,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'recoil': 0.25},
    },

    # Lowers target's Attack and Special Attack
    "Tearful Look": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'target': {'dm': -1, 'sp_atk': -1}},
    },

    "Techno Blast": {
        "type": "Normal",
        "power": 120,
        "acc": 100,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": None,
    },

    # High-power physical attack, user becomes confused after
    "Thrash": {
        "type": "Normal",
        "power": 120,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'confuse_after': True},
    },

    # Lowers target's Attack and Defense
    "Tickle": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'target': {'dm': -1, 'def': -1}},
    },

    # Removes hazards, raises Attack and Speed
    "Tidy Up": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status",
        "priority": 0,
        "effect": {'remove_hazards': True, 'self': {'dm': 1, 'speed': 1}},
    },

    # Copies target's appearance, stats, and moves
    "Transform": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'transform': True},
    },

    # May paralyze, burn, or freeze target
    "Tri Attack": {
        "type": "Normal",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'tri_attack': True},
    },

    # Power increases with fewer PP remaining
    "Trump Card": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'desperation': True},
    },

    # Attacks for 3 turns, prevents sleep
    "Uproar": {
        "type": "Normal",
        "power": 90,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'uproar': True},
    },

    # Type and power change with weather
    "Weather Ball": {
        "type": "Normal",
        "power": 50,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    # Forces target to switch out
    "Whirlwind": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": -6,
        "effect": {'force_switch': True},
    },

    # Traps target for 4-5 turns
    "Wrap": {
        "type": "Normal",
        "power": 15,
        "acc": 85,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'trap': True},
    },

    # Target falls asleep next turn
    "Yawn": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'yawn': True},
    },


    # ═════════════════════════════════════════════════════════════
    # FIRE TYPE MOVES
    # Fire-type moves are super effective against Grass, Ice, Bug, and Steel.
    # They are resisted by Fire, Water, Rock, and Dragon.
    # Fire moves frequently inflict Burn status, which halves physical attack power.
    # Key strategies: Burn infliction, high special attack moves, and sun-boosted attacks.
    # ═════════════════════════════════════════════════════════════

    "Armor Cannon": {
        "type": "Fire",
        "power": 120,
        "acc": 100,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'self': {'def': -1, 'sp_def': -1}},
    },

    "Bitter Blade": {
        "type": "Fire",
        "power": 90,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'heal': 0.5},
    },

    "Blast Burn": {
        "type": "Fire",
        "power": 150,
        "acc": 90,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'recharge': True},
    },

    "Blazing Torque": {
        "type": "Fire",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.3},
    },

    "Blue Flare": {
        "type": "Fire",
        "power": 130,
        "acc": 85,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.2},
    },

    "Burn Up": {
        "type": "Fire",
        "power": 130,
        "acc": 100,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'burn_up': True},
    },

    "Burning Bulwark": {
        "type": "Fire",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status",
        "priority": 4,
        "effect": {'protect': True, 'status': 'Burn', 'chance': 1.0},
    },

    "Ember": {
        "type": "Fire",
        "power": 40,
        "acc": 100,
        "pp": 25,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.1},
    },

    "Eruption": {
        "type": "Fire",
        "power": 150,
        "acc": 100,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'desperation': True},
    },

    "Fire Blast": {
        "type": "Fire",
        "power": 110,
        "acc": 85,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.1},
    },

    "Fire Fang": {
        "type": "Fire",
        "power": 65,
        "acc": 95,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.1},
    },

    "Fire Punch": {
        "type": "Fire",
        "power": 75,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.1},
    },

    "Fire Spin": {
        "type": "Fire",
        "power": 35,
        "acc": 85,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'trap': True},
    },

    "Flame Charge": {
        "type": "Fire",
        "power": 50,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'self': {'speed': 1}},
    },

    "Flame Wheel": {
        "type": "Fire",
        "power": 60,
        "acc": 100,
        "pp": 25,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.1},
    },

    "Flamethrower": {
        "type": "Fire",
        "power": 90,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.1},
    },

    "Flare Blitz": {
        "type": "Fire",
        "power": 120,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'recoil': 0.33, 'status': 'Burn', 'chance': 0.1},
    },

    "Fusion Flare": {
        "type": "Fire",
        "power": 100,
        "acc": 100,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": None,
    },

    "Heat Wave": {
        "type": "Fire",
        "power": 95,
        "acc": 90,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.1},
    },

    "Inferno": {
        "type": "Fire",
        "power": 100,
        "acc": 70,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 1.0},
    },

    "Inferno Cataclysm": {
        "type": "Fire",
        "power": 195,
        "acc": 70,
        "pp": 1,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.8},
    },

    "Lava Plume": {
        "type": "Fire",
        "power": 80,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.3},
    },

    "Magma Storm": {
        "type": "Fire",
        "power": 100,
        "acc": 75,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'trap': True},
    },

    "Magma Surge": {
        "type": "Fire",
        "power": 120,
        "acc": 90,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.3},
    },

    "Mind Blown": {
        "type": "Fire",
        "power": 150,
        "acc": 100,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'recoil': 0.5},
    },

    "Nova Burst": {
        "type": "Fire",
        "power": 150,
        "acc": 85,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'recoil': 0.25},
    },

    "Overheat": {
        "type": "Fire",
        "power": 130,
        "acc": 90,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'self': {'sp_atk': -2}},
    },

    "Pyro Apocalypse": {
        "type": "Fire",
        "power": 160,
        "acc": 85,
        "pp": 3,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.6},
    },

    "Pyro Ball": {
        "type": "Fire",
        "power": 120,
        "acc": 90,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.1},
    },

    "Raging Fury": {
        "type": "Fire",
        "power": 120,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'confuse_after': True},
    },

    "Revelation Dance": {
        "type": "Fire",
        "power": 90,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Sacred Fire": {
        "type": "Fire",
        "power": 100,
        "acc": 95,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.5},
    },

    "Searing Shot": {
        "type": "Fire",
        "power": 80,
        "acc": 100,
        "pp": 15,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.3},
    },

    "Shell Trap": {
        "type": "Fire",
        "power": 150,
        "acc": 100,
        "pp": 5,
        "category": "Special ",
        "priority": -3,
        "effect": {'shell_trap': True},
    },

    "Steam Overload": {
        "type": "Fire",
        "power": 140,
        "acc": 95,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.5},
    },

    "Sunny Day": {
        "type": "Fire",
        "power": 0,
        "acc": 100,
        "pp": 5,
        "category": "Status",
        "priority": 0,
        "effect": {'sunny_day': True},
    },

    "Temper Flare": {
        "type": "Fire",
        "power": 75,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'double_if_failed': True},
    },

    "V-Create": {
        "type": "Fire",
        "power": 180,
        "acc": 95,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'self': {'speed': -1, 'def': -1, 'sp_def': -1}},
    },

    "V-create": {
        "type": "Fire",
        "power": 180,
        "acc": 95,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'self': {'speed': -1, 'def': -1, 'sp_def': -1}},
    },

    "Will-o-Wisp": {
        "type": "Fire",
        "power": 0,
        "acc": 85,
        "pp": 15,
        "category": "Status  ",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 1.0},
    },


    # ═════════════════════════════════════════════════════════════
    # WATER TYPE MOVES
    # Water-type moves are super effective against Fire, Ground, and Rock.
    # They are resisted by Water, Grass, and Dragon.
    # Water moves are among the most reliable in the game with great coverage.
    # Key strategies: Consistent damage, rain-boosted attacks, and speed reduction.
    # ═════════════════════════════════════════════════════════════

    "Abyssal Maelstrom": {
        "type": "Water",
        "power": 155,
        "acc": 80,
        "pp": 3,
        "category": "Special",
        "priority": 0,
        "effect": {'target': {'speed': -1}},
    },

    "Aqua Cutter": {
        "type": "Water",
        "power": 70,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Aqua Jet": {
        "type": "Water",
        "power": 40,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 1,
        "effect": None,
    },

    "Aqua Step": {
        "type": "Water",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'self': {'speed': 1}},
    },

    "Aqua Tail": {
        "type": "Water",
        "power": 90,
        "acc": 90,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Brine": {
        "type": "Water",
        "power": 65,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'double_if_half_hp': True},
    },

    "Bubble": {
        "type": "Water",
        "power": 40,
        "acc": 100,
        "pp": 30,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'speed': -1}, 'chance': 0.1},
    },

    "Bubble Beam": {
        "type": "Water",
        "power": 65,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'speed': -1}, 'chance': 0.1},
    },

    "Chaos Torrent": {
        "type": "Water",
        "power": 165,
        "acc": 85,
        "pp": 1,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Confuse', 'chance': 0.3},
    },

    "Clamp": {
        "type": "Water",
        "power": 35,
        "acc": 85,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'trap': True},
    },

    "Crabhammer": {
        "type": "Water",
        "power": 100,
        "acc": 90,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Dive": {
        "type": "Water",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'charge': True},
    },

    "Flip Turn": {
        "type": "Water",
        "power": 60,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'switch_user': True},
    },

    "Hydro Pump": {
        "type": "Water",
        "power": 110,
        "acc": 80,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Jet Punch": {
        "type": "Water",
        "power": 60,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 1,
        "effect": None,
    },

    "Life Dew": {
        "type": "Water",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status",
        "priority": 0,
        "effect": {'ally_heal': 0.25},
    },

    "Muddy Water": {
        "type": "Water",
        "power": 90,
        "acc": 85,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'acc': -1}, 'chance': 0.3},
    },

    "Octazooka": {
        "type": "Water",
        "power": 65,
        "acc": 85,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'acc': -1}, 'chance': 0.5},
    },

    "Origin Pulse": {
        "type": "Water",
        "power": 110,
        "acc": 85,
        "pp": 10,
        "category": "Special",
        "priority": 0,
        "effect": None,
    },

    "Rain Dance": {
        "type": "Water",
        "power": 0,
        "acc": 100,
        "pp": 5,
        "category": "Status",
        "priority": 0,
        "effect": {'rain_dance': True},
    },

    "Razor Shell": {
        "type": "Water",
        "power": 75,
        "acc": 95,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'target': {'def': -1}, 'chance': 0.5},
    },

    "Scald": {
        "type": "Water",
        "power": 80,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.3},
    },

    "Snipe Shot": {
        "type": "Water",
        "power": 80,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Sparkling Aria": {
        "type": "Water",
        "power": 90,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'cure_burn': True},
    },

    # Does absolutely nothing
    "Splash": {
        "type": "Water",
        "power": 0,
        "acc": 100,
        "pp": 40,
        "category": "Status  ",
        "priority": 0,
        "effect": None,
    },

    "Steam Eruption": {
        "type": "Water",
        "power": 110,
        "acc": 95,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.3},
    },

    "Surf": {
        "type": "Water",
        "power": 90,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Surging Strikes": {
        "type": "Water",
        "power": 25,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'multi_hit': 3},
    },

    "Swamp Entrap": {
        "type": "Water",
        "power": 130,
        "acc": 95,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'trap': True},
    },

    "Tidal Wave": {
        "type": "Water",
        "power": 115,
        "acc": 85,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": None,
    },

    "Water Gun": {
        "type": "Water",
        "power": 40,
        "acc": 100,
        "pp": 25,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Water Pulse": {
        "type": "Water",
        "power": 60,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Confuse', 'chance': 0.2},
    },

    "Water Sport": {
        "type": "Water",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status",
        "priority": 0,
        "effect": {'weaken_fire': True},
    },

    "Waterfall": {
        "type": "Water",
        "power": 80,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.2},
    },

    "Wave Crash": {
        "type": "Water",
        "power": 120,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'recoil': 0.33},
    },

    "Whirlpool": {
        "type": "Water",
        "power": 35,
        "acc": 85,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'trap': True},
    },


    # ═════════════════════════════════════════════════════════════
    # GRASS TYPE MOVES
    # Grass-type moves are super effective against Water, Ground, and Rock.
    # They are resisted by Fire, Grass, Poison, Flying, Bug, Dragon, and Steel.
    # Grass moves excel at healing, status infliction, and leech effects.
    # Key strategies: HP draining, sleep/paralysis powder, and sun synergy.
    # ═════════════════════════════════════════════════════════════

    "Absorb": {
        "type": "Grass",
        "power": 20,
        "acc": 100,
        "pp": 25,
        "category": "Special ",
        "priority": 0,
        "effect": {'heal': 0.5},
    },

    "Chloroflame": {
        "type": "Grass",
        "power": 135,
        "acc": 90,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.3},
    },

    "Energy Ball": {
        "type": "Grass",
        "power": 90,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'sp_def': -1}, 'chance': 0.1},
    },

    "Flower Shield": {
        "type": "Grass",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status",
        "priority": 0,
        "effect": {'ally': {'def': 1}},
    },

    "Flower Trick": {
        "type": "Grass",
        "power": 70,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Frenzy Plant": {
        "type": "Grass",
        "power": 150,
        "acc": 90,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'recharge': True},
    },

    "Giga Drain": {
        "type": "Grass",
        "power": 75,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'heal': 0.5},
    },

    "Grass Knot": {
        "type": "Grass",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": {'weight_based': True},
    },

    "Grav Apple": {
        "type": "Grass",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'target': {'def': -1}},
    },

    "Horn Leech": {
        "type": "Grass",
        "power": 75,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'heal': 0.5},
    },

    "Ivy Cudgel": {
        "type": "Grass",
        "power": 100,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Jungle Healing": {
        "type": "Grass",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status",
        "priority": 0,
        "effect": {'cure_status': True, 'heal': 0.25},
    },

    "Leaf Blade": {
        "type": "Grass",
        "power": 90,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Leaf Storm": {
        "type": "Grass",
        "power": 130,
        "acc": 90,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'self': {'sp_atk': -2}},
    },

    "Leaf Tornado": {
        "type": "Grass",
        "power": 65,
        "acc": 90,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'acc': -1}, 'chance': 0.5},
    },

    "Leafage": {
        "type": "Grass",
        "power": 40,
        "acc": 100,
        "pp": 40,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Leech Seed": {
        "type": "Grass",
        "power": 0,
        "acc": 90,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'leech_seed': True},
    },

    "Magical Leaf": {
        "type": "Grass",
        "power": 60,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Matcha Gotcha": {
        "type": "Grass",
        "power": 80,
        "acc": 90,
        "pp": 15,
        "category": "Special",
        "priority": 0,
        "effect": {'heal': 0.5, 'status': 'Burn', 'chance': 0.1},
    },

    "Mega Drain": {
        "type": "Grass",
        "power": 40,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'heal': 0.5},
    },

    "Nature's Blessing": {
        "type": "Grass",
        "power": 0,
        "acc": 100,
        "pp": 5,
        "category": "Status",
        "priority": 0,
        "effect": {'heal': 0.5, 'self': {'def': 1}},
    },

    "Needle Arm": {
        "type": "Grass",
        "power": 65,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.3},
    },

    "Petal Blizzard": {
        "type": "Grass",
        "power": 90,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Petal Dance": {
        "type": "Grass",
        "power": 120,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'confuse_after': True},
    },

    "Poison Powder": {
        "type": "Grass",
        "power": 0,
        "acc": 75,
        "pp": 35,
        "category": "Status  ",
        "priority": 0,
        "effect": {'status': 'Poison', 'chance': 1.0},
    },

    "Power Whip": {
        "type": "Grass",
        "power": 120,
        "acc": 85,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Razor Leaf": {
        "type": "Grass",
        "power": 55,
        "acc": 95,
        "pp": 25,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Seed Bomb": {
        "type": "Grass",
        "power": 80,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Sleep Powder": {
        "type": "Grass",
        "power": 0,
        "acc": 75,
        "pp": 15,
        "category": "Status  ",
        "priority": 0,
        "effect": {'status': 'Sleep', 'chance': 1.0},
    },

    "Snap Trap": {
        "type": "Grass",
        "power": 35,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'trap': True},
    },

    "Solar Beam": {
        "type": "Grass",
        "power": 120,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'charge': True},
    },

    "Spiky Shield": {
        "type": "Grass",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status",
        "priority": 4,
        "effect": {'spiky_shield': True},
    },

    "Spore": {
        "type": "Grass",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status  ",
        "priority": 0,
        "effect": {'status': 'Sleep', 'chance': 1.0},
    },

    "Stun Spore": {
        "type": "Grass",
        "power": 0,
        "acc": 75,
        "pp": 30,
        "category": "Status  ",
        "priority": 0,
        "effect": {'status': 'Paralyze', 'chance': 1.0},
    },

    # Restores HP, more in sunny weather
    "Synthesis": {
        "type": "Grass",
        "power": 0,
        "acc": 100,
        "pp": 5,
        "category": "Status  ",
        "priority": 0,
        "effect": {'heal': 0.5},
    },

    "Syrup Bomb": {
        "type": "Grass",
        "power": 60,
        "acc": 85,
        "pp": 10,
        "category": "Special",
        "priority": 0,
        "effect": {'trap': True},
    },

    "Trailblaze": {
        "type": "Grass",
        "power": 50,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'self': {'speed': 1}},
    },

    "Verdant Cataclysm": {
        "type": "Grass",
        "power": 150,
        "acc": 90,
        "pp": 3,
        "category": "Special",
        "priority": 0,
        "effect": {'leech_seed': True},
    },

    "Vine Whip": {
        "type": "Grass",
        "power": 45,
        "acc": 100,
        "pp": 25,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Wood Hammer": {
        "type": "Grass",
        "power": 120,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'recoil': 0.33},
    },

    # Changes target's ability to Insomnia
    "Worry Seed": {
        "type": "Grass",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'ability_swap': True},
    },


    # ═════════════════════════════════════════════════════════════
    # ELECTRIC TYPE MOVES
    # Electric-type moves are super effective against Water and Flying.
    # They have no effect on Ground-type Pokemon.
    # Electric moves are excellent for paralysis infliction and consistent damage.
    # Key strategies: Paralysis chains, rain synergy, and special attack boosting.
    # ═════════════════════════════════════════════════════════════

    "Aura Wheel": {
        "type": "Electric",
        "power": 110,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'self': {'speed': 1}},
    },

    "Bolt Beak": {
        "type": "Electric",
        "power": 85,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'double_if_first': True},
    },

    "Bolt Strike": {
        "type": "Electric",
        "power": 130,
        "acc": 85,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Paralyze', 'chance': 0.2},
    },

    "Charge Beam": {
        "type": "Electric",
        "power": 50,
        "acc": 90,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'self': {'sp_atk': 1}, 'chance': 0.7},
    },

    "Discharge": {
        "type": "Electric",
        "power": 80,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Paralyze', 'chance': 0.3},
    },

    "Double Shock": {
        "type": "Electric",
        "power": 120,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'burn_up': True},
    },

    "Eerie Impulse": {
        "type": "Electric",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status",
        "priority": 0,
        "effect": {'target': {'sp_atk': -2}},
    },

    "Electrify": {
        "type": "Electric",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status",
        "priority": 0,
        "effect": {'electrify': True},
    },

    "Electro Ball": {
        "type": "Electric",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'speed_based': True},
    },

    "Electro Drift": {
        "type": "Electric",
        "power": 100,
        "acc": 100,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'super_effective_boost': True},
    },

    "Electro Shot": {
        "type": "Electric",
        "power": 130,
        "acc": 100,
        "pp": 10,
        "category": "Special",
        "priority": 0,
        "effect": {'charge': True},
    },

    "Electroweb": {
        "type": "Electric",
        "power": 55,
        "acc": 95,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'speed': -1}},
    },

    "Energize": {
        "type": "Electric",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status",
        "priority": 0,
        "effect": {'self': {'sp_atk': 2, 'speed': 1}},
    },

    "Fusion Bolt": {
        "type": "Electric",
        "power": 100,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Hydro-Shock": {
        "type": "Electric",
        "power": 140,
        "acc": 95,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Paralyze', 'chance': 0.5},
    },

    "Lightning Rod": {
        "type": "Electric",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'sp_atk': 3}},
    },

    "Nuzzle": {
        "type": "Electric",
        "power": 20,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Paralyze', 'chance': 1.0},
    },

    "Parabolic Charge": {
        "type": "Electric",
        "power": 65,
        "acc": 100,
        "pp": 20,
        "category": "Special",
        "priority": 0,
        "effect": {'heal': 0.5},
    },

    "Plasma Bolt": {
        "type": "Electric",
        "power": 140,
        "acc": 95,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.2},
    },

    "Plasma Fists": {
        "type": "Electric",
        "power": 100,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Rising Voltage": {
        "type": "Electric",
        "power": 70,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": {'double_on_terrain': True},
    },

    "Shock Wave": {
        "type": "Electric",
        "power": 60,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Spark": {
        "type": "Electric",
        "power": 65,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Paralyze', 'chance': 0.3},
    },

    "Supercell Slam": {
        "type": "Electric",
        "power": 110,
        "acc": 95,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'recoil': 0.33},
    },

    "Thunder": {
        "type": "Electric",
        "power": 110,
        "acc": 70,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Paralyze', 'chance': 0.3},
    },

    "Thunder Fang": {
        "type": "Electric",
        "power": 65,
        "acc": 95,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Paralyze', 'chance': 0.1},
    },

    "Thunder Punch": {
        "type": "Electric",
        "power": 75,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Paralyze', 'chance': 0.1},
    },

    "Thunder Shock": {
        "type": "Electric",
        "power": 40,
        "acc": 100,
        "pp": 30,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Paralyze', 'chance': 0.1},
    },

    "Thunder Storm": {
        "type": "Electric",
        "power": 125,
        "acc": 80,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Paralyze', 'chance': 0.4},
    },

    "Thunder Wave": {
        "type": "Electric",
        "power": 0,
        "acc": 90,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'status': 'Paralyze', 'chance': 1.0},
    },

    "Thunderbolt": {
        "type": "Electric",
        "power": 90,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Paralyze', 'chance': 0.1},
    },

    "Thunderclap": {
        "type": "Electric",
        "power": 70,
        "acc": 100,
        "pp": 5,
        "category": "Special",
        "priority": 1,
        "effect": None,
    },

    "Thunderous Kick": {
        "type": "Electric",
        "power": 90,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'target': {'def': -1}},
    },

    "Volt Annihilation": {
        "type": "Electric",
        "power": 165,
        "acc": 80,
        "pp": 3,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Paralyze', 'chance': 0.7},
    },

    "Volt Switch": {
        "type": "Electric",
        "power": 70,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": {'switch_user': True},
    },

    "Volt Tackle": {
        "type": "Electric",
        "power": 120,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'recoil': 0.33, 'status': 'Paralyze', 'chance': 0.1},
    },

    "Wild Charge": {
        "type": "Electric",
        "power": 90,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'recoil': 0.25},
    },

    "Zap Cannon": {
        "type": "Electric",
        "power": 120,
        "acc": 50,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Paralyze', 'chance': 1.0},
    },

    "Zing Zap": {
        "type": "Electric",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.3},
    },


    # ═════════════════════════════════════════════════════════════
    # ICE TYPE MOVES
    # Ice-type moves are super effective against Grass, Ground, Flying, and Dragon.
    # They are resisted by Fire, Water, Ice, and Steel.
    # Ice moves provide crucial coverage against Dragon-types and can freeze opponents.
    # Key strategies: Dragon slaying, freeze chance, and hail/snow synergy.
    # ═════════════════════════════════════════════════════════════

    "Aurora Beam": {
        "type": "Ice",
        "power": 95,
        "acc": 100,
        "pp": 10,
        "category": "Special",
        "priority": 0,
        "effect": {'target': {'dm': -1}, 'chance': 0.1},
    },

    "Avalanche": {
        "type": "Ice",
        "power": 60,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": -4,
        "effect": {'double_if_hit_first': True},
    },

    "Blizzard": {
        "type": "Ice",
        "power": 110,
        "acc": 70,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Freeze', 'chance': 0.1},
    },

    "Chilly Reception": {
        "type": "Ice",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status",
        "priority": 0,
        "effect": {'snow_weather': True, 'switch_user': True},
    },

    "Crystal Shard": {
        "type": "Ice",
        "power": 110,
        "acc": 95,
        "pp": 10,
        "category": "Special",
        "priority": 0,
        "effect": None,
    },

    "Freeze Shock": {
        "type": "Ice",
        "power": 140,
        "acc": 90,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'charge': True},
    },

    "Freeze-Dry": {
        "type": "Ice",
        "power": 70,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": {'super_vs_water': True},
    },

    "Frost Breath": {
        "type": "Ice",
        "power": 60,
        "acc": 90,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'always_crit': True},
    },

    "Frost Oblivion": {
        "type": "Ice",
        "power": 155,
        "acc": 85,
        "pp": 3,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Freeze', 'chance': 0.4},
    },

    "Glacial Avalanche": {
        "type": "Ice",
        "power": 140,
        "acc": 95,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Freeze', 'chance': 0.2},
    },

    "Glacial Lance": {
        "type": "Ice",
        "power": 130,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Glaciate": {
        "type": "Ice",
        "power": 65,
        "acc": 95,
        "pp": 10,
        "category": "Special",
        "priority": 0,
        "effect": {'target': {'speed': -1}},
    },

    "Hail": {
        "type": "Ice",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status",
        "priority": 0,
        "effect": {'hail': True},
    },

    "Ice Ball": {
        "type": "Ice",
        "power": 30,
        "acc": 90,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'multi_turn': True},
    },

    "Ice Beam": {
        "type": "Ice",
        "power": 90,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Freeze', 'chance': 0.1},
    },

    "Ice Burn": {
        "type": "Ice",
        "power": 140,
        "acc": 90,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'charge': True, 'status': 'Burn', 'chance': 0.3},
    },

    "Ice Fang": {
        "type": "Ice",
        "power": 65,
        "acc": 95,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Freeze', 'chance': 0.1},
    },

    "Ice Punch": {
        "type": "Ice",
        "power": 75,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Freeze', 'chance': 0.1},
    },

    "Ice Shard": {
        "type": "Ice",
        "power": 40,
        "acc": 100,
        "pp": 30,
        "category": "Physical",
        "priority": 1,
        "effect": None,
    },

    "Ice Spinner": {
        "type": "Ice",
        "power": 80,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Icicle Crash": {
        "type": "Ice",
        "power": 85,
        "acc": 90,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.3},
    },

    "Icicle Spear": {
        "type": "Ice",
        "power": 25,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'multi_hit': [2, 5]},
    },

    "Icy Wind": {
        "type": "Ice",
        "power": 55,
        "acc": 95,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'speed': -1}},
    },

    "Powder Snow": {
        "type": "Ice",
        "power": 40,
        "acc": 100,
        "pp": 25,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Freeze', 'chance': 0.1},
    },

    "Sheer Cold": {
        "type": "Ice",
        "power": 0,
        "acc": 30,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'ohko': True},
    },

    "Snowscape": {
        "type": "Ice",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status",
        "priority": 0,
        "effect": {'snow_weather': True},
    },

    "Triple Axel": {
        "type": "Ice",
        "power": 20,
        "acc": 90,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'multi_hit_escalating': 3},
    },


    # ═════════════════════════════════════════════════════════════
    # FIGHTING TYPE MOVES
    # Fighting-type moves are super effective against Normal, Ice, Rock, Dark, and Steel.
    # They have no effect on Ghost-type Pokemon.
    # Fighting moves offer excellent coverage and many have secondary effects.
    # Key strategies: Dark/Steel/Normals coverage, recoil management, and stat boosting.
    # ═════════════════════════════════════════════════════════════

    "Aura Sphere": {
        "type": "Fighting",
        "power": 80,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Body Press": {
        "type": "Fighting",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Brawler's Zenith": {
        "type": "Fighting",
        "power": 160,
        "acc": 90,
        "pp": 3,
        "category": "Physical",
        "priority": 0,
        "effect": {'self': {'dm': 1}},
    },

    "Brick Break": {
        "type": "Fighting",
        "power": 75,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Bulk Up": {
        "type": "Fighting",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'dm': 1, 'def': 1}},
    },

    "Circle Throw": {
        "type": "Fighting",
        "power": 60,
        "acc": 90,
        "pp": 10,
        "category": "Physical",
        "priority": -6,
        "effect": {'force_switch': True},
    },

    "Close Combat": {
        "type": "Fighting",
        "power": 120,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'self': {'def': -1, 'sp_def': -1}},
    },

    "Coaching": {
        "type": "Fighting",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status",
        "priority": 0,
        "effect": {'ally': {'dm': 1, 'def': 1}},
    },

    "Collision Course": {
        "type": "Fighting",
        "power": 100,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'super_effective_boost': True},
    },

    "Cross Chop": {
        "type": "Fighting",
        "power": 100,
        "acc": 80,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Detect": {
        "type": "Fighting",
        "power": 0,
        "acc": 100,
        "pp": 5,
        "category": "Status  ",
        "priority": 4,
        "effect": {'protect': True},
    },

    "Drain Punch": {
        "type": "Fighting",
        "power": 75,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'heal': 0.5},
    },

    "Dynamic Punch": {
        "type": "Fighting",
        "power": 100,
        "acc": 50,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Confuse', 'chance': 1.0},
    },

    "Flying Press": {
        "type": "Fighting",
        "power": 100,
        "acc": 95,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Focus Blast": {
        "type": "Fighting",
        "power": 120,
        "acc": 70,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'sp_def': -1}, 'chance': 0.1},
    },

    "Focus Punch": {
        "type": "Fighting",
        "power": 150,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": -3,
        "effect": {'focus_punch': True},
    },

    "Force Palm": {
        "type": "Fighting",
        "power": 60,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Paralyze', 'chance': 0.3},
    },

    "Hammer Arm": {
        "type": "Fighting",
        "power": 100,
        "acc": 90,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'self': {'speed': -1}},
    },

    "High Jump Kick": {
        "type": "Fighting",
        "power": 130,
        "acc": 90,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'crash_damage': True},
    },

    "Jump Kick": {
        "type": "Fighting",
        "power": 100,
        "acc": 95,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'crash_damage': True},
    },

    "Karate Chop": {
        "type": "Fighting",
        "power": 50,
        "acc": 100,
        "pp": 25,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Low Kick": {
        "type": "Fighting",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'weight_based': True},
    },

    "Low Sweep": {
        "type": "Fighting",
        "power": 65,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'target': {'speed': -1}},
    },

    "Mach Punch": {
        "type": "Fighting",
        "power": 40,
        "acc": 100,
        "pp": 30,
        "category": "Physical",
        "priority": 1,
        "effect": None,
    },

    "Mat Block": {
        "type": "Fighting",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": -5,
        "effect": {'protect_ally': True},
    },

    "Meteor Assault": {
        "type": "Fighting",
        "power": 150,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'recharge': True},
    },

    "No Retreat": {
        "type": "Fighting",
        "power": 0,
        "acc": 100,
        "pp": 5,
        "category": "Status",
        "priority": 0,
        "effect": {'self': {'dm': 1, 'def': 1, 'sp_atk': 1, 'sp_def': 1, 'speed': 1}},
    },

    "Quick Guard": {
        "type": "Fighting",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status  ",
        "priority": 3,
        "effect": {'priority_protect': True},
    },

    "Rage Mode": {
        "type": "Fighting",
        "power": 0,
        "acc": 100,
        "pp": 5,
        "category": "Status",
        "priority": 0,
        "effect": {'self': {'dm': 3, 'sp_atk': 3, 'def': -1, 'sp_def': -1}},
    },

    "Revenge": {
        "type": "Fighting",
        "power": 60,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": -4,
        "effect": {'double_if_hit_first': True},
    },

    "Rock Smash": {
        "type": "Fighting",
        "power": 40,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'target': {'def': -1}, 'chance': 0.5},
    },

    "Rolling Kick": {
        "type": "Fighting",
        "power": 65,
        "acc": 85,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.3},
    },

    "Sacred Sword": {
        "type": "Fighting",
        "power": 90,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Secret Sword": {
        "type": "Fighting",
        "power": 85,
        "acc": 100,
        "pp": 10,
        "category": "Special",
        "priority": 0,
        "effect": None,
    },

    "Seismic Toss": {
        "type": "Fighting",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'level_damage': True},
    },

    "Sky Uppercut": {
        "type": "Fighting",
        "power": 85,
        "acc": 90,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Storm Throw": {
        "type": "Fighting",
        "power": 60,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'always_crit': True},
    },

    "Submission": {
        "type": "Fighting",
        "power": 80,
        "acc": 80,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'recoil': 0.25},
    },

    # High power but lowers user's Attack and Defense
    "Superpower": {
        "type": "Fighting",
        "power": 120,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'self': {'dm': -1, 'def': -1}},
    },

    "Triple Arrows": {
        "type": "Fighting",
        "power": 90,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.5},
    },

    "Upper Hand": {
        "type": "Fighting",
        "power": 65,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 3,
        "effect": None,
    },

    "Vacuum Wave": {
        "type": "Fighting",
        "power": 40,
        "acc": 100,
        "pp": 30,
        "category": "Special ",
        "priority": 1,
        "effect": None,
    },

    "Vital Throw": {
        "type": "Fighting",
        "power": 70,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": -1,
        "effect": None,
    },

    "Wake-Up Slap": {
        "type": "Fighting",
        "power": 70,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'double_if_sleeping': True},
    },

    "Wide Guard": {
        "type": "Fighting",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 3,
        "effect": {'ally_protect': True},
    },

    # Raises Attack and Special Attack
    "Work Up": {
        "type": "Fighting",
        "power": 0,
        "acc": 100,
        "pp": 30,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'dm': 1, 'sp_atk': 1}},
    },


    # ═════════════════════════════════════════════════════════════
    # POISON TYPE MOVES
    # Poison-type moves are super effective against Grass and Fairy.
    # They have no effect on Steel-type Pokemon.
    # Poison moves excel at status infliction and damage over time effects.
    # Key strategies: Toxic chains, Fairy counter, and hazard setting.
    # ═════════════════════════════════════════════════════════════

    "Acid": {
        "type": "Poison",
        "power": 40,
        "acc": 100,
        "pp": 30,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'def': -1}, 'chance': 0.1},
    },

    "Acid Armor": {
        "type": "Poison",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'def': 2}},
    },

    "Acid Spray": {
        "type": "Poison",
        "power": 40,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'sp_def': -2}},
    },

    "Baneful Bunker": {
        "type": "Poison",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 4,
        "effect": {'poison_contact': True},
    },

    "Barb Barrage": {
        "type": "Poison",
        "power": 60,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'double_if_poisoned': True},
    },

    "Clear Smog": {
        "type": "Poison",
        "power": 50,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'reset_stages': True},
    },

    "Corrosive Gas": {
        "type": "Poison",
        "power": 0,
        "acc": 100,
        "pp": 40,
        "category": "Status  ",
        "priority": 0,
        "effect": {'destroy_item': True},
    },

    "Cross Poison": {
        "type": "Poison",
        "power": 70,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Poison', 'chance': 0.1},
    },

    "Dire Claw": {
        "type": "Poison",
        "power": 80,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Poison', 'chance': 0.5},
    },

    "Gunk Shot": {
        "type": "Poison",
        "power": 120,
        "acc": 80,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Poison', 'chance': 0.3},
    },

    "Mortal Spin": {
        "type": "Poison",
        "power": 30,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'remove_hazards': True, 'cure_status': True},
    },

    "Poison Fang": {
        "type": "Poison",
        "power": 50,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Badly Poison', 'chance': 0.5},
    },

    "Poison Gas": {
        "type": "Poison",
        "power": 0,
        "acc": 90,
        "pp": 40,
        "category": "Status  ",
        "priority": 0,
        "effect": {'status': 'Poison', 'chance': 1.0},
    },

    "Poison Jab": {
        "type": "Poison",
        "power": 80,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Poison', 'chance': 0.3},
    },

    "Poison Sting": {
        "type": "Poison",
        "power": 15,
        "acc": 100,
        "pp": 35,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Poison', 'chance': 0.3},
    },

    "Poison Tail": {
        "type": "Poison",
        "power": 50,
        "acc": 100,
        "pp": 25,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Poison', 'chance': 0.1},
    },

    "Purify": {
        "type": "Poison",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'cure_status': True, 'heal': 0.5},
    },

    "Shell Side Arm": {
        "type": "Poison",
        "power": 90,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Poison', 'chance': 0.2},
    },

    "Sludge": {
        "type": "Poison",
        "power": 65,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Poison', 'chance': 0.3},
    },

    "Sludge Bomb": {
        "type": "Poison",
        "power": 90,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Poison', 'chance': 0.3},
    },

    "Sludge Wave": {
        "type": "Poison",
        "power": 95,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Poison', 'chance': 0.1},
    },

    "Smog": {
        "type": "Poison",
        "power": 30,
        "acc": 70,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Poison', 'chance': 0.4},
    },

    "Toxic": {
        "type": "Poison",
        "power": 0,
        "acc": 90,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'status': 'Badly Poison', 'chance': 1.0},
    },

    "Toxic Apocalypse": {
        "type": "Poison",
        "power": 145,
        "acc": 85,
        "pp": 3,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Badly Poison', 'chance': 0.8},
    },

    "Toxic Spikes": {
        "type": "Poison",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'hazard': 'Toxic Spikes'},
    },

    "Toxic Thread": {
        "type": "Poison",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'status': 'Poison', 'chance': 1.0, 'target': {'speed': -1}},
    },

    "Venom Blast": {
        "type": "Poison",
        "power": 120,
        "acc": 90,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Badly Poison', 'chance': 0.5},
    },


    # ═════════════════════════════════════════════════════════════
    # GROUND TYPE MOVES
    # Ground-type moves are super effective against Fire, Electric, Poison, Rock, and Steel.
    # They have no effect on Flying-type Pokemon.
    # Ground moves provide crucial Electric immunity and excellent coverage.
    # Key strategies: Electric counter, hazard setting, and sandstorm synergy.
    # ═════════════════════════════════════════════════════════════

    "Bone Club": {
        "type": "Ground",
        "power": 65,
        "acc": 85,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.1},
    },

    "Bonemerang": {
        "type": "Ground",
        "power": 50,
        "acc": 90,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'multi_hit': 2},
    },

    "Bulldoze": {
        "type": "Ground",
        "power": 60,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'target': {'speed': -1}},
    },

    "Dig": {
        "type": "Ground",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'charge': True},
    },

    "Drill Run": {
        "type": "Ground",
        "power": 80,
        "acc": 95,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Earth Power": {
        "type": "Ground",
        "power": 90,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'sp_def': -1}, 'chance': 0.1},
    },

    "Earthquake": {
        "type": "Ground",
        "power": 100,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Fissure": {
        "type": "Ground",
        "power": 0,
        "acc": 30,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'ohko': True},
    },

    "Gaia's Wrath": {
        "type": "Ground",
        "power": 175,
        "acc": 80,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "High Horsepower": {
        "type": "Ground",
        "power": 95,
        "acc": 95,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Magnitude": {
        "type": "Ground",
        "power": 0,
        "acc": 100,
        "pp": 30,
        "category": "Physical",
        "priority": 0,
        "effect": {'random_power': True},
    },

    "Mud Bomb": {
        "type": "Ground",
        "power": 65,
        "acc": 85,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'acc': -1}, 'chance': 0.3},
    },

    "Mud Shot": {
        "type": "Ground",
        "power": 55,
        "acc": 95,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'speed': -1}},
    },

    # Weakens Electric-type moves
    "Mud Sport": {
        "type": "Ground",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status  ",
        "priority": 0,
        "effect": {'weaken_electric': True},
    },

    "Mud-Slap": {
        "type": "Ground",
        "power": 20,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'acc': -1}},
    },

    "Precipice Blades": {
        "type": "Ground",
        "power": 120,
        "acc": 85,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Raises Attack of all grounded Pokemon
    "Rototiller": {
        "type": "Ground",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'dm': 1}, 'ally': {'dm': 1}},
    },

    "Sand Attack": {
        "type": "Ground",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status  ",
        "priority": 0,
        "effect": {'target': {'acc': -1}},
    },

    "Sand Tomb": {
        "type": "Ground",
        "power": 35,
        "acc": 85,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'trap': True},
    },

    "Sandsear Storm": {
        "type": "Ground",
        "power": 80,
        "acc": 80,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.2},
    },

    "Scorching Sands": {
        "type": "Ground",
        "power": 70,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Burn', 'chance': 0.3},
    },

    "Seismic Rupture": {
        "type": "Ground",
        "power": 155,
        "acc": 90,
        "pp": 3,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Shore Up": {
        "type": "Ground",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'heal': 0.5},
    },

    "Spikes": {
        "type": "Ground",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'hazard': 'Spikes'},
    },

    "Stomping Tantrum": {
        "type": "Ground",
        "power": 75,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'double_if_failed': True},
    },

    "Thousand Arrows": {
        "type": "Ground",
        "power": 90,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Thousand Waves": {
        "type": "Ground",
        "power": 90,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'prevent_switch': True},
    },


    # ═════════════════════════════════════════════════════════════
    # FLYING TYPE MOVES
    # Flying-type moves are super effective against Grass, Fighting, and Bug.
    # They are resisted by Electric, Rock, and Steel.
    # Flying moves often provide immunity to Ground attacks and have good speed synergy.
    # Key strategies: Ground immunity, Fighting counter, and speed-based tactics.
    # ═════════════════════════════════════════════════════════════

    "Acrobatics": {
        "type": "Flying",
        "power": 55,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Aerial Ace": {
        "type": "Flying",
        "power": 60,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Aeroblast": {
        "type": "Flying",
        "power": 100,
        "acc": 95,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": None,
    },

    "Air Cutter": {
        "type": "Flying",
        "power": 60,
        "acc": 95,
        "pp": 25,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Air Slash": {
        "type": "Flying",
        "power": 75,
        "acc": 95,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.3},
    },

    "Bounce": {
        "type": "Flying",
        "power": 85,
        "acc": 85,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'charge': True, 'status': 'Paralyze', 'chance': 0.3},
    },

    "Brave Bird": {
        "type": "Flying",
        "power": 120,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'recoil': 0.33},
    },

    "Chatter": {
        "type": "Flying",
        "power": 75,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Confuse', 'chance': 1.0},
    },

    "Defog": {
        "type": "Flying",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status  ",
        "priority": 0,
        "effect": {'clear_hazards': True},
    },

    "Dragon Ascent": {
        "type": "Flying",
        "power": 120,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'self': {'def': -1, 'sp_def': -1}},
    },

    "Dual Wingbeat": {
        "type": "Flying",
        "power": 40,
        "acc": 90,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'multi_hit': 2},
    },

    "Fly": {
        "type": "Flying",
        "power": 90,
        "acc": 95,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'charge': True},
    },

    "Gust": {
        "type": "Flying",
        "power": 40,
        "acc": 100,
        "pp": 35,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Hurricane": {
        "type": "Flying",
        "power": 110,
        "acc": 70,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Confuse', 'chance': 0.3},
    },

    "Oblivion Wing": {
        "type": "Flying",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Special",
        "priority": 0,
        "effect": {'heal': 0.75},
    },

    "Peck": {
        "type": "Flying",
        "power": 35,
        "acc": 100,
        "pp": 35,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Pluck": {
        "type": "Flying",
        "power": 60,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'eat_berry': True},
    },

    "Roost": {
        "type": "Flying",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'heal': 0.5},
    },

    "Sky Attack": {
        "type": "Flying",
        "power": 140,
        "acc": 90,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'charge': True},
    },

    "Sky Drop": {
        "type": "Flying",
        "power": 60,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'charge': True},
    },

    "Skyfall": {
        "type": "Flying",
        "power": 150,
        "acc": 85,
        "pp": 3,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.3},
    },

    "Tornado Fury": {
        "type": "Flying",
        "power": 130,
        "acc": 85,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Confuse', 'chance': 0.3},
    },

    "Wing Attack": {
        "type": "Flying",
        "power": 60,
        "acc": 100,
        "pp": 35,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },


    # ═════════════════════════════════════════════════════════════
    # PSYCHIC TYPE MOVES
    # Psychic-type moves are super effective against Fighting and Poison.
    # They have no effect on Dark-type Pokemon.
    # Psychic moves excel at stat manipulation, healing, and special damage.
    # Key strategies: Fighting counter, stat boosting, and trick room tactics.
    # ═════════════════════════════════════════════════════════════

    "Agility": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 30,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'speed': 2}},
    },

    "Amnesia": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'sp_def': 2}},
    },

    "Barrier": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'def': 2}},
    },

    "Calm Mind": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'sp_atk': 1, 'sp_def': 1}},
    },

    "Confuse Ray": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'status': 'Confuse', 'chance': 1.0},
    },

    "Confusion": {
        "type": "Psychic",
        "power": 50,
        "acc": 100,
        "pp": 25,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Confuse', 'chance': 0.1},
    },

    "Cosmic Power": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'def': 1, 'sp_def': 1}},
    },

    "Dream Eater": {
        "type": "Psychic",
        "power": 100,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'heal': 0.5, 'sleep_only': True},
    },

    "Expanding Force": {
        "type": "Psychic",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Extrasensory": {
        "type": "Psychic",
        "power": 80,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.1},
    },

    "Future Sight": {
        "type": "Psychic",
        "power": 120,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Guard Split": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'stat_split': True},
    },

    "Heal Pulse": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'ally_heal': 0.5},
    },

    # User faints, next Pokemon fully healed
    "Healing Wish": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'healing_wish': True},
    },

    "Heart Stamp": {
        "type": "Psychic",
        "power": 60,
        "acc": 100,
        "pp": 25,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.3},
    },

    "Hypnosis": {
        "type": "Psychic",
        "power": 0,
        "acc": 60,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'status': 'Sleep', 'chance': 1.0},
    },

    "Imprison": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'imprison': True},
    },

    "Kinesis": {
        "type": "Psychic",
        "power": 0,
        "acc": 80,
        "pp": 15,
        "category": "Status  ",
        "priority": 0,
        "effect": {'target': {'acc': -1}},
    },

    "Lumina Crash": {
        "type": "Psychic",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Special",
        "priority": 0,
        "effect": {'target': {'sp_def': -2}},
    },

    # User faints, next Pokemon fully healed with PP restored
    "Lunar Dance": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'lunar_dance': True},
    },

    "Magic Coat": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status  ",
        "priority": 4,
        "effect": {'magic_coat': True},
    },

    "Magic Room": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'magic_room': True},
    },

    "Mediate": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'dm': 1, 'sp_atk': 1}},
    },

    "Mind Shatter": {
        "type": "Psychic",
        "power": 160,
        "acc": 85,
        "pp": 3,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Confuse', 'chance': 0.5},
    },

    # Copies target's last move
    "Mirror Move": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'mirror_move': True},
    },

    "Photon Geyser": {
        "type": "Psychic",
        "power": 100,
        "acc": 100,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": None,
    },

    "Power Split": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'stat_split': True},
    },

    "Power Swap": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'stat_swap': True},
    },

    "Prismatic Laser": {
        "type": "Psychic",
        "power": 160,
        "acc": 100,
        "pp": 10,
        "category": "Special",
        "priority": 0,
        "effect": {'recharge': True},
    },

    "Psybeam": {
        "type": "Psychic",
        "power": 65,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Confuse', 'chance': 0.1},
    },

    "Psyblade": {
        "type": "Psychic",
        "power": 80,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Psych Up": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'copy_stages': True},
    },

    "Psychic": {
        "type": "Psychic",
        "power": 90,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'sp_def': -1}, 'chance': 0.1},
    },

    "Psychic Noise": {
        "type": "Psychic",
        "power": 75,
        "acc": 100,
        "pp": 10,
        "category": "Special",
        "priority": 0,
        "effect": {'disable_healing': True},
    },

    "Psycho Boost": {
        "type": "Psychic",
        "power": 140,
        "acc": 90,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'self': {'sp_atk': -2}},
    },

    "Psycho Cut": {
        "type": "Psychic",
        "power": 70,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Psycho Shift": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'status_transfer': True},
    },

    "Psyshield Bash": {
        "type": "Psychic",
        "power": 70,
        "acc": 90,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'self': {'def': 1}},
    },

    "Psyshock": {
        "type": "Psychic",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Psywave": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'level_damage': True},
    },

    "Quantum Rift": {
        "type": "Psychic",
        "power": 185,
        "acc": 75,
        "pp": 1,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Confuse', 'chance': 0.5},
    },

    "Reflect": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'reflect': True},
    },

    # Fully heals HP but puts user to sleep for 2 turns
    "Rest": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'rest': True},
    },

    "Role Play": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'ability_copy': True},
    },

    "Skill Swap": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'ability_swap': True},
    },

    "Speed Swap": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'speed_swap': True},
    },

    "Stored Power": {
        "type": "Psychic",
        "power": 20,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'stat_based_power': True},
    },

    "Synchronoise": {
        "type": "Psychic",
        "power": 120,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    # Cures status, raises Special Attack
    "Take Heart": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status",
        "priority": 0,
        "effect": {'cure_status': True, 'self': {'sp_atk': 1}},
    },

    "Telekinesis": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status  ",
        "priority": 0,
        "effect": {'telekinesis': True},
    },

    "Teleport": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": -6,
        "effect": {'switch_user': True},
    },

    "Time Warp": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 5,
        "category": "Status  ",
        "priority": 0,
        "effect": {'trick_room': True},
    },

    "Trick": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'item_swap': True},
    },

    "Trick Room": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 5,
        "category": "Status  ",
        "priority": -7,
        "effect": {'trick_room': True},
    },

    "Twin Beam": {
        "type": "Psychic",
        "power": 40,
        "acc": 100,
        "pp": 10,
        "category": "Special",
        "priority": 0,
        "effect": {'multi_hit': 2},
    },

    "Wonder Room": {
        "type": "Psychic",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'wonder_room': True},
    },

    "Zen Headbutt": {
        "type": "Psychic",
        "power": 80,
        "acc": 90,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.2},
    },


    # ═════════════════════════════════════════════════════════════
    # BUG TYPE MOVES
    # Bug-type moves are super effective against Grass, Psychic, and Dark.
    # They are resisted by Fire, Fighting, Poison, Flying, Ghost, Steel, and Fairy.
    # Bug moves often have multi-hit effects and utility moves.
    # Key strategies: Psychic/Dark counter, quiver dance setup, and U-turn pivoting.
    # ═════════════════════════════════════════════════════════════

    "Attack Order": {
        "type": "Bug",
        "power": 60,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Bug Bite": {
        "type": "Bug",
        "power": 60,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Bug Buzz": {
        "type": "Bug",
        "power": 90,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'sp_def': -1}, 'chance': 0.1},
    },

    "Defend Order": {
        "type": "Bug",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'def': 1, 'sp_def': 1}},
    },

    "First Impression": {
        "type": "Bug",
        "power": 90,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 2,
        "effect": None,
    },

    "Fury Cutter": {
        "type": "Bug",
        "power": 40,
        "acc": 95,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'escalating': True},
    },

    "Heal Order": {
        "type": "Bug",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'heal': 0.5},
    },

    "Infestation": {
        "type": "Bug",
        "power": 20,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": {'trap': True},
    },

    "Leech Life": {
        "type": "Bug",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'heal': 0.5},
    },

    "Lunge": {
        "type": "Bug",
        "power": 80,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'target': {'dm': -1}},
    },

    "Megahorn": {
        "type": "Bug",
        "power": 120,
        "acc": 85,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Pin Missile": {
        "type": "Bug",
        "power": 25,
        "acc": 95,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'multi_hit': [2, 5]},
    },

    "Quiver Dance": {
        "type": "Bug",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'sp_atk': 1, 'sp_def': 1, 'speed': 1}},
    },

    "Rage Powder": {
        "type": "Bug",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status",
        "priority": 2,
        "effect": {'rage_powder': True},
    },

    "Signal Beam": {
        "type": "Bug",
        "power": 75,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Confuse', 'chance': 0.1},
    },

    "Silk Trap": {
        "type": "Bug",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status",
        "priority": 4,
        "effect": {'silk_trap': True},
    },

    "Silver Wind": {
        "type": "Bug",
        "power": 60,
        "acc": 100,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'self': {'dm': 1, 'def': 1, 'speed': 1, 'sp_def': 1, 'acc': 1}, 'chance': 0.1},
    },

    "Skitter Smack": {
        "type": "Bug",
        "power": 70,
        "acc": 90,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'target': {'sp_atk': -1}},
    },

    "Spider Web": {
        "type": "Bug",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'prevent_switch': True},
    },

    "Steamroller": {
        "type": "Bug",
        "power": 65,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.3},
    },

    "String Shot": {
        "type": "Bug",
        "power": 0,
        "acc": 95,
        "pp": 40,
        "category": "Status  ",
        "priority": 0,
        "effect": {'target': {'speed': -1}},
    },

    "Struggle Bug": {
        "type": "Bug",
        "power": 50,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'sp_atk': -1}},
    },

    "Swarm Onslaught": {
        "type": "Bug",
        "power": 145,
        "acc": 90,
        "pp": 3,
        "category": "Physical",
        "priority": 0,
        "effect": {'multi_hit': 3},
    },

    "Tailwind": {
        "type": "Bug",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status  ",
        "priority": 0,
        "effect": {'ally': {'speed': 2}},
    },

    "Twineedle": {
        "type": "Bug",
        "power": 25,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'multi_hit': 2, 'status': 'Poison', 'chance': 0.2},
    },

    "U-turn": {
        "type": "Bug",
        "power": 70,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'switch_user': True},
    },

    "X-Scissor": {
        "type": "Bug",
        "power": 80,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },


    # ═════════════════════════════════════════════════════════════
    # ROCK TYPE MOVES
    # Rock-type moves are super effective against Fire, Ice, Flying, and Bug.
    # They are resisted by Fighting, Ground, and Steel.
    # Rock moves provide excellent coverage and hazard setting capabilities.
    # Key strategies: Flying/Fire/Ice coverage, stealth rock, and sandstorm synergy.
    # ═════════════════════════════════════════════════════════════

    "Accelerock": {
        "type": "Rock",
        "power": 40,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 1,
        "effect": None,
    },

    "Ancient Power": {
        "type": "Rock",
        "power": 60,
        "acc": 100,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'self': {'all_stats': 1}, 'chance': 0.1},
    },

    "Diamond Storm": {
        "type": "Rock",
        "power": 100,
        "acc": 95,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'self': {'def': 2}, 'chance': 0.5},
    },

    "Earth Shatter": {
        "type": "Rock",
        "power": 135,
        "acc": 90,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.4},
    },

    "Head Smash": {
        "type": "Rock",
        "power": 150,
        "acc": 80,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'recoil': 0.5},
    },

    "Meteor Beam": {
        "type": "Rock",
        "power": 120,
        "acc": 90,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'charge': True},
    },

    "Meteor Strike": {
        "type": "Rock",
        "power": 140,
        "acc": 80,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Mighty Cleave": {
        "type": "Rock",
        "power": 95,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'break_protect': True},
    },

    "Power Gem": {
        "type": "Rock",
        "power": 80,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Rock Blast": {
        "type": "Rock",
        "power": 25,
        "acc": 90,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'multi_hit': [2, 5]},
    },

    "Rock Polish": {
        "type": "Rock",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'speed': 2}},
    },

    "Rock Slide": {
        "type": "Rock",
        "power": 75,
        "acc": 90,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.3},
    },

    "Rock Throw": {
        "type": "Rock",
        "power": 50,
        "acc": 90,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Rock Tomb": {
        "type": "Rock",
        "power": 60,
        "acc": 95,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'target': {'speed': -1}},
    },

    "Rock Wrecker": {
        "type": "Rock",
        "power": 150,
        "acc": 90,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'recharge': True},
    },

    "Rollout": {
        "type": "Rock",
        "power": 30,
        "acc": 90,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'multi_turn': True},
    },

    "Salt Cure": {
        "type": "Rock",
        "power": 40,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'salt_cure': True},
    },

    "Sandstorm": {
        "type": "Rock",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status",
        "priority": 0,
        "effect": {'sandstorm': True},
    },

    "Smack Down": {
        "type": "Rock",
        "power": 50,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'ground_flying': True},
    },

    "Stealth Rock": {
        "type": "Rock",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'hazard': 'Stealth Rock'},
    },

    "Stone Edge": {
        "type": "Rock",
        "power": 100,
        "acc": 80,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Tar Shot": {
        "type": "Rock",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status",
        "priority": 0,
        "effect": {'target': {'speed': -1}, 'fire_weak': True},
    },

    "Throw": {
        "type": "Rock",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'force_switch': True},
    },


    # ═════════════════════════════════════════════════════════════
    # GHOST TYPE MOVES
    # Ghost-type moves are super effective against Psychic and Ghost.
    # They have no effect on Normal-type Pokemon.
    # Ghost moves provide immunity to Normal/Fighting and have unique effects.
    # Key strategies: Psychic counter, trapping, and destiny bond tactics.
    # ═════════════════════════════════════════════════════════════

    "Astonish": {
        "type": "Ghost",
        "power": 30,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.3},
    },

    "Astral Barrage": {
        "type": "Ghost",
        "power": 120,
        "acc": 100,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Confide": {
        "type": "Ghost",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'target': {'sp_atk': -1}},
    },

    "Curse": {
        "type": "Ghost",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'curse': True},
    },

    "Destiny Bond": {
        "type": "Ghost",
        "power": 0,
        "acc": 100,
        "pp": 5,
        "category": "Status  ",
        "priority": 0,
        "effect": {'destiny_bond': True},
    },

    "Dimension Slash": {
        "type": "Ghost",
        "power": 170,
        "acc": 80,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": {'break_protect': True},
    },

    "Hex": {
        "type": "Ghost",
        "power": 65,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'double_if_status': True},
    },

    "Last Respects": {
        "type": "Ghost",
        "power": 50,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'escalating': True},
    },

    "Lick": {
        "type": "Ghost",
        "power": 30,
        "acc": 100,
        "pp": 30,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Paralyze', 'chance': 0.3},
    },

    "Moongeist Beam": {
        "type": "Ghost",
        "power": 100,
        "acc": 100,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": None,
    },

    "Night Shade": {
        "type": "Ghost",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'level_damage': True},
    },

    "Ominous Wind": {
        "type": "Ghost",
        "power": 60,
        "acc": 100,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'self': {'all_stats': 1}, 'chance': 0.1},
    },

    "Phantom Force": {
        "type": "Ghost",
        "power": 90,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'charge': True},
    },

    "Poltergeist": {
        "type": "Ghost",
        "power": 110,
        "acc": 90,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Rage Fist": {
        "type": "Ghost",
        "power": 50,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'escalating': True},
    },

    "Shadow Ball": {
        "type": "Ghost",
        "power": 80,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'sp_def': -1}, 'chance': 0.2},
    },

    "Shadow Bone": {
        "type": "Ghost",
        "power": 85,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'target': {'def': -1}, 'chance': 0.2},
    },

    "Shadow Claw": {
        "type": "Ghost",
        "power": 70,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Shadow Force": {
        "type": "Ghost",
        "power": 120,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'charge': True},
    },

    "Shadow Sneak": {
        "type": "Ghost",
        "power": 40,
        "acc": 100,
        "pp": 30,
        "category": "Physical",
        "priority": 1,
        "effect": None,
    },

    "Shadow Strike": {
        "type": "Ghost",
        "power": 80,
        "acc": 95,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'target': {'def': -1}},
    },

    "Shadow Void": {
        "type": "Ghost",
        "power": 145,
        "acc": 95,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Sleep', 'chance': 0.2},
    },

    "Soul Drain": {
        "type": "Ghost",
        "power": 70,
        "acc": 100,
        "pp": 10,
        "category": "Special",
        "priority": 0,
        "effect": {'heal': 0.5},
    },

    "Spectral Nightmare": {
        "type": "Ghost",
        "power": 155,
        "acc": 85,
        "pp": 3,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Sleep', 'chance': 0.3},
    },

    "Spectral Thief": {
        "type": "Ghost",
        "power": 90,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'steal_stages': True},
    },

    "Spirit Shackle": {
        "type": "Ghost",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'prevent_switch': True},
    },

    "Void Pulse": {
        "type": "Ghost",
        "power": 125,
        "acc": 90,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'target': {'sp_def': -1}},
    },


    # ═════════════════════════════════════════════════════════════
    # DRAGON TYPE MOVES
    # Dragon-type moves are super effective against Dragon.
    # They have no effect on Fairy-type Pokemon.
    # Dragon moves are among the most powerful but have limited coverage.
    # Key strategies: Dragon vs Dragon, dragon dance setup, and outrage sweeps.
    # ═════════════════════════════════════════════════════════════

    "Breaking Swipe": {
        "type": "Dragon",
        "power": 60,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'target': {'dm': -1}},
    },

    "Clanging Scales": {
        "type": "Dragon",
        "power": 110,
        "acc": 100,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'self': {'def': -1}},
    },

    "Clangorous Soul": {
        "type": "Dragon",
        "power": 0,
        "acc": 100,
        "pp": 5,
        "category": "Status",
        "priority": 0,
        "effect": {'self': {'all_stats': 1}},
    },

    "Core Enforcer": {
        "type": "Dragon",
        "power": 100,
        "acc": 100,
        "pp": 10,
        "category": "Special",
        "priority": 0,
        "effect": {'suppress_ability': True},
    },

    "Cosmic Rage": {
        "type": "Dragon",
        "power": 150,
        "acc": 90,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'self': {'dm': 1}},
    },

    "Draco Meteor": {
        "type": "Dragon",
        "power": 130,
        "acc": 90,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'self': {'sp_atk': -2}},
    },

    "Dragon Breath": {
        "type": "Dragon",
        "power": 60,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Paralyze', 'chance': 0.3},
    },

    "Dragon Cheer": {
        "type": "Dragon",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status",
        "priority": 0,
        "effect": {'ally': {'dm': 1}, 'crit_boost': True},
    },

    "Dragon Claw": {
        "type": "Dragon",
        "power": 80,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Dragon Dance": {
        "type": "Dragon",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'dm': 1, 'speed': 1}},
    },

    "Dragon Darts": {
        "type": "Dragon",
        "power": 50,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'multi_hit': 2},
    },

    "Dragon Energy": {
        "type": "Dragon",
        "power": 150,
        "acc": 100,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'desperation': True},
    },

    "Dragon Hammer": {
        "type": "Dragon",
        "power": 90,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Dragon Pulse": {
        "type": "Dragon",
        "power": 85,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Dragon Rage": {
        "type": "Dragon",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Special",
        "priority": 0,
        "effect": {'fixed_damage': 40},
    },

    "Dragon Rush": {
        "type": "Dragon",
        "power": 100,
        "acc": 75,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.2},
    },

    "Dragon Tail": {
        "type": "Dragon",
        "power": 60,
        "acc": 90,
        "pp": 10,
        "category": "Physical",
        "priority": -6,
        "effect": {'force_switch': True},
    },

    "Dual Chop": {
        "type": "Dragon",
        "power": 40,
        "acc": 90,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'multi_hit': 2},
    },

    "Dynamax Cannon": {
        "type": "Dragon",
        "power": 100,
        "acc": 100,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'double_vs_dynamax': True},
    },

    "Eternabeam": {
        "type": "Dragon",
        "power": 160,
        "acc": 90,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'recharge': True},
    },

    "Fickle Beam": {
        "type": "Dragon",
        "power": 80,
        "acc": 100,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'fickle_beam': True},
    },

    "Genesis Wave": {
        "type": "Dragon",
        "power": 180,
        "acc": 80,
        "pp": 1,
        "category": "Special",
        "priority": 0,
        "effect": {'self': {'sp_atk': -2}},
    },

    "Glaive Rush": {
        "type": "Dragon",
        "power": 120,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'self': {'def': -1}},
    },

    "Order Up": {
        "type": "Dragon",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Outrage": {
        "type": "Dragon",
        "power": 120,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'confuse_after': True},
    },

    "Roar of Time": {
        "type": "Dragon",
        "power": 150,
        "acc": 90,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'recharge': True},
    },

    "Scale Shot": {
        "type": "Dragon",
        "power": 25,
        "acc": 90,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'multi_hit': [2, 5], 'self': {'speed': 1, 'def': -1}},
    },

    "Spacial Rend": {
        "type": "Dragon",
        "power": 100,
        "acc": 95,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": None,
    },

    "Stellar Annihilation": {
        "type": "Dragon",
        "power": 200,
        "acc": 65,
        "pp": 1,
        "category": "Special",
        "priority": 0,
        "effect": {'recoil': 0.33},
    },

    "Twister": {
        "type": "Dragon",
        "power": 40,
        "acc": 100,
        "pp": 20,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.2},
    },

    "Wyrm's Fury": {
        "type": "Dragon",
        "power": 165,
        "acc": 85,
        "pp": 3,
        "category": "Physical",
        "priority": 0,
        "effect": {'self': {'speed': 1}},
    },


    # ═════════════════════════════════════════════════════════════
    # DARK TYPE MOVES
    # Dark-type moves are super effective against Psychic and Ghost.
    # They are resisted by Fighting, Dark, and Fairy.
    # Dark moves provide immunity to Psychic and have priority options.
    # Key strategies: Psychic counter, priority attacks, and trick/disruption.
    # ═════════════════════════════════════════════════════════════

    "Abyssal Darkness": {
        "type": "Dark",
        "power": 155,
        "acc": 90,
        "pp": 3,
        "category": "Special",
        "priority": 0,
        "effect": {'target': {'sp_def': -2}},
    },

    "Apocalypse Strike": {
        "type": "Dark",
        "power": 190,
        "acc": 70,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": {'recoil': 0.5},
    },

    "Assurance": {
        "type": "Dark",
        "power": 60,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'double_if_hit': True},
    },

    "Baddy Bad": {
        "type": "Dark",
        "power": 80,
        "acc": 95,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Bite": {
        "type": "Dark",
        "power": 60,
        "acc": 100,
        "pp": 25,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.3},
    },

    "Comeuppance": {
        "type": "Dark",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'counter': True},
    },

    "Crunch": {
        "type": "Dark",
        "power": 80,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'target': {'def': -1}, 'chance': 0.2},
    },

    "Dark Pact": {
        "type": "Dark",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status",
        "priority": 0,
        "effect": {'self': {'sp_atk': 3}, 'recoil': 0.25},
    },

    "Dark Pulse": {
        "type": "Dark",
        "power": 80,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.2},
    },

    "Darkest Lariat": {
        "type": "Dark",
        "power": 85,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "False Surrender": {
        "type": "Dark",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Priority +2, breaks Protect and Detect
    "Feint": {
        "type": "Dark",
        "power": 30,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 2,
        "effect": {'break_protect': True},
    },

    "Feint Attack": {
        "type": "Dark",
        "power": 60,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Flatter": {
        "type": "Dark",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status  ",
        "priority": 0,
        "effect": {'target': {'sp_atk': 1}, 'status': 'Confuse', 'chance': 1.0},
    },

    "Foul Play": {
        "type": "Dark",
        "power": 95,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'use_target_attack': True},
    },

    "Hone Claws": {
        "type": "Dark",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'dm': 1, 'acc': 1}},
    },

    "Jaw Lock": {
        "type": "Dark",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'prevent_switch': True},
    },

    "Knock Off": {
        "type": "Dark",
        "power": 65,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'remove_item': True},
    },

    "Kowtow Cleave": {
        "type": "Dark",
        "power": 85,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Lash Out": {
        "type": "Dark",
        "power": 75,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'double_if_stats_lowered': True},
    },

    "Nasty Plot": {
        "type": "Dark",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'sp_atk': 2}},
    },

    "Night Daze": {
        "type": "Dark",
        "power": 85,
        "acc": 95,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'acc': -1}, 'chance': 0.4},
    },

    "Night Slash": {
        "type": "Dark",
        "power": 70,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Obstruct": {
        "type": "Dark",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status",
        "priority": 4,
        "effect": {'protect': True},
    },

    # Lowers target's stats, then switches out
    "Parting Shot": {
        "type": "Dark",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'target': {'dm': -1, 'sp_atk': -1}, 'switch_user': True},
    },

    "Power Trip": {
        "type": "Dark",
        "power": 20,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'stat_based_power': True},
    },

    "Punishment": {
        "type": "Dark",
        "power": 0,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'stat_based_power': True},
    },

    "Quash": {
        "type": "Dark",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status  ",
        "priority": 0,
        "effect": {'quash': True},
    },

    "Ruin Moves": {
        "type": "Dark",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Ruination": {
        "type": "Dark",
        "power": 0,
        "acc": 90,
        "pp": 10,
        "category": "Special",
        "priority": 0,
        "effect": {'half_hp': True},
    },

    "Snarl": {
        "type": "Dark",
        "power": 55,
        "acc": 95,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'sp_atk': -1}},
    },

    "Snatch": {
        "type": "Dark",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 4,
        "effect": {'snatch': True},
    },

    "Sucker Punch": {
        "type": "Dark",
        "power": 70,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 1,
        "effect": None,
    },

    "Switcheroo": {
        "type": "Dark",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'item_swap': True},
    },

    "Taunt": {
        "type": "Dark",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 1,
        "effect": {'taunt': True},
    },

    "Throat Chop": {
        "type": "Dark",
        "power": 80,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'disable_sound': True},
    },

    "Torment": {
        "type": "Dark",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status  ",
        "priority": 0,
        "effect": {'torment': True},
    },

    "Wicked Blow": {
        "type": "Dark",
        "power": 80,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'always_crit': True},
    },

    "Wicked Torque": {
        "type": "Dark",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Sleep', 'chance': 0.1},
    },


    # ═════════════════════════════════════════════════════════════
    # STEEL TYPE MOVES
    # Steel-type moves are super effective against Ice and Fairy.
    # They are resisted by Fire, Water, Electric, and Steel.
    # Steel moves provide excellent defensive typing and priority options.
    # Key strategies: Fairy counter, bullet punch priority, and defensive setup.
    # ═════════════════════════════════════════════════════════════

    "Anchor Shot": {
        "type": "Steel",
        "power": 80,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": {'prevent_switch': True},
    },

    "Behemoth Bash": {
        "type": "Steel",
        "power": 100,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'double_vs_dynamax': True},
    },

    "Behemoth Blade": {
        "type": "Steel",
        "power": 100,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'double_vs_dynamax': True},
    },

    "Bullet Punch": {
        "type": "Steel",
        "power": 40,
        "acc": 100,
        "pp": 30,
        "category": "Physical",
        "priority": 1,
        "effect": None,
    },

    "Double Iron Bash": {
        "type": "Steel",
        "power": 60,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'multi_hit': 2, 'status': 'Flinch', 'chance': 0.3},
    },

    "Flash Cannon": {
        "type": "Steel",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'sp_def': -1}, 'chance': 0.1},
    },

    "Fortify": {
        "type": "Steel",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status",
        "priority": 0,
        "effect": {'self': {'def': 2, 'sp_def': 2}},
    },

    "Gear Grind": {
        "type": "Steel",
        "power": 50,
        "acc": 85,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'multi_hit': 2},
    },

    "Gear Up": {
        "type": "Steel",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'ally': {'dm': 1, 'speed': 1}},
    },

    # Maximum power physical attack, requires recharge turn
    "Giga Impact": {
        "type": "Steel",
        "power": 150,
        "acc": 90,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'recharge': True},
    },

    "Hard Press": {
        "type": "Steel",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'desperation': True},
    },

    "Heavy Slam": {
        "type": "Steel",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'weight_based': True},
    },

    "Iron Ball": {
        "type": "Steel",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'iron_ball': True},
    },

    "Iron Defense": {
        "type": "Steel",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'def': 2}},
    },

    "Iron Fist": {
        "type": "Steel",
        "power": 135,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.3},
    },

    "Iron Head": {
        "type": "Steel",
        "power": 80,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'status': 'Flinch', 'chance': 0.3},
    },

    "Iron Tail": {
        "type": "Steel",
        "power": 100,
        "acc": 75,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'target': {'def': -1}, 'chance': 0.3},
    },

    "King's Shield": {
        "type": "Steel",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 4,
        "effect": {'king_shield': True},
    },

    "Magnet Bomb": {
        "type": "Steel",
        "power": 60,
        "acc": 100,
        "pp": 20,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Magnet Rise": {
        "type": "Steel",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'levitate': True},
    },

    "Make It Rain": {
        "type": "Steel",
        "power": 120,
        "acc": 100,
        "pp": 5,
        "category": "Special",
        "priority": 0,
        "effect": {'self': {'sp_atk': -1}},
    },

    "Metal Burst": {
        "type": "Steel",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'metal_burst': True},
    },

    "Metal Claw": {
        "type": "Steel",
        "power": 50,
        "acc": 95,
        "pp": 35,
        "category": "Physical",
        "priority": 0,
        "effect": {'self': {'dm': 1}, 'chance': 0.1},
    },

    "Metal Sound": {
        "type": "Steel",
        "power": 0,
        "acc": 85,
        "pp": 40,
        "category": "Status  ",
        "priority": 0,
        "effect": {'target': {'sp_def': -2}},
    },

    "Metal Tempest": {
        "type": "Steel",
        "power": 150,
        "acc": 90,
        "pp": 3,
        "category": "Physical",
        "priority": 0,
        "effect": {'self': {'def': 1}},
    },

    "Meteor Mash": {
        "type": "Steel",
        "power": 90,
        "acc": 90,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'self': {'dm': 1}, 'chance': 0.2},
    },

    "Mirror Shot": {
        "type": "Steel",
        "power": 65,
        "acc": 85,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'acc': -1}, 'chance': 0.3},
    },

    "Shield Bash": {
        "type": "Steel",
        "power": 80,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'self': {'def': 1}, 'chance': 0.1},
    },

    # Raises Speed by 2, Attack by 1
    "Shift Gear": {
        "type": "Steel",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'self': {'speed': 2, 'dm': 1}},
    },

    "Smart Strike": {
        "type": "Steel",
        "power": 70,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Steel Beam": {
        "type": "Steel",
        "power": 140,
        "acc": 95,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'recoil': 0.5},
    },

    "Steel Roller": {
        "type": "Steel",
        "power": 130,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": {'remove_terrain': True},
    },

    "Steel Wing": {
        "type": "Steel",
        "power": 70,
        "acc": 90,
        "pp": 25,
        "category": "Physical",
        "priority": 0,
        "effect": {'self': {'def': 1}, 'chance': 0.1},
    },

    "Sunsteel Strike": {
        "type": "Steel",
        "power": 100,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Tachyon Cutter": {
        "type": "Steel",
        "power": 50,
        "acc": 100,
        "pp": 10,
        "category": "Special",
        "priority": 0,
        "effect": {'multi_hit': 2},
    },


    # ═════════════════════════════════════════════════════════════
    # FAIRY TYPE MOVES
    # Fairy-type moves are super effective against Fighting, Dragon, and Dark.
    # They are resisted by Fire, Poison, and Steel.
    # Fairy moves provide Dragon immunity and excellent healing options.
    # Key strategies: Dragon counter, healing moves, and charm disruption.
    # ═════════════════════════════════════════════════════════════

    "Alluring Voice": {
        "type": "Fairy",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Confuse', 'chance': 1.0},
    },

    "Aromatic Mist": {
        "type": "Fairy",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'ally': {'sp_def': 1}},
    },

    "Baby-Doll Eyes": {
        "type": "Fairy",
        "power": 0,
        "acc": 100,
        "pp": 30,
        "category": "Status  ",
        "priority": 1,
        "effect": {'target': {'dm': -1}},
    },

    "Celestial Judgement": {
        "type": "Fairy",
        "power": 175,
        "acc": 85,
        "pp": 1,
        "category": "Special",
        "priority": 0,
        "effect": {'heal': 0.25},
    },

    "Charm": {
        "type": "Fairy",
        "power": 0,
        "acc": 100,
        "pp": 20,
        "category": "Status  ",
        "priority": 0,
        "effect": {'target': {'dm': -2}},
    },

    "Crafty Shield": {
        "type": "Fairy",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 3,
        "effect": {'status_protect': True},
    },

    "Dazzling Gleam": {
        "type": "Fairy",
        "power": 80,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Decorate": {
        "type": "Fairy",
        "power": 0,
        "acc": 100,
        "pp": 15,
        "category": "Status",
        "priority": 0,
        "effect": {'ally': {'dm': 2, 'sp_atk': 2}},
    },

    "Disarming Voice": {
        "type": "Fairy",
        "power": 40,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Draining Kiss": {
        "type": "Fairy",
        "power": 50,
        "acc": 100,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'heal': 0.75},
    },

    "Fairy Lock": {
        "type": "Fairy",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'prevent_switch': True},
    },

    "Fairy Wind": {
        "type": "Fairy",
        "power": 40,
        "acc": 100,
        "pp": 30,
        "category": "Special ",
        "priority": 0,
        "effect": None,
    },

    "Fairy's Requiem": {
        "type": "Fairy",
        "power": 155,
        "acc": 90,
        "pp": 3,
        "category": "Special",
        "priority": 0,
        "effect": {'heal': 0.25},
    },

    "Fleur Cannon": {
        "type": "Fairy",
        "power": 130,
        "acc": 90,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'self': {'sp_atk': -2}},
    },

    "Floral Healing": {
        "type": "Fairy",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'ally_heal': 0.5},
    },

    "Geomancy": {
        "type": "Fairy",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status",
        "priority": 0,
        "effect": {'self': {'dm': 2, 'sp_atk': 2, 'speed': 2}},
    },

    "Healing Aura": {
        "type": "Fairy",
        "power": 0,
        "acc": 100,
        "pp": 5,
        "category": "Status",
        "priority": 0,
        "effect": {'heal': 0.5, 'cure_status': True},
    },

    "Let's Snuggle Forever": {
        "type": "Fairy",
        "power": 190,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Light of Ruin": {
        "type": "Fairy",
        "power": 100,
        "acc": 90,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'recoil': 0.5},
    },

    "Misty Explosion": {
        "type": "Fairy",
        "power": 100,
        "acc": 100,
        "pp": 5,
        "category": "Special ",
        "priority": 0,
        "effect": {'recoil': 1.0, 'misty_boost': True},
    },

    "Misty Terrain": {
        "type": "Fairy",
        "power": 0,
        "acc": 100,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'misty_terrain': True},
    },

    "Moonblast": {
        "type": "Fairy",
        "power": 95,
        "acc": 100,
        "pp": 15,
        "category": "Special ",
        "priority": 0,
        "effect": {'target': {'sp_atk': -1}, 'chance': 0.3},
    },

    # Restores HP, more at night
    "Moonlight": {
        "type": "Fairy",
        "power": 0,
        "acc": 100,
        "pp": 5,
        "category": "Status  ",
        "priority": 0,
        "effect": {'heal': 0.5},
    },

    "Nature's Madness": {
        "type": "Fairy",
        "power": 0,
        "acc": 90,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'half_hp': True},
    },

    "Play Rough": {
        "type": "Fairy",
        "power": 90,
        "acc": 90,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": {'target': {'dm': -1}, 'chance': 0.1},
    },

    "Spirit Break": {
        "type": "Fairy",
        "power": 75,
        "acc": 100,
        "pp": 15,
        "category": "Physical",
        "priority": 0,
        "effect": {'target': {'sp_atk': -1}},
    },

    "Strange Steam": {
        "type": "Fairy",
        "power": 90,
        "acc": 95,
        "pp": 10,
        "category": "Special ",
        "priority": 0,
        "effect": {'status': 'Confuse', 'chance': 0.2},
    },

    "Sweet Kiss": {
        "type": "Fairy",
        "power": 0,
        "acc": 75,
        "pp": 10,
        "category": "Status  ",
        "priority": 0,
        "effect": {'status': 'Confuse', 'chance': 1.0},
    },


    # ═════════════════════════════════════════════════════════════
    # Z-Moves
    # ═════════════════════════════════════════════════════════════

    "10,000,000 Volt Thunderbolt": {
        "type": "Electric",
        "power": 195,
        "acc": 100,
        "pp": 1,
        "category": "Special",
        "priority": 0,
        "effect": {'always_crit': True},
    },

    "Acid Downpour": {
        "type": "Poison",
        "power": 100,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "All-Out Pummeling": {
        "type": "Fighting",
        "power": 100,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Black Hole Eclipse": {
        "type": "Dark",
        "power": 100,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Bloom Doom": {
        "type": "Grass",
        "power": 100,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Z-Move: Normal-type ultra attack
    "Breakneck Blitz": {
        "type": "Normal",
        "power": 100,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Z-Move: Pikachu's ultimate attack
    "Catastropika": {
        "type": "Electric",
        "power": 210,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Continental Crush": {
        "type": "Rock",
        "power": 100,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Corkscrew Crash": {
        "type": "Steel",
        "power": 100,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Devastating Drake": {
        "type": "Dragon",
        "power": 100,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Z-Move: Sharply raises all stats
    "Extreme Evoboost": {
        "type": "Normal",
        "power": 0,
        "acc": 100,
        "pp": 1,
        "category": "Status",
        "priority": 0,
        "effect": {'self': {'all_stats': 2}},
    },

    "Genesis Supernova": {
        "type": "Psychic",
        "power": 185,
        "acc": 100,
        "pp": 1,
        "category": "Special",
        "priority": 0,
        "effect": {'misty_terrain': True},
    },

    "Gigavolt Havoc": {
        "type": "Electric",
        "power": 100,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Guardian of Alola": {
        "type": "Fairy",
        "power": 0,
        "acc": 100,
        "pp": 1,
        "category": "Special",
        "priority": 0,
        "effect": {'half_hp': True},
    },

    "Hydro Vortex": {
        "type": "Water",
        "power": 100,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Inferno Overdrive": {
        "type": "Fire",
        "power": 100,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Light That Burns the Sky": {
        "type": "Psychic",
        "power": 200,
        "acc": 100,
        "pp": 1,
        "category": "Special",
        "priority": 0,
        "effect": None,
    },

    "Malicious Moonsault": {
        "type": "Dark",
        "power": 180,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Menacing Moonraze Maelstrom": {
        "type": "Ghost",
        "power": 200,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Never-Ending Nightmare": {
        "type": "Ghost",
        "power": 100,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # Z-Move: Snorlax's ultimate attack
    "Pulverizing Pancake": {
        "type": "Normal",
        "power": 210,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Savage Spin-Out": {
        "type": "Bug",
        "power": 100,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Searing Sunraze Smash": {
        "type": "Steel",
        "power": 200,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Shattered Psyche": {
        "type": "Psychic",
        "power": 100,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Soul-Stealing 7-Star Strike": {
        "type": "Ghost",
        "power": 195,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Stoked Sparksurfer": {
        "type": "Electric",
        "power": 175,
        "acc": 100,
        "pp": 1,
        "category": "Special",
        "priority": 0,
        "effect": {'status': 'Paralyze', 'chance': 1.0},
    },

    "Subzero Slammer": {
        "type": "Ice",
        "power": 100,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Supersonic Skystrike": {
        "type": "Flying",
        "power": 100,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Tectonic Rage": {
        "type": "Ground",
        "power": 100,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "Twinkle Tackle": {
        "type": "Fairy",
        "power": 100,
        "acc": 100,
        "pp": 1,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },


    # ═════════════════════════════════════════════════════════════
    # G-Max Moves
    # ═════════════════════════════════════════════════════════════

    "G-Max Befuddle": {
        "type": "Bug",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Cannonade": {
        "type": "Water",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Centiferno": {
        "type": "Fire",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Chi Strike": {
        "type": "Fighting",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Depletion": {
        "type": "Dragon",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Drum Solo": {
        "type": "Grass",
        "power": 160,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Finale": {
        "type": "Fairy",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Finality": {
        "type": "Fighting",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Fireball": {
        "type": "Fire",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # G-Max: Scatters coins
    "G-Max Gold Rush": {
        "type": "Normal",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Gravitas": {
        "type": "Psychic",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Hydrosnipe": {
        "type": "Water",
        "power": 160,
        "acc": 100,
        "pp": 5,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Malodor": {
        "type": "Poison",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Meltdown": {
        "type": "Steel",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max One Blow": {
        "type": "Dark",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Rapid Flow": {
        "type": "Water",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    # G-Max: Restores berries
    "G-Max Replenish": {
        "type": "Normal",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Resonance": {
        "type": "Ice",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Sandblast": {
        "type": "Ground",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Smite": {
        "type": "Fairy",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Steelsurge": {
        "type": "Steel",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Stonesurge": {
        "type": "Water",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Sweetness": {
        "type": "Grass",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Tartness": {
        "type": "Grass",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Terror": {
        "type": "Ghost",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Vine Lash": {
        "type": "Grass",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Volcalith": {
        "type": "Rock",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Volt Crash": {
        "type": "Electric",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Wildfire": {
        "type": "Fire",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },

    "G-Max Wind Rage": {
        "type": "Flying",
        "power": 10,
        "acc": 100,
        "pp": 10,
        "category": "Physical",
        "priority": 0,
        "effect": None,
    },


    # ═════════════════════════════════════════════════════════════
    # Custom Fusion
    # ═════════════════════════════════════════════════════════════

}


def get_effectiveness(atk_type, def_type):
    """Return type effectiveness multiplier. Handles dual types (list or single string)."""
    if isinstance(def_type, list):
        multiplier = 1.0
        for dt in def_type:
            multiplier *= TYPE_CHART.get(atk_type, {}).get(dt, 1.0)
        return multiplier
    return TYPE_CHART.get(atk_type, {}).get(def_type, 1.0)


# ═══════════════════════════════════════════════════════════════════
# MOVE EFFECT REFERENCE GUIDE
# ═══════════════════════════════════════════════════════════════════
# This section documents all possible effect types used in the MOVES dict.
# Each effect is a dictionary that may contain one or more of the following keys:

# STATUS EFFECTS:
#   {"status": "Burn", "chance": 0.1}
#     - Inflicts Burn status, dealing 1/16 max HP damage per turn
#     - Burned Pokemon have their Attack halved
#     - Fire-type Pokemon cannot be burned
#
#   {"status": "Paralyze", "chance": 0.3}
#     - Inflicts Paralysis, 25% chance to be unable to move
#     - Paralyzed Pokemon have their Speed reduced by 50%
#     - Electric-type Pokemon cannot be paralyzed
#
#   {"status": "Poison", "chance": 0.3}
#     - Inflicts Poison, dealing 1/8 max HP damage per turn
#     - Poison/Steel-type Pokemon cannot be poisoned
#
#   {"status": "Badly Poison", "chance": 1.0}
#     - Inflicts Toxic, damage increases each turn (1/16, 2/16, 3/16...)
#     - Poison/Steel-type Pokemon cannot be badly poisoned
#
#   {"status": "Sleep", "chance": 1.0}
#     - Inflicts Sleep, Pokemon cannot move for 1-3 turns
#     - Pokemon with Early Bird wake up faster
#
#   {"status": "Freeze", "chance": 0.1}
#     - Inflicts Freeze, Pokemon cannot move until thawed
#     - 20% chance to thaw each turn, Fire moves thaw instantly
#     - Ice-type Pokemon cannot be frozen
#
#   {"status": "Confuse", "chance": 0.2}
#     - Inflicts Confusion, 33% chance to hurt self instead of attacking
#     - Lasts 1-4 turns
#
#   {"status": "Flinch", "chance": 0.3}
#     - Causes Flinch, target cannot move this turn
#     - Only works if user moves first (higher priority or faster)

# RECOIL EFFECTS:
#   {"recoil": 0.25}
#     - User takes 25% of damage dealt as recoil damage
#     - Recoil damage is not reduced by type resistance
#     - Rock Head ability prevents recoil damage
#
#   {"recoil": 0.33}
#     - User takes 33% of damage dealt as recoil damage
#     - Common on high-power physical moves
#
#   {"recoil": 0.5}
#     - User takes 50% of damage dealt as recoil damage
#     - Very high risk/reward moves
#
#   {"recoil": 1.0}
#     - User takes 100% of damage dealt as recoil damage
#     - User will faint if target has less HP than user
#     - Used on Self-Destruct and Explosion

# HEALING EFFECTS:
#   {"heal": 0.5}
#     - Restores 50% of user's max HP
#     - Healing is capped at max HP
#     - Used by Recover, Soft-Boiled, Milk Drink, etc.
#
#   {"heal": 0.25}
#     - Restores 25% of user's max HP
#     - Used by weaker healing moves

# TRAPPING EFFECTS:
#   {"trap": True}
#     - Prevents target from switching for 4-5 turns
#     - Target takes damage each turn
#     - Can be escaped with Rapid Spin or switching items

# CHARGE EFFECTS:
#   {"charge": True}
#     - Requires one turn to charge before attacking
#     - User is vulnerable during charge turn
#     - Can be interrupted by flinch or status

# RECHARGE EFFECTS:
#   {"recharge": True}
#     - User must rest on the turn after using
#     - User cannot attack or switch during recharge
#     - Used on Hyper Beam, Giga Impact, etc.

# MULTI-HIT EFFECTS:
#   {"multi_hit": 2}
#     - Hits exactly 2 times in one turn
#     - Each hit calculates damage separately
#
#   {"multi_hit": [2, 5]}
#     - Hits 2-5 times randomly
#     - Each hit has equal probability
#     - Used by Fury Swipes, Icicle Spear, etc.
#
#   {"multi_hit_escalating": 3}
#     - Hits 3 times with increasing power
#     - Each successive hit deals more damage

# ONE-HIT KO EFFECTS:
#   {"ohko": True}
#     - Instantly knocks out target if it hits
#     - Accuracy is typically 30%
#     - Does not work on higher-level Pokemon
#     - Sturdy ability prevents OHKO

# PROTECTION EFFECTS:
#   {"protect": True}
#     - Blocks all incoming attacks this turn
#     - Success rate decreases with consecutive use
#     - Does not block status moves
#
#   {"max_protect": True}
#     - Dynamax version of Protect
#     - Does not decrease success rate

# SWITCHING EFFECTS:
#   {"force_switch": True}
#     - Forces target to switch to a random Pokemon
#     - Does not work on Pokemon with Suction Cups
#     - Used by Whirlwind, Roar, Circle Throw, etc.
#
#   {"switch_user": True}
#     - User switches out after using the move
#     - Used by U-turn, Volt Switch, Parting Shot, etc.

# STAT CHANGE EFFECTS:
#   {"self": {"dm": 1}}
#     - Raises user's Attack by 1 stage
#     - "dm" = Attack, "def" = Defense, "speed" = Speed
#     - "sp_atk" = Special Attack, "sp_def" = Special Defense, "acc" = Accuracy
#
#   {"target": {"dm": -1}}
#     - Lowers target's Attack by 1 stage
#     - Negative values lower stats, positive raise
#
#   {"ally": {"speed": 1}}
#     - Raises ally's Speed by 1 stage
#     - Used in double battles

# FIXED DAMAGE EFFECTS:
#   {"fixed_damage": 40}
#     - Deals exactly 40 damage regardless of stats
#     - Not affected by type effectiveness
#     - Used by Sonic Boom
#
#   {"level_damage": True}
#     - Deals damage equal to user's level
#     - Used by Seismic Toss, Night Shade
#
#   {"half_hp": True}
#     - Reduces target's HP by half
#     - Used by Super Fang, Nature's Madness

# SPECIAL EFFECTS:
#   {"desperation": True}
#     - Power increases as user's HP decreases
#     - Used by Flail, Reversal, Eruption
#
#   {"always_crit": True}
#     - Always lands a critical hit
#     - Critical hits ignore stat changes
#     - Used by Frost Breath, Storm Throw
#
#   {"double_if_half_hp": True}
#     - Power doubles if target is below 50% HP
#     - Used by Brine
#
#   {"double_if_first": True}
#     - Power doubles if user moves first
#     - Used by Bolt Beak
#
#   {"double_if_failed": True}
#     - Power doubles if last move failed
#     - Used by Stomping Tantrum, Temper Flare
#
#   {"double_if_poisoned": True}
#     - Power doubles if user is poisoned
#     - Used by Barb Barrage
#
#   {"double_if_sleeping": True}
#     - Power doubles if target is asleep
#     - Used by Wake-Up Slap
#
#   {"double_if_hit": True}
#     - Power doubles if target was hit this turn
#     - Used by Assurance
#
#   {"double_if_stats_lowered": True}
#     - Power doubles if user's stats were lowered
#     - Used by Lash Out
#
#   {"super_effective_boost": True}
#     - Deals 1.5x damage when super effective
#     - Used by Collision Course, Electro Drift
#
#   {"super_vs_water": True}
#     - Super effective against Water-type
#     - Used by Freeze-Dry
#
#   {"weight_based": True}
#     - Power based on target's weight
#     - Heavier targets take more damage
#     - Used by Low Kick, Grass Knot, Heavy Slam
#
#   {"speed_based": True}
#     - Power based on speed difference
#     - Faster user = more damage
#     - Used by Electro Ball
#
#   {"stat_based_power": True}
#     - Power based on user's stat stages
#     - Used by Stored Power, Punishment
#
#   {"use_target_attack": True}
#     - Uses target's Attack stat instead of user's
#     - Used by Foul Play
#
#   {"random_power": True}
#     - Random power level each use
#     - Used by Magnitude
#
#   {"escalating": True}
#     - Power increases with each consecutive use
#     - Used by Fury Cutter, Rollout
#
#   {"multi_turn": True}
#     - Continues for multiple turns
#     - Power increases each turn
#     - Used by Rollout, Ice Ball

# UTILITY EFFECTS:
#   {"remove_hazards": True}
#     - Removes entry hazards from user's side
#     - Used by Rapid Spin, Mortal Spin, Tidy Up
#
#   {"cure_status": True}
#     - Cures user's status condition
#     - Used by Refresh, Aromatherapy, Heal Bell
#
#   {"hazard": "Spikes"}
#     - Sets entry hazard on target's side
#     - Damages switching Pokemon
#     - Types: "Spikes", "Stealth Rock", "Toxic Spikes"
#
#   {"leech_seed": True}
#     - Seeds target, draining HP each turn
#     - Heals user for drained amount
#     - Does not work on Grass-types
#
#   {"yawn": True}
#     - Target falls asleep next turn
#     - Can be prevented by switching out
#
#   {"transform": True}
#     - Copies target's appearance, stats, and moves
#     - Used by Ditto's Transform
#
#   {"random_move": True}
#     - Randomly selects any move in the game
#     - Used by Metronome
#
#   {"sleep_talk": True}
#     - Randomly uses one of user's moves while asleep
#     - Does not consume PP
#
#   {"mimic": True}
#     - Copies target's last used move
#     - Replaces Mimic in user's moveset
#
#   {"sketch": True}
#     - Permanently copies target's last move
#     - Only usable by Smeargle
#
#   {"focus_energy": True}
#     - Increases critical hit ratio by 2 stages
#
#   {"endure": True}
#     - Survives any hit with 1 HP this turn
#     - Fails if used consecutively
#
#   {"attract": True}
#     - Infatuates target of opposite gender
#     - 50% chance to be unable to move
#
#   {"encore": True}
#     - Forces target to repeat last move for 3 turns
#
#   {"perish_song": True}
#     - All active Pokemon faint in 3 turns
#     - Can be avoided by switching out
#
#   {"baton_pass": True}
#     - Switches out, passing stat changes to replacement
#
#   {"pain_split": True}
#     - Averages user and target's current HP
#
#   {"wish": True}
#     - Heals next Pokemon that switches in
#     - Takes effect at end of next turn
#
#   {"healing_wish": True}
#     - User faints, next Pokemon fully healed
#
#   {"lunar_dance": True}
#     - User faints, next Pokemon fully healed with PP restored
#
#   {"stockpile": True}
#     - Stores energy to power up Spit Up/Swallow
#     - Can stockpile up to 3 times
#
#   {"stockpile_damage": True}
#     - Releases stored Stockpile power as damage
#
#   {"stockpile_heal": True}
#     - Heals based on Stockpile count
#
#   {"break_protect": True}
#     - Bypasses Protect and Detect
#     - Used by Feint
#
#   {"no_ko": True}
#     - Cannot knock out target (leaves 1 HP)
#     - Used by Hold Back
#
#   {"money": True}
#     - Scatters coins after battle
#     - Amount based on user's level
#
#   {"eat_berry": True}
#     - Consumes and uses target's held Berry
#     - Used by Pluck, Bug Bite
#
#   {"remove_item": True}
#     - Removes target's held item
#     - Used by Knock Off
#
#   {"item_swap": True}
#     - Swaps held items with target
#     - Used by Trick, Switcheroo
#
#   {"ability_swap": True}
#     - Swaps abilities with target
#     - Used by Skill Swap, Worry Seed
#
#   {"ability_copy": True}
#     - Copies target's ability
#     - Used by Role Play, Doodle
#
#   {"copy_stages": True}
#     - Copies target's stat stages
#     - Used by Psych Up
#
#   {"stat_swap": True}
#     - Swaps stat stages with target
#     - Used by Power Swap, Guard Swap
#
#   {"stat_split": True}
#     - Averages stat stages with target
#     - Used by Power Split, Guard Split
#
#   {"telekinesis": True}
#     - Makes target immune to Ground moves for 3 turns
#     - All moves hit target (no miss)
#
#   {"trick_room": True}
#     - Reverses move order for 5 turns
#     - Slower Pokemon move first
#
#   {"wonder_room": True}
#     - Swaps Defense and Special Defense for 5 turns
#
#   {"magic_room": True}
#     - Negates held item effects for 5 turns
#
#   {"gravity": True}
#     - Grounds all Pokemon for 5 turns
#     - Flying/Levitate Pokemon can be hit by Ground moves
#
#   {"reflect": True}
#     - Reduces physical damage for 5 turns
#
#   {"light_screen": True}
#     - Reduces special damage for 5 turns
#
#   {"safeguard": True}
#     - Prevents status conditions for 5 turns
#
#   {"mist": True}
#     - Prevents stat reduction for 5 turns
#
#   {"aurora_veil": True}
#     - Reduces all damage for 5 turns (hail/snow only)
#
#   {"tailwind": True}
#     - Doubles team's Speed for 4 turns
#
#   {"rain_dance": True}
#     - Sets rain weather for 5 turns
#     - Boosts Water moves, weakens Fire moves
#
#   {"sunny_day": True}
#     - Sets sunny weather for 5 turns
#     - Boosts Fire moves, weakens Water moves
#
#   {"sandstorm": True}
#     - Sets sandstorm weather for 5 turns
#     - Damages non-Rock/Ground/Steel types
#
#   {"hail": True}
#     - Sets hail weather for 5 turns
#     - Damages non-Ice types
#
#   {"snow_weather": True}
#     - Sets snow weather for 5 turns
#     - Boosts Ice-type Defense
#
#   {"misty_terrain": True}
#     - Sets misty terrain for 5 turns
#     - Prevents status, halves Dragon damage
#
#   {"grassy_terrain": True}
#     - Sets grassy terrain for 5 turns
#     - Heals grounded Pokemon each turn
#
#   {"electric_terrain": True}
#     - Sets electric terrain for 5 turns
#     - Prevents sleep, boosts Electric moves
#
#   {"psychic_terrain": True}
#     - Sets psychic terrain for 5 turns
#     - Protects grounded Pokemon from priority
#
#   {"ally_boost": True}
#     - Boosts ally's move power by 50%
#     - Used by Helping Hand
#
#   {"ally_heal": 0.5}
#     - Heals ally for 50% of their max HP
#
#   {"ally_protect": True}
#     - Protects all allies from attacks
#
#   {"priority_protect": True}
#     - Protects from priority moves
#
#   {"status_protect": True}
#     - Protects from status moves
#
#   {"rage_powder": True}
#     - Redirects all attacks to user
#
#   {"spiky_shield": True}
#     - Protects and damages contact attackers
#
#   {"king_shield": True}
#     - Protects and lowers attacker's Attack
#
#   {"baneful_bunker": True}
#     - Protects and poisons contact attackers
#
#   {"silk_trap": True}
#     - Protects and lowers attacker's Speed
#
#   {"shell_trap": True}
#     - Only works if hit by physical move
#
#   {"focus_punch": True}
#     - Only works if not hit before use
#
#   {"bide": True}
#     - Stores damage for 2 turns, releases double
#
#   {"counter": True}
#     - Returns double physical damage taken
#
#   {"mirror_coat": True}
#     - Returns double special damage taken
#
#   {"metal_burst": True}
#     - Returns 1.5x damage taken
#
#   {"destiny_bond": True}
#     - If user faints, attacker faints too
#
#   {"curse": True}
#     - Ghost: Curses target, damages each turn
#     - Non-Ghost: Lowers Speed, raises Attack/Defense
#
#   {"nightmare": True}
#     - Damages sleeping target each turn
#
#   {"dream_eater": True}
#     - Heals 50% of damage dealt to sleeping target
#
#   {"imprison": True}
#     - Prevents opponents from using user's moves
#
#   {"torment": True}
#     - Prevents target from using same move twice
#
#   {"taunt": True}
#     - Prevents target from using status moves
#
#   {"disable": True}
#     - Prevents target from using last move
#
#   {"quash": True}
#     - Forces target to move last this turn
#
#   {"snatch": True}
#     - Steals healing/stat-boosting moves
#
#   {"magic_coat": True}
#     - Reflects status moves back at user
#
#   {"mirror_move": True}
#     - Copies and uses target's last move
#
#   {"copycat": True}
#     - Copies last move used in battle
#
#   {"assist": True}
#     - Randomly uses move from team
#
#   {"me_first": True}
#     - Copies target's move with 50% boost
#
#   {"nature_power": True}
#     - Changes based on terrain
#
#   {"terrain_effect": True}
#     - Effect varies based on terrain
#
#   {"clear_hazards": True}
#     - Removes all entry hazards
#
#   {"defog": True}
#     - Lowers target's evasion, removes hazards
#
#   {"reset_stages": True}
#     - Resets all stat changes to 0
#
#   {"suppress_ability": True}
#     - Suppresses target's ability
#
#   {"disable_healing": True}
#     - Prevents target from healing
#
#   {"disable_sound": True}
#     - Prevents sound-based moves
#
#   {"tri_attack": True}
#     - May paralyze, burn, or freeze target
#
#   {"present": True}
#     - Damages or heals target randomly
#
#   {"rage": True}
#     - Attack increases each time user is hit
#
#   {"confuse_after": True}
#     - User becomes confused after using
#
#   {"burn_up": True}
#     - User loses Fire type after using
#
#   {"salt_cure": True}
#     - Damages target each turn, more for Steel/Water
#
#   {"fickle_beam": True}
#     - Random chance for 2x damage
#
#   {"ground_flying": True}
#     - Makes Flying-type vulnerable to Ground
#
#   {"fire_weak": True}
#     - Makes target take 2x Fire damage
#
#   {"prevent_switch": True}
#     - Prevents target from switching
#
#   {"steal_stages": True}
#     - Steals target's stat boosts
#
#   {"double_vs_dynamax": True}
#     - Deals 2x damage to Dynamax Pokemon
#
#   {"double_on_terrain": True}
#     - Deals 2x damage on Electric Terrain
#
#   {"always_crit": True}
#     - Always lands a critical hit
#
#   {"crit_boost": True}
#     - Increases critical hit ratio
#
#   {"cure_burn": True}
#     - Cures target's burn status
#
#   {"sleep_only": True}
#     - Only works on sleeping targets
#
#   {"crash_damage": True}
#     - User takes damage if move misses


# ═══════════════════════════════════════════════════════════════════
# TYPE EFFECTIVENESS CHART - COMPLETE REFERENCE
# ═══════════════════════════════════════════════════════════════════
# This chart shows all type matchups for the 18-type system.
# 2.0 = Super Effective (2x damage)
# 1.0 = Neutral damage (normal)
# 0.5 = Not Very Effective (0.5x damage)
# 0.0 = No Effect (immune)

# NORMAL TYPE ATTACKING:
#   Super Effective: None
#   Not Very Effective: Rock, Steel
#   No Effect: Ghost
#   Weak Against: Fighting
#   Resists: None
#   Immune To: Ghost

# FIRE TYPE ATTACKING:
#   Super Effective: Grass, Ice, Bug, Steel
#   Not Very Effective: Fire, Water, Rock, Dragon
#   No Effect: None
#   Weak Against: Water, Ground, Rock
#   Resists: Fire, Grass, Ice, Bug, Steel, Fairy
#   Immune To: None

# WATER TYPE ATTACKING:
#   Super Effective: Fire, Ground, Rock
#   Not Very Effective: Water, Grass, Dragon
#   No Effect: None
#   Weak Against: Electric, Grass
#   Resists: Fire, Water, Ice, Steel
#   Immune To: None

# GRASS TYPE ATTACKING:
#   Super Effective: Water, Ground, Rock
#   Not Very Effective: Fire, Grass, Poison, Flying, Bug, Dragon, Steel
#   No Effect: None
#   Weak Against: Fire, Ice, Poison, Flying, Bug
#   Resists: Water, Electric, Grass, Ground
#   Immune To: None

# ELECTRIC TYPE ATTACKING:
#   Super Effective: Water, Flying
#   Not Very Effective: Grass, Electric, Dragon
#   No Effect: Ground
#   Weak Against: Ground
#   Resists: Electric, Flying, Steel
#   Immune To: None

# ICE TYPE ATTACKING:
#   Super Effective: Grass, Ground, Flying, Dragon
#   Not Very Effective: Fire, Water, Ice, Steel
#   No Effect: None
#   Weak Against: Fire, Fighting, Rock, Steel
#   Resists: Ice
#   Immune To: None

# FIGHTING TYPE ATTACKING:
#   Super Effective: Normal, Ice, Rock, Dark, Steel
#   Not Very Effective: Poison, Flying, Psychic, Bug, Fairy
#   No Effect: Ghost
#   Weak Against: Flying, Psychic, Fairy
#   Resists: Bug, Rock, Dark
#   Immune To: None

# POISON TYPE ATTACKING:
#   Super Effective: Grass, Fairy
#   Not Very Effective: Poison, Ground, Rock, Ghost
#   No Effect: Steel
#   Weak Against: Ground, Psychic
#   Resists: Grass, Fighting, Poison, Bug, Fairy
#   Immune To: None

# GROUND TYPE ATTACKING:
#   Super Effective: Fire, Electric, Poison, Rock, Steel
#   Not Very Effective: Grass, Bug
#   No Effect: Flying
#   Weak Against: Water, Grass, Ice
#   Resists: Poison, Rock
#   Immune To: Electric

# FLYING TYPE ATTACKING:
#   Super Effective: Grass, Fighting, Bug
#   Not Very Effective: Electric, Rock, Steel
#   No Effect: None
#   Weak Against: Electric, Ice, Rock
#   Resists: Grass, Fighting, Bug
#   Immune To: Ground

# PSYCHIC TYPE ATTACKING:
#   Super Effective: Fighting, Poison
#   Not Very Effective: Psychic, Steel
#   No Effect: Dark
#   Weak Against: Bug, Ghost, Dark
#   Resists: Fighting, Psychic
#   Immune To: None

# BUG TYPE ATTACKING:
#   Super Effective: Grass, Psychic, Dark
#   Not Very Effective: Fire, Fighting, Poison, Flying, Ghost, Steel, Fairy
#   No Effect: None
#   Weak Against: Fire, Flying, Rock
#   Resists: Grass, Fighting, Ground
#   Immune To: None

# ROCK TYPE ATTACKING:
#   Super Effective: Fire, Ice, Flying, Bug
#   Not Very Effective: Fighting, Ground, Steel
#   No Effect: None
#   Weak Against: Water, Grass, Fighting, Ground, Steel
#   Resists: Normal, Fire, Poison, Flying
#   Immune To: None

# GHOST TYPE ATTACKING:
#   Super Effective: Psychic, Ghost
#   Not Very Effective: Dark
#   No Effect: Normal
#   Weak Against: Ghost, Dark
#   Resists: Poison, Bug
#   Immune To: Normal, Fighting

# DRAGON TYPE ATTACKING:
#   Super Effective: Dragon
#   Not Very Effective: Steel
#   No Effect: Fairy
#   Weak Against: Ice, Dragon, Fairy
#   Resists: Fire, Water, Grass, Electric
#   Immune To: None

# DARK TYPE ATTACKING:
#   Super Effective: Psychic, Ghost
#   Not Very Effective: Fighting, Dark, Fairy
#   No Effect: None
#   Weak Against: Fighting, Bug, Fairy
#   Resists: Ghost, Dark
#   Immune To: Psychic

# STEEL TYPE ATTACKING:
#   Super Effective: Ice, Rock, Fairy
#   Not Very Effective: Fire, Water, Electric, Steel
#   No Effect: None
#   Weak Against: Fire, Fighting, Ground
#   Resists: Normal, Grass, Ice, Flying, Psychic, Bug, Rock, Dragon, Steel, Fairy
#   Immune To: Poison

# FAIRY TYPE ATTACKING:
#   Super Effective: Fighting, Dragon, Dark
#   Not Very Effective: Fire, Poison, Steel
#   No Effect: None
#   Weak Against: Poison, Steel
#   Resists: Fighting, Bug, Dark
#   Immune To: Dragon

# ═══════════════════════════════════════════════════════════════════
# PRIORITY BRACKET REFERENCE
# ═══════════════════════════════════════════════════════════════════
# Moves with higher priority always go first, regardless of Speed.
# Within the same priority bracket, faster Pokemon move first.

# Priority +5: Helping Hand
# Priority +4: Protect, Detect, King's Shield, Spiky Shield, Baneful Bunker, Silk Trap, Burning Bulwark, Max Guard, Endure, Magic Coat
# Priority +3: Fake Out, Upper Hand, Rage Powder, Follow Me, Quick Guard, Wide Guard, Crafty Shield, Mat Block
# Priority +2: Extreme Speed, Feint, First Impression, Quick Guard
# Priority +1: Quick Attack, Aqua Jet, Ice Shard, Mach Punch, Vacuum Wave, Bullet Punch, Shadow Sneak, Aqua Jet, Jet Punch, Baby-Doll Eyes, Tailwind, Ally Switch
# Priority 0: Most moves (default)
# Priority -1: Vital Throw, Circle Throw, Dragon Tail, Whirlwind, Roar, Teleport
# Priority -2: Focus Punch, Shell Trap
# Priority -3: Shell Trap
# Priority -4: Avalanche, Revenge
# Priority -5: Counter, Mirror Coat, Metal Burst
# Priority -6: Whirlwind, Roar, Circle Throw, Dragon Tail, Teleport
# Priority -7: Trick Room

# ═══════════════════════════════════════════════════════════════════
# STAT STAGE REFERENCE
# ═══════════════════════════════════════════════════════════════════
# Stats can be raised or lowered by up to 6 stages.
# Each stage modifies the stat by a multiplier.

# Stage | Attack/Defense/Speed/Sp.Atk/Sp.Def Multiplier
# ------|---------------------------------------------
#   -6  | 2/8  (0.25x)
#   -5  | 2/7  (0.286x)
#   -4  | 2/6  (0.333x)
#   -3  | 2/5  (0.4x)
#   -2  | 2/4  (0.5x)
#   -1  | 2/3  (0.667x)
#    0  | 2/2  (1.0x) - Neutral
#   +1  | 3/2  (1.5x)
#   +2  | 4/2  (2.0x)
#   +3  | 5/2  (2.5x)
#   +4  | 6/2  (3.0x)
#   +5  | 7/2  (3.5x)
#   +6  | 8/2  (4.0x)

# Accuracy/Evasion stages use a different formula:
# Stage | Accuracy/Evasion Multiplier
# ------|---------------------------
#   -6  | 3/9  (0.333x)
#   -5  | 3/8  (0.375x)
#   -4  | 3/7  (0.429x)
#   -3  | 3/6  (0.5x)
#   -2  | 3/5  (0.6x)
#   -1  | 3/4  (0.75x)
#    0  | 3/3  (1.0x) - Neutral
#   +1  | 4/3  (1.333x)
#   +2  | 5/3  (1.667x)
#   +3  | 6/3  (2.0x)
#   +4  | 7/3  (2.333x)
#   +5  | 8/3  (2.667x)
#   +6  | 9/3  (3.0x)

# ═══════════════════════════════════════════════════════════════════
# STATUS CONDITION REFERENCE
# ═══════════════════════════════════════════════════════════════════
# Each status condition has specific effects on the Pokemon.

# BURN:
#   - Deals 1/16 of max HP as damage at end of each turn
#   - Halves the Pokemon's Attack stat
#   - Can be cured by: switching out, items, abilities, moves
#   - Fire-type Pokemon cannot be burned
#   - Guts ability ignores Attack reduction
#   - Flame Orb inflicts burn when held

# PARALYSIS:
#   - 25% chance to be unable to move each turn
#   - Reduces Speed by 50%
#   - Can be cured by: switching out, items, abilities, moves
#   - Electric-type Pokemon cannot be paralyzed
#   - Quick Feet ability ignores Speed reduction
#   - Limber ability prevents paralysis
#   - Thunder Wave, Stun Spore, Nuzzle inflict paralysis

# POISON:
#   - Deals 1/8 of max HP as damage at end of each turn
#   - Can be cured by: switching out, items, abilities, moves
#   - Poison/Steel-type Pokemon cannot be poisoned
#   - Can spread to other Pokemon via Toxic Chain
#   - Poison Heal ability heals instead of damaging

# BADLY POISON (TOXIC):
#   - Damage increases each turn: 1/16, 2/16, 3/16, 4/16, 5/16, 6/16
#   - Resets to 1/16 if switched out and back in
#   - Can be cured by: switching out, items, abilities, moves
#   - Poison/Steel-type Pokemon cannot be badly poisoned
#   - Toxic Orb inflicts badly poison when held

# SLEEP:
#   - Pokemon cannot move while asleep
#   - Lasts 1-3 turns (random)
#   - Early Bird ability halves sleep duration
#   - Can be cured by: switching out, items, abilities, moves
#   - Snore, Sleep Talk can be used while asleep
#   - Rest puts user to sleep for 2 turns

# FREEZE:
#   - Pokemon cannot move while frozen
#   - 20% chance to thaw each turn
#   - Fire-type moves thaw the frozen Pokemon
#   - Ice-type Pokemon cannot be frozen
#   - Can be cured by: switching out, items, abilities, moves
#   - Magma Armor, Flame Body can thaw adjacent Pokemon

# CONFUSION:
#   - 33% chance to hurt self instead of attacking
#   - Self-hit damage calculated as level 40, 0 Attack, 0 Defense
#   - Lasts 1-4 turns (random)
#   - Can be cured by: switching out, items, abilities, moves
#   - Own Tempo ability prevents confusion
#   - Own Tempo also prevents infatuation

# ═══════════════════════════════════════════════════════════════════
# WEATHER EFFECTS REFERENCE
# ═══════════════════════════════════════════════════════════════════
# Weather affects battles in various ways.

# SUNNY DAY / HARSH SUNLIGHT:
#   - Fire-type moves deal 1.5x damage
#   - Water-type moves deal 0.5x damage
#   - Solar Beam charges instantly
#   - Synthesis, Morning Sun, Moonlight heal 2/3 HP
#   - Thunder has 50% accuracy
#   - Growth raises Attack and Sp. Atk by 2 stages each
#   - Chlorophyll ability doubles Speed
#   - Dry Skin ability damages 1/8 HP per turn
#   - Flower Gift ability boosts Attack and Sp. Def

# RAIN DANCE / HEAVY RAIN:
#   - Water-type moves deal 1.5x damage
#   - Fire-type moves deal 0.5x damage
#   - Thunder never misses
#   - Synthesis, Morning Sun, Moonlight heal 1/4 HP
#   - Solar Beam requires charge turn
#   - Swift Swim ability doubles Speed
#   - Dry Skin ability heals 1/8 HP per turn
#   - Hydration ability cures status each turn
#   - Rain Dish ability heals 1/16 HP per turn

# SANDSTORM:
#   - Damages non-Rock/Ground/Steel types for 1/16 HP per turn
#   - Rock-type Sp. Def increased by 50%
#   - Synthesis, Morning Sun, Moonlight heal 1/4 HP
#   - Solar Beam requires charge turn
#   - Sand Rush ability doubles Speed
#   - Sand Force boosts Rock/Ground/Steel moves by 30%
#   - Sand Veil ability increases evasion by 20%
#   - Overcoat ability prevents sandstorm damage

# HAIL / SNOW:
#   - Damages non-Ice types for 1/16 HP per turn
#   - Blizzard never misses
#   - Synthesis, Morning Sun, Moonlight heal 1/4 HP
#   - Solar Beam requires charge turn
#   - Snow Cloak ability increases evasion by 20%
#   - Ice Body ability heals 1/16 HP per turn
#   - Slush Rush ability doubles Speed

# ═══════════════════════════════════════════════════════════════════
# TERRAIN EFFECTS REFERENCE
# ═══════════════════════════════════════════════════════════════════
# Terrain affects all grounded Pokemon for 5 turns.

# ELECTRIC TERRAIN:
#   - Electric-type moves deal 1.3x damage
#   - Prevents sleep for grounded Pokemon
#   - Boosts priority of Electric moves
#   - Surge Surfer ability doubles Speed

# GRASSY TERRAIN:
#   - Grass-type moves deal 1.3x damage
#   - Heals grounded Pokemon for 1/16 HP per turn
#   - Reduces damage from Earthquake, Bulldoze, Magnitude by 50%
#   - Grassy Surge ability sets terrain on switch-in

# MISTY TERRAIN:
#   - Fairy-type moves deal 1.3x damage
#   - Prevents status conditions for grounded Pokemon
#   - Reduces damage from Dragon-type moves by 50%
#   - Misty Surge ability sets terrain on switch-in

# PSYCHIC TERRAIN:
#   - Psychic-type moves deal 1.3x damage
#   - Prevents priority moves from affecting grounded Pokemon
#   - Expanding Force deals 1.5x damage and hits all opponents
#   - Psychic Surge ability sets terrain on switch-in

# ═══════════════════════════════════════════════════════════════════
# ENTRY HAZARDS REFERENCE
# ═══════════════════════════════════════════════════════════════════
# Entry hazards damage Pokemon when they switch into battle.

# STEALTH ROCK:
#   - Damages based on type effectiveness against Rock
#   - 4x weak: 50% HP (Bug, Fire, Flying, Ice)
#   - 2x weak: 25% HP (Normal, Fighting, Poison, Ground, etc.)
#   - Neutral: 12.5% HP
#   - Resists: 6.25% HP (Steel)
#   - Immune: 0% HP (Rock, Ground with Levitate)
#   - Can be set multiple times (no stacking)
#   - Removed by Rapid Spin, Defog, Court Change

# SPIKES:
#   - Can be set up to 3 layers
#   - 1 layer: 1/8 HP damage
#   - 2 layers: 1/6 HP damage
#   - 3 layers: 1/4 HP damage
#   - Does not affect Flying/Levitate Pokemon
#   - Removed by Rapid Spin, Defog, Court Change

# TOXIC SPIKES:
#   - Can be set up to 2 layers
#   - 1 layer: Poisons switching Pokemon
#   - 2 layers: Badly poisons switching Pokemon
#   - Does not affect Poison/Steel/Flying/Levitate Pokemon
#   - Removed by Rapid Spin, Defog, Court Change
#   - Poison-type Pokemon absorb and remove Toxic Spikes

# STICKY WEB:
#   - Lowers Speed of switching Pokemon by 1 stage
#   - Does not affect Flying/Levitate Pokemon
#   - Removed by Rapid Spin, Defog, Court Change

# ═══════════════════════════════════════════════════════════════════
# CRITICAL HIT REFERENCE
# ═══════════════════════════════════════════════════════════════════
# Critical hits deal 1.5x damage and ignore negative stat stages.

# Critical Hit Ratios:
#   Normal: 1/24 (4.17%)
#   +1 stage (Focus Energy, Razor Leaf): 1/8 (12.5%)
#   +2 stages: 1/2 (50%)
#   +3 stages: 1/1 (100%)
#   Always crit moves (Frost Breath, Storm Throw): 1/1 (100%)

# Abilities that affect critical hits:
#   Super Luck: +1 stage to critical hit ratio
#   Sniper: Critical hits deal 2.25x damage instead of 1.5x
#   Battle Armor: Prevents critical hits
#   Shell Armor: Prevents critical hits

# Items that affect critical hits:
#   Scope Lens: +1 stage to critical hit ratio
#   Razor Claw: +1 stage to critical hit ratio (specific Pokemon)
#   Dire Hit: +1 stage to critical hit ratio (temporary)

# ═══════════════════════════════════════════════════════════════════
# DAMAGE CALCULATION FORMULA
# ═══════════════════════════════════════════════════════════════════
# The Pokemon damage formula is as follows:

# Damage = ((((2 * Level / 5 + 2) * Power * A / D) / 50) + 2)
#          * Modifier

# Where:
#   Level = Attacker's level
#   Power = Move's base power
#   A = Attacker's Attack or Special Attack stat
#   D = Defender's Defense or Special Defense stat
#   Modifier = Product of all applicable multipliers:
#     - Type effectiveness (0, 0.25, 0.5, 1, 2, 4)
#     - STAB (1.5x if move type matches Pokemon type)
#     - Critical hit (1.5x)
#     - Weather (1.5x or 0.5x)
#     - Random factor (0.85 to 1.0)
#     - Burn (0.5x for physical attacks)
#     - Other multipliers (abilities, items, etc.)

# The final damage is rounded down to the nearest integer.
# Minimum damage is 1 (unless the move has 0 power or no effect).

# ═══════════════════════════════════════════════════════════════════
# ABILITY INTERACTIONS WITH MOVES
# ═══════════════════════════════════════════════════════════════════
# Some abilities interact with specific move effects.

# DAMAGE-RELATED ABILITIES:
#   Adaptability: STAB increased from 1.5x to 2x
#   Analytic: +30% damage if user moves last
#   Aura Break: Reverses aura abilities
#   Dark Aura: +33% Dark-type move damage
#   Fairy Aura: +33% Fairy-type move damage
#   Flare Boost: +50% special damage while burned
#   Guts: +50% physical damage while statused
#   Hustle: +50% physical damage, -20% accuracy
#   Iron Fist: +20% punching move damage
#   Megalauncher: +50% pulse move damage
#   Motor Drive: Immune to Electric, +1 Speed when hit
#   No Guard: All moves hit (100% accuracy)
#   Normalize: All moves become Normal-type
#   Punk Rock: +30% sound move damage, -50% sound damage taken
#   Reckless: +20% recoil move damage
#   Sand Force: +30% Rock/Ground/Steel damage in sandstorm
#   Sheer Force: +30% damage, removes secondary effects
#   Strong Jaw: +50% biting move damage
#   Technician: +50% damage for moves with 60 or less base power
#   Tinted Lens: +50% damage for not very effective moves
#   Tough Claws: +30% contact move damage
#   Water Bubble: +100% Water damage, prevents burn, halves Fire damage

# DEFENSIVE ABILITIES:
#   Bulletproof: Immune to ball/bomb moves
#   Clear Body: Prevents stat reduction
#   Contrary: Reverses stat changes
#   Damp: Prevents self-destruct moves
#   Filter: -25% super effective damage
#   Fluffy: -50% contact damage, +100% Fire damage
#   Fur Coat: -50% physical damage
#   Heatproof: -50% Fire damage
#   Ice Scales: -50% special damage
#   Marvel Scale: +50% Defense while statused
#   Multiscale: -50% damage at full HP
#   Prism Armor: -25% super effective damage
#   Purifying Salt: Immune to status, -50% Ghost damage
#   Shadow Shield: -25% damage at full HP
#   Solid Rock: -25% super effective damage
#   Thick Fat: -50% Fire/Ice damage
#   Unaware: Ignores opponent's stat changes
#   Water Bubble: -50% Fire damage
#   Water Compaction: +2 Defense when hit by Water
#   Well-Baked Body: Immune to Fire, +1 Defense when hit

# STATUS-RELATED ABILITIES:
#   Comatose: Always asleep, can use any move
#   Insomnia: Prevents sleep
#   Vital Spirit: Prevents sleep
#   Early Bird: Wakes up faster from sleep
#   Limber: Prevents paralysis
#   Immunity: Prevents poison
#   Water Veil: Prevents burn
#   Magma Armor: Prevents freeze, thaws faster
#   Oblivious: Prevents infatuation
#   Own Tempo: Prevents confusion
#   Inner Focus: Prevents flinch
#   Shield Dust: Prevents secondary effects
#   Sweet Veil: Prevents sleep for team
#   Flower Veil: Protects Grass allies from status/stat reduction
#   Leaf Guard: Prevents status in sunny weather
#   Hydration: Cures status in rain
#   Natural Cure: Cures status on switch
#   Shed Skin: 33% chance to cure status each turn
#   Healer: 30% chance to cure ally's status

# MOVEMENT-RELATED ABILITIES:
#   Arena Trap: Prevents grounded Pokemon from switching
#   Magnet Pull: Prevents Steel-type Pokemon from switching
#   Shadow Tag: Prevents Pokemon from switching
#   Suction Cups: Prevents forced switching
#   Sticky Hold: Prevents item removal
#   Speed Boost: +1 Speed each turn
#   Swift Swim: +100% Speed in rain
#   Chlorophyll: +100% Speed in sun
#   Sand Rush: +100% Speed in sandstorm
#   Slush Rush: +100% Speed in hail/snow
#   Surge Surfer: +100% Speed on Electric Terrain
#   Quick Feet: +50% Speed while statused
#   Unburden: +100% Speed when item is used/lost
#   Rattled: +1 Speed when hit by Bug/Dark/Ghost

# OTHER ABILITIES:
#   Color Change: Changes type to match last move hit by
#   Protean/Libero: Changes type to match move used
#   Imposter: Transforms on switch-in
#   Trace: Copies opponent's ability on switch-in
#   Role Play: Copies opponent's ability
#   Skill Swap: Swaps abilities with opponent
#   Worry Seed: Changes opponent's ability to Insomnia
#   Simple: Doubles stat changes
#   Moody: Randomly raises one stat, lowers another each turn
#   Slow Start: Halves Attack and Speed for 5 turns
#   Truant: Can only attack every other turn
#   Klutz: Negates held item effects
#   Unnerve: Prevents opponent from eating Berries
#   Frisk: Reveals opponent's held item on switch-in
#   Forewarn: Reveals opponent's strongest move on switch-in
#   Telepathy: Avoids damage from ally's moves
#   Friend Guard: Reduces damage to allies by 25%
#   Weak Armor: +1 Speed, -1 Defense when hit physically
#   Stamina: +1 Defense when hit
#   Justified: +1 Attack when hit by Dark
#   Rattled: +1 Speed when hit by Bug/Dark/Ghost
#   Wind Rider: +1 Attack when Tailwind is used, immune to Wind
#   Good as Gold: Immune to status moves
#   Earth Eater: Heals 25% HP when hit by Ground
#   Cud Chew: Consumes Berry twice
#   Supersweet Syrup: Lowers opponent's evasion on switch-in
#   Hospitalize: Heals ally's status when switching in
#   Mind's Eye: Ignores accuracy changes, hits Ghost with Normal/Fighting
#   Scrappy: Hits Ghost with Normal/Fighting
#   Mold Breaker: Ignores opponent's ability
#   Teravolt: Ignores opponent's ability
#   Turboblaze: Ignores opponent's ability
#   Stalwart: Ignores redirecting effects
#   Propeller Tail: Ignores redirecting effects
#   Infiltrator: Bypasses Substitute and barriers
#   Pickpocket: Steals item when hit by contact move
#   Symbiosis: Passes item to ally when ally uses theirs
#   Harvest: 50% chance to restore used Berry each turn (100% in sun)
#   Magician: Steals item when using a move
#   Receiver: Copies fainted ally's ability
#   Power of Alchemy: Copies fainted ally's ability
#   Battle Bond: Transforms after knocking out opponent
#   Disguise: Blocks first hit (Mimikyu)
#   Ice Face: Blocks first physical hit (Eiscue)
#   Zero to Hero: Transforms when switching out (Palafin)
#   Commander: Enters Dondozo's mouth (Tatsugiri)
#   Costar: Copies ally's stat changes (Tinkaton)
#   Poison Puppeteer: Poisons confused targets (Pecharunt)
#   Toxic Chain: May badly poison on contact (Glimmora)
#   Embody Aspect: Raises a stat (Ogerpon)
#   Supreme Overlord: +10% damage per fainted ally (Kingambit)
#   Protosynthesis: Boosts highest stat in sun (Paradox)
#   Quark Drive: Boosts highest stat on Electric Terrain (Paradox)
#   Hadron Engine: Creates Electric Terrain, boosts Sp. Atk (Iron Leaves)
#   Orichalcum Pulse: Creates sun, boosts Attack (Koraidon)
#   Transistor: +30% Electric damage (Regieleki)
#   Dragon's Maw: +30% Dragon damage (Regidrago)
#   Steelworker: +30% Steel damage (Aegislash)
#   Steely Spirit: +50% Steel damage for team (Copperajah)
#   Battery: +30% ally's special damage (Togedemaru)
#   Steam Engine: +600% Speed when hit by Fire/Water (Coalossal)
#   Wandering Spirit: Swaps abilities on contact (Yamask)
#   Gorilla Tactics: +50% Attack, locked to one move (Gorilla)
#   Dauntless Shield: +1 Defense on switch-in (Zacian)
#   Intrepid Sword: +1 Attack on switch-in (Zamazenta)
#   Pressure: Doubles opponent's PP usage
#   Snow Warning: Sets hail/snow on switch-in
#   Sand Stream: Sets sandstorm on switch-in
#   Drizzle: Sets rain on switch-in
#   Drought: Sets sun on switch-in
#   Desolate Land: Sets harsh sunlight (primal Groudon)
#   Primordial Sea: Sets heavy rain (primal Kyogre)
#   Delta Stream: Sets strong winds (Mega Rayquaza)
#   Air Lock: Negates weather effects (Rayquaza)
#   Cloud Nine: Negates weather effects
#   Shell Bell: Heals 1/8 of damage dealt
#   Leftovers: Heals 1/16 HP per turn
#   Black Sludge: Heals Poison types, damages others
#   Rocky Helmet: Damages contact attackers
#   Iron Barbs: Damages contact attackers
#   Rough Skin: Damages contact attackers
#   Liquid Ooze: Damages draining moves
#   Aftermath: Damages attacker when knocked out by contact
#   Explosion: Damages all Pokemon when knocked out
#   Perish Body: Both Pokemon faint in 3 turns when hit by contact
#   Wimp Out: Switches out when below 50% HP
#   Emergency Exit: Switches out when below 50% HP
#   RKS System: Changes type based on held Memory (Silvally)
#   Multitype: Changes type based on held Plate (Arceus)
#   Zen Mode: Transforms when below 50% HP (Darmanitan)
#   Stance Change: Changes form based on move used (Aegislash)
#   Power Construct: Transforms when below 50% HP (Zygarde)
#   Schooling: Transforms when above 25% HP (Wishiwashi)
#   Shields Down: Transforms when below 50% HP (Minior)
#   Battle Bond: Transforms after KO (Greninja)
#   Power of Alchemy: Copies fainted ally's ability
#   Receiver: Copies fainted ally's ability
#   Anticipation: Reveals if opponent has super effective move
#   Download: Raises Attack or Sp. Atk based on opponent's Defense
#   Moxie: +1 Attack after knocking out opponent
#   Beast Boost: Raises highest stat after knocking out opponent
#   Grim Neigh: +1 Sp. Atk after knocking out opponent
#   Chilling Neigh: +1 Attack after knocking out opponent
#   As One: Combines two abilities (Calyrex)
#   Neutron Star: Combines two abilities (Terapagos)
#   Tera Shift: Changes to Terastal form (Terapagos)
#   Tera Shell: All moves not very effective at full HP (Terapagos)
#   Teraform Zero: Clears weather and terrain (Terapagos)
#   Supersweet Syrup: Lowers opponent's evasion on switch-in
#   Mind's Eye: Ignores accuracy changes
#   Scrappy: Hits Ghost with Normal/Fighting
#   Cud Chew: Consumes Berry twice
#   Armor Tail: Protects allies from priority moves
#   Good as Gold: Immune to status moves
#   Earth Eater: Heals when hit by Ground
#   Well-Baked Body: Immune to Fire, +1 Defense
#   Wind Rider: Immune to Wind, +1 Attack on Tailwind
#   Toxic Debris: Sets Toxic Spikes when hit physically
#   Lingering Aroma: Spreads ability on contact
#   Mycelium Might: Status moves ignore ability, go last
#   Opportunist: Copies stat boosts
#   Purifying Salt: Immune to status, -50% Ghost damage
#   Seed Sower: Sets Grassy Terrain when hit
#   Sharpness: +50% slicing move damage
#   Silk Screen: Sets Light Screen on switch-in
#   Stamina: +1 Defense when hit
#   Supreme Overlord: +10% damage per fainted ally
#   Sword of Ruin: Lowers all Pokemon's Defense
#   Tablet of Ruin: Lowers all Pokemon's Attack
#   Vessel of Ruin: Lowers all Pokemon's Sp. Atk
#   Beads of Ruin: Lowers all Pokemon's Sp. Def
#   Thermal Exchange: +1 Attack when hit by Fire
#   Unseen Fist: Contact moves bypass Protect
#   Water Bubble: +100% Water damage, prevents burn
#   Zero to Hero: Transforms when switching out
