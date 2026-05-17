"""
World Map System: Regions and Spawns
"""
from ui_core import (
    DAY_TIME_ART, BEACH_ART, CAVE_ART, VOLCANO_ART,
    UNDERWATER_ART, SPACE_ART, CYBER_CITY_ART, TUNDRA_ART
)

REGIONS = {
    "Grasslands": {
        "art": DAY_TIME_ART,
        "description": "Lush green fields where many common Pokemon roam.",
        "spawns": ["Pidgey", "Rattata", "Caterpie", "Weedle", "Bulbasaur", "Pikachu", "Eevee"]
    },
    "Forest": {
        "art": BEACH_ART,
        "description": "A dense, mysterious forest filled with Bug and Grass types.",
        "spawns": ["Metapod", "Kakuna", "Butterfree", "Beedrill", "Gastly", "Scrafty"]
    },
    "Cave": {
        "art": CAVE_ART,
        "description": "A dark damp cave. Watch out for Rock and Ghost types.",
        "spawns": ["Zubat", "Geodude", "Onix", "Machop", "Gengar", "Dusknoir"]
    },
    "Volcano": {
        "art": VOLCANO_ART,
        "description": "Extremely hot! Home to Fire and Ground types.",
        "spawns": ["Charmander", "Growlithe", "Tyranitar", "Blaziken", "Magmortar"]
    },
    "Ocean": {
        "art": UNDERWATER_ART,
        "description": "The deep blue sea. Water types thrive here.",
        "spawns": ["Squirtle", "Magikarp", "Gyarados", "Lapras", "Vaporeon", "Milotic"]
    },
    "Space": {
        "art": SPACE_ART,
        "description": "The final frontier. Legendary and Ultra-strong Pokemon await.",
        "spawns": ["Mewtwo", "Rayquaza", "Dragonite", "Garchomp", "Metagross", "Deoxys"]
    },
    "Cyber City": {
        "art": CYBER_CITY_ART,
        "description": "A neon-lit future. Steel and Psychic types dominate.",
        "spawns": ["Lucario", "Bisharp", "Magnezone", "Alakazam", "Gholdengo"]
    },
    "Tundra": {
        "art": TUNDRA_ART,
        "description": "A frozen wasteland of snow and ice. Only the hardy survive.",
        "spawns": ["Articuno", "Lapras", "Mamoswine", "Glaceon", "Weavile", "Froslass", "Abomasnow", "Cloyster"]
    }
}
