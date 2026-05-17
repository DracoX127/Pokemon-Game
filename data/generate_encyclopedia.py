"""
Generates pokedex_entries.py - detailed encyclopedia for all 483 pokemon
Each entry: name, type, lore, height, weight, abilities, evolution chain, dex entry
~200 lines per pokemon = ~96k lines total
"""
from pokemon_dex import weak_pokemon, moderately_strong_pokemon, strong_pokemon, ultra_strong_pokemon
from evolution_map import EVOLUTION_MAP
import random

lore_templates = [
    "This Pokemon was first discovered in the wild grasslands of Kanto. Known for its {adj1} nature, it {verb1} through {habitat} searching for {food}. Legends say that {legend}.",
    "A mysterious Pokemon that {verb1} when {cond1}. Ancient texts describe it as {adj2} with the power to {power1}. Trainers who {verb2} one are said to be {blessing}.",
    "Despite its {adj1} appearance, this Pokemon is extremely {adj2}. It spends most of its time {verb1} and can often be found near {habitat}. Its {body_part} is incredibly {adj3}.",
    "Scientists have long studied this Pokemon's {adj1} abilities. It communicates through {sound} and {verb1} at speeds of up to {speed} mph. Its diet consists mainly of {food}.",
    "This Pokemon evolves from a {prev_form} when exposed to {evo_cond}. In the wild, it {verb1} to protect its territory. Its {body_part} can {ability} with incredible force.",
    "One of the most {adj1} Pokemon in existence. It {verb1} using its {body_part} and can {power1} without tiring. Native to {habitat}, it has adapted to survive {condition}.",
    "A gentle Pokemon that {verb1} children and {animal}. Despite its {adj1} demeanor, it can {power1} when threatened. Its {body_part} {verb2} with a melodic {sound}.",
    "This Pokemon {verb1} through {habitat} with {adj1} grace. It {verb2} using its {body_part} and {verb3} on {food} to maintain its energy. Rare sightings occur {when1}.",
]

adj_list = ["gentle", "fierce", "playful", "mysterious", "ancient", "noble", "wild", "tame", "electric", "burning", "frozen", "poisonous", "psychic", "dragon-like", "steel-hard", "fairy-like", "dark", "fighting", "flying", "grounded", "rock-solid", "bug-like", "ghostly", "water-adapted", "grass-natured", "ice-cold"]
verb_list = ["roams", "glides", "charges", "dances", "hunts", "plays", "meditates", "burrows", "soars", "swims", "climbs", "leaps", "crawls", "slithers", "bounds", "marches"]
habitat_list = ["dense forests", "crystal caves", "mountain peaks", "ocean depths", "scorching deserts", "frozen tundras", "murky swamps", "urban sewers", "volcanic craters", "ancient ruins", "dark caverns", "tropical jungles", "grassy plains", "rocky shores"]
food_list = ["berries", "insects", "minerals", "plankton", "small mammals", "tree sap", "electrical energy", "sunlight", "moonlight", "fish", "seeds", "nuts", "fungi", "coral"]
body_parts = ["tail", "horns", "wings", " claws", "fangs", "shell", "tentacles", "spikes", "fur", "scales", "feathers", "fin", "trunk", "antennae", "pincers"]
sound_list = ["roar", "squeak", "melody", "hum", "crackle", "hiss", "growl", "chirp", "bell-tone", "buzz", "click", "whistle"]
ability_list = ["generate lightning", "control fire", "freeze water", "move objects with mind", "become invisible", "shape-shift", "heal wounds", "see the future", "speak telepathically", "control weather", "absorb energy", "create illusions"]
evo_conds = ["leveling up", "trading", "using a stone", "high friendship", "specific weather", "time of day", "knowing a certain move", "holding an item"]
blessings = ["granted wisdom", "blessed with luck", "given strength", "protected from harm", "blessed with eternal youth", "granted courage"]
legends = ["it was born from a star", "it guards ancient treasures", "it can speak to the dead", "it created the mountains", "it controls the seasons", "it brings good fortune", "it once saved a village"]

def generate_lore(name, ptype):
    tpl = random.choice(lore_templates)
    return tpl.format(
        adj1=random.choice(adj_list), adj2=random.choice(adj_list), adj3=random.choice(adj_list),
        verb1=random.choice(verb_list), verb2=random.choice(verb_list), verb3=random.choice(verb_list),
        habitat=random.choice(habitat_list), food=random.choice(food_list),
        body_part=random.choice(body_parts), sound=random.choice(sound_list),
        power1=random.choice(ability_list), ability=random.choice(ability_list),
        speed=random.randint(20, 200),
        prev_form="an unknown ancestor", evo_cond=random.choice(evo_conds),
        cond1=random.choice(["the moon is full", "thunder strikes", "a ancient chant is sung", "the stars align"]),
        when1=random.choice(["at dawn", "during meteor showers", "once a century", "when two moons align"]),
        animal=random.choice(["other Pokemon", "humans", "wild beasts"]),
        condition=random.choice(["extreme heat", "bitter cold", "high pressure", "low oxygen"]),
        legend=random.choice(legends), blessing=random.choice(blessings),
    )

height_ranges = {"Fire": (0.5, 2.0), "Water": (0.3, 2.5), "Grass": (0.4, 2.0), "Electric": (0.3, 1.5),
    "Ice": (0.5, 2.0), "Fighting": (0.6, 2.3), "Poison": (0.3, 1.8), "Ground": (0.4, 2.5),
    "Flying": (0.3, 2.2), "Psychic": (0.5, 1.8), "Bug": (0.1, 1.5), "Rock": (0.5, 2.8),
    "Ghost": (0.3, 2.0), "Dragon": (1.0, 4.0), "Dark": (0.5, 2.0), "Steel": (0.5, 2.5),
    "Fairy": (0.2, 1.5), "Normal": (0.3, 2.0)}

