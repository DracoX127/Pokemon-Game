"""
Gym Leader and Badge Data
"""

GYM_LEADERS = {
    "Brock": {
        "city": "Pewter City",
        "type": "Rock",
        "badge": "Boulder Badge",
        "message": "My rock-hard willpower is my greatest asset!",
        "team": {
            "Geodude": {"hp": 80, "maxhp": 80, "dm": 35, "lvl": 12, "type": "Rock", "moves": ["Rock Throw", "Tackle"], "speed": 20, "stages": {"dm": 0, "speed": 0}, "pp": {}},
            "Onix": {"hp": 120, "maxhp": 120, "dm": 45, "lvl": 14, "type": "Rock", "moves": ["Rock Slide", "Bite"], "speed": 30, "stages": {"dm": 0, "speed": 0}, "pp": {}}
        }
    },
    "Misty": {
        "city": "Cerulean City",
        "type": "Water",
        "badge": "Cascade Badge",
        "message": "My policy is an all-out offensive with Water-type Pokemon!",
        "team": {
            "Staryu": {"hp": 90, "maxhp": 90, "dm": 40, "lvl": 18, "type": "Water", "moves": ["Water Gun", "Swift"], "speed": 85, "stages": {"dm": 0, "speed": 0}, "pp": {}},
            "Starmie": {"hp": 130, "maxhp": 130, "dm": 55, "lvl": 21, "type": "Water", "moves": ["Bubble Beam", "Psychic"], "speed": 115, "stages": {"dm": 0, "speed": 0}, "pp": {}}
        }
    },
    "Lt. Surge": {
        "city": "Vermilion City",
        "type": "Electric",
        "badge": "Thunder Badge",
        "message": "Hey, kid! You think you're ready for war?!",
        "team": {
            "Voltorb": {"hp": 100, "maxhp": 100, "dm": 50, "lvl": 24, "type": "Electric", "moves": ["Thunder Shock", "Sonic Boom"], "speed": 100, "stages": {"dm": 0, "speed": 0}, "pp": {}},
            "Pikachu": {"hp": 110, "maxhp": 110, "dm": 60, "lvl": 26, "type": "Electric", "moves": ["Thunderbolt", "Quick Attack"], "speed": 90, "stages": {"dm": 0, "speed": 0}, "pp": {}},
            "Raichu": {"hp": 150, "maxhp": 150, "dm": 75, "lvl": 28, "type": "Electric", "moves": ["Thunderbolt", "Iron Tail"], "speed": 110, "stages": {"dm": 0, "speed": 0}, "pp": {}}
        }
    },
    "Erika": {
        "city": "Celadon City",
        "type": "Grass",
        "badge": "Rainbow Badge",
        "message": "I am a student of the art of flower arranging...",
        "team": {
            "Victreebel": {"hp": 160, "maxhp": 160, "dm": 80, "lvl": 32, "type": "Grass", "moves": ["Razor Leaf", "Poison Powder"], "speed": 70, "stages": {"dm": 0, "speed": 0}, "pp": {}},
            "Tangela": {"hp": 150, "maxhp": 150, "dm": 70, "lvl": 30, "type": "Grass", "moves": ["Vine Whip", "Bind"], "speed": 60, "stages": {"dm": 0, "speed": 0}, "pp": {}},
            "Vileplume": {"hp": 180, "maxhp": 180, "dm": 85, "lvl": 34, "type": "Grass", "moves": ["Solar Beam", "Stun Spore"], "speed": 50, "stages": {"dm": 0, "speed": 0}, "pp": {}}
        }
    },
    "Koga": {
        "city": "Fuchsia City",
        "type": "Poison",
        "badge": "Soul Badge",
        "message": "Despair to the wall of ninjutsu!",
        "team": {
            "Koffing": {"hp": 140, "maxhp": 140, "dm": 65, "lvl": 37, "type": "Poison", "moves": ["Sludge", "Smokescreen"], "speed": 35, "stages": {"dm": 0, "speed": 0}, "pp": {}},
            "Muk": {"hp": 200, "maxhp": 200, "dm": 90, "lvl": 39, "type": "Poison", "moves": ["Sludge Bomb", "Acid Armor"], "speed": 50, "stages": {"dm": 0, "speed": 0}, "pp": {}},
            "Weezing": {"hp": 180, "maxhp": 180, "dm": 95, "lvl": 43, "type": "Poison", "moves": ["Toxic", "Self-Destruct"], "speed": 60, "stages": {"dm": 0, "speed": 0}, "pp": {}}
        }
    },
    "Sabrina": {
        "city": "Saffron City",
        "type": "Psychic",
        "badge": "Marsh Badge",
        "message": "I had a vision of your defeat...",
        "team": {
            "Kadabra": {"hp": 150, "maxhp": 150, "dm": 110, "lvl": 45, "type": "Psychic", "moves": ["Psychic", "Recover"], "speed": 105, "stages": {"dm": 0, "speed": 0}, "pp": {}},
            "Mr. Mime": {"hp": 160, "maxhp": 160, "dm": 100, "lvl": 45, "type": "Psychic", "moves": ["Confusion", "Barrier"], "speed": 90, "stages": {"dm": 0, "speed": 0}, "pp": {}},
            "Alakazam": {"hp": 180, "maxhp": 180, "dm": 130, "lvl": 50, "type": "Psychic", "moves": ["Psychic", "Future Sight"], "speed": 120, "stages": {"dm": 0, "speed": 0}, "pp": {}}
        }
    },
    "Blaine": {
        "city": "Cinnabar Island",
        "type": "Fire",
        "badge": "Volcano Badge",
        "message": "You better have a Burn Heal! My fire is hot!",
        "team": {
            "Growlithe": {"hp": 180, "maxhp": 180, "dm": 100, "lvl": 52, "type": "Fire", "moves": ["Flame Wheel", "Take Down"], "speed": 60, "stages": {"dm": 0, "speed": 0}, "pp": {}},
            "Rapidash": {"hp": 200, "maxhp": 200, "dm": 110, "lvl": 54, "type": "Fire", "moves": ["Fire Blast", "Agility"], "speed": 105, "stages": {"dm": 0, "speed": 0}, "pp": {}},
            "Arcanine": {"hp": 250, "maxhp": 250, "dm": 140, "lvl": 58, "type": "Fire", "moves": ["Flamethrower", "Extreme Speed"], "speed": 95, "stages": {"dm": 0, "speed": 0}, "pp": {}}
        }
    },
    "Giovanni": {
        "city": "Viridian City",
        "type": "Ground",
        "badge": "Earth Badge",
        "message": "Welcome to my gym. Team Rocket is eternal!",
        "team": {
            "Rhyhorn": {"hp": 220, "maxhp": 220, "dm": 120, "lvl": 60, "type": "Ground", "moves": ["Stomp", "Horn Drill"], "speed": 25, "stages": {"dm": 0, "speed": 0}, "pp": {}},
            "Dugtrio": {"hp": 180, "maxhp": 180, "dm": 150, "lvl": 62, "type": "Ground", "moves": ["Earthquake", "Slash"], "speed": 120, "stages": {"dm": 0, "speed": 0}, "pp": {}},
            "Nidoqueen": {"hp": 240, "maxhp": 240, "dm": 130, "lvl": 64, "type": "Ground", "moves": ["Body Slam", "Earthquake"], "speed": 76, "stages": {"dm": 0, "speed": 0}, "pp": {}},
            "Nidoking": {"hp": 240, "maxhp": 240, "dm": 140, "lvl": 64, "type": "Ground", "moves": ["Thrash", "Earthquake"], "speed": 85, "stages": {"dm": 0, "speed": 0}, "pp": {}},
            "Rhydon": {"hp": 280, "maxhp": 280, "dm": 160, "lvl": 65, "type": "Ground", "moves": ["Earthquake", "Rock Slide"], "speed": 40, "stages": {"dm": 0, "speed": 0}, "pp": {}}
        }
    }
}

