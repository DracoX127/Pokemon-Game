"""
Tactical Move System: Types and Move Data
"""

TYPE_CHART = {
    "Normal":   {"Rock": 0.5, "Ghost": 0.0, "Steel": 0.5},
    "Fire":     {"Fire": 0.5, "Water": 0.5, "Grass": 2.0, "Ice": 2.0, "Bug": 2.0, "Rock": 0.5, "Dragon": 0.5, "Steel": 2.0},
    "Water":    {"Fire": 2.0, "Water": 0.5, "Grass": 0.5, "Ground": 2.0, "Rock": 2.0, "Dragon": 0.5},
    "Grass":    {"Fire": 0.5, "Water": 2.0, "Grass": 0.5, "Poison": 0.5, "Ground": 2.0, "Flying": 0.5, "Bug": 0.5, "Rock": 2.0, "Dragon": 0.5, "Steel": 0.5},
    "Electric": {"Water": 2.0, "Grass": 0.5, "Electric": 0.5, "Ground": 0.0, "Flying": 2.0, "Dragon": 0.5},
    "Ice":      {"Fire": 0.5, "Water": 0.5, "Grass": 2.0, "Ice": 0.5, "Ground": 2.0, "Flying": 2.0, "Dragon": 2.0, "Steel": 0.5},
    "Fighting": {"Normal": 2.0, "Ice": 2.0, "Rock": 2.0, "Dark": 2.0, "Steel": 2.0, "Poison": 0.5, "Flying": 0.5, "Psychic": 0.5, "Bug": 0.5, "Ghost": 0.0, "Fairy": 0.5},
    "Poison":   {"Grass": 2.0, "Poison": 0.5, "Ground": 0.5, "Rock": 0.5, "Ghost": 0.5, "Steel": 0.0, "Fairy": 2.0},
    "Ground":   {"Fire": 2.0, "Electric": 2.0, "Grass": 0.5, "Poison": 2.0, "Flying": 0.0, "Bug": 0.5, "Rock": 2.0, "Steel": 2.0},
    "Flying":   {"Grass": 2.0, "Electric": 0.5, "Fighting": 2.0, "Bug": 2.0, "Rock": 0.5, "Steel": 0.5},
    "Psychic":  {"Fighting": 2.0, "Poison": 2.0, "Psychic": 0.5, "Dark": 0.0, "Steel": 0.5},
    "Bug":      {"Fire": 0.5, "Grass": 2.0, "Fighting": 0.5, "Poison": 0.5, "Flying": 0.5, "Psychic": 2.0, "Ghost": 0.5, "Dark": 2.0, "Steel": 0.5, "Fairy": 0.5},
    "Rock":     {"Fire": 2.0, "Ice": 2.0, "Fighting": 0.5, "Ground": 0.5, "Flying": 2.0, "Bug": 2.0, "Steel": 0.5},
    "Ghost":    {"Normal": 0.0, "Psychic": 2.0, "Ghost": 2.0, "Dark": 0.5},
    "Dragon":   {"Dragon": 2.0, "Steel": 0.5, "Fairy": 0.0},
    "Dark":     {"Fighting": 0.5, "Psychic": 2.0, "Ghost": 2.0, "Dark": 0.5, "Fairy": 0.5},
    "Steel":    {"Fire": 0.5, "Water": 0.5, "Electric": 0.5, "Ice": 2.0, "Rock": 2.0, "Steel": 0.5, "Fairy": 2.0},
    "Fairy":    {"Fire": 0.5, "Fighting": 2.0, "Poison": 0.5, "Dragon": 2.0, "Dark": 2.0, "Steel": 0.5}
}