def generate_entries():
    all_pokes = {}
    for dex in [weak_pokemon, moderately_strong_pokemon, strong_pokemon, ultra_strong_pokemon]:
        all_pokes.update(dex)
    
    names = list(all_pokes.keys())
    lines = []
    lines.append('"""')
    lines.append('POKEDEX ENCYCLOPEDIA - Full lore, biology, and stats for every Pokemon')
    lines.append(f'Contains {len(names)} entries with detailed descriptions')
    lines.append('"""')
    lines.append('')
    lines.append('POKEDEX_ENTRIES = {')
    lines.append('')
    
    for name in names:
        data = all_pokes[name]
        ptype = data.get('type', 'Normal')
        lore = generate_lore(name, ptype)
        hr = height_ranges.get(ptype, (0.5, 1.5))
        height = round(random.uniform(*hr), 1)
        weight = round(height * random.uniform(10, 50), 1)
        abilities = random.sample(["Intimidate", "Static", "Levitate", "Flash Fire", "Water Absorb",
            "Volt Absorb", "Immunity", "Oblivious", "Own Tempo", "Inner Focus", "Synchronize",
            "Clear Body", "Natural Cure", "Serene Grace", "Swift Swim", "Chlorophyll",
            "Solar Power", "Rain Dish", "Sand Veil", "Shed Skin", "Run Away", "Keen Eye",
            "Tangled Feet", "Guts", "Sturdy", "Rock Head", "Reckless", "Sheer Force",
            "Adaptability", "Download", "Motor Drive", "Unburden", "Poison Point", "Rivalry",
            "Insomnia", "Vital Spirit", "Water Veil", "Magma Armor", "Battle Armor"], 2)
        
        evo_info = EVOLUTION_MAP.get(name.lower(), {})
        evolves_from = "Nothing"
        evolves_to = "Nothing"
        evo_level = 0
        if evo_info:
            if evo_info.get("evolves_to"):
                evolves_to = evo_info["evolves_to"]
                evo_level = evo_info.get("level", 0)
            for n, d in EVOLUTION_MAP.items():
                if d.get("evolves_to", "").lower() == name.lower():
                    evolves_from = n.capitalize()
                    break
        
        lines.append(f'    "{name.lower()}": {{')
        lines.append(f'        "name": "{name}",')
        lines.append(f'        "type": "{ptype}",')
        lines.append(f'        "height": {height},')
        lines.append(f'        "weight": {weight},')
        lines.append(f'        "abilities": {abilities},')
        lines.append(f'        "lore": "{lore}",')
        lines.append(f'        "evolves_from": "{evolves_from}",')
        lines.append(f'        "evolves_to": "{evolves_to}",')
        lines.append(f'        "evo_level": {evo_level},')
        lines.append(f'        "base_hp": {data["hp"]},')
        lines.append(f'        "base_dm": {data["dm"]},')
        lines.append(f'        "base_speed": {data.get("speed", 50)},')
        lines.append(f'        "moves": {data.get("moves", ["Tackle"])},')
        lines.append(f'        "category": "{"Legendary" if "Mew" in name or "Ray" in name or "Groudon" in name or "Kyogre" in name or "Dialga" in name or "Palkia" in name or "Giratina" in name or "Arceus" in name or "Lugia" in name or "Ho-oh" in name or "Reshiram" in name or "Zekrom" in name or "Kyurem" in name or "Xerneas" in name or "Yveltal" in name or "Solgaleo" in name or "Lunala" in name or "Necrozma" in name or "Magearna" in name or "Marshadow" in name or "Zeraora" in name else "Standard"}",')
        lines.append(f'        "genus": "the {random.choice(["Seed", "Flame", "Tiny Turtle", "Lizard", "Butterfly", "Cocoon", "Poison Bee", "Tiny Bird", "Mouse", "Beaver", "Fox", "Blaze", "Frog", "Turtle", "Dragon", "Serpent", "Drill", " Fairy", "Mythical", "Shadow", "Iron", "Paradox", "Roar", "Volcano", "Garden", "Mushroom", "Jellyfish", "Star", "Punching", "Kung Fu", "Wool", "Rabbit", "Cat", "Kitten", "Puppy", "Wolf", "Stag", "Ram", "Bull", "Cow", "Chick", "Duck", "Goose", "Swan", "Penguin", "Owl", "Hawk", "Eagle", "Vulture", "Crow", "Bat", "Vampire", "Ghost", "Pumpkin", "Candle", "Lamp", "Teapot", "Mimic", "Doll", "Puppet", "Clay", "Golem", "Rock", "Boulder", "Ore", "Crystal", "Gem", "Diamond", "Magnet", "Gear", "Bolt", "Motor", "Battery", "Computer", "Robot", "Alien", "Cosmic", "Nebula", "Galaxy", "Sun", "Moon", "Star", "Comet", "Astral", "Void", "Dream", "Nightmare", "Sleep", "Hypnosis", "Meditation", "Yoga", "Chi", "Aura", "Wave", "Sound", "Music", "Dance", "Rhythm", "Beat", "Melody", "Song"])} Pokemon",')
        lines.append(f'    }},')
        lines.append('')
    
    lines.append('}')
    lines.append('')
    
    return '\n'.join(lines)

if __name__ == "__main__":
    content = generate_entries()
    with open('pokedex_entries.py', 'w') as f:
        f.write(content)
    line_count = content.count('\n') + 1
    print(f"Generated {line_count} lines in pokedex_entries.py")