# ═══════════════════════════════════════════════
# ELITE FOUR + CHAMPION (post-game gauntlet)
# ═══════════════════════════════════════════════

ELITE_FOUR = [
    {
        "name": "Lorelei",
        "type": "Ice",
        "message": "Let's see if you can handle the cold!",
        "team": {
            "Dewgong": {"hp": 350, "maxhp": 350, "dm": 120, "lvl": 68, "type": "Ice", "moves": ["Ice Beam", "Surf", "Aqua Tail"], "speed": 70, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Thick Fat"},
            "Cloyster": {"hp": 300, "maxhp": 300, "dm": 140, "lvl": 69, "type": "Ice", "moves": ["Ice Shard", "Blizzard", "Hydro Pump"], "speed": 70, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Skill Link"},
            "Slowbro": {"hp": 400, "maxhp": 400, "dm": 100, "lvl": 68, "type": "Water", "moves": ["Surf", "Psychic", "Flamethrower"], "speed": 30, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Oblivious"},
            "Jynx": {"hp": 320, "maxhp": 320, "dm": 135, "lvl": 70, "type": "Ice", "moves": ["Blizzard", "Psychic", "Focus Blast"], "speed": 95, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Dry Skin"},
            "Lapras": {"hp": 450, "maxhp": 450, "dm": 130, "lvl": 72, "type": "Ice", "moves": ["Ice Beam", "Surf", "Thunderbolt"], "speed": 60, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Water Absorb"}
        }
    },
    {
        "name": "Bruno",
        "type": "Fighting",
        "message": "Show me your fighting spirit!",
        "team": {
            "Hitmonlee": {"hp": 320, "maxhp": 320, "dm": 150, "lvl": 70, "type": "Fighting", "moves": ["Close Combat", "Stone Edge", "Earthquake"], "speed": 87, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Limber"},
            "Hitmonchan": {"hp": 320, "maxhp": 320, "dm": 145, "lvl": 70, "type": "Fighting", "moves": ["Brick Break", "Ice Punch", "Fire Punch"], "speed": 76, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Iron Fist"},
            "Onix": {"hp": 350, "maxhp": 350, "dm": 110, "lvl": 71, "type": "Rock", "moves": ["Rock Slide", "Earthquake", "Iron Head"], "speed": 30, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Sturdy"},
            "Machamp": {"hp": 400, "maxhp": 400, "dm": 160, "lvl": 72, "type": "Fighting", "moves": ["Dynamic Punch", "Earthquake", "Stone Edge"], "speed": 55, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Guts"},
            "Lucario": {"hp": 360, "maxhp": 360, "dm": 155, "lvl": 74, "type": "Fighting", "moves": ["Aura Sphere", "Dragon Pulse", "Extreme Speed"], "speed": 90, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Steadfast"}
        }
    },
    {
        "name": "Agatha",
        "type": "Ghost",
        "message": "The spirits have foreseen your defeat!",
        "team": {
            "Gengar": {"hp": 350, "maxhp": 350, "dm": 160, "lvl": 72, "type": "Ghost", "moves": ["Shadow Ball", "Dark Pulse", "Sludge Bomb"], "speed": 110, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Levitate"},
            "Golbat": {"hp": 320, "maxhp": 320, "dm": 110, "lvl": 71, "type": "Poison", "moves": ["Air Slash", "Dark Pulse", "Poison Fang"], "speed": 90, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Inner Focus"},
            "Haunter": {"hp": 280, "maxhp": 280, "dm": 140, "lvl": 70, "type": "Ghost", "moves": ["Shadow Ball", "Psychic", "Sludge Bomb"], "speed": 95, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Levitate"},
            "Arbok": {"hp": 300, "maxhp": 300, "dm": 125, "lvl": 71, "type": "Poison", "moves": ["Crunch", "Gunk Shot", "Earthquake"], "speed": 80, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Intimidate"},
            "Mismagius": {"hp": 340, "maxhp": 340, "dm": 145, "lvl": 74, "type": "Ghost", "moves": ["Shadow Ball", "Dazzling Gleam", "Psychic"], "speed": 105, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Levitate"}
        }
    },
    {
        "name": "Lance",
        "type": "Dragon",
        "message": "I am the strongest Dragon Master alive!",
        "team": {
            "Dragonite": {"hp": 420, "maxhp": 420, "dm": 155, "lvl": 74, "type": "Dragon", "moves": ["Dragon Pulse", "Hurricane", "Thunder"], "speed": 80, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Marvel Scale"},
            "Aerodactyl": {"hp": 340, "maxhp": 340, "dm": 145, "lvl": 73, "type": "Rock", "moves": ["Stone Edge", "Earthquake", "Aerial Ace"], "speed": 130, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Pressure"},
            "Charizard": {"hp": 360, "maxhp": 360, "dm": 140, "lvl": 74, "type": "Fire", "moves": ["Flamethrower", "Air Slash", "Solar Beam"], "speed": 100, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Blaze"},
            "Gyarados": {"hp": 400, "maxhp": 400, "dm": 150, "lvl": 74, "type": "Water", "moves": ["Aqua Tail", "Ice Beam", "Earthquake"], "speed": 81, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Intimidate"},
            "Dragonite": {"hp": 450, "maxhp": 450, "dm": 165, "lvl": 76, "type": "Dragon", "moves": ["Draco Meteor", "Fire Blast", "Extreme Speed"], "speed": 80, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Inner Focus"}
        }
    },
    {
        "name": "Champion Blue",
        "type": "Champion",
        "badge": "Champion Ribbon",
        "message": "I've beaten the Elite Four! Now it's your turn to face ME!",
        "team": {
            "Pidgeot": {"hp": 380, "maxhp": 380, "dm": 130, "lvl": 78, "type": "Normal", "moves": ["Hurricane", "Quick Attack", "Heat Wave"], "speed": 101, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Keen Eye"},
            "Alakazam": {"hp": 320, "maxhp": 320, "dm": 170, "lvl": 78, "type": "Psychic", "moves": ["Psychic", "Shadow Ball", "Dazzling Gleam"], "speed": 120, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Magic Guard"},
            "Rhydon": {"hp": 420, "maxhp": 420, "dm": 160, "lvl": 78, "type": "Ground", "moves": ["Earthquake", "Rock Slide", "Megahorn"], "speed": 40, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Lightning Rod"},
            "Arcanine": {"hp": 400, "maxhp": 400, "dm": 155, "lvl": 79, "type": "Fire", "moves": ["Flare Blitz", "Wild Charge", "Extreme Speed"], "speed": 95, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Intimidate"},
            "Gyarados": {"hp": 400, "maxhp": 400, "dm": 160, "lvl": 79, "type": "Water", "moves": ["Aqua Tail", "Ice Beam", "Thunderbolt"], "speed": 81, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Intimidate"},
            "Charizard": {"hp": 380, "maxhp": 380, "dm": 170, "lvl": 80, "type": "Fire", "moves": ["Blast Burn", "Air Slash", "Focus Blast"], "speed": 100, "stages": {"dm": 0, "speed": 0}, "pp": {}, "ability": "Blaze"}
        }
    }
]