MOVES = {
    # --- Normal ---
    "Tackle":       {"type": "Normal", "power": 40,  "acc": 100, "pp": 35, "category": "Physical", "priority": 0, "effect": None},
    "Scratch":      {"type": "Normal", "power": 40,  "acc": 100, "pp": 35, "category": "Physical", "priority": 0, "effect": None},
    "Pound":        {"type": "Normal", "power": 40,  "acc": 100, "pp": 35, "category": "Physical", "priority": 0, "effect": None},
    "Quick Attack": {"type": "Normal", "power": 40,  "acc": 100, "pp": 30, "category": "Physical", "priority": 1, "effect": None},
    "Fury Swipes":  {"type": "Normal", "power": 18,  "acc": 80,  "pp": 15, "category": "Physical", "priority": 0, "effect": None},
    "Stomp":        {"type": "Normal", "power": 65,  "acc": 100, "pp": 20, "category": "Physical", "priority": 0, "effect": {"status": "Flinch", "chance": 0.3}},
    "Headbutt":     {"type": "Normal", "power": 70,  "acc": 100, "pp": 15, "category": "Physical", "priority": 0, "effect": {"status": "Flinch", "chance": 0.3}},
    "Slash":        {"type": "Normal", "power": 70,  "acc": 100, "pp": 20, "category": "Physical", "priority": 0, "effect": None},
    "Body Slam":    {"type": "Normal", "power": 85,  "acc": 100, "pp": 15, "category": "Physical", "priority": 0, "effect": {"status": "Paralyze", "chance": 0.3}},
    "Take Down":    {"type": "Normal", "power": 90,  "acc": 85,  "pp": 20, "category": "Physical", "priority": 0, "effect": {"recoil": 0.25}},
    "Double-Edge":  {"type": "Normal", "power": 120, "acc": 100, "pp": 15, "category": "Physical", "priority": 0, "effect": {"recoil": 0.33}},
    "Thrash":       {"type": "Normal", "power": 120, "acc": 100, "pp": 10, "category": "Physical", "priority": 0, "effect": {"confuse_after": True}},
    "Giga Impact":  {"type": "Normal", "power": 150, "acc": 90,  "pp": 5,  "category": "Physical", "priority": 0, "effect": {"recharge": True}},
    "Hyper Beam":   {"type": "Normal", "power": 150, "acc": 90,  "pp": 5,  "category": "Special",  "priority": 0, "effect": {"recharge": True}},
    "Leer":         {"type": "Normal", "power": 0,   "acc": 100, "pp": 30, "category": "Status",   "priority": 0, "effect": {"target": {"dm": -1}}},
    "Growl":        {"type": "Normal", "power": 0,   "acc": 100, "pp": 40, "category": "Status",   "priority": 0, "effect": {"target": {"dm": -1}}},
    "Tail Whip":    {"type": "Normal", "power": 0,   "acc": 100, "pp": 30, "category": "Status",   "priority": 0, "effect": {"target": {"dm": -1}}},
    "Defense Curl": {"type": "Normal", "power": 0,   "acc": 100, "pp": 40, "category": "Status",   "priority": 0, "effect": {"self": {"def": 1}}},
    "Swords Dance": {"type": "Normal", "power": 0,   "acc": 100, "pp": 20, "category": "Status",   "priority": 0, "effect": {"self": {"dm": 2}}},
    "Recover":      {"type": "Normal", "power": 0,   "acc": 100, "pp": 10, "category": "Status",   "priority": 0, "effect": {"heal": 0.5}},
    "Protect":      {"type": "Normal", "power": 0,   "acc": 100, "pp": 10, "category": "Status",   "priority": 4, "effect": {"protect": True}},
    "Substitute":   {"type": "Normal", "power": 0,   "acc": 100, "pp": 10, "category": "Status",   "priority": 0, "effect": {"substitute": 0.25}},

    # --- Fire ---
    "Ember":        {"type": "Fire",   "power": 40,  "acc": 100, "pp": 25, "category": "Special",  "priority": 0, "effect": {"status": "Burn", "chance": 0.1}},
    "Flame Wheel":  {"type": "Fire",   "power": 60,  "acc": 100, "pp": 25, "category": "Physical", "priority": 0, "effect": {"status": "Burn", "chance": 0.1}},
    "Flame Charge": {"type": "Fire",   "power": 50,  "acc": 100, "pp": 20, "category": "Physical", "priority": 0, "effect": {"self": {"speed": 1}}},
    "Fire Spin":    {"type": "Fire",   "power": 35,  "acc": 85,  "pp": 15, "category": "Special",  "priority": 0, "effect": {"trap": True}},
    "Flamethrower": {"type": "Fire",   "power": 90,  "acc": 100, "pp": 15, "category": "Special",  "priority": 0, "effect": {"status": "Burn", "chance": 0.1}},
    "Heat Wave":    {"type": "Fire",   "power": 95,  "acc": 90,  "pp": 10, "category": "Special",  "priority": 0, "effect": {"status": "Burn", "chance": 0.1}},
    "Fire Blast":   {"type": "Fire",   "power": 110, "acc": 85,  "pp": 5,  "category": "Special",  "priority": 0, "effect": {"status": "Burn", "chance": 0.1}},
    "Will-o-Wisp":  {"type": "Fire",   "power": 0,   "acc": 85,  "pp": 15, "category": "Status",   "priority": 0, "effect": {"status": "Burn", "chance": 1.0}},

    # --- Water ---
    "Water Gun":    {"type": "Water",  "power": 40,  "acc": 100, "pp": 25, "category": "Special",  "priority": 0, "effect": None},
    "Bubble Beam":  {"type": "Water",  "power": 65,  "acc": 100, "pp": 20, "category": "Special",  "priority": 0, "effect": {"target": {"speed": -1}, "chance": 0.1}},
    "Water Pulse":  {"type": "Water",  "power": 60,  "acc": 100, "pp": 20, "category": "Special",  "priority": 0, "effect": {"status": "Confuse", "chance": 0.2}},
    "Scald":        {"type": "Water",  "power": 80,  "acc": 100, "pp": 15, "category": "Special",  "priority": 0, "effect": {"status": "Burn", "chance": 0.3}},
    "Surf":         {"type": "Water",  "power": 90,  "acc": 100, "pp": 15, "category": "Special",  "priority": 0, "effect": None},
    "Aqua Tail":    {"type": "Water",  "power": 90,  "acc": 90,  "pp": 10, "category": "Physical", "priority": 0, "effect": None},
    "Hydro Pump":   {"type": "Water",  "power": 110, "acc": 80,  "pp": 5,  "category": "Special",  "priority": 0, "effect": None},

    # --- Grass ---
    "Vine Whip":    {"type": "Grass",  "power": 45,  "acc": 100, "pp": 25, "category": "Physical", "priority": 0, "effect": None},
    "Absorb":       {"type": "Grass",  "power": 20,  "acc": 100, "pp": 25, "category": "Special",  "priority": 0, "effect": {"heal": 0.5}},
    "Mega Drain":   {"type": "Grass",  "power": 40,  "acc": 100, "pp": 15, "category": "Special",  "priority": 0, "effect": {"heal": 0.5}},
    "Razor Leaf":   {"type": "Grass",  "power": 55,  "acc": 95,  "pp": 25, "category": "Physical", "priority": 0, "effect": None},
    "Seed Bomb":    {"type": "Grass",  "power": 80,  "acc": 100, "pp": 15, "category": "Physical", "priority": 0, "effect": None},
    "Energy Ball":  {"type": "Grass",  "power": 90,  "acc": 100, "pp": 10, "category": "Special",  "priority": 0, "effect": {"target": {"sp_def": -1}, "chance": 0.1}},
    "Solar Beam":   {"type": "Grass",  "power": 120, "acc": 100, "pp": 10, "category": "Special",  "priority": 0, "effect": {"charge": True}},
    "Leaf Storm":   {"type": "Grass",  "power": 130, "acc": 90,  "pp": 5,  "category": "Special",  "priority": 0, "effect": {"self": {"dm": -2}}},
    "Sleep Powder": {"type": "Grass",  "power": 0,   "acc": 75,  "pp": 15, "category": "Status",   "priority": 0, "effect": {"status": "Sleep", "chance": 1.0}},
    "Stun Spore":   {"type": "Grass",  "power": 0,   "acc": 75,  "pp": 30, "category": "Status",   "priority": 0, "effect": {"status": "Paralyze", "chance": 1.0}},
    "Poison Powder": {"type": "Grass", "power": 0,   "acc": 75,  "pp": 35, "category": "Status",   "priority": 0, "effect": {"status": "Poison", "chance": 1.0}},
    "Leech Seed":   {"type": "Grass",  "power": 0,   "acc": 90,  "pp": 10, "category": "Status",   "priority": 0, "effect": {"leech_seed": True}},

    # --- Electric ---
    "Thunder Shock":{"type": "Electric","power": 40,  "acc": 100, "pp": 30, "category": "Special",  "priority": 0, "effect": {"status": "Paralyze", "chance": 0.1}},
    "Nuzzle":       {"type": "Electric","power": 20,  "acc": 100, "pp": 20, "category": "Physical", "priority": 0, "effect": {"status": "Paralyze", "chance": 1.0}},
    "Spark":        {"type": "Electric","power": 65,  "acc": 100, "pp": 20, "category": "Physical", "priority": 0, "effect": {"status": "Paralyze", "chance": 0.3}},
    "Thunderbolt":  {"type": "Electric","power": 90,  "acc": 100, "pp": 15, "category": "Special",  "priority": 0, "effect": {"status": "Paralyze", "chance": 0.1}},
    "Thunder":      {"type": "Electric","power": 110, "acc": 70,  "pp": 10, "category": "Special",  "priority": 0, "effect": {"status": "Paralyze", "chance": 0.3}},
    "Thunder Wave": {"type": "Electric","power": 0,   "acc": 90,  "pp": 20, "category": "Status",   "priority": 0, "effect": {"status": "Paralyze", "chance": 1.0}},
    "Volt Switch":  {"type": "Electric","power": 70,  "acc": 100, "pp": 20, "category": "Special",  "priority": 0, "effect": {"switch_user": True}},

    # --- Ice ---
    "Powder Snow":  {"type": "Ice",    "power": 40,  "acc": 100, "pp": 25, "category": "Special",  "priority": 0, "effect": {"status": "Freeze", "chance": 0.1}},
    "Ice Shard":    {"type": "Ice",    "power": 40,  "acc": 100, "pp": 30, "category": "Physical", "priority": 1, "effect": None},
    "Icy Wind":     {"type": "Ice",    "power": 55,  "acc": 95,  "pp": 15, "category": "Special",  "priority": 0, "effect": {"target": {"speed": -1}}},
    "Ice Beam":     {"type": "Ice",    "power": 90,  "acc": 100, "pp": 15, "category": "Special",  "priority": 0, "effect": {"status": "Freeze", "chance": 0.1}},
    "Blizzard":     {"type": "Ice",    "power": 110, "acc": 70,  "pp": 5,  "category": "Special",  "priority": 0, "effect": {"status": "Freeze", "chance": 0.1}},

    # --- Fighting ---
    "Low Kick":     {"type": "Fighting","power": 0,   "acc": 100, "pp": 20, "category": "Physical", "priority": 0, "effect": None},
    "Brick Break":  {"type": "Fighting","power": 75,  "acc": 100, "pp": 15, "category": "Physical", "priority": 0, "effect": None},
    "Close Combat": {"type": "Fighting","power": 120, "acc": 100, "pp": 5,  "category": "Physical", "priority": 0, "effect": {"self": {"dm": -1, "def": -1}}},
    "Focus Blast":  {"type": "Fighting","power": 120, "acc": 70,  "pp": 5,  "category": "Special",  "priority": 0, "effect": {"target": {"sp_def": -1}, "chance": 0.1}},
    "Bulk Up":      {"type": "Fighting","power": 0,   "acc": 100, "pp": 20, "category": "Status",   "priority": 0, "effect": {"self": {"dm": 1, "def": 1}}},

    # --- Poison ---
    "Poison Sting": {"type": "Poison", "power": 15,  "acc": 100, "pp": 35, "category": "Physical", "priority": 0, "effect": {"status": "Poison", "chance": 0.3}},
    "Poison Jab":   {"type": "Poison", "power": 80,  "acc": 100, "pp": 20, "category": "Physical", "priority": 0, "effect": {"status": "Poison", "chance": 0.3}},
    "Sludge Bomb":  {"type": "Poison", "power": 90,  "acc": 100, "pp": 10, "category": "Special",  "priority": 0, "effect": {"status": "Poison", "chance": 0.3}},
    "Toxic":        {"type": "Poison", "power": 0,   "acc": 90,  "pp": 10, "category": "Status",   "priority": 0, "effect": {"status": "Badly Poison", "chance": 1.0}},

    # --- Ground ---
    "Mud-Slap":     {"type": "Ground", "power": 20,  "acc": 100, "pp": 20, "category": "Special",  "priority": 0, "effect": {"target": {"acc": -1}}},
    "Bulldoze":     {"type": "Ground", "power": 60,  "acc": 100, "pp": 20, "category": "Physical", "priority": 0, "effect": {"target": {"speed": -1}}},
    "Drill Run":    {"type": "Ground", "power": 80,  "acc": 95,  "pp": 10, "category": "Physical", "priority": 0, "effect": None},
    "Earthquake":   {"type": "Ground", "power": 100, "acc": 100, "pp": 10, "category": "Physical", "priority": 0, "effect": None},
    "Spikes":       {"type": "Ground", "power": 0,   "acc": 100, "pp": 20, "category": "Status",   "priority": 0, "effect": {"hazard": "Spikes"}},
    "Sand Attack":  {"type": "Ground", "power": 0,   "acc": 100, "pp": 15, "category": "Status",   "priority": 0, "effect": {"target": {"acc": -1}}},

    # --- Flying ---
    "Gust":         {"type": "Flying", "power": 40,  "acc": 100, "pp": 35, "category": "Special",  "priority": 0, "effect": None},
    "Wing Attack":  {"type": "Flying", "power": 60,  "acc": 100, "pp": 35, "category": "Physical", "priority": 0, "effect": None},
    "Aerial Ace":   {"type": "Flying", "power": 60,  "acc": 100, "pp": 20, "category": "Physical", "priority": 0, "effect": None},
    "Air Slash":    {"type": "Flying", "power": 75,  "acc": 95,  "pp": 15, "category": "Special",  "priority": 0, "effect": {"status": "Flinch", "chance": 0.3}},
    "Hurricane":    {"type": "Flying", "power": 110, "acc": 70,  "pp": 10, "category": "Special",  "priority": 0, "effect": {"status": "Confuse", "chance": 0.3}},
    "Roost":        {"type": "Flying", "power": 0,   "acc": 100, "pp": 10, "category": "Status",   "priority": 0, "effect": {"heal": 0.5}},

    # --- Psychic ---
    "Confusion":    {"type": "Psychic","power": 50,  "acc": 100, "pp": 25, "category": "Special",  "priority": 0, "effect": {"status": "Confuse", "chance": 0.1}},
    "Psychic":      {"type": "Psychic","power": 90,  "acc": 100, "pp": 15, "category": "Special",  "priority": 0, "effect": {"target": {"sp_def": -1}, "chance": 0.1}},
    "Zen Headbutt": {"type": "Psychic","power": 80,  "acc": 90,  "pp": 15, "category": "Physical", "priority": 0, "effect": {"status": "Flinch", "chance": 0.2}},
    "Agility":      {"type": "Psychic","power": 0,   "acc": 100, "pp": 30, "category": "Status",   "priority": 0, "effect": {"self": {"speed": 2}}},
    "Amnesia":      {"type": "Psychic","power": 0,   "acc": 100, "pp": 20, "category": "Status",   "priority": 0, "effect": {"self": {"sp_def": 2}}},
    "Hypnosis":     {"type": "Psychic","power": 0,   "acc": 60,  "pp": 20, "category": "Status",   "priority": 0, "effect": {"status": "Sleep", "chance": 1.0}},
    "Rest":         {"type": "Psychic","power": 0,   "acc": 100, "pp": 10, "category": "Status",   "priority": 0, "effect": {"rest": True}},
    "Calm Mind":    {"type": "Psychic","power": 0,   "acc": 100, "pp": 20, "category": "Status",   "priority": 0, "effect": {"self": {"dm": 1, "sp_def": 1}}},

    # --- Bug ---
    "Bug Bite":     {"type": "Bug",    "power": 60,  "acc": 100, "pp": 20, "category": "Physical", "priority": 0, "effect": None},
    "Signal Beam":  {"type": "Bug",    "power": 75,  "acc": 100, "pp": 15, "category": "Special",  "priority": 0, "effect": {"status": "Confuse", "chance": 0.1}},
    "X-Scissor":    {"type": "Bug",    "power": 80,  "acc": 100, "pp": 15, "category": "Physical", "priority": 0, "effect": None},
    "Megahorn":     {"type": "Bug",    "power": 120, "acc": 85,  "pp": 10, "category": "Physical", "priority": 0, "effect": None},
    "Silver Wind":  {"type": "Bug",    "power": 60,  "acc": 100, "pp": 5,  "category": "Special",  "priority": 0, "effect": {"self": {"dm": 1, "def": 1, "speed": 1, "sp_def": 1, "acc": 1}, "chance": 0.1}},
    "String Shot":  {"type": "Bug",    "power": 0,   "acc": 95,  "pp": 40, "category": "Status",   "priority": 0, "effect": {"target": {"speed": -1}}},
    "U-turn":       {"type": "Bug",    "power": 70,  "acc": 100, "pp": 20, "category": "Physical", "priority": 0, "effect": {"switch_user": True}},

    # --- Rock ---
    "Rock Throw":   {"type": "Rock",   "power": 50,  "acc": 90,  "pp": 20, "category": "Physical", "priority": 0, "effect": None},
    "Rollout":      {"type": "Rock",   "power": 30,  "acc": 90,  "pp": 20, "category": "Physical", "priority": 0, "effect": {"multi_turn": True}},
    "Rock Slide":   {"type": "Rock",   "power": 75,  "acc": 90,  "pp": 10, "category": "Physical", "priority": 0, "effect": {"status": "Flinch", "chance": 0.3}},
    "Stone Edge":   {"type": "Rock",   "power": 100, "acc": 80,  "pp": 5,  "category": "Physical", "priority": 0, "effect": None},
    "Stealth Rock": {"type": "Rock",   "power": 0,   "acc": 100, "pp": 20, "category": "Status",   "priority": 0, "effect": {"hazard": "Stealth Rock"}},

    # --- Ghost ---
    "Astonish":     {"type": "Ghost",  "power": 30,  "acc": 100, "pp": 25, "category": "Physical", "priority": 0, "effect": {"status": "Flinch", "chance": 0.3}},
    "Lick":         {"type": "Ghost",  "power": 30,  "acc": 100, "pp": 30, "category": "Physical", "priority": 0, "effect": {"status": "Paralyze", "chance": 0.3}},
    "Ominous Wind": {"type": "Ghost",  "power": 60,  "acc": 100, "pp": 5,  "category": "Special",  "priority": 0, "effect": {"self": {"dm": 1, "def": 1, "speed": 1, "sp_def": 1, "acc": 1}, "chance": 0.1}},
    "Shadow Ball":  {"type": "Ghost",  "power": 80,  "acc": 100, "pp": 15, "category": "Special",  "priority": 0, "effect": {"target": {"sp_def": -1}, "chance": 0.2}},
    "Curse":        {"type": "Ghost",  "power": 0,   "acc": 100, "pp": 10, "category": "Status",   "priority": 0, "effect": {"curse": True}},
    "Destiny Bond": {"type": "Ghost",  "power": 0,   "acc": 100, "pp": 5,  "category": "Status",   "priority": 0, "effect": {"destiny_bond": True}},

    # --- Dragon ---
    "Twister":      {"type": "Dragon", "power": 40,  "acc": 100, "pp": 20, "category": "Special",  "priority": 0, "effect": {"status": "Flinch", "chance": 0.2}},
    "Dragon Pulse": {"type": "Dragon", "power": 85,  "acc": 100, "pp": 10, "category": "Special",  "priority": 0, "effect": None},
    "Draco Meteor": {"type": "Dragon", "power": 130, "acc": 90,  "pp": 5,  "category": "Special",  "priority": 0, "effect": {"self": {"dm": -2}}},
    "Dragon Dance": {"type": "Dragon", "power": 0,   "acc": 100, "pp": 20, "category": "Status",   "priority": 0, "effect": {"self": {"dm": 1, "speed": 1}}},

    # --- Dark ---
    "Bite":         {"type": "Dark",   "power": 60,  "acc": 100, "pp": 25, "category": "Physical", "priority": 0, "effect": {"status": "Flinch", "chance": 0.3}},
    "Feint Attack": {"type": "Dark",   "power": 60,  "acc": 100, "pp": 20, "category": "Physical", "priority": 0, "effect": None},
    "Night Slash":  {"type": "Dark",   "power": 70,  "acc": 100, "pp": 15, "category": "Physical", "priority": 0, "effect": None},
    "Dark Pulse":   {"type": "Dark",   "power": 80,  "acc": 100, "pp": 15, "category": "Special",  "priority": 0, "effect": {"status": "Flinch", "chance": 0.2}},
    "Nasty Plot":   {"type": "Dark",   "power": 0,   "acc": 100, "pp": 20, "category": "Status",   "priority": 0, "effect": {"self": {"dm": 2}}},

    # --- Steel ---
    "Iron Defense": {"type": "Steel",  "power": 0,   "acc": 100, "pp": 15, "category": "Status",   "priority": 0, "effect": {"self": {"def": 2}}},
    "Iron Head":    {"type": "Steel",  "power": 80,  "acc": 100, "pp": 15, "category": "Physical", "priority": 0, "effect": {"status": "Flinch", "chance": 0.3}},
    "Flash Cannon": {"type": "Steel",  "power": 80,  "acc": 100, "pp": 10, "category": "Special",  "priority": 0, "effect": {"target": {"sp_def": -1}, "chance": 0.1}},

    # --- Fairy ---
    "Fairy Wind":   {"type": "Fairy",  "power": 40,  "acc": 100, "pp": 30, "category": "Special",  "priority": 0, "effect": None},
    "Charm":        {"type": "Fairy",  "power": 0,   "acc": 100, "pp": 20, "category": "Status",   "priority": 0, "effect": {"target": {"dm": -2}}},
    "Sweet Kiss":   {"type": "Fairy",  "power": 0,   "acc": 75,  "pp": 10, "category": "Status",   "priority": 0, "effect": {"status": "Confuse", "chance": 1.0}},
    "Play Rough":   {"type": "Fairy",  "power": 90,  "acc": 90,  "pp": 10, "category": "Physical", "priority": 0, "effect": {"target": {"dm": -1}, "chance": 0.1}},
    "Dazzling Gleam":{"type": "Fairy",  "power": 80,  "acc": 100, "pp": 10, "category": "Special",  "priority": 0, "effect": None},
    "Moonblast":    {"type": "Fairy",  "power": 95,  "acc": 100, "pp": 15, "category": "Special",  "priority": 0, "effect": {"target": {"dm": -1}, "chance": 0.3}},

    # --- Extra coverage moves used by shops and gym teams ---
    "Swift":        {"type": "Normal",  "power": 60,  "acc": 100, "pp": 20, "category": "Special",  "priority": 0, "effect": None},
    "Sonic Boom":   {"type": "Normal",  "power": 40,  "acc": 90,  "pp": 20, "category": "Special",  "priority": 0, "effect": None},
    "Bind":         {"type": "Normal",  "power": 35,  "acc": 85,  "pp": 20, "category": "Physical", "priority": 0, "effect": {"trap": True}},
    "Self-Destruct":{"type": "Normal",  "power": 200, "acc": 100, "pp": 5,  "category": "Physical", "priority": 0, "effect": {"recoil": 1.0}},
    "Extreme Speed":{"type": "Normal",  "power": 80,  "acc": 100, "pp": 5,  "category": "Physical", "priority": 2, "effect": None},
    "Horn Drill":   {"type": "Normal",  "power": 120, "acc": 30,  "pp": 5,  "category": "Physical", "priority": 0, "effect": None},
    "Fire Punch":   {"type": "Fire",    "power": 75,  "acc": 100, "pp": 15, "category": "Physical", "priority": 0, "effect": {"status": "Burn", "chance": 0.1}},
    "Ice Punch":    {"type": "Ice",     "power": 75,  "acc": 100, "pp": 15, "category": "Physical", "priority": 0, "effect": {"status": "Freeze", "chance": 0.1}},
    "Sky Attack":   {"type": "Flying",  "power": 140, "acc": 90,  "pp": 5,  "category": "Physical", "priority": 0, "effect": {"charge": True}},
    "Acrobatics":   {"type": "Flying",  "power": 55,  "acc": 100, "pp": 15, "category": "Physical", "priority": 0, "effect": None},
    "Sand Tomb":    {"type": "Ground",  "power": 35,  "acc": 85,  "pp": 15, "category": "Physical", "priority": 0, "effect": {"trap": True}},
    "Earth Power":  {"type": "Ground",  "power": 90,  "acc": 100, "pp": 10, "category": "Special",  "priority": 0, "effect": {"target": {"sp_def": -1}, "chance": 0.1}},
    "Future Sight": {"type": "Psychic", "power": 120, "acc": 100, "pp": 10, "category": "Special",  "priority": 0, "effect": None},
    "Dynamic Punch":{"type": "Fighting","power": 100, "acc": 50,  "pp": 5,  "category": "Physical", "priority": 0, "effect": {"status": "Confuse", "chance": 1.0}},
    "Wild Charge":  {"type": "Electric","power": 90,  "acc": 100, "pp": 15, "category": "Physical", "priority": 0, "effect": {"recoil": 0.25}},
    "Metal Claw":   {"type": "Steel",   "power": 50,  "acc": 95,  "pp": 35, "category": "Physical", "priority": 0, "effect": {"self": {"dm": 1}, "chance": 0.1}},
    "Zap Cannon":   {"type": "Electric","power": 120, "acc": 50,  "pp": 5,  "category": "Special",  "priority": 0, "effect": {"status": "Paralyze", "chance": 1.0}},
    "Iron Tail":    {"type": "Steel",   "power": 100, "acc": 75,  "pp": 15, "category": "Physical", "priority": 0, "effect": {"target": {"def": -1}, "chance": 0.3}},
    "Revelation Dance":{"type": "Fire", "power": 90,  "acc": 100, "pp": 15, "category": "Special",  "priority": 0, "effect": None},
    "Sludge":       {"type": "Poison",  "power": 65,  "acc": 100, "pp": 20, "category": "Special",  "priority": 0, "effect": {"status": "Poison", "chance": 0.3}},
    "Smokescreen":  {"type": "Normal",  "power": 0,   "acc": 100, "pp": 20, "category": "Status",   "priority": 0, "effect": {"target": {"acc": -1}}},
    "Acid Armor":   {"type": "Poison",  "power": 0,   "acc": 100, "pp": 20, "category": "Status",   "priority": 0, "effect": {"self": {"def": 2}}},
    "Barrier":      {"type": "Psychic", "power": 0,   "acc": 100, "pp": 20, "category": "Status",   "priority": 0, "effect": {"self": {"def": 2}}},

    # --- Leech Life (Bug) ---
    "Leech Life":   {"type": "Bug",    "power": 80,  "acc": 100, "pp": 10, "category": "Physical", "priority": 0, "effect": {"heal": 0.5}},
}

def get_effectiveness(atk_type, def_type):
    return TYPE_CHART.get(atk_type, {}).get(def_type, 1.0)
