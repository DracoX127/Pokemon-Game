"""
Massive Evolution Map for every Pokemon in the game.
Maps a pokemon to its evolved form at a specific level, with massive stat boosts.
"""

EVOLUTION_MAP = {
    # Starters
    "charmander": {
        "level": 16,
        "evolves_to": "charmeleon",
        "stats": {"hp": 60, "maxhp": 60, "dm": 45},
        "learns": {
            1: ["Scratch", "Growl"],
            7: ["Ember"],
            11: ["Flame Charge"],
            16: ["Flame Wheel", "Fire Spin"]
        }
    },
    "charmeleon": {
        "level": 36,
        "evolves_to": "charizard",
        "stats": {"hp": 150, "maxhp": 150, "dm": 110},
        "learns": {
            1: ["Scratch", "Growl", "Ember"],
            7: ["Flame Charge"],
            13: ["Fire Spin"],
            19: ["Flame Wheel"],
            24: ["Slash"],
            29: ["Flamethrower"],
            36: ["Heat Wave", "Dragon Pulse"]
        }
    },
    "squirtle": {
        "level": 16,
        "evolves_to": "wartortle",
        "stats": {"hp": 70, "maxhp": 70, "dm": 40},
        "learns": {
            1: ["Tackle", "Tail Whip"],
            7: ["Water Gun"],
            11: ["Bubble Beam"],
            16: ["Water Pulse", "Aqua Tail"]
        }
    },
    "wartortle": {
        "level": 36,
        "evolves_to": "blastoise",
        "stats": {"hp": 160, "maxhp": 160, "dm": 95},
        "learns": {
            1: ["Tackle", "Tail Whip", "Water Gun"],
            7: ["Bubble Beam"],
            13: ["Water Pulse"],
            19: ["Aqua Tail"],
            24: ["Bite"],
            29: ["Scald"],
            36: ["Surf", "Hydro Pump"]
        }
    },
    "bulbasaur": {
        "level": 16,
        "evolves_to": "ivysaur",
        "stats": {"hp": 80, "maxhp": 80, "dm": 35},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Vine Whip"],
            11: ["Razor Leaf"],
            16: ["Seed Bomb", "Leech Seed"]
        }
    },
    "ivysaur": {
        "level": 36,
        "evolves_to": "venusaur",
        "stats": {"hp": 180, "maxhp": 180, "dm": 85},
        "learns": {
            1: ["Tackle", "Growl", "Vine Whip"],
            7: ["Razor Leaf"],
            13: ["Leech Seed"],
            19: ["Seed Bomb"],
            24: ["Sleep Powder"],
            29: ["Energy Ball"],
            36: ["Leaf Storm", "Solar Beam"]
        }
    },
    "pikachu": {
        "level": 25,
        "evolves_to": "raichu",
        "stats": {"hp": 100, "maxhp": 100, "dm": 80},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            6: ["Tail Whip"],
            10: ["Quick Attack"],
            14: ["Spark"],
            18: ["Nuzzle"],
            22: ["Thunder Wave"],
            25: ["Thunderbolt", "Volt Switch"]
        }
    },
    "eevee": {
        "level": 25,
        "evolves_to": "sylveon",
        "stats": {"hp": 120, "maxhp": 120, "dm": 70},
        "learns": {
            1: ["Tackle", "Growl"],
            6: ["Quick Attack"],
            10: ["Bite"],
            14: ["Charm"],
            18: ["Sweet Kiss"],
            22: ["Dazzling Gleam"],
            25: ["Moonblast", "Hyper Beam"]
        }
    },

    # Weak Tier (evolving)
    "pidgey": {
        "level": 18,
        "evolves_to": "pidgeotto",
        "stats": {"hp": 45, "maxhp": 45, "dm": 30},
        "learns": {
            1: ["Tackle", "Sand Attack"],
            6: ["Gust"],
            11: ["Quick Attack"],
            15: ["Wing Attack"],
            18: ["Aerial Ace", "Air Slash"]
        }
    },
    "pidgeotto": {
        "level": 36,
        "evolves_to": "pidgeot",
        "stats": {"hp": 100, "maxhp": 100, "dm": 70},
        "learns": {
            1: ["Tackle", "Sand Attack", "Gust"],
            6: ["Quick Attack"],
            11: ["Wing Attack"],
            16: ["Aerial Ace"],
            21: ["Air Slash"],
            26: ["Roost"],
            31: ["Agility"],
            36: ["Hurricane", "Heat Wave"]
        }
    },
    "rattata": {
        "level": 20,
        "evolves_to": "raticate",
        "stats": {"hp": 55, "maxhp": 55, "dm": 45},
        "learns": {
            1: ["Tackle", "Tail Whip"],
            6: ["Quick Attack"],
            10: ["Bite"],
            14: ["Take Down"],
            18: ["Body Slam"],
            20: ["Thrash", "Hyper Beam"]
        }
    },
    "zubat": {
        "level": 22,
        "evolves_to": "golbat",
        "stats": {"hp": 60, "maxhp": 60, "dm": 40},
        "learns": {
            1: ["Leech Life", "Astonish"],
            6: ["Gust"],
            10: ["Bite"],
            14: ["Wing Attack"],
            18: ["Air Slash"],
            22: ["Sludge Bomb", "Toxic"]
        }
    },
    "golbat": {
        "level": 40,
        "evolves_to": "crobat",
        "stats": {"hp": 110, "maxhp": 110, "dm": 85},
        "learns": {
            1: ["Leech Life", "Astonish", "Gust"],
            6: ["Bite"],
            11: ["Wing Attack"],
            16: ["Air Slash"],
            21: ["Sludge Bomb"],
            26: ["Poison Jab"],
            31: ["Dark Pulse"],
            36: ["Ominous Wind"],
            40: ["Roost", "Toxic"]
        }
    },
    "magikarp": {
        "level": 20,
        "evolves_to": "gyarados",
        "stats": {"hp": 150, "maxhp": 150, "dm": 120},
        "learns": {
            1: ["Tackle"],
            20: ["Hydro Pump", "Aqua Tail"]
        }
    },
    "caterpie": {
        "level": 7,
        "evolves_to": "metapod",
        "stats": {"hp": 40, "maxhp": 40, "dm": 15},
        "learns": {
            1: ["Tackle", "String Shot"],
            7: ["Bug Bite", "Stun Spore"]
        }
    },
    "metapod": {
        "level": 10,
        "evolves_to": "butterfree",
        "stats": {"hp": 80, "maxhp": 80, "dm": 60},
        "learns": {
            1: ["Tackle", "String Shot"],
            7: ["Bug Bite", "Stun Spore"],
            10: ["Iron Defense", "Confusion"]
        }
    },
    "weedle": {
        "level": 7,
        "evolves_to": "kakuna",
        "stats": {"hp": 40, "maxhp": 40, "dm": 15},
        "learns": {
            1: ["Poison Sting", "String Shot"],
            7: ["Bug Bite", "Toxic"]
        }
    },
    "kakuna": {
        "level": 10,
        "evolves_to": "beedrill",
        "stats": {"hp": 80, "maxhp": 80, "dm": 70},
        "learns": {
            1: ["Poison Sting", "String Shot"],
            7: ["Bug Bite", "Toxic"],
            10: ["Iron Defense", "Fury Swipes"]
        }
    },
    "jigglypuff": {
        "level": 30,
        "evolves_to": "wigglytuff",
        "stats": {"hp": 160, "maxhp": 160, "dm": 50},
        "learns": {
            1: ["Pound", "Growl"],
            6: ["Charm"],
            11: ["Sweet Kiss"],
            16: ["Body Slam"],
            21: ["Play Rough"],
            26: ["Rest"],
            30: ["Hyper Beam", "Dazzling Gleam"]
        }
    },

    # Moderately Strong Tier (evolving)
    "machop": {
        "level": 28,
        "evolves_to": "machoke",
        "stats": {"hp": 90, "maxhp": 90, "dm": 65},
        "learns": {
            1: ["Low Kick", "Leer"],
            7: ["Focus Blast"],
            12: ["Brick Break"],
            17: ["Bulk Up"],
            22: ["Rock Slide"],
            28: ["Close Combat", "Earthquake"]
        }
    },
    "machoke": {
        "level": 45,
        "evolves_to": "machamp",
        "stats": {"hp": 140, "maxhp": 140, "dm": 130},
        "learns": {
            1: ["Low Kick", "Leer", "Focus Blast"],
            7: ["Brick Break"],
            13: ["Bulk Up"],
            19: ["Rock Slide"],
            25: ["Close Combat"],
            31: ["Earthquake"],
            37: ["Giga Impact"],
            45: ["Focus Blast", "Stone Edge"]
        }
    },
    "geodude": {
        "level": 25,
        "evolves_to": "graveler",
        "stats": {"hp": 80, "maxhp": 80, "dm": 55},
        "learns": {
            1: ["Tackle", "Defense Curl"],
            7: ["Rock Throw"],
            12: ["Bulldoze"],
            17: ["Rock Slide"],
            21: ["Stealth Rock"],
            25: ["Stone Edge", "Earthquake"]
        }
    },
    "graveler": {
        "level": 45,
        "evolves_to": "golem",
        "stats": {"hp": 130, "maxhp": 130, "dm": 110},
        "learns": {
            1: ["Tackle", "Defense Curl", "Rock Throw"],
            7: ["Bulldoze"],
            13: ["Rock Slide"],
            19: ["Stealth Rock"],
            25: ["Stone Edge"],
            31: ["Earthquake"],
            37: ["Double-Edge"],
            45: ["Rock Slide", "Iron Head"]
        }
    },
    "gastly": {
        "level": 25,
        "evolves_to": "haunter",
        "stats": {"hp": 60, "maxhp": 60, "dm": 70},
        "learns": {
            1: ["Lick", "Astonish"],
            7: ["Confusion"],
            12: ["Shadow Ball"],
            17: ["Hypnosis"],
            21: ["Dark Pulse"],
            25: ["Destiny Bond", "Sludge Bomb"]
        }
    },
    "haunter": {
        "level": 45,
        "evolves_to": "gengar",
        "stats": {"hp": 110, "maxhp": 110, "dm": 140},
        "learns": {
            1: ["Lick", "Astonish", "Confusion"],
            7: ["Shadow Ball"],
            13: ["Hypnosis"],
            19: ["Dark Pulse"],
            25: ["Destiny Bond"],
            31: ["Sludge Bomb"],
            37: ["Psychic"],
            45: ["Shadow Ball", "Focus Blast"]
        }
    },
    "abra": {
        "level": 16,
        "evolves_to": "kadabra",
        "stats": {"hp": 50, "maxhp": 50, "dm": 60},
        "learns": {
            1: ["Confusion"],
            7: ["Zen Headbutt"],
            11: ["Calm Mind"],
            16: ["Psychic", "Shadow Ball"]
        }
    },
    "kadabra": {
        "level": 40,
        "evolves_to": "alakazam",
        "stats": {"hp": 90, "maxhp": 90, "dm": 150},
        "learns": {
            1: ["Confusion", "Zen Headbutt"],
            7: ["Calm Mind"],
            13: ["Psychic"],
            19: ["Recover"],
            25: ["Shadow Ball"],
            31: ["Energy Ball"],
            36: ["Nasty Plot"],
            40: ["Focus Blast", "Psychic"]
        }
    },
    "togepi": {
        "level": 20,
        "evolves_to": "togetic",
        "stats": {"hp": 80, "maxhp": 80, "dm": 40},
        "learns": {
            1: ["Pound", "Growl"],
            6: ["Charm"],
            10: ["Sweet Kiss"],
            14: ["Fairy Wind"],
            18: ["Dazzling Gleam"],
            20: ["Moonblast", "Headbutt"]
        }
    },
    "togetic": {
        "level": 40,
        "evolves_to": "togekiss",
        "stats": {"hp": 140, "maxhp": 140, "dm": 100},
        "learns": {
            1: ["Pound", "Growl", "Charm"],
            6: ["Sweet Kiss"],
            11: ["Fairy Wind"],
            16: ["Dazzling Gleam"],
            21: ["Air Slash"],
            26: ["Roost"],
            31: ["Heat Wave"],
            36: ["Moonblast"],
            40: ["Hyper Beam", "Aerial Ace"]
        }
    },

    # Strong Tier (evolving)
    "scyther": {
        "level": 30,
        "evolves_to": "scizor",
        "stats": {"hp": 120, "maxhp": 120, "dm": 130},
        "learns": {
            1: ["Quick Attack", "Leer"],
            7: ["Wing Attack"],
            12: ["Slash"],
            17: ["Aerial Ace"],
            22: ["Swords Dance"],
            26: ["Night Slash"],
            30: ["X-Scissor", "U-turn"]
        }
    },

    # Strong Tier (evolving)
    "onix": {
        "level": 40,
        "evolves_to": "steelix",
        "stats": {"hp": 180, "maxhp": 180, "dm": 110},
        "learns": {
            1: ["Tackle", "Sand Attack"],
            7: ["Rock Throw"],
            13: ["Bulldoze"],
            19: ["Rock Slide"],
            25: ["Stealth Rock"],
            31: ["Stone Edge"],
            36: ["Earthquake"],
            40: ["Iron Head", "Double-Edge"]
        }
    },
    "ralts": {
        "level": 20,
        "evolves_to": "kirlia",
        "stats": {"hp": 70, "maxhp": 70, "dm": 50},
        "learns": {
            1: ["Confusion", "Growl"],
            7: ["Charm"],
            12: ["Calm Mind"],
            16: ["Dazzling Gleam"],
            20: ["Psychic", "Moonblast"]
        }
    },
    "kirlia": {
        "level": 30,
        "evolves_to": "gardevoir",
        "stats": {"hp": 130, "maxhp": 130, "dm": 120},
        "learns": {
            1: ["Confusion", "Growl", "Charm"],
            7: ["Calm Mind"],
            12: ["Dazzling Gleam"],
            17: ["Psychic"],
            22: ["Shadow Ball"],
            26: ["Energy Ball"],
            30: ["Moonblast", "Hyper Beam"]
        }
    },
    "bagon": {
        "level": 30,
        "evolves_to": "shelgon",
        "stats": {"hp": 90, "maxhp": 90, "dm": 70},
        "learns": {
            1: ["Tackle", "Leer"],
            7: ["Bite"],
            13: ["Headbutt"],
            19: ["Twister"],
            24: ["Zen Headbutt"],
            30: ["Dragon Pulse", "Aqua Tail"]
        }
    },
    "shelgon": {
        "level": 50,
        "evolves_to": "salamence",
        "stats": {"hp": 170, "maxhp": 170, "dm": 160},
        "learns": {
            1: ["Tackle", "Leer", "Bite"],
            7: ["Headbutt"],
            13: ["Twister"],
            19: ["Zen Headbutt"],
            25: ["Dragon Pulse"],
            31: ["Dragon Dance"],
            37: ["Aqua Tail"],
            43: ["Air Slash"],
            50: ["Draco Meteor", "Hydro Pump"]
        }
    },
    "beldom": {
        "level": 20,
        "evolves_to": "metang",
        "stats": {"hp": 80, "maxhp": 80, "dm": 60},
        "learns": {
            1: ["Take Down", "Iron Defense"],
            7: ["Confusion"],
            12: ["Zen Headbutt"],
            16: ["Bulldoze"],
            20: ["Flash Cannon", "Psychic"]
        }
    },
    "metang": {
        "level": 45,
        "evolves_to": "metagross",
        "stats": {"hp": 160, "maxhp": 160, "dm": 150},
        "learns": {
            1: ["Take Down", "Iron Defense", "Confusion"],
            7: ["Zen Headbutt"],
            13: ["Bulldoze"],
            19: ["Flash Cannon"],
            25: ["Psychic"],
            31: ["Earthquake"],
            37: ["Iron Head"],
            45: ["Hyper Beam", "Giga Impact"]
        }
    },
    "gible": {
        "level": 24,
        "evolves_to": "gabite",
        "stats": {"hp": 90, "maxhp": 90, "dm": 70},
        "learns": {
            1: ["Tackle", "Sand Attack"],
            7: ["Twister"],
            12: ["Bulldoze"],
            17: ["Bite"],
            21: ["Slash"],
            24: ["Dragon Pulse", "Earthquake"]
        }
    },
    "gabite": {
        "level": 48,
        "evolves_to": "garchomp",
        "stats": {"hp": 180, "maxhp": 180, "dm": 170},
        "learns": {
            1: ["Tackle", "Sand Attack", "Twister"],
            7: ["Bulldoze"],
            13: ["Bite"],
            19: ["Slash"],
            25: ["Dragon Pulse"],
            31: ["Stone Edge"],
            37: ["Earthquake"],
            42: ["Dragon Dance"],
            48: ["Draco Meteor", "Giga Impact"]
        }
    },
    "larvitar": {
        "level": 30,
        "evolves_to": "pupitar",
        "stats": {"hp": 100, "maxhp": 100, "dm": 80},
        "learns": {
            1: ["Bite", "Leer"],
            7: ["Rock Throw"],
            13: ["Bulldoze"],
            19: ["Rock Slide"],
            24: ["Dark Pulse"],
            30: ["Stone Edge", "Earthquake"]
        }
    },
    "pupitar": {
        "level": 55,
        "evolves_to": "tyranitar",
        "stats": {"hp": 200, "maxhp": 200, "dm": 180},
        "learns": {
            1: ["Bite", "Leer", "Rock Throw"],
            7: ["Bulldoze"],
            13: ["Rock Slide"],
            19: ["Dark Pulse"],
            25: ["Stone Edge"],
            31: ["Earthquake"],
            37: ["Night Slash"],
            43: ["Hyper Beam"],
            49: ["Dragon Pulse"],
            55: ["Giga Impact", "Focus Blast"]
        }
    },
    "dratini": {
        "level": 30,
        "evolves_to": "dragonair",
        "stats": {"hp": 90, "maxhp": 90, "dm": 70},
        "learns": {
            1: ["Tackle", "Leer"],
            7: ["Thunder Wave"],
            13: ["Twister"],
            19: ["Aqua Tail"],
            24: ["Dragon Dance"],
            30: ["Dragon Pulse", "Hyper Beam"]
        }
    },
    "dragonair": {
        "level": 55,
        "evolves_to": "dragonite",
        "stats": {"hp": 180, "maxhp": 180, "dm": 160},
        "learns": {
            1: ["Tackle", "Leer", "Thunder Wave"],
            7: ["Twister"],
            13: ["Aqua Tail"],
            19: ["Dragon Dance"],
            25: ["Dragon Pulse"],
            31: ["Agility"],
            37: ["Thunder"],
            43: ["Hydro Pump"],
            49: ["Hyper Beam"],
            55: ["Draco Meteor", "Hurricane"]
        }
    },
    "lucario": {
        "level": 50,
        "evolves_to": "MegaLucario",
        "stats": {"hp": 200, "maxhp": 200, "dm": 180},
        "learns": {
            1: ["Quick Attack", "Leer"],
            7: ["Brick Break"],
            13: ["Bulk Up"],
            19: ["Rock Slide"],
            25: ["Swords Dance"],
            31: ["Dragon Pulse"],
            37: ["Dark Pulse"],
            43: ["Close Combat"],
            50: ["Flash Cannon", "Earthquake"]
        }
    },
    # Moderately Strong Tier (evolving)
    "growlithe": {
        "level": 30,
        "evolves_to": "arcanine",
        "stats": {"hp": 150, "maxhp": 150, "dm": 140},
        "learns": {
            1: ["Bite", "Growl"],
            7: ["Ember"],
            12: ["Flame Wheel"],
            17: ["Flame Charge"],
            22: ["Take Down"],
            26: ["Flamethrower"],
            30: ["Heat Wave", "Fire Blast"]
        }
    },

    # Non-Evolving Pokemon
    "abomasnow": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 90, "maxhp": 90, "dm": 92, "speed": 60},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"]
        }
    },
    "absol": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 130, "speed": 75},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"]
        }
    },
    "accelgor": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 119, "speed": 145},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"]
        }
    },
    "aegislash": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 50, "speed": 60},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"],
            42: ["Flash Cannon", "Hyper Beam"]
        }
    },
    "aggron": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 110, "speed": 50},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"],
            42: ["Stone Edge", "Giga Impact"]
        }
    },
    "alakazam": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 55, "maxhp": 55, "dm": 135, "speed": 120},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"],
            30: ["Energy Ball", "Focus Blast"],
            42: ["Psychic", "Moonblast"]
        }
    },
    "altaria": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 70, "speed": 80},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "amoonguss": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 114, "maxhp": 114, "dm": 85, "speed": 30},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"]
        }
    },
    "ampharos": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 90, "maxhp": 90, "dm": 75, "speed": 55},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "annihilape": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 110, "maxhp": 110, "dm": 115, "speed": 90},
        "learns": {
            1: ["Lick", "Astonish"],
            8: ["Confusion", "Shadow Ball"],
            18: ["Dark Pulse", "Will-o-Wisp"],
            30: ["Destiny Bond", "Shadow Ball"],
            42: ["Focus Blast", "Psychic"]
        }
    },
    "appletun": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 85, "maxhp": 85, "dm": 100, "speed": 30},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "araquanid": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 88, "maxhp": 88, "dm": 70, "speed": 42},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "arbok": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 95, "speed": 80},
        "learns": {
            1: ["Poison Sting", "Growl"],
            8: ["Bite", "Poison Jab"],
            18: ["Sludge Bomb", "Dark Pulse"],
            30: ["Flamethrower", "Toxic"]
        }
    },
    "arboliva": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 78, "maxhp": 78, "dm": 69, "speed": 39},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "arcanine": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 90, "maxhp": 90, "dm": 110, "speed": 95},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "arceus": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 120, "maxhp": 120, "dm": 120, "speed": 120},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"],
            40: ["Giga Impact", "Earthquake"]
        }
    },
    "archeops": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 140, "speed": 110},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"],
            42: ["Stone Edge", "Giga Impact"]
        }
    },
    "arctibax": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 85, "speed": 62},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "arctovish": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 90, "maxhp": 90, "dm": 110, "speed": 55},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "arctozolt": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 90, "maxhp": 90, "dm": 135, "speed": 55},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "armarouge": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 72, "maxhp": 72, "dm": 109, "speed": 75},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "aromatisse": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 72, "maxhp": 72, "dm": 72, "speed": 29},
        "learns": {
            1: ["Fairy Wind", "Growl"],
            8: ["Charm", "Dazzling Gleam"],
            18: ["Play Rough", "Moonblast"],
            30: ["Psychic", "Hyper Beam"]
        }
    },
    "articuno": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 90, "maxhp": 90, "dm": 85, "speed": 85},
        "learns": {
            1: ["Ice Shard", "Powder Snow"],
            8: ["Icy Wind", "Ice Beam"],
            18: ["Blizzard", "Surf"],
            30: ["Earthquake", "Hyper Beam"],
            42: ["Blizzard", "Focus Blast"]
        }
    },
    "audino": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 103, "maxhp": 103, "dm": 60, "speed": 50},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "aurorus": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 123, "maxhp": 123, "dm": 77, "speed": 58},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"]
        }
    },
    "avalugg": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 95, "maxhp": 95, "dm": 117, "speed": 28},
        "learns": {
            1: ["Ice Shard", "Powder Snow"],
            8: ["Icy Wind", "Ice Beam"],
            18: ["Blizzard", "Surf"],
            30: ["Earthquake", "Hyper Beam"],
            42: ["Blizzard", "Focus Blast"]
        }
    },
    "barbaracle": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 72, "maxhp": 72, "dm": 105, "speed": 68},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"]
        }
    },
    "barraskewda": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 145, "speed": 136},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "baxcalibur": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 115, "maxhp": 115, "dm": 145, "speed": 87},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "beheeyem": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 75, "speed": 40},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"],
            30: ["Energy Ball", "Focus Blast"],
            42: ["Psychic", "Moonblast"]
        }
    },
    "bellibolt": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 104, "maxhp": 104, "dm": 87, "speed": 45},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "bellossom": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 80, "speed": 50},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"]
        }
    },
    "bewear": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 111, "maxhp": 111, "dm": 133, "speed": 60},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"],
            40: ["Giga Impact", "Earthquake"]
        }
    },
    "bidoof": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 59, "maxhp": 59, "dm": 45, "speed": 31},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"]
        }
    },
    "bisharp": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 125, "speed": 70},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"],
            42: ["Focus Blast", "Hyper Beam"]
        }
    },
    "blacephalon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 127, "maxhp": 127, "dm": 127, "speed": 107},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "blastoise": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 79, "maxhp": 79, "dm": 83, "speed": 78},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "blaziken": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 120, "speed": 80},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "blipbug": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 25, "maxhp": 25, "dm": 20, "speed": 36},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"]
        }
    },
    "boltund": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 121, "maxhp": 121, "dm": 103, "speed": 121},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "bombirdier": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 103, "speed": 82},
        "learns": {
            1: ["Gust", "Quick Attack"],
            8: ["Wing Attack", "Aerial Ace"],
            18: ["Air Slash", "Roost"],
            30: ["Hurricane", "Heat Wave"],
            42: ["Hurricane", "Hyper Beam"]
        }
    },
    "bouffalant": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 110, "maxhp": 110, "dm": 100, "speed": 55},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "braviary": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 123, "speed": 80},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"],
            40: ["Giga Impact", "Earthquake"]
        }
    },
    "breloom": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 130, "speed": 70},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "bronzong": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 79, "maxhp": 79, "dm": 89, "speed": 33},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"]
        }
    },
    "bunnelby": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 38, "maxhp": 38, "dm": 36, "speed": 57},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"]
        }
    },
    "burmy": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 34, "maxhp": 34, "dm": 48, "speed": 36},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"]
        }
    },
    "butterfree": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 45, "speed": 70},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"]
        }
    },
    "buzzwole": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 79, "maxhp": 79, "dm": 139, "speed": 79},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"],
            42: ["Signal Beam", "Megahorn"]
        }
    },
    "cacturne": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 115, "speed": 55},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"]
        }
    },
    "calyrex": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 80, "speed": 80},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"],
            30: ["Energy Ball", "Focus Blast"],
            42: ["Psychic", "Moonblast"]
        }
    },
    "capsakid": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 50, "maxhp": 50, "dm": 62, "speed": 30},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "carracosta": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 74, "maxhp": 74, "dm": 108, "speed": 32},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "cascoon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 50, "maxhp": 50, "dm": 35, "speed": 25},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"]
        }
    },
    "celebi": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 100, "speed": 100},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"],
            30: ["Energy Ball", "Focus Blast"],
            42: ["Psychic", "Moonblast"]
        }
    },
    "celesteela": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 101, "maxhp": 101, "dm": 73, "speed": 61},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"],
            42: ["Flash Cannon", "Hyper Beam"]
        }
    },
    "centiskorch": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 85, "maxhp": 85, "dm": 104, "speed": 65},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "ceruledge": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 66, "maxhp": 66, "dm": 125, "speed": 85},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "cetitan": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 120, "maxhp": 120, "dm": 60, "speed": 73},
        "learns": {
            1: ["Ice Shard", "Powder Snow"],
            8: ["Icy Wind", "Ice Beam"],
            18: ["Blizzard", "Surf"],
            30: ["Earthquake", "Hyper Beam"],
            42: ["Blizzard", "Focus Blast"]
        }
    },
    "cetoddle": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 55, "maxhp": 55, "dm": 22, "speed": 20},
        "learns": {
            1: ["Ice Shard", "Powder Snow"],
            8: ["Icy Wind", "Ice Beam"],
            18: ["Blizzard", "Surf"],
            30: ["Earthquake", "Hyper Beam"],
            42: ["Blizzard", "Focus Blast"]
        }
    },
    "chandelure": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 90, "speed": 80},
        "learns": {
            1: ["Lick", "Astonish"],
            8: ["Confusion", "Shadow Ball"],
            18: ["Dark Pulse", "Will-o-Wisp"],
            30: ["Destiny Bond", "Shadow Ball"],
            42: ["Focus Blast", "Psychic"]
        }
    },
    "charcadet": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 40, "maxhp": 40, "dm": 61, "speed": 35},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "charizard": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 78, "maxhp": 78, "dm": 84, "speed": 100},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "chesnaught": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 88, "maxhp": 88, "dm": 107, "speed": 64},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"]
        }
    },
    "chewtle": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 50, "maxhp": 50, "dm": 53, "speed": 37},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"]
        }
    },
    "cinccino": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 95, "speed": 115},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "cinderace": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 116, "speed": 119},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "clawitzer": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 73, "maxhp": 73, "dm": 120, "speed": 59},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "claydol": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 108, "maxhp": 108, "dm": 70, "speed": 75},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "clodsire": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 75, "speed": 20},
        "learns": {
            1: ["Poison Sting", "Growl"],
            8: ["Bite", "Poison Jab"],
            18: ["Sludge Bomb", "Dark Pulse"],
            30: ["Flamethrower", "Toxic"],
            42: ["Sludge Bomb", "Giga Impact"]
        }
    },
    "cloyster": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 50, "maxhp": 50, "dm": 95, "speed": 70},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"]
        }
    },
    "cobalion": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 91, "maxhp": 91, "dm": 109, "speed": 108},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"],
            42: ["Flash Cannon", "Hyper Beam"]
        }
    },
    "cofagrigus": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 145, "maxhp": 145, "dm": 95, "speed": 30},
        "learns": {
            1: ["Lick", "Astonish"],
            8: ["Confusion", "Shadow Ball"],
            18: ["Dark Pulse", "Will-o-Wisp"],
            30: ["Destiny Bond", "Shadow Ball"],
            42: ["Focus Blast", "Psychic"]
        }
    },
    "combee": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 30, "maxhp": 30, "dm": 42, "speed": 70},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"]
        }
    },
    "conkeldurr": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 105, "maxhp": 105, "dm": 140, "speed": 45},
        "learns": {
            1: ["Low Kick", "Leer"],
            8: ["Brick Break", "Bulk Up"],
            18: ["Rock Slide", "Close Combat"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Close Combat", "Giga Impact"]
        }
    },
    "copperajah": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 122, "maxhp": 122, "dm": 129, "speed": 30},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"],
            42: ["Flash Cannon", "Hyper Beam"]
        }
    },
    "corviknight": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 98, "maxhp": 98, "dm": 87, "speed": 67},
        "learns": {
            1: ["Gust", "Quick Attack"],
            8: ["Wing Attack", "Aerial Ace"],
            18: ["Air Slash", "Roost"],
            30: ["Hurricane", "Heat Wave"],
            42: ["Hurricane", "Hyper Beam"]
        }
    },
    "crabominable": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 97, "maxhp": 97, "dm": 132, "speed": 43},
        "learns": {
            1: ["Low Kick", "Leer"],
            8: ["Brick Break", "Bulk Up"],
            18: ["Rock Slide", "Close Combat"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Close Combat", "Giga Impact"]
        }
    },
    "cradily": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 86, "maxhp": 86, "dm": 81, "speed": 43},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"]
        }
    },
    "cramorant": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 85, "speed": 85},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "crawdaunt": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 63, "maxhp": 63, "dm": 120, "speed": 55},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"]
        }
    },
    "cresselia": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 120, "maxhp": 120, "dm": 70, "speed": 85},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"],
            30: ["Energy Ball", "Focus Blast"],
            42: ["Psychic", "Moonblast"]
        }
    },
    "crobat": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 85, "maxhp": 85, "dm": 90, "speed": 130},
        "learns": {
            1: ["Poison Sting", "Growl"],
            8: ["Bite", "Poison Jab"],
            18: ["Sludge Bomb", "Dark Pulse"],
            30: ["Flamethrower", "Toxic"],
            42: ["Sludge Bomb", "Giga Impact"]
        }
    },
    "cursola": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 95, "speed": 30},
        "learns": {
            1: ["Lick", "Astonish"],
            8: ["Confusion", "Shadow Ball"],
            18: ["Dark Pulse", "Will-o-Wisp"],
            30: ["Destiny Bond", "Shadow Ball"],
            42: ["Focus Blast", "Psychic"]
        }
    },
    "cyclizar": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 109, "maxhp": 109, "dm": 100, "speed": 121},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "dachsbun": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 79, "maxhp": 79, "dm": 110, "speed": 95},
        "learns": {
            1: ["Fairy Wind", "Growl"],
            8: ["Charm", "Dazzling Gleam"],
            18: ["Play Rough", "Moonblast"],
            30: ["Psychic", "Hyper Beam"],
            42: ["Moonblast", "Dazzling Gleam"]
        }
    },
    "darkrai": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 90, "speed": 125},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"],
            42: ["Focus Blast", "Hyper Beam"]
        }
    },
    "decidueye": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 78, "maxhp": 78, "dm": 107, "speed": 70},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "dedenne": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 67, "maxhp": 67, "dm": 79, "speed": 101},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"]
        }
    },
    "delcatty": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 70, "speed": 70},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "delibird": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 45, "maxhp": 45, "dm": 55, "speed": 75},
        "learns": {
            1: ["Ice Shard", "Powder Snow"],
            8: ["Icy Wind", "Ice Beam"],
            18: ["Blizzard", "Surf"],
            30: ["Earthquake", "Hyper Beam"]
        }
    },
    "deoxys": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 50, "maxhp": 50, "dm": 150, "speed": 150},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"],
            30: ["Energy Ball", "Focus Blast"],
            42: ["Psychic", "Moonblast"]
        }
    },
    "dhelmise": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 131, "speed": 40},
        "learns": {
            1: ["Lick", "Astonish"],
            8: ["Confusion", "Shadow Ball"],
            18: ["Dark Pulse", "Will-o-Wisp"],
            30: ["Destiny Bond", "Shadow Ball"],
            42: ["Focus Blast", "Psychic"]
        }
    },
    "dialga": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 120, "speed": 90},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"],
            42: ["Flash Cannon", "Hyper Beam"]
        }
    },
    "diancie": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 50, "maxhp": 50, "dm": 131, "speed": 50},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"],
            42: ["Stone Edge", "Giga Impact"]
        }
    },
    "dolliv": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 52, "maxhp": 52, "dm": 48, "speed": 30},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "dondozo": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 120, "maxhp": 120, "dm": 80, "speed": 35},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "donphan": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 120, "maxhp": 120, "dm": 120, "speed": 50},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "dracovish": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 90, "maxhp": 90, "dm": 135, "speed": 55},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "dracozolt": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 145, "speed": 75},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "dragapult": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 120, "speed": 142},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "dragonite": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 91, "maxhp": 91, "dm": 134, "speed": 80},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "drampa": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 78, "maxhp": 78, "dm": 120, "speed": 36},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"],
            40: ["Giga Impact", "Earthquake"]
        }
    },
    "drapion": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 90, "speed": 95},
        "learns": {
            1: ["Poison Sting", "Growl"],
            8: ["Bite", "Poison Jab"],
            18: ["Sludge Bomb", "Dark Pulse"],
            30: ["Flamethrower", "Toxic"],
            42: ["Sludge Bomb", "Giga Impact"]
        }
    },
    "drednaw": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 90, "maxhp": 90, "dm": 115, "speed": 74},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "druddigon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 77, "maxhp": 77, "dm": 120, "speed": 48},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"]
        }
    },
    "dubwool": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 72, "maxhp": 72, "dm": 60, "speed": 88},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"],
            40: ["Giga Impact", "Earthquake"]
        }
    },
    "dugtrio": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 35, "maxhp": 35, "dm": 100, "speed": 120},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"]
        }
    },
    "dunsparce": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 70, "speed": 45},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "duraludon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 95, "speed": 85},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"],
            42: ["Flash Cannon", "Hyper Beam"]
        }
    },
    "dusclops": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 40, "maxhp": 40, "dm": 70, "speed": 25},
        "learns": {
            1: ["Lick", "Astonish"],
            8: ["Confusion", "Shadow Ball"],
            18: ["Dark Pulse", "Will-o-Wisp"],
            30: ["Destiny Bond", "Shadow Ball"],
            42: ["Focus Blast", "Psychic"]
        }
    },
    "dusknoir": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 65, "speed": 45},
        "learns": {
            1: ["Lick", "Astonish"],
            8: ["Confusion", "Shadow Ball"],
            18: ["Dark Pulse", "Will-o-Wisp"],
            30: ["Destiny Bond", "Shadow Ball"],
            42: ["Focus Blast", "Psychic"]
        }
    },
    "eelektross": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 85, "maxhp": 85, "dm": 115, "speed": 50},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "eiscue": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 80, "speed": 50},
        "learns": {
            1: ["Ice Shard", "Powder Snow"],
            8: ["Icy Wind", "Ice Beam"],
            18: ["Blizzard", "Surf"],
            30: ["Earthquake", "Hyper Beam"],
            42: ["Blizzard", "Focus Blast"]
        }
    },
    "eldegoss": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 85, "speed": 60},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "electabuzz": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 83, "speed": 105},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "electivire": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 123, "speed": 95},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "emboar": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 123, "maxhp": 123, "dm": 100, "speed": 65},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "emolga": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 55, "maxhp": 55, "dm": 86, "speed": 103},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"]
        }
    },
    "entei": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 111, "speed": 100},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "espeon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 65, "speed": 110},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"],
            30: ["Energy Ball", "Focus Blast"],
            42: ["Psychic", "Moonblast"]
        }
    },
    "eternatus": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 135, "maxhp": 135, "dm": 115, "speed": 130},
        "learns": {
            1: ["Poison Sting", "Growl"],
            8: ["Bite", "Poison Jab"],
            18: ["Sludge Bomb", "Dark Pulse"],
            30: ["Flamethrower", "Toxic"],
            42: ["Sludge Bomb", "Giga Impact"]
        }
    },
    "exeggutor": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 95, "maxhp": 95, "dm": 95, "speed": 55},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "exploud": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 104, "maxhp": 104, "dm": 91, "speed": 68},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "farfetch'd": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 52, "maxhp": 52, "dm": 90, "speed": 60},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "feebas": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 20, "maxhp": 20, "dm": 15, "speed": 40},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"]
        }
    },
    "ferrothorn": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 74, "maxhp": 74, "dm": 94, "speed": 20},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "fidough": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 37, "maxhp": 37, "dm": 67, "speed": 55},
        "learns": {
            1: ["Fairy Wind", "Growl"],
            8: ["Charm", "Dazzling Gleam"],
            18: ["Play Rough", "Moonblast"],
            30: ["Psychic", "Hyper Beam"],
            42: ["Moonblast", "Dazzling Gleam"]
        }
    },
    "finizen": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 64, "speed": 63},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "flamigo": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 78, "maxhp": 78, "dm": 115, "speed": 90},
        "learns": {
            1: ["Gust", "Quick Attack"],
            8: ["Wing Attack", "Aerial Ace"],
            18: ["Air Slash", "Roost"],
            30: ["Hurricane", "Heat Wave"],
            42: ["Hurricane", "Hyper Beam"]
        }
    },
    "flapple": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 110, "speed": 70},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "flareon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 130, "speed": 65},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"]
        }
    },
    "floatzel": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 85, "maxhp": 85, "dm": 105, "speed": 115},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"]
        }
    },
    "flutter mane": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 55, "maxhp": 55, "dm": 55, "speed": 135},
        "learns": {
            1: ["Lick", "Astonish"],
            8: ["Confusion", "Shadow Ball"],
            18: ["Dark Pulse", "Will-o-Wisp"],
            30: ["Destiny Bond", "Shadow Ball"],
            42: ["Focus Blast", "Psychic"]
        }
    },
    "flygon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 100, "speed": 100},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "frigibax": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 35, "maxhp": 35, "dm": 47, "speed": 35},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "froslass": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 80, "speed": 110},
        "learns": {
            1: ["Ice Shard", "Powder Snow"],
            8: ["Icy Wind", "Ice Beam"],
            18: ["Blizzard", "Surf"],
            30: ["Earthquake", "Hyper Beam"],
            42: ["Blizzard", "Focus Blast"]
        }
    },
    "frosmoth": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 65, "speed": 65},
        "learns": {
            1: ["Ice Shard", "Powder Snow"],
            8: ["Icy Wind", "Ice Beam"],
            18: ["Blizzard", "Surf"],
            30: ["Earthquake", "Hyper Beam"],
            42: ["Blizzard", "Focus Blast"]
        }
    },
    "furfrou": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 80, "speed": 102},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "gallade": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 68, "maxhp": 68, "dm": 125, "speed": 80},
        "learns": {
            1: ["Low Kick", "Leer"],
            8: ["Brick Break", "Bulk Up"],
            18: ["Rock Slide", "Close Combat"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Close Combat", "Giga Impact"]
        }
    },
    "galvantula": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 72, "maxhp": 72, "dm": 77, "speed": 108},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "garchomp": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 108, "maxhp": 108, "dm": 130, "speed": 102},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "gardevoir": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 68, "maxhp": 68, "dm": 65, "speed": 80},
        "learns": {
            1: ["Fairy Wind", "Growl"],
            8: ["Charm", "Dazzling Gleam"],
            18: ["Play Rough", "Moonblast"],
            30: ["Psychic", "Hyper Beam"],
            42: ["Moonblast", "Dazzling Gleam"]
        }
    },
    "garganacl": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 65, "speed": 35},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"],
            42: ["Stone Edge", "Giga Impact"]
        }
    },
    "genesect": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 72, "maxhp": 72, "dm": 120, "speed": 99},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"],
            42: ["Signal Beam", "Megahorn"]
        }
    },
    "gengar": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 130, "speed": 110},
        "learns": {
            1: ["Lick", "Astonish"],
            8: ["Confusion", "Shadow Ball"],
            18: ["Dark Pulse", "Will-o-Wisp"],
            30: ["Destiny Bond", "Shadow Ball"],
            42: ["Focus Blast", "Psychic"]
        }
    },
    "gholdengo": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 87, "maxhp": 87, "dm": 60, "speed": 84},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"],
            42: ["Flash Cannon", "Hyper Beam"]
        }
    },
    "gigalith": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 85, "maxhp": 85, "dm": 135, "speed": 25},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"]
        }
    },
    "girafarig": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 80, "speed": 85},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "giratina": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 150, "maxhp": 150, "dm": 100, "speed": 90},
        "learns": {
            1: ["Lick", "Astonish"],
            8: ["Confusion", "Shadow Ball"],
            18: ["Dark Pulse", "Will-o-Wisp"],
            30: ["Destiny Bond", "Shadow Ball"],
            42: ["Focus Blast", "Psychic"]
        }
    },
    "glalie": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 80, "speed": 80},
        "learns": {
            1: ["Ice Shard", "Powder Snow"],
            8: ["Icy Wind", "Ice Beam"],
            18: ["Blizzard", "Surf"],
            30: ["Earthquake", "Hyper Beam"]
        }
    },
    "glastrier": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 130, "maxhp": 130, "dm": 85, "speed": 30},
        "learns": {
            1: ["Ice Shard", "Powder Snow"],
            8: ["Icy Wind", "Ice Beam"],
            18: ["Blizzard", "Surf"],
            30: ["Earthquake", "Hyper Beam"],
            42: ["Blizzard", "Focus Blast"]
        }
    },
    "gligar": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 75, "speed": 85},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "glimmora": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 55, "maxhp": 55, "dm": 120, "speed": 60},
        "learns": {
            1: ["Poison Sting", "Growl"],
            8: ["Bite", "Poison Jab"],
            18: ["Sludge Bomb", "Dark Pulse"],
            30: ["Flamethrower", "Toxic"],
            42: ["Sludge Bomb", "Giga Impact"]
        }
    },
    "gliscor": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 95, "speed": 95},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "golduck": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 80, "speed": 85},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"]
        }
    },
    "golem": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 120, "speed": 45},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"],
            42: ["Stone Edge", "Giga Impact"]
        }
    },
    "golisopod": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 125, "speed": 40},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "golurk": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 89, "maxhp": 89, "dm": 124, "speed": 55},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "goodra": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 90, "maxhp": 90, "dm": 100, "speed": 80},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "gorebyss": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 84, "maxhp": 84, "dm": 84, "speed": 52},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"]
        }
    },
    "gothitelle": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 75, "speed": 55},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"],
            30: ["Energy Ball", "Focus Blast"]
        }
    },
    "gourgeist": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 58, "speed": 84},
        "learns": {
            1: ["Lick", "Astonish"],
            8: ["Confusion", "Shadow Ball"],
            18: ["Dark Pulse", "Will-o-Wisp"],
            30: ["Destiny Bond", "Shadow Ball"],
            42: ["Focus Blast", "Psychic"]
        }
    },
    "grafaiai": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 78, "maxhp": 78, "dm": 120, "speed": 84},
        "learns": {
            1: ["Poison Sting", "Growl"],
            8: ["Bite", "Poison Jab"],
            18: ["Sludge Bomb", "Dark Pulse"],
            30: ["Flamethrower", "Toxic"],
            42: ["Sludge Bomb", "Giga Impact"]
        }
    },
    "granbull": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 120, "maxhp": 120, "dm": 65, "speed": 45},
        "learns": {
            1: ["Fairy Wind", "Growl"],
            8: ["Charm", "Dazzling Gleam"],
            18: ["Play Rough", "Moonblast"],
            30: ["Psychic", "Hyper Beam"]
        }
    },
    "grapploct": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 130, "speed": 42},
        "learns": {
            1: ["Low Kick", "Leer"],
            8: ["Brick Break", "Bulk Up"],
            18: ["Rock Slide", "Close Combat"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Close Combat", "Giga Impact"]
        }
    },
    "great tusk": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 115, "maxhp": 115, "dm": 131, "speed": 87},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "greavard": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 51, "maxhp": 51, "dm": 71, "speed": 55},
        "learns": {
            1: ["Lick", "Astonish"],
            8: ["Confusion", "Shadow Ball"],
            18: ["Dark Pulse", "Will-o-Wisp"],
            30: ["Destiny Bond", "Shadow Ball"],
            42: ["Focus Blast", "Psychic"]
        }
    },
    "greedent": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 120, "maxhp": 120, "dm": 95, "speed": 20},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"],
            40: ["Giga Impact", "Earthquake"]
        }
    },
    "greninja": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 72, "maxhp": 72, "dm": 145, "speed": 122},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "grimmsnarl": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 100, "speed": 60},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"],
            42: ["Focus Blast", "Hyper Beam"]
        }
    },
    "groudon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 150, "speed": 90},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "gumshoos": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 86, "maxhp": 86, "dm": 110, "speed": 45},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "gurdurr": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 100, "speed": 40},
        "learns": {
            1: ["Low Kick", "Leer"],
            8: ["Brick Break", "Bulk Up"],
            18: ["Rock Slide", "Close Combat"],
            30: ["Earthquake", "Stone Edge"]
        }
    },
    "guzzlord": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 223, "maxhp": 223, "dm": 101, "speed": 29},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"],
            42: ["Focus Blast", "Hyper Beam"]
        }
    },
    "gyarados": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 95, "maxhp": 95, "dm": 125, "speed": 81},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "hariyama": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 144, "maxhp": 144, "dm": 100, "speed": 50},
        "learns": {
            1: ["Low Kick", "Leer"],
            8: ["Brick Break", "Bulk Up"],
            18: ["Rock Slide", "Close Combat"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Close Combat", "Giga Impact"]
        }
    },
    "hatterene": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 57, "maxhp": 57, "dm": 65, "speed": 29},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"],
            30: ["Energy Ball", "Focus Blast"],
            42: ["Psychic", "Moonblast"]
        }
    },
    "hawlucha": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 63, "maxhp": 63, "dm": 92, "speed": 118},
        "learns": {
            1: ["Low Kick", "Leer"],
            8: ["Brick Break", "Bulk Up"],
            18: ["Rock Slide", "Close Combat"],
            30: ["Earthquake", "Stone Edge"]
        }
    },
    "haxorus": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 76, "maxhp": 76, "dm": 147, "speed": 97},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "heatran": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 91, "maxhp": 91, "dm": 109, "speed": 77},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "heliolisk": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 62, "maxhp": 62, "dm": 109, "speed": 109},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "hippowdon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 108, "maxhp": 108, "dm": 112, "speed": 47},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "hitmonchan": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 50, "maxhp": 50, "dm": 105, "speed": 76},
        "learns": {
            1: ["Low Kick", "Leer"],
            8: ["Brick Break", "Bulk Up"],
            18: ["Rock Slide", "Close Combat"],
            30: ["Earthquake", "Stone Edge"]
        }
    },
    "hitmonlee": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 50, "maxhp": 50, "dm": 120, "speed": 87},
        "learns": {
            1: ["Low Kick", "Leer"],
            8: ["Brick Break", "Bulk Up"],
            18: ["Rock Slide", "Close Combat"],
            30: ["Earthquake", "Stone Edge"]
        }
    },
    "hitmontop": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 50, "maxhp": 50, "dm": 95, "speed": 70},
        "learns": {
            1: ["Low Kick", "Leer"],
            8: ["Brick Break", "Bulk Up"],
            18: ["Rock Slide", "Close Combat"],
            30: ["Earthquake", "Stone Edge"]
        }
    },
    "ho-oh": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 106, "maxhp": 106, "dm": 130, "speed": 90},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "honchkrow": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 125, "speed": 71},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"]
        }
    },
    "hoopa": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 110, "speed": 70},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"],
            30: ["Energy Ball", "Focus Blast"],
            42: ["Psychic", "Moonblast"]
        }
    },
    "houndoom": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 90, "speed": 95},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"],
            42: ["Focus Blast", "Hyper Beam"]
        }
    },
    "houndstone": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 72, "maxhp": 72, "dm": 115, "speed": 68},
        "learns": {
            1: ["Lick", "Astonish"],
            8: ["Confusion", "Shadow Ball"],
            18: ["Dark Pulse", "Will-o-Wisp"],
            30: ["Destiny Bond", "Shadow Ball"],
            42: ["Focus Blast", "Psychic"]
        }
    },
    "hydreigon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 92, "maxhp": 92, "dm": 147, "speed": 98},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"],
            42: ["Focus Blast", "Hyper Beam"]
        }
    },
    "hypno": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 73, "maxhp": 73, "dm": 73, "speed": 67},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"],
            30: ["Energy Ball", "Focus Blast"]
        }
    },
    "incineroar": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 95, "maxhp": 95, "dm": 115, "speed": 60},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "indeedee": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 65, "speed": 40},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"],
            30: ["Energy Ball", "Focus Blast"],
            42: ["Psychic", "Moonblast"]
        }
    },
    "infernape": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 76, "maxhp": 76, "dm": 120, "speed": 108},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "inteleon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 85, "speed": 120},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "iron bundle": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 56, "maxhp": 56, "dm": 80, "speed": 124},
        "learns": {
            1: ["Ice Shard", "Powder Snow"],
            8: ["Icy Wind", "Ice Beam"],
            18: ["Blizzard", "Surf"],
            30: ["Earthquake", "Hyper Beam"],
            42: ["Blizzard", "Focus Blast"]
        }
    },
    "iron hands": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 102, "maxhp": 102, "dm": 72, "speed": 50},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "iron jugulis": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 82, "maxhp": 82, "dm": 80, "speed": 108},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"],
            42: ["Focus Blast", "Hyper Beam"]
        }
    },
    "iron moth": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 72, "maxhp": 72, "dm": 120, "speed": 110},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "iron thorns": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 72, "maxhp": 72, "dm": 120, "speed": 72},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"],
            42: ["Stone Edge", "Giga Impact"]
        }
    },
    "iron treads": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 90, "maxhp": 90, "dm": 112, "speed": 106},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "iron valiant": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 74, "maxhp": 74, "dm": 130, "speed": 116},
        "learns": {
            1: ["Fairy Wind", "Growl"],
            8: ["Charm", "Dazzling Gleam"],
            18: ["Play Rough", "Moonblast"],
            30: ["Psychic", "Hyper Beam"],
            42: ["Moonblast", "Dazzling Gleam"]
        }
    },
    "jellicent": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 60, "speed": 60},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "jirachi": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 100, "speed": 100},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"],
            42: ["Flash Cannon", "Hyper Beam"]
        }
    },
    "jumpluff": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 55, "speed": 110},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"]
        }
    },
    "jynx": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 50, "speed": 95},
        "learns": {
            1: ["Ice Shard", "Powder Snow"],
            8: ["Icy Wind", "Ice Beam"],
            18: ["Blizzard", "Surf"],
            30: ["Earthquake", "Hyper Beam"],
            42: ["Blizzard", "Focus Blast"]
        }
    },
    "kabutops": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 115, "speed": 80},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"]
        }
    },
    "kartana": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 59, "maxhp": 59, "dm": 181, "speed": 109},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "kecleon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 90, "speed": 40},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "kilowattrel": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 98, "speed": 125},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "kingambit": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 135, "speed": 50},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"],
            42: ["Focus Blast", "Hyper Beam"]
        }
    },
    "kingdra": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 95, "speed": 85},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "kingler": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 55, "maxhp": 55, "dm": 130, "speed": 75},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "klang": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 80, "speed": 50},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"]
        }
    },
    "klinklang": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 100, "speed": 90},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"]
        }
    },
    "komala": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 65, "speed": 65},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"],
            40: ["Giga Impact", "Earthquake"]
        }
    },
    "kommo-o": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 110, "speed": 85},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "koraidon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 135, "speed": 135},
        "learns": {
            1: ["Low Kick", "Leer"],
            8: ["Brick Break", "Bulk Up"],
            18: ["Rock Slide", "Close Combat"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Close Combat", "Giga Impact"]
        }
    },
    "kricketot": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 37, "maxhp": 37, "dm": 25, "speed": 25},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"]
        }
    },
    "kricketune": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 77, "maxhp": 77, "dm": 85, "speed": 65},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"]
        }
    },
    "kyogre": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 100, "speed": 90},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "landorus": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 89, "maxhp": 89, "dm": 125, "speed": 101},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "lanturn": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 76, "maxhp": 76, "dm": 76, "speed": 67},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "lapras": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 130, "maxhp": 130, "dm": 85, "speed": 60},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "latias": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 90, "speed": 110},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "latios": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 90, "speed": 110},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "leavanny": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 76, "maxhp": 76, "dm": 70, "speed": 92},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"]
        }
    },
    "ledian": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 55, "maxhp": 55, "dm": 35, "speed": 85},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"]
        }
    },
    "lickilicky": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 85, "maxhp": 85, "dm": 75, "speed": 50},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"],
            40: ["Giga Impact", "Earthquake"]
        }
    },
    "liepard": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 64, "maxhp": 64, "dm": 88, "speed": 106},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"]
        }
    },
    "lilligant": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 60, "speed": 90},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"]
        }
    },
    "linoone": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 78, "maxhp": 78, "dm": 70, "speed": 100},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "lopunny": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 76, "speed": 105},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "lugia": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 106, "maxhp": 106, "dm": 90, "speed": 110},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"],
            30: ["Energy Ball", "Focus Blast"],
            42: ["Psychic", "Moonblast"]
        }
    },
    "lumineon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 69, "maxhp": 69, "dm": 69, "speed": 91},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"]
        }
    },
    "lunala": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 137, "maxhp": 137, "dm": 107, "speed": 97},
        "learns": {
            1: ["Lick", "Astonish"],
            8: ["Confusion", "Shadow Ball"],
            18: ["Dark Pulse", "Will-o-Wisp"],
            30: ["Destiny Bond", "Shadow Ball"],
            42: ["Focus Blast", "Psychic"]
        }
    },
    "lurantis": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 105, "speed": 45},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"]
        }
    },
    "luvdisc": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 43, "maxhp": 43, "dm": 30, "speed": 97},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"]
        }
    },
    "lycanroc": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 115, "speed": 112},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"],
            42: ["Stone Edge", "Giga Impact"]
        }
    },
    "machamp": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 90, "maxhp": 90, "dm": 130, "speed": 55},
        "learns": {
            1: ["Low Kick", "Leer"],
            8: ["Brick Break", "Bulk Up"],
            18: ["Rock Slide", "Close Combat"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Close Combat", "Giga Impact"]
        }
    },
    "magearna": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 129, "speed": 65},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"],
            42: ["Flash Cannon", "Hyper Beam"]
        }
    },
    "magmar": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 95, "speed": 93},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "magmortar": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 130, "speed": 83},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "magnezone": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 90, "speed": 60},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "malamar": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 73, "maxhp": 73, "dm": 120, "speed": 73},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"]
        }
    },
    "mamoswine": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 110, "maxhp": 110, "dm": 130, "speed": 80},
        "learns": {
            1: ["Ice Shard", "Powder Snow"],
            8: ["Icy Wind", "Ice Beam"],
            18: ["Blizzard", "Surf"],
            30: ["Earthquake", "Hyper Beam"],
            42: ["Blizzard", "Focus Blast"]
        }
    },
    "manaphy": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 100, "speed": 100},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "mandibuzz": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 110, "maxhp": 110, "dm": 65, "speed": 80},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"],
            42: ["Focus Blast", "Hyper Beam"]
        }
    },
    "manectric": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 105, "speed": 105},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "mantine": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 85, "maxhp": 85, "dm": 40, "speed": 100},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"]
        }
    },
    "maractus": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 86, "speed": 60},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"]
        }
    },
    "marowak": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 100, "speed": 45},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"]
        }
    },
    "marshadow": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 90, "maxhp": 90, "dm": 125, "speed": 125},
        "learns": {
            1: ["Low Kick", "Leer"],
            8: ["Brick Break", "Bulk Up"],
            18: ["Rock Slide", "Close Combat"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Close Combat", "Giga Impact"]
        }
    },
    "masquerain": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 60, "speed": 80},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"]
        }
    },
    "medicham": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 66, "speed": 80},
        "learns": {
            1: ["Low Kick", "Leer"],
            8: ["Brick Break", "Bulk Up"],
            18: ["Rock Slide", "Close Combat"],
            30: ["Earthquake", "Stone Edge"]
        }
    },
    "meganium": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 60, "speed": 80},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"]
        }
    },
    "melmetal": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 135, "maxhp": 135, "dm": 143, "speed": 34},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"],
            42: ["Flash Cannon", "Hyper Beam"]
        }
    },
    "meloetta": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 77, "speed": 90},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"],
            40: ["Giga Impact", "Earthquake"]
        }
    },
    "meowscarada": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 76, "maxhp": 76, "dm": 110, "speed": 123},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "metagross": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 135, "speed": 70},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"],
            42: ["Flash Cannon", "Hyper Beam"]
        }
    },
    "mewtwo": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 106, "maxhp": 106, "dm": 110, "speed": 130},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"],
            30: ["Energy Ball", "Focus Blast"],
            42: ["Psychic", "Moonblast"]
        }
    },
    "mightyena": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 90, "speed": 70},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"]
        }
    },
    "milotic": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 95, "maxhp": 95, "dm": 60, "speed": 81},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "miltank": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 95, "maxhp": 95, "dm": 80, "speed": 100},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"],
            40: ["Giga Impact", "Earthquake"]
        }
    },
    "mimikyu": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 55, "maxhp": 55, "dm": 90, "speed": 96},
        "learns": {
            1: ["Lick", "Astonish"],
            8: ["Confusion", "Shadow Ball"],
            18: ["Dark Pulse", "Will-o-Wisp"],
            30: ["Destiny Bond", "Shadow Ball"],
            42: ["Focus Blast", "Psychic"]
        }
    },
    "minior": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 60, "speed": 120},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"],
            42: ["Stone Edge", "Giga Impact"]
        }
    },
    "miraidon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 111, "maxhp": 111, "dm": 144, "speed": 135},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "mismagius": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 75, "speed": 105},
        "learns": {
            1: ["Lick", "Astonish"],
            8: ["Confusion", "Shadow Ball"],
            18: ["Dark Pulse", "Will-o-Wisp"],
            30: ["Destiny Bond", "Shadow Ball"]
        }
    },
    "moltres": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 90, "maxhp": 90, "dm": 125, "speed": 90},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "morpeko": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 58, "maxhp": 58, "dm": 95, "speed": 97},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "mothim": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 94, "speed": 66},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"]
        }
    },
    "mudsdale": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 125, "speed": 35},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "muk": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 75, "speed": 50},
        "learns": {
            1: ["Poison Sting", "Growl"],
            8: ["Bite", "Poison Jab"],
            18: ["Sludge Bomb", "Dark Pulse"],
            30: ["Flamethrower", "Toxic"]
        }
    },
    "musharna": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 116, "maxhp": 116, "dm": 55, "speed": 29},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"],
            30: ["Energy Ball", "Focus Blast"]
        }
    },
    "nacli": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 55, "maxhp": 55, "dm": 35, "speed": 35},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"],
            42: ["Stone Edge", "Giga Impact"]
        }
    },
    "naclstack": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 60, "speed": 35},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"],
            42: ["Stone Edge", "Giga Impact"]
        }
    },
    "naganadel": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 73, "maxhp": 73, "dm": 73, "speed": 121},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "necrozma": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 97, "maxhp": 97, "dm": 101, "speed": 79},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"],
            30: ["Energy Ball", "Focus Blast"],
            42: ["Psychic", "Moonblast"]
        }
    },
    "nidoking": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 81, "maxhp": 81, "dm": 102, "speed": 85},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "nidoqueen": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 87, "maxhp": 87, "dm": 92, "speed": 76},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "ninetales": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 73, "maxhp": 73, "dm": 76, "speed": 100},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"]
        }
    },
    "noctowl": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 86, "maxhp": 86, "dm": 68, "speed": 70},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "noivern": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 85, "maxhp": 85, "dm": 97, "speed": 123},
        "learns": {
            1: ["Gust", "Quick Attack"],
            8: ["Wing Attack", "Aerial Ace"],
            18: ["Air Slash", "Roost"],
            30: ["Hurricane", "Heat Wave"],
            42: ["Hurricane", "Hyper Beam"]
        }
    },
    "obstagoon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 79, "maxhp": 79, "dm": 120, "speed": 95},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"],
            42: ["Focus Blast", "Hyper Beam"]
        }
    },
    "oranguru": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 86, "maxhp": 86, "dm": 60, "speed": 60},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"],
            40: ["Giga Impact", "Earthquake"]
        }
    },
    "orbeetle": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 84, "speed": 90},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"],
            42: ["Signal Beam", "Megahorn"]
        }
    },
    "oricorio": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 70, "speed": 96},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"]
        }
    },
    "orthworm": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 72, "maxhp": 72, "dm": 85, "speed": 65},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"],
            42: ["Flash Cannon", "Hyper Beam"]
        }
    },
    "pachirisu": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 45, "speed": 95},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"]
        }
    },
    "palafin": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 160, "speed": 100},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "palkia": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 120, "speed": 100},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "palossand": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 72, "maxhp": 72, "dm": 82, "speed": 35},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "parasect": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 95, "speed": 30},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"]
        }
    },
    "passimian": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 120, "speed": 80},
        "learns": {
            1: ["Low Kick", "Leer"],
            8: ["Brick Break", "Bulk Up"],
            18: ["Rock Slide", "Close Combat"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Close Combat", "Giga Impact"]
        }
    },
    "patrat": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 45, "maxhp": 45, "dm": 55, "speed": 31},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"]
        }
    },
    "pelipper": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 50, "speed": 65},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"]
        }
    },
    "perrserker": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 66, "maxhp": 66, "dm": 120, "speed": 50},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"],
            42: ["Flash Cannon", "Hyper Beam"]
        }
    },
    "persian": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 70, "speed": 115},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "pheromosa": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 71, "maxhp": 71, "dm": 137, "speed": 151},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"],
            42: ["Signal Beam", "Megahorn"]
        }
    },
    "phione": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 68, "maxhp": 68, "dm": 92, "speed": 80},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "pidgeot": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 83, "maxhp": 83, "dm": 100, "speed": 101},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "pikipek": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 35, "maxhp": 35, "dm": 75, "speed": 65},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"]
        }
    },
    "pinsir": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 125, "speed": 85},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"],
            42: ["Signal Beam", "Megahorn"]
        }
    },
    "politoed": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 70, "speed": 70},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"]
        }
    },
    "poliwrath": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 90, "maxhp": 90, "dm": 95, "speed": 70},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"]
        }
    },
    "polteageist": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 86, "maxhp": 86, "dm": 65, "speed": 70},
        "learns": {
            1: ["Lick", "Astonish"],
            8: ["Confusion", "Shadow Ball"],
            18: ["Dark Pulse", "Will-o-Wisp"],
            30: ["Destiny Bond", "Shadow Ball"],
            42: ["Focus Blast", "Psychic"]
        }
    },
    "porygon-z": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 84, "speed": 90},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"],
            40: ["Giga Impact", "Earthquake"]
        }
    },
    "primarina": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 74, "speed": 60},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "primeape": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 105, "speed": 95},
        "learns": {
            1: ["Low Kick", "Leer"],
            8: ["Brick Break", "Bulk Up"],
            18: ["Rock Slide", "Close Combat"],
            30: ["Earthquake", "Stone Edge"]
        }
    },
    "probopass": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 90, "speed": 40},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"]
        }
    },
    "pyroar": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 86, "maxhp": 86, "dm": 72, "speed": 106},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "quaquaval": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 85, "maxhp": 85, "dm": 120, "speed": 85},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "qwilfish": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 95, "speed": 85},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"]
        }
    },
    "rabsca": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 65, "speed": 45},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"],
            42: ["Signal Beam", "Megahorn"]
        }
    },
    "raichu": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 100, "speed": 110},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "raikou": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 115, "speed": 115},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "rampardos": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 97, "maxhp": 97, "dm": 165, "speed": 58},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"]
        }
    },
    "rapidash": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 100, "speed": 105},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"]
        }
    },
    "raticate": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 55, "maxhp": 55, "dm": 81, "speed": 97},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "rayquaza": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 105, "maxhp": 105, "dm": 150, "speed": 95},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "regice": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 100, "speed": 50},
        "learns": {
            1: ["Ice Shard", "Powder Snow"],
            8: ["Icy Wind", "Ice Beam"],
            18: ["Blizzard", "Surf"],
            30: ["Earthquake", "Hyper Beam"],
            42: ["Blizzard", "Focus Blast"]
        }
    },
    "regidrago": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 200, "maxhp": 200, "dm": 100, "speed": 50},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "regieleki": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 100, "speed": 200},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "regigigas": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 110, "maxhp": 110, "dm": 160, "speed": 100},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"],
            40: ["Giga Impact", "Earthquake"]
        }
    },
    "regirock": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 100, "speed": 50},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"],
            42: ["Stone Edge", "Giga Impact"]
        }
    },
    "registeel": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 100, "speed": 50},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"],
            42: ["Flash Cannon", "Hyper Beam"]
        }
    },
    "relicanth": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 90, "speed": 55},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"]
        }
    },
    "rellor": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 37, "maxhp": 37, "dm": 57, "speed": 25},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"],
            42: ["Signal Beam", "Megahorn"]
        }
    },
    "reshiram": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 150, "speed": 90},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "reuniclus": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 110, "maxhp": 110, "dm": 60, "speed": 30},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"],
            30: ["Energy Ball", "Focus Blast"]
        }
    },
    "revavroom": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 120, "speed": 90},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"],
            42: ["Flash Cannon", "Hyper Beam"]
        }
    },
    "rhydon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 104, "maxhp": 104, "dm": 120, "speed": 40},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "rhyperior": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 115, "maxhp": 115, "dm": 140, "speed": 40},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "ribombee": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 55, "speed": 124},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"],
            42: ["Signal Beam", "Megahorn"]
        }
    },
    "rillaboom": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 125, "speed": 85},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "roaring moon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 105, "maxhp": 105, "dm": 139, "speed": 123},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "roserade": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 125, "speed": 90},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"]
        }
    },
    "rotom-heat": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 65, "speed": 86},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "rotom-wash": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 65, "speed": 86},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "runerigus": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 95, "maxhp": 95, "dm": 145, "speed": 30},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "sableye": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 75, "speed": 50},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"]
        }
    },
    "salamence": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 95, "maxhp": 95, "dm": 135, "speed": 100},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "salazzle": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 68, "maxhp": 68, "dm": 111, "speed": 117},
        "learns": {
            1: ["Poison Sting", "Growl"],
            8: ["Bite", "Poison Jab"],
            18: ["Sludge Bomb", "Dark Pulse"],
            30: ["Flamethrower", "Toxic"]
        }
    },
    "samurott": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 100, "speed": 85},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "sandaconda": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 72, "maxhp": 72, "dm": 107, "speed": 71},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "sandslash": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 100, "speed": 65},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"]
        }
    },
    "sandy shocks": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 72, "maxhp": 72, "dm": 120, "speed": 101},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "sawsbuck": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 100, "speed": 95},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"],
            40: ["Giga Impact", "Earthquake"]
        }
    },
    "scatterbug": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 38, "maxhp": 38, "dm": 35, "speed": 35},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"]
        }
    },
    "sceptile": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 105, "speed": 120},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "scizor": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 130, "speed": 65},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"],
            42: ["Signal Beam", "Megahorn"]
        }
    },
    "scovillain": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 115, "speed": 65},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "scrafty": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 90, "speed": 58},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"],
            42: ["Focus Blast", "Hyper Beam"]
        }
    },
    "scream tail": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 115, "maxhp": 115, "dm": 65, "speed": 111},
        "learns": {
            1: ["Fairy Wind", "Growl"],
            8: ["Charm", "Dazzling Gleam"],
            18: ["Play Rough", "Moonblast"],
            30: ["Psychic", "Hyper Beam"],
            42: ["Moonblast", "Dazzling Gleam"]
        }
    },
    "seaking": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 92, "speed": 68},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"]
        }
    },
    "seismitoad": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 104, "maxhp": 104, "dm": 82, "speed": 74},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "serperior": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 75, "speed": 113},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "seviper": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 73, "maxhp": 73, "dm": 100, "speed": 65},
        "learns": {
            1: ["Poison Sting", "Growl"],
            8: ["Bite", "Poison Jab"],
            18: ["Sludge Bomb", "Dark Pulse"],
            30: ["Flamethrower", "Toxic"]
        }
    },
    "shiftry": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 90, "maxhp": 90, "dm": 100, "speed": 80},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"]
        }
    },
    "shiinotic": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 75, "speed": 30},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"]
        }
    },
    "shrudle": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 50, "maxhp": 50, "dm": 130, "speed": 30},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "sigilyph": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 72, "maxhp": 72, "dm": 97, "speed": 97},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"],
            30: ["Energy Ball", "Focus Blast"],
            42: ["Psychic", "Moonblast"]
        }
    },
    "silcoon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 50, "maxhp": 50, "dm": 35, "speed": 25},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"]
        }
    },
    "silvally": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 95, "maxhp": 95, "dm": 131, "speed": 95},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"],
            40: ["Giga Impact", "Earthquake"]
        }
    },
    "simipour": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 98, "speed": 101},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"]
        }
    },
    "simisage": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 98, "speed": 101},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"]
        }
    },
    "simisear": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 98, "speed": 101},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"]
        }
    },
    "sirfetch'd": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 62, "maxhp": 62, "dm": 138, "speed": 65},
        "learns": {
            1: ["Low Kick", "Leer"],
            8: ["Brick Break", "Bulk Up"],
            18: ["Rock Slide", "Close Combat"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Close Combat", "Giga Impact"]
        }
    },
    "skarmory": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 65, "speed": 70},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"],
            42: ["Flash Cannon", "Hyper Beam"]
        }
    },
    "skeledirge": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 104, "maxhp": 104, "dm": 75, "speed": 66},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "skuntank": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 73, "maxhp": 73, "dm": 103, "speed": 84},
        "learns": {
            1: ["Poison Sting", "Growl"],
            8: ["Bite", "Poison Jab"],
            18: ["Sludge Bomb", "Dark Pulse"],
            30: ["Flamethrower", "Toxic"]
        }
    },
    "skwovet": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 42, "maxhp": 42, "dm": 63, "speed": 45},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"]
        }
    },
    "slaking": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 150, "maxhp": 150, "dm": 160, "speed": 100},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"],
            40: ["Giga Impact", "Earthquake"]
        }
    },
    "slither wing": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 62, "maxhp": 62, "dm": 65, "speed": 81},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"],
            42: ["Signal Beam", "Megahorn"]
        }
    },
    "slowking": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 95, "maxhp": 95, "dm": 75, "speed": 30},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "slurpuff": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 72, "maxhp": 72, "dm": 86, "speed": 72},
        "learns": {
            1: ["Fairy Wind", "Growl"],
            8: ["Charm", "Dazzling Gleam"],
            18: ["Play Rough", "Moonblast"],
            30: ["Psychic", "Hyper Beam"]
        }
    },
    "smeargle": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 55, "maxhp": 55, "dm": 20, "speed": 75},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"]
        }
    },
    "smoliv": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 41, "maxhp": 41, "dm": 35, "speed": 30},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "sneasel": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 55, "maxhp": 55, "dm": 95, "speed": 115},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"]
        }
    },
    "snorlax": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 150, "maxhp": 150, "dm": 65, "speed": 30},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"],
            40: ["Giga Impact", "Earthquake"]
        }
    },
    "solgaleo": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 137, "maxhp": 137, "dm": 137, "speed": 97},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"],
            30: ["Energy Ball", "Focus Blast"],
            42: ["Psychic", "Moonblast"]
        }
    },
    "solrock": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 95, "speed": 70},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"]
        }
    },
    "spectrier": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 95, "speed": 130},
        "learns": {
            1: ["Lick", "Astonish"],
            8: ["Confusion", "Shadow Ball"],
            18: ["Dark Pulse", "Will-o-Wisp"],
            30: ["Destiny Bond", "Shadow Ball"],
            42: ["Focus Blast", "Psychic"]
        }
    },
    "spewpa": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 47, "maxhp": 47, "dm": 47, "speed": 29},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"]
        }
    },
    "spinda": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 60, "speed": 60},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "squawkabilly": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 85, "maxhp": 85, "dm": 125, "speed": 92},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"],
            40: ["Giga Impact", "Earthquake"]
        }
    },
    "stakataka": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 72, "maxhp": 72, "dm": 61, "speed": 13},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"],
            42: ["Stone Edge", "Giga Impact"]
        }
    },
    "stantler": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 73, "maxhp": 73, "dm": 95, "speed": 85},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "starmie": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 115, "speed": 115},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "steelix": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 85, "speed": 30},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"],
            42: ["Flash Cannon", "Hyper Beam"]
        }
    },
    "stonjourner": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 125, "speed": 70},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"],
            42: ["Stone Edge", "Giga Impact"]
        }
    },
    "stunfisk": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 109, "maxhp": 109, "dm": 66, "speed": 32},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"]
        }
    },
    "sudowoodo": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 100, "speed": 30},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"]
        }
    },
    "suicune": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 75, "speed": 85},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "sunkern": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 30, "maxhp": 30, "dm": 30, "speed": 30},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"]
        }
    },
    "swalot": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 73, "speed": 55},
        "learns": {
            1: ["Poison Sting", "Growl"],
            8: ["Bite", "Poison Jab"],
            18: ["Sludge Bomb", "Dark Pulse"],
            30: ["Flamethrower", "Toxic"]
        }
    },
    "swampert": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 99, "maxhp": 99, "dm": 109, "speed": 60},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "swanna": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 87, "speed": 98},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"]
        }
    },
    "sylveon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 65, "speed": 60},
        "learns": {
            1: ["Fairy Wind", "Growl"],
            8: ["Charm", "Dazzling Gleam"],
            18: ["Play Rough", "Moonblast"],
            30: ["Psychic", "Hyper Beam"],
            42: ["Moonblast", "Dazzling Gleam"]
        }
    },
    "tadbulb": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 35, "maxhp": 35, "dm": 47, "speed": 55},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "talonflame": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 78, "maxhp": 78, "dm": 81, "speed": 126},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "tangrowth": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 100, "speed": 50},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "tapu bulu": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 130, "speed": 75},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "tapu fini": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 75, "speed": 85},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "tapu koko": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 115, "speed": 130},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "tapu lele": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 85, "speed": 95},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"],
            30: ["Energy Ball", "Focus Blast"],
            42: ["Psychic", "Moonblast"]
        }
    },
    "tatsugiri": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 48, "maxhp": 48, "dm": 126, "speed": 82},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "tauros": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 100, "speed": 110},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "tentacruel": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 70, "speed": 100},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"]
        }
    },
    "terrakion": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 89, "maxhp": 89, "dm": 129, "speed": 108},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"],
            42: ["Stone Edge", "Giga Impact"]
        }
    },
    "thievul": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 110, "speed": 90},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"],
            42: ["Focus Blast", "Hyper Beam"]
        }
    },
    "throh": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 120, "maxhp": 120, "dm": 100, "speed": 45},
        "learns": {
            1: ["Low Kick", "Leer"],
            8: ["Brick Break", "Bulk Up"],
            18: ["Rock Slide", "Close Combat"],
            30: ["Earthquake", "Stone Edge"]
        }
    },
    "thundurus": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 79, "maxhp": 79, "dm": 115, "speed": 111},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "tinkatink": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 27, "maxhp": 27, "dm": 48, "speed": 58},
        "learns": {
            1: ["Fairy Wind", "Growl"],
            8: ["Charm", "Dazzling Gleam"],
            18: ["Play Rough", "Moonblast"],
            30: ["Psychic", "Hyper Beam"],
            42: ["Moonblast", "Dazzling Gleam"]
        }
    },
    "tinkaton": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 85, "maxhp": 85, "dm": 128, "speed": 94},
        "learns": {
            1: ["Fairy Wind", "Growl"],
            8: ["Charm", "Dazzling Gleam"],
            18: ["Play Rough", "Moonblast"],
            30: ["Psychic", "Hyper Beam"],
            42: ["Moonblast", "Dazzling Gleam"]
        }
    },
    "tinkatuff": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 102, "speed": 58},
        "learns": {
            1: ["Fairy Wind", "Growl"],
            8: ["Charm", "Dazzling Gleam"],
            18: ["Play Rough", "Moonblast"],
            30: ["Psychic", "Hyper Beam"],
            42: ["Moonblast", "Dazzling Gleam"]
        }
    },
    "toedscool": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 40, "maxhp": 40, "dm": 52, "speed": 40},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "toedscruel": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 100, "speed": 80},
        "learns": {
            1: ["Mud-Slap", "Sand Attack"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Earthquake"],
            30: ["Stone Edge", "Iron Head"],
            42: ["Earthquake", "Giga Impact"]
        }
    },
    "togedemaru": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 98, "speed": 96},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "togekiss": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 85, "maxhp": 85, "dm": 120, "speed": 80},
        "learns": {
            1: ["Fairy Wind", "Growl"],
            8: ["Charm", "Dazzling Gleam"],
            18: ["Play Rough", "Moonblast"],
            30: ["Psychic", "Hyper Beam"],
            42: ["Moonblast", "Dazzling Gleam"]
        }
    },
    "torkoal": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 85, "speed": 20},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "tornadus": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 101, "maxhp": 101, "dm": 112, "speed": 111},
        "learns": {
            1: ["Gust", "Quick Attack"],
            8: ["Wing Attack", "Aerial Ace"],
            18: ["Air Slash", "Roost"],
            30: ["Hurricane", "Heat Wave"],
            42: ["Hurricane", "Hyper Beam"]
        }
    },
    "toxtricity": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 98, "speed": 75},
        "learns": {
            1: ["Poison Sting", "Growl"],
            8: ["Bite", "Poison Jab"],
            18: ["Sludge Bomb", "Dark Pulse"],
            30: ["Flamethrower", "Toxic"],
            42: ["Sludge Bomb", "Giga Impact"]
        }
    },
    "trevenant": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 76, "maxhp": 76, "dm": 65, "speed": 56},
        "learns": {
            1: ["Lick", "Astonish"],
            8: ["Confusion", "Shadow Ball"],
            18: ["Dark Pulse", "Will-o-Wisp"],
            30: ["Destiny Bond", "Shadow Ball"],
            42: ["Focus Blast", "Psychic"]
        }
    },
    "tropius": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 99, "maxhp": 99, "dm": 68, "speed": 51},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"]
        }
    },
    "tsareena": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 72, "maxhp": 72, "dm": 120, "speed": 72},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "turtonator": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 84, "speed": 36},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "tyranitar": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 134, "speed": 61},
        "learns": {
            1: ["Rock Throw", "Tackle"],
            8: ["Bulldoze", "Rock Slide"],
            18: ["Stealth Rock", "Stone Edge"],
            30: ["Earthquake", "Iron Head"],
            42: ["Stone Edge", "Giga Impact"]
        }
    },
    "umbreon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 95, "maxhp": 95, "dm": 65, "speed": 65},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"],
            42: ["Focus Blast", "Hyper Beam"]
        }
    },
    "unfezant": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 105, "speed": 93},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "unown": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 48, "maxhp": 48, "dm": 72, "speed": 48},
        "learns": {
            1: ["Confusion", "Growl"],
            8: ["Zen Headbutt", "Calm Mind"],
            18: ["Psychic", "Shadow Ball"]
        }
    },
    "ursaring": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 90, "maxhp": 90, "dm": 130, "speed": 55},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"],
            40: ["Giga Impact", "Earthquake"]
        }
    },
    "urshifu": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 130, "speed": 97},
        "learns": {
            1: ["Low Kick", "Leer"],
            8: ["Brick Break", "Bulk Up"],
            18: ["Rock Slide", "Close Combat"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Close Combat", "Giga Impact"]
        }
    },
    "vanilluxe": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 71, "maxhp": 71, "dm": 65, "speed": 79},
        "learns": {
            1: ["Ice Shard", "Powder Snow"],
            8: ["Icy Wind", "Ice Beam"],
            18: ["Blizzard", "Surf"],
            30: ["Earthquake", "Hyper Beam"]
        }
    },
    "vaporeon": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 130, "maxhp": 130, "dm": 65, "speed": 65},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"]
        }
    },
    "varoom": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 55, "maxhp": 55, "dm": 85, "speed": 47},
        "learns": {
            1: ["Iron Defense", "Tackle"],
            8: ["Flash Cannon", "Iron Head"],
            18: ["Thunderbolt", "Rock Slide"],
            30: ["Earthquake", "Giga Impact"],
            42: ["Flash Cannon", "Hyper Beam"]
        }
    },
    "veluza": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 102, "speed": 70},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "venusaur": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 82, "speed": 80},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "vespiquen": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 80, "speed": 40},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"]
        }
    },
    "victreebel": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 105, "speed": 70},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"]
        }
    },
    "vigoroth": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 80, "maxhp": 80, "dm": 80, "speed": 90},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "vileplume": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 80, "speed": 50},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"]
        }
    },
    "virizion": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 91, "maxhp": 91, "dm": 90, "speed": 108},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"],
            42: ["Sludge Bomb", "Earthquake"]
        }
    },
    "volbeat": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 73, "speed": 85},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"]
        }
    },
    "volcarona": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 79, "maxhp": 79, "dm": 125, "speed": 100},
        "learns": {
            1: ["Ember", "Growl"],
            8: ["Flame Charge", "Fire Spin"],
            18: ["Flamethrower", "Flame Wheel"],
            30: ["Fire Blast", "Heat Wave"],
            42: ["Solar Beam", "Hyper Beam"]
        }
    },
    "wailord": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 170, "maxhp": 170, "dm": 80, "speed": 60},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"]
        }
    },
    "walrein": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 110, "maxhp": 110, "dm": 80, "speed": 65},
        "learns": {
            1: ["Ice Shard", "Powder Snow"],
            8: ["Icy Wind", "Ice Beam"],
            18: ["Blizzard", "Surf"],
            30: ["Earthquake", "Hyper Beam"]
        }
    },
    "weavile": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 70, "maxhp": 70, "dm": 120, "speed": 125},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"],
            42: ["Focus Blast", "Hyper Beam"]
        }
    },
    "weezing": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 65, "maxhp": 65, "dm": 90, "speed": 60},
        "learns": {
            1: ["Poison Sting", "Growl"],
            8: ["Bite", "Poison Jab"],
            18: ["Sludge Bomb", "Dark Pulse"],
            30: ["Flamethrower", "Toxic"]
        }
    },
    "whimsicott": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 67, "speed": 116},
        "learns": {
            1: ["Absorb", "Growl"],
            8: ["Razor Leaf", "Mega Drain"],
            18: ["Seed Bomb", "Energy Ball"],
            30: ["Solar Beam", "Leaf Storm"]
        }
    },
    "whiscash": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 110, "maxhp": 110, "dm": 78, "speed": 60},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"]
        }
    },
    "wigglytuff": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 140, "maxhp": 140, "dm": 70, "speed": 45},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "wiglett": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 35, "maxhp": 35, "dm": 35, "speed": 55},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "wooloo": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 42, "maxhp": 42, "dm": 40, "speed": 60},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"]
        }
    },
    "wormadam": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 59, "speed": 36},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"]
        }
    },
    "wugtrio": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 90, "speed": 120},
        "learns": {
            1: ["Water Gun", "Growl"],
            8: ["Bubble Beam", "Water Pulse"],
            18: ["Aqua Tail", "Scald"],
            30: ["Surf", "Hydro Pump"],
            42: ["Ice Beam", "Blizzard"]
        }
    },
    "wurmple": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 38, "maxhp": 38, "dm": 29, "speed": 20},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"]
        }
    },
    "xerneas": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 131, "maxhp": 131, "dm": 131, "speed": 99},
        "learns": {
            1: ["Fairy Wind", "Growl"],
            8: ["Charm", "Dazzling Gleam"],
            18: ["Play Rough", "Moonblast"],
            30: ["Psychic", "Hyper Beam"],
            42: ["Moonblast", "Dazzling Gleam"]
        }
    },
    "xurkitree": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 131, "speed": 83},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "yanmega": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 86, "maxhp": 86, "dm": 76, "speed": 95},
        "learns": {
            1: ["Bug Bite", "String Shot"],
            8: ["Fury Swipes", "Signal Beam"],
            18: ["Leech Life", "X-Scissor"],
            30: ["Air Slash", "U-turn"],
            42: ["Signal Beam", "Megahorn"]
        }
    },
    "yungoos": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 48, "maxhp": 48, "dm": 48, "speed": 45},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"]
        }
    },
    "yveltal": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 126, "maxhp": 126, "dm": 131, "speed": 99},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"],
            42: ["Focus Blast", "Hyper Beam"]
        }
    },
    "zacian": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 92, "maxhp": 92, "dm": 170, "speed": 148},
        "learns": {
            1: ["Fairy Wind", "Growl"],
            8: ["Charm", "Dazzling Gleam"],
            18: ["Play Rough", "Moonblast"],
            30: ["Psychic", "Hyper Beam"],
            42: ["Moonblast", "Dazzling Gleam"]
        }
    },
    "zamazenta": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 92, "maxhp": 92, "dm": 141, "speed": 128},
        "learns": {
            1: ["Low Kick", "Leer"],
            8: ["Brick Break", "Bulk Up"],
            18: ["Rock Slide", "Close Combat"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Close Combat", "Giga Impact"]
        }
    },
    "zangoose": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 73, "maxhp": 73, "dm": 115, "speed": 90},
        "learns": {
            1: ["Tackle", "Growl"],
            7: ["Quick Attack", "Headbutt"],
            16: ["Body Slam", "Take Down"],
            28: ["Double-Edge", "Hyper Beam"]
        }
    },
    "zapdos": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 90, "maxhp": 90, "dm": 125, "speed": 100},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"],
            42: ["Thunderbolt", "Signal Beam"]
        }
    },
    "zarude": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 105, "maxhp": 105, "dm": 120, "speed": 105},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"],
            42: ["Focus Blast", "Hyper Beam"]
        }
    },
    "zebstrika": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 75, "maxhp": 75, "dm": 100, "speed": 116},
        "learns": {
            1: ["Thunder Shock", "Growl"],
            8: ["Spark", "Nuzzle"],
            18: ["Thunderbolt", "Thunder Wave"],
            30: ["Thunder", "Volt Switch"]
        }
    },
    "zekrom": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 100, "maxhp": 100, "dm": 150, "speed": 90},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    },
    "zoroark": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 60, "maxhp": 60, "dm": 105, "speed": 105},
        "learns": {
            1: ["Bite", "Leer"],
            8: ["Feint Attack", "Night Slash"],
            18: ["Dark Pulse", "Nasty Plot"],
            30: ["Flamethrower", "Dark Pulse"],
            42: ["Focus Blast", "Hyper Beam"]
        }
    },
    "zygarde": {
        "level": 0,
        "evolves_to": None,
        "stats": {"hp": 108, "maxhp": 108, "dm": 121, "speed": 85},
        "learns": {
            1: ["Twister", "Leer"],
            8: ["Bite", "Dragon Pulse"],
            18: ["Dragon Dance", "Dragon Pulse"],
            30: ["Earthquake", "Stone Edge"],
            42: ["Draco Meteor", "Hyper Beam"]
        }
    }
}
