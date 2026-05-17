import json
import os
import random
from pokemon_dex import weak_pokemon, moderately_strong_pokemon, strong_pokemon, ultra_strong_pokemon

def get_fusion_type(name1, name2):
    """Get the blended type for a fusion of two pokemon."""
    for dex in [weak_pokemon, moderately_strong_pokemon, strong_pokemon, ultra_strong_pokemon]:
        if name1 in dex:
            t1 = dex[name1].get("type", "Normal")
            break
    else:
        t1 = "Normal"
    for dex in [weak_pokemon, moderately_strong_pokemon, strong_pokemon, ultra_strong_pokemon]:
        if name2 in dex:
            t2 = dex[name2].get("type", "Normal")
            break
    else:
        t2 = "Normal"
    if t1 == t2:
        return t1
    type_priority = ["Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark", "Steel", "Fighting", "Ghost", "Poison", "Ground", "Flying", "Bug", "Rock", "Normal"]
    for t in type_priority:
        if t == t1 or t == t2:
            return t
    return t1

def generate_fusion_name(name1, name2):
    part1 = name1[:len(name1)//2]
    part2 = name2[len(name2)//2:]
    return (part1 + part2).capitalize()

def generate_massive_fusion_dex():
    all_pokes = {**weak_pokemon, **moderately_strong_pokemon, **strong_pokemon, **ultra_strong_pokemon}
    names = list(all_pokes.keys())
    
    print(f"Generating fusions for {len(names)} pokemon...")
    total = len(names) * len(names)
    print(f"Total combinations: {total}")
    
    count = 0
    with open('fusion_dex.py', 'w') as f:
        f.write('"""\n')
        f.write('THE ULTIMATE FUSION DEX - EVERY POSSIBLE COMBINATION\n')
        f.write(f'Generated from {len(names)} base pokemon = {total} fusions\n')
        f.write('"""\n\n')
        f.write('# Each fusion: hybrid name, averaged+boosted stats, merged type, combined moves\n')
        f.write('# speed and generation track fusion depth for the in-game Fusion Lab\n\n')
        f.write('FUSION_DEX = {\n')
        
        for name1 in names:
            p1 = all_pokes[name1]
            for name2 in names:
                f_name = generate_fusion_name(name1, name2)
                p2 = all_pokes[name2]
                
                f_hp = int(((p1['hp'] + p2['hp']) / 2) * 1.2)
                f_dm = int(((p1['dm'] + p2['dm']) / 2) * 1.2)
                f_speed = int(((p1.get('speed', 50) + p2.get('speed', 50)) / 2) * 1.1)
                f_type = p1.get('type', 'Normal')
                f_moves = list(set(p1.get('moves', []) + p2.get('moves', [])))[:4]
                
                line = f'    "{f_name.lower()}": {{"hp": {f_hp}, "maxhp": {f_hp}, "dm": {f_dm}, "speed": {f_speed}, "type": "{f_type}", "moves": {f_moves}}},\n'
                f.write(line)
                count += 1
                
                if count % 50000 == 0:
                    print(f"Generated {count}/{total} fusions ({count*100//total}%)...")
                    f.flush()
        
        f.write('}\n')
    
    print(f"Successfully generated {count} fusions in fusion_dex.py!")

if __name__ == "__main__":
    generate_massive_fusion_dex()
