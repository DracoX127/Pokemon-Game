"""
Generates quest_system.py - 10,000 quests with objectives, rewards, and lore
~30 lines per quest = ~300k lines total
"""
import random

quest_types = [
    ("Catch", "Catch {count} {target}-type Pokemon.", lambda: random.randint(3, 50)),
    ("Defeat", "Defeat {count} wild {target} Pokemon.", lambda: random.randint(5, 100)),
    ("Explore", "Travel to {target} and discover its secrets.", lambda: 1),
    ("Collect", "Gather {count} {target} from the wild.", lambda: random.randint(1, 20)),
    ("Battle", "Win {count} battles in {target}.", lambda: random.randint(3, 30)),
    ("Evolve", "Evolve a {target}-type Pokemon.", lambda: 1),
    ("Train", "Reach level {count} with any {target}-type Pokemon.", lambda: random.randint(15, 100)),
    ("Fuse", "Create {count} fusion Pokemon.", lambda: random.randint(1, 10)),
    ("Tower", "Reach round {count} in the Battle Tower.", lambda: random.randint(5, 100)),
]

types = ["Normal", "Fire", "Water", "Grass", "Electric", "Ice", "Fighting", "Poison", 
         "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

regions = ["Grasslands", "Forest", "Cave", "Volcano", "Ocean", "Space", "Cyber City"]

reward_items = ["Potion", "Super Potion", "Ultra Ball", "Ether", "Elixir", "Full Heal", "Rare Candy", "Revive", "X Attack", "X Speed"]

def generate_quests(count=10000):
    lines = []
    lines.append('"""')
    lines.append('QUEST SYSTEM - 10,000 procedurally generated quests')
    lines.append('Each quest has a type, objective, target, count, reward, and flavor text')
    lines.append('"""')
    lines.append('')
    lines.append('QUESTS = [')
    lines.append('')
    
    for i in range(1, count + 1):
        qt = random.choice(quest_types)
        qtype = qt[0]
        template = qt[1]
        count_func = qt[2]
        cnt = count_func()
        target = random.choice(types + regions + ["rare", "shiny", "legendary", "mythical", "ancient", "mysterious", "dark", "light", "chaos", "order"])
        
        objective = template.format(count=cnt, target=target)
        
        reward_type = random.choice(["coins", "item", "trophies", "xp"])
        if reward_type == "coins":
            reward_amount = cnt * random.randint(10, 50)
            reward_desc = f"{reward_amount} coins"
            reward = {"type": "coins", "value": reward_amount}
        elif reward_type == "item":
            reward_item = random.choice(reward_items)
            reward_qty = random.randint(1, 5)
            reward_desc = f"{reward_qty}x {reward_item}"
            reward = {"type": "item", "name": reward_item, "qty": reward_qty}
        elif reward_type == "trophies":
            reward_amount = cnt * random.randint(5, 25)
            reward_desc = f"{reward_amount} trophies"
            reward = {"type": "trophies", "value": reward_amount}
        else:
            reward_amount = cnt * random.randint(10, 30)
            reward_desc = f"{reward_amount} bonus XP"
            reward = {"type": "xp", "value": reward_amount}
        
        difficulty = "easy" if cnt < 10 else "medium" if cnt < 30 else "hard" if cnt < 60 else "expert"
        
        lines.append(f'    {{')
        lines.append(f'        "id": {i},')
        lines.append(f'        "type": "{qtype}",')
        lines.append(f'        "objective": "{objective}",')
        lines.append(f'        "target": "{target}",')
        lines.append(f'        "count": {cnt},')
        lines.append(f'        "reward": {reward},')
        lines.append(f'        "reward_desc": "{reward_desc}",')
        lines.append(f'        "difficulty": "{difficulty}",')
        giver = random.choice(["Professor Oak", "Gym Guide", "Mysterious Stranger", "Old Man", "Youngster", "Lass", "Hiker", "Fisherman", "Pokemon Breeder", "Ace Trainer", "Veteran", "Nurse Joy", "Officer Jenny", "Mr. Pokemon", "Silph Co. Executive", "Game Freak Developer", "Pokemon Ranger", "Elite Four Member"])
        description_prefix = "I need your help! " if random.random() < 0.3 else "There's a task I need done: "
        description = description_prefix + objective
        lines.append(f'        "giver": "{giver}",')
        safe_desc = description.replace('\\', '\\\\').replace('"', '\\"')
        lines.append(f'        "description": "{safe_desc}",')
        lines.append(f'        "repeatable": {str(random.random() < 0.2)},')
        lines.append(f'        "region": "{random.choice(regions)}",')
        lines.append(f'    }},')
        lines.append('')
        
        if i % 1000 == 0:
            print(f"Generated {i}/{count} quests ({i*100//count}%)...")
    
    lines.append(']')
    lines.append('')
    
    return '\n'.join(lines)

if __name__ == "__main__":
    content = generate_quests(10000)
    with open('quest_system.py', 'w') as f:
        f.write(content)
    line_count = content.count('\n') + 1
    print(f"Generated {line_count} lines in quest_system.py")
