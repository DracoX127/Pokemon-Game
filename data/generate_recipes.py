"""
Generates item_recipes.py - 100,000 crafting recipes
~8 lines per recipe = ~800k lines total
"""
import random

ingredients = [
    "Potion", "Super Potion", "Hyper Potion", "Max Potion", "Full Restore",
    "Revive", "Max Revive", "Ether", "Max Ether", "Elixir", "Max Elixir",
    "Poke Ball", "Great Ball", "Ultra Ball", "Master Ball",
    "Rare Candy", "PP Up", "PP Max", "Protein", "Iron", "Calcium", "Zinc", "Carbos", "HP Up",
    "Fire Stone", "Water Stone", "Thunder Stone", "Leaf Stone", "Moon Stone", "Sun Stone",
    "Shiny Stone", "Dusk Stone", "Dawn Stone", "Ice Stone",
    "Oran Berry", "Sitrus Berry", "Leppa Berry", "Pecha Berry", "Cheri Berry",
    "Chesto Berry", "Rawst Berry", "Aspear Berry", "Persim Berry", "Lum Berry",
    "Star Piece", "Stardust", "Pearl", "Big Pearl", "Nugget", "Big Nugget",
    "Honey", "Sweet Honey", "Moomoo Milk", "Fresh Water", "Soda Pop", "Lemonade",
    "Burn Heal", "Ice Heal", "Antidote", "Parlyz Heal", "Awakening", "Full Heal",
    "Oval Stone", "Razor Claw", "Razor Fang", "Electirizer", "Magmarizer",
    "Up-Grade", "Dubious Disc", "Reaper Cloth", "Protector", "Whipped Dream",
    "Sachet", "King's Rock", "Metal Coat", "Dragon Scale", "Sun Stone",
]

results = [
    "Super Potion", "Hyper Potion", "Max Potion", "Full Restore",
    "Revive", "Max Revive", "Ether", "Max Ether", "Elixir", "Max Elixir",
    "Ultra Ball", "Master Ball",
    "Rare Candy", "PP Up", "PP Max",
    "Fire Stone", "Water Stone", "Thunder Stone", "Leaf Stone", "Moon Stone",
    "Shiny Stone", "Dusk Stone", "Dawn Stone", "Ice Stone",
    "Star Piece", "Nugget", "Big Nugget",
    "Max Honey", "Moomoo Milk", "Full Heal",
    "Up-Grade", "Dubious Disc", "Reaper Cloth", "Protector",
    "King's Rock", "Metal Coat", "Dragon Scale",
]

def generate_recipes(count=100000):
    lines = []
    lines.append('"""')
    lines.append(f'ITEM RECIPES - {count} crafting recipes for items and evolutions')
    lines.append('Each recipe: ingredients list, result, crafting time, success rate')
    lines.append('"""')
    lines.append('')
    lines.append('RECIPES = [')
    lines.append('')
    
    for i in range(1, count + 1):
        num_ingredients = random.randint(2, 5)
        recipe_ingredients = {}
        for _ in range(num_ingredients):
            ing = random.choice(ingredients)
            qty = random.randint(1, 10)
            recipe_ingredients[ing] = qty
        
        result = random.choice(results)
        result_qty = random.randint(1, 3)
        
        craft_time = random.randint(1, 60)
        success_rate = random.randint(50, 99)
        
        recipe_str = " + ".join([f"{qty}x {name}" for name, qty in recipe_ingredients.items()])
        
        lines.append(f'    {{')
        lines.append(f'        "id": {i},')
        lines.append(f'        "ingredients": {recipe_ingredients},')
        lines.append(f'        "result": "{result}",')
        lines.append(f'        "result_qty": {result_qty},')
        lines.append(f'        "craft_time": {craft_time},')
        lines.append(f'        "success_rate": {success_rate},')
        lines.append(f'        "recipe": "{recipe_str}",')
        lines.append(f'        "difficulty": "{"easy" if craft_time < 20 else "medium" if craft_time < 40 else "hard"}",')
        lines.append(f'    }},')
        lines.append('')
        
        if i % 10000 == 0:
            print(f"Generated {i}/{count} recipes ({i*100//count}%)...")
    
    lines.append(']')
    lines.append('')
    
    return '\n'.join(lines)

if __name__ == "__main__":
    content = generate_recipes(100000)
    with open('item_recipes.py', 'w') as f:
        f.write(content)
    line_count = content.count('\n') + 1
    print(f"Generated {line_count} lines in item_recipes.py")
