"""
Knowledge Base for Pokemon Chatbot
Math solver, physics helper, science facts, game hints.
NO API keys, NO LLMs. Pure Python.
"""

import re
import math
import random

# ══════════════════════════════════════════════════════════════════════════════
# MATH SOLVER
# ══════════════════════════════════════════════════════════════════════════════

def solve_math(text):
    """Solve math expressions from natural language."""
    text = text.lower().strip()
    
    # Percentage: "15% of 200"
    pct_match = re.search(r'(\d+(?:\.\d+)?)\s*%\s*of\s*(\d+(?:\.\d+)?)', text)
    if pct_match:
        pct = float(pct_match.group(1))
        num = float(pct_match.group(2))
        result = (pct / 100) * num
        return f"🧮 {pct}% of {num} = {result}"
    
    # Factorial: "factorial 5" or "5!"
    fact_match = re.search(r'factorial\s*(\d+)|(\d+)\s*!', text)
    if fact_match:
        n = int(fact_match.group(1) or fact_match.group(2))
        if n > 170:
            return f"🧮 {n}! is too large to compute!"
        result = math.factorial(n)
        return f"🧮 {n}! = {result}"
    
    # Square root: "sqrt(16)" or "square root of 16"
    sqrt_match = re.search(r'sqrt\s*\(\s*(\d+(?:\.\d+)?)\s*\)|square\s*root\s*of\s*(\d+(?:\.\d+)?)', text)
    if sqrt_match:
        n = float(sqrt_match.group(1) or sqrt_match.group(2))
        result = math.sqrt(n)
        return f"🧮 {n} = {result:.4f}"
    
    # Power: "2^8" or "2 to the power of 8" or "2 raised to 8"
    pow_match = re.search(r'(\d+(?:\.\d+)?)\s*\^\s*(\d+(?:\.\d+)?)|(\d+(?:\.\d+)?)\s*(?:to the power of|raised to|power)\s*(\d+(?:\.\d+)?)', text)
    if pow_match:
        base = float(pow_match.group(1) or pow_match.group(3))
        exp = float(pow_match.group(2) or pow_match.group(4))
        result = base ** exp
        return f"🧮 {base}^{exp} = {result}"
    
    # Basic expression: "2+2", "15*3", "100/4", "10-3"
    expr_match = re.search(r'(\d+(?:\.\d+)?)\s*([\+\-\*\/\%])\s*(\d+(?:\.\d+)?)', text)
    if expr_match:
        a = float(expr_match.group(1))
        op = expr_match.group(2)
        b = float(expr_match.group(3))
        try:
            if op == '+': result = a + b
            elif op == '-': result = a - b
            elif op == '*': result = a * b
            elif op == '/':
                if b == 0: return "🧮 Division by zero! That's undefined!"
                result = a / b
            elif op == '%':
                if b == 0: return "🧮 Modulo by zero! That's undefined!"
                result = a % b
            # Format result
            if result == int(result):
                result = int(result)
            else:
                result = round(result, 4)
            op_names = {'+': '+', '-': '−', '*': '×', '/': '÷', '%': 'mod'}
            return f"🧮 {a} {op_names[op]} {b} = {result}"
        except:
            pass
    
    # Multi-step expression with parentheses
    if re.search(r'[\d\+\-\*\/\(\)\s\.]+', text) and any(op in text for op in ['+', '-', '*', '/', '(', ')']):
        try:
            # Safe eval - only allow numbers and math operators
            safe_text = re.sub(r'[^0-9\+\-\*\/\(\)\.\s]', '', text)
            if safe_text.strip():
                result = eval(safe_text)
                if result == int(result):
                    result = int(result)
                else:
                    result = round(result, 4)
                return f"🧮 {safe_text.strip()} = {result}"
        except:
            pass
    
    return None

# ══════════════════════════════════════════════════════════════════════════════
# PHYSICS HELPER
# ══════════════════════════════════════════════════════════════════════════════

PHYSICS_KNOWLEDGE = {
    'force': {
        'formula': 'F = m × a',
        'name': "Newton's Second Law",
        'description': 'Force equals mass times acceleration.',
        'units': 'Newtons (N) = kg × m/s²',
        'example': 'A 10kg object accelerating at 5m/s² has F = 10 × 5 = 50N'
    },
    'velocity': {
        'formula': 'v = d / t',
        'name': 'Velocity',
        'description': 'Velocity is displacement divided by time.',
        'units': 'meters per second (m/s)',
        'example': 'Traveling 100m in 10s gives v = 100/10 = 10 m/s'
    },
    'acceleration': {
        'formula': 'a = Δv / t',
        'name': 'Acceleration',
        'description': 'Acceleration is the change in velocity over time.',
        'units': 'meters per second squared (m/s²)',
        'example': 'Going from 0 to 20m/s in 4s gives a = 20/4 = 5 m/s²'
    },
    'energy': {
        'formula': 'E = ½mv² (kinetic) or E = mgh (potential)',
        'name': 'Energy',
        'description': 'Kinetic energy depends on mass and velocity. Potential energy depends on height.',
        'units': 'Joules (J)',
        'example': 'A 2kg ball at 10m/s has KE = ½ × 2 × 100 = 100J'
    },
    'momentum': {
        'formula': 'p = m × v',
        'name': 'Momentum',
        'description': 'Momentum is mass times velocity.',
        'units': 'kg·m/s',
        'example': 'A 5kg object moving at 3m/s has p = 5 × 3 = 15 kg·m/s'
    },
    'gravity': {
        'formula': 'F = G × (m₁ × m₂) / r²',
        'name': "Newton's Law of Gravitation",
        'description': 'Gravitational force between two masses.',
        'units': 'Newtons (N)',
        'example': 'On Earth, g ≈ 9.8 m/s², so a 10kg object weighs 98N'
    },
    'work': {
        'formula': 'W = F × d × cos(θ)',
        'name': 'Work',
        'description': 'Work is force times distance in the direction of force.',
        'units': 'Joules (J)',
        'example': 'Pushing with 10N for 5m gives W = 10 × 5 = 50J'
    },
    'power': {
        'formula': 'P = W / t',
        'name': 'Power',
        'description': 'Power is work done per unit time.',
        'units': 'Watts (W) = J/s',
        'example': 'Doing 100J of work in 5s gives P = 100/5 = 20W'
    },
    'pressure': {
        'formula': 'P = F / A',
        'name': 'Pressure',
        'description': 'Pressure is force per unit area.',
        'units': 'Pascals (Pa) = N/m²',
        'example': '100N on 2m² gives P = 100/2 = 50 Pa'
    },
    'density': {
        'formula': 'ρ = m / V',
        'name': 'Density',
        'description': 'Density is mass per unit volume.',
        'units': 'kg/m³',
        'example': '5kg in 2m³ gives ρ = 5/2 = 2.5 kg/m³'
    },
    'ohm': {
        'formula': 'V = I × R',
        'name': "Ohm's Law",
        'description': 'Voltage equals current times resistance.',
        'units': 'Volts (V) = Amps × Ohms',
        'example': '2A through 5Ω gives V = 2 × 5 = 10V'
    },
    'wave': {
        'formula': 'v = f × λ',
        'name': 'Wave Equation',
        'description': 'Wave speed equals frequency times wavelength.',
        'units': 'm/s = Hz × m',
        'example': 'A 100Hz wave with λ=2m has v = 100 × 2 = 200 m/s'
    },
    'kinetic energy': {
        'formula': 'KE = ½mv²',
        'name': 'Kinetic Energy',
        'description': 'Energy of motion.',
        'units': 'Joules (J)',
        'example': 'A 3kg object at 4m/s has KE = ½ × 3 × 16 = 24J'
    },
    'potential energy': {
        'formula': 'PE = mgh',
        'name': 'Gravitational Potential Energy',
        'description': 'Energy stored due to height.',
        'units': 'Joules (J)',
        'example': 'A 2kg object at 10m height has PE = 2 × 9.8 × 10 = 196J'
    },
}

def get_physics_help(text):
    """Answer physics questions."""
    text = text.lower()
    
    for key, info in PHYSICS_KNOWLEDGE.items():
        if key in text or any(w in text for w in key.split()):
            return (
                f"⚛️ {info['name']}\n"
                f"  📐 Formula: {info['formula']}\n"
                f"  📝 {info['description']}\n"
                f"  📏 Units: {info['units']}\n"
                f"  💡 Example: {info['example']}"
            )
    
    # General physics questions
    if 'formula' in text or 'equation' in text:
        return (
            "⚛️ I know these physics formulas:\n"
            "  • Force: F = ma\n"
            "  • Velocity: v = d/t\n"
            "  • Energy: E = ½mv² or E = mgh\n"
            "  • Momentum: p = mv\n"
            "  • Gravity: F = G(m₁m₂)/r²\n"
            "  • Work: W = F×d\n"
            "  • Power: P = W/t\n"
            "  • Ohm's Law: V = IR\n"
            "  • Wave: v = fλ\n"
            "  Ask me about any of these!"
        )
    
    if 'what is force' in text or 'define force' in text:
        return get_physics_help('force')
    if 'what is velocity' in text or 'define velocity' in text:
        return get_physics_help('velocity')
    if 'what is energy' in text or 'define energy' in text:
        return get_physics_help('energy')
    if 'what is momentum' in text or 'define momentum' in text:
        return get_physics_help('momentum')
    if 'what is gravity' in text or 'define gravity' in text:
        return get_physics_help('gravity')
    if 'what is work' in text or 'define work' in text:
        return get_physics_help('work')
    if 'what is power' in text or 'define power' in text:
        return get_physics_help('power')
    if 'what is pressure' in text or 'define pressure' in text:
        return get_physics_help('pressure')
    if 'what is density' in text or 'define density' in text:
        return get_physics_help('density')
    
    return None

# ══════════════════════════════════════════════════════════════════════════════
# SCIENCE FACTS
# ══════════════════════════════════════════════════════════════════════════════

SCIENCE_FACTS = [
    "🔬 Light travels at 299,792,458 meters per second in a vacuum.",
    "🔬 Water is the only substance that exists naturally as solid, liquid, and gas on Earth.",
    "🔬 A teaspoon of neutron star material weighs about 6 billion tons.",
    "🔬 The human body contains about 37.2 trillion cells.",
    "🔬 Sound cannot travel through a vacuum because there are no molecules to vibrate.",
    "🔬 Gold is so malleable that 1 gram can be stretched into a wire 2.4 km long.",
    "🔬 The Eiffel Tower can grow up to 15 cm in summer due to thermal expansion.",
    "🔬 A bolt of lightning is 5 times hotter than the surface of the Sun.",
    "🔬 Honey never spoils — archaeologists found 3,000-year-old honey in Egyptian tombs that was still edible.",
    "🔬 The human brain uses about 20% of the body's total energy.",
    "🔬 There are more possible chess games than atoms in the observable universe.",
    "🔬 A photon takes about 8 minutes to travel from the Sun to Earth.",
    "🔬 The core of the Earth is as hot as the surface of the Sun (~5,500°C).",
    "🔬 DNA from a single human cell, if stretched out, would be about 2 meters long.",
    "🔬 Octopuses have three hearts and blue blood.",
    "🔬 The average person walks about 100,000 miles in their lifetime.",
    "🔬 Bananas are slightly radioactive due to their potassium content.",
    "🔬 The total weight of all ants on Earth is roughly equal to the total weight of all humans.",
    "🔬 Hot water freezes faster than cold water under certain conditions (Mpemba effect).",
    "🔬 The human nose can detect over 1 trillion different scents.",
    "🔬 Glass is technically an amorphous solid, not a liquid.",
    "🔬 The speed of light is exactly 299,792,458 m/s by definition.",
    "🔬 Jupiter's Great Red Spot is a storm that has been raging for at least 350 years.",
    "🔬 The average human body contains about 5 liters of blood.",
    "🔬 Venus is the hottest planet in our solar system at 462°C.",
]

def get_science_fact():
    """Return a random science fact."""
    return random.choice(SCIENCE_FACTS)

# ══════════════════════════════════════════════════════════════════════════════
# ELEMENT INFO
# ══════════════════════════════════════════════════════════════════════════════

ELEMENTS = {
    'hydrogen': {'symbol': 'H', 'number': 1, 'mass': 1.008, 'type': 'Nonmetal', 'fact': 'Most abundant element in the universe.'},
    'helium': {'symbol': 'He', 'number': 2, 'mass': 4.003, 'type': 'Noble Gas', 'fact': 'Second most abundant element. Used in balloons.'},
    'carbon': {'symbol': 'C', 'number': 6, 'mass': 12.011, 'type': 'Nonmetal', 'fact': 'Basis of all known life. Forms diamonds and graphite.'},
    'nitrogen': {'symbol': 'N', 'number': 7, 'mass': 14.007, 'type': 'Nonmetal', 'fact': 'Makes up 78% of Earth\'s atmosphere.'},
    'oxygen': {'symbol': 'O', 'number': 8, 'mass': 15.999, 'type': 'Nonmetal', 'fact': 'Essential for respiration. Makes up 21% of air.'},
    'iron': {'symbol': 'Fe', 'number': 26, 'mass': 55.845, 'type': 'Metal', 'fact': 'Most common element on Earth by mass.'},
    'gold': {'symbol': 'Au', 'number': 79, 'mass': 196.967, 'type': 'Metal', 'fact': 'Doesn\'t tarnish. Used in jewelry and electronics.'},
    'silver': {'symbol': 'Ag', 'number': 47, 'mass': 107.868, 'type': 'Metal', 'fact': 'Best conductor of electricity.'},
    'copper': {'symbol': 'Cu', 'number': 29, 'mass': 63.546, 'type': 'Metal', 'fact': 'Used in electrical wiring and plumbing.'},
    'aluminum': {'symbol': 'Al', 'number': 13, 'mass': 26.982, 'type': 'Metal', 'fact': 'Most abundant metal in Earth\'s crust.'},
    'silicon': {'symbol': 'Si', 'number': 14, 'mass': 28.086, 'type': 'Metalloid', 'fact': 'Basis of computer chips and solar cells.'},
    'sodium': {'symbol': 'Na', 'number': 11, 'mass': 22.990, 'type': 'Metal', 'fact': 'Explodes in water. Part of table salt (NaCl).'},
    'chlorine': {'symbol': 'Cl', 'number': 17, 'mass': 35.453, 'type': 'Nonmetal', 'fact': 'Used to disinfect water. Greenish-yellow gas.'},
    'calcium': {'symbol': 'Ca', 'number': 20, 'mass': 40.078, 'type': 'Metal', 'fact': 'Essential for bones and teeth.'},
    'potassium': {'symbol': 'K', 'number': 19, 'mass': 39.098, 'type': 'Metal', 'fact': 'Essential for nerve function. Found in bananas.'},
    'uranium': {'symbol': 'U', 'number': 92, 'mass': 238.029, 'type': 'Metal', 'fact': 'Used in nuclear power plants. Radioactive.'},
    'platinum': {'symbol': 'Pt', 'number': 78, 'mass': 195.084, 'type': 'Metal', 'fact': 'Rarer than gold. Used in catalytic converters.'},
    'mercury': {'symbol': 'Hg', 'number': 80, 'mass': 200.592, 'type': 'Metal', 'fact': 'Only metal that is liquid at room temperature.'},
    'lead': {'symbol': 'Pb', 'number': 82, 'mass': 207.2, 'type': 'Metal', 'fact': 'Heavy and dense. Used in batteries.'},
    'titanium': {'symbol': 'Ti', 'number': 22, 'mass': 47.867, 'type': 'Metal', 'fact': 'Strong as steel but much lighter. Used in aerospace.'},
}

def get_element_info(text):
    """Get info about a chemical element."""
    text = text.lower()
    
    # Check for element name in text
    for name, info in ELEMENTS.items():
        if name in text:
            return (
                f"🧪 {info['symbol'].upper()} — {name.capitalize()}\n"
                f"  🔢 Atomic Number: {info['number']}\n"
                f"  ⚖️ Atomic Mass: {info['mass']}\n"
                f"  🏷️ Type: {info['type']}\n"
                f"  💡 {info['fact']}"
            )
    
    # Check for "tell me about [element]"
    for name, info in ELEMENTS.items():
        if f"about {name}" in text or f"tell me {name}" in text:
            return (
                f"🧪 {info['symbol'].upper()} — {name.capitalize()}\n"
                f"  🔢 Atomic Number: {info['number']}\n"
                f"  ⚖️ Atomic Mass: {info['mass']}\n"
                f"  🏷️ Type: {info['type']}\n"
                f"  💡 {info['fact']}"
            )
    
    return None

# ══════════════════════════════════════════════════════════════════════════════
# BIOLOGY FACTS
# ══════════════════════════════════════════════════════════════════════════════

BIOLOGY_FACTS = [
    "🧬 DNA stands for Deoxyribonucleic Acid. It carries genetic instructions for life.",
    "🧬 The human genome contains about 3 billion DNA base pairs.",
    "🧬 Humans share about 99.9% of their DNA with each other.",
    "🧬 Mitochondria are the powerhouses of the cell — they produce ATP energy.",
    "🧬 Photosynthesis converts sunlight, CO₂, and water into glucose and oxygen.",
    "🧬 The human body has about 206 bones at birth, but adults have 206.",
    "🧬 Red blood cells live for about 120 days before being replaced.",
    "🧬 The brain contains about 86 billion neurons.",
    "🧬 Evolution by natural selection was proposed by Charles Darwin in 1859.",
    "🧬 Bacteria are single-celled organisms without a nucleus (prokaryotes).",
    "🧬 The human heart beats about 100,000 times per day.",
    "🧬 Skin is the largest organ of the human body.",
    "🧬 The average human body contains about 100 trillion cells.",
    "🧬 Enzymes are biological catalysts that speed up chemical reactions.",
    "🧬 The human microbiome contains more bacterial cells than human cells.",
    "🧬 ATP (Adenosine Triphosphate) is the energy currency of cells.",
    "🧬 Meiosis produces gametes (sperm and egg cells) with half the chromosomes.",
    "🧬 The human eye can distinguish about 10 million different colors.",
    "🧬 Bones are living tissue that constantly regenerate and remodel.",
    "🧬 The liver is the only organ that can regenerate itself completely.",
]

def get_biology_fact():
    """Return a random biology fact."""
    return random.choice(BIOLOGY_FACTS)

# ══════════════════════════════════════════════════════════════════════════════
# ASTRONOMY FACTS
# ══════════════════════════════════════════════════════════════════════════════

ASTRONOMY_FACTS = [
    "🌌 The observable universe is about 93 billion light-years in diameter.",
    "🌌 There are more stars in the universe than grains of sand on Earth.",
    "🌌 A light-year is about 9.46 trillion kilometers.",
    "🌌 The Sun contains 99.86% of the mass in our solar system.",
    "🌌 Jupiter is so large that 1,300 Earths could fit inside it.",
    "🌌 Neptune's winds can reach speeds of 2,100 km/h — the fastest in the solar system.",
    "🌌 A day on Venus is longer than its year.",
    "🌌 The Moon is moving away from Earth at about 3.8 cm per year.",
    "🌌 Black holes have gravity so strong that not even light can escape.",
    "🌌 The Milky Way galaxy contains 100-400 billion stars.",
    "🌌 Mars has the tallest volcano in the solar system: Olympus Mons (21.9 km).",
    "🌌 Saturn's rings are made of ice and rock particles ranging from tiny grains to house-sized chunks.",
    "🌌 The nearest star to the Sun is Proxima Centauri, 4.24 light-years away.",
    "🌌 A neutron star is so dense that a teaspoon would weigh about 6 billion tons.",
    "🌌 The universe is about 13.8 billion years old.",
    "🌌 There are more galaxies in the observable universe than stars in the Milky Way.",
    "🌌 The Sun will become a red giant in about 5 billion years.",
    "🌌 Pluto was reclassified as a dwarf planet in 2006.",
    "🌌 Europa, a moon of Jupiter, may have a subsurface ocean that could harbor life.",
    "🌌 The cosmic microwave background is the afterglow of the Big Bang.",
]

def get_astronomy_fact():
    """Return a random astronomy fact."""
    return random.choice(ASTRONOMY_FACTS)

# ══════════════════════════════════════════════════════════════════════════════
# GAME HINTS
# ══════════════════════════════════════════════════════════════════════════════

GAME_HINTS = {
    'catch': (
        "🎮 Catching Pokemon:\n"
        "  • Weaken the Pokemon first for better catch rates\n"
        "  • Use Ultra Balls for higher catch rates\n"
        "  • Type 'CATCH' quickly during the minigame for a bonus!\n"
        "  • Shiny Pokemon are harder to catch but give 2x XP\n"
        "  • Master Balls guarantee a catch (100% rate)"
    ),
    'fuse': (
        "🧬 Fusion Lab:\n"
        "  • Select two Pokemon to fuse into one\n"
        "  • Fusion has 3 outcomes: 90% Decent, 4% CRAZY, 6% SHIT\n"
        "  • CRAZY fusions get 2.5-4x stat boosts!\n"
        "  • Fusions can go up to 5 generations deep\n"
        "  • Type combinations unlock secret hybrid moves"
    ),
    'gym': (
        "🏅 Gym Challenge:\n"
        "  • Defeat all 8 gym leaders to earn badges\n"
        "  • Each gym has a type specialist\n"
        "  • Badges unlock the Elite Four\n"
        "  • Gym battles reward coins and trophies\n"
        "  • Use type advantages for easier wins"
    ),
    'elite': (
        "👑 Elite Four:\n"
        "  • Available after earning all 8 badges\n"
        "  • 5 members: Lorelei, Bruno, Agatha, Lance, Blue\n"
        "  • You can heal between members (500 coins)\n"
        "  • Beat all 5 to become Champion!\n"
        "  • Champions get massive trophy and coin rewards"
    ),
    'tower': (
        "🗼 Battle Tower:\n"
        "  • Endless gauntlet — how far can you go?\n"
        "  • Place wagers for bonus coins (doubles every 5 rounds)\n"
        "  • Environmental rules change each round\n"
        "  • Boss rounds every 10 rounds\n"
        "  • Set new records for trophies"
    ),
    'boss': (
        "👑 Boss Raids:\n"
        "  • Challenge legendary bosses (Mewtwo, Rayquaza, etc.)\n"
        "  • Bosses have 10-20x HP and Elemental Shields\n"
        "  • Super-effective moves bypass shields\n"
        "  • Bosses have phase transitions at 50% and 25% HP\n"
        "  • Massive rewards for victories"
    ),
    'heal': (
        "🏥 Hospital:\n"
        "  • Heal HP for 1 ticket\n"
        "  • Cure status for 2 tickets\n"
        "  • Heal all for 5 tickets\n"
        "  • Buy tickets at the shop\n"
        "  • Pokemon also passively heal 5% per menu action"
    ),
    'shop': (
        "🏪 Shop:\n"
        "  • Buy Pokemon from Starter/Competitive/Legendary shops\n"
        "  • Buy items: Potions, Balls, Held Items\n"
        "  • Buy Heal Tickets (10 for 200 coins)\n"
        "  • Train Pokemon stats\n"
        "  • Craft items from your bag\n"
        "  • Relearn moves at the Move Relearner"
    ),
    'daycare': (
        "🏡 Daycare:\n"
        "  • Deposit up to 2 Pokemon for passive EXP\n"
        "  • Compatible pairs can produce Eggs\n"
        "  • Eggs hatch after 20 steps\n"
        "  • Eggs have 1/128 shiny chance\n"
        "  • Eggs can be fusions if parents are different species"
    ),
    'pokedex': (
        "📖 Pokédex:\n"
        "  • Track all Pokemon you've seen and caught\n"
        "  • View type effectiveness table\n"
        "  • Browse cosmetics shop\n"
        "  • Search for specific Pokemon\n"
        "  • Milestone rewards at 10 and 30 catches"
    ),
    'cloud': (
        "☁️ Cloud Account:\n"
        "  • Register/login to save your progress online\n"
        "  • Push saves to cloud and pull from any device\n"
        "  • View registered accounts\n"
        "  • Auto-saves to cloud on exit\n"
        "  • Works with the online server"
    ),
    'ranked': (
        "📶 GTS & Ranked PvP:\n"
        "  • Battle Ghost AI trainers at your skill level\n"
        "  • 5 tiers: Bronze → Silver → Gold → Master → Champion\n"
        "  • Win to gain RP, lose to lose RP\n"
        "  • Higher tiers give better rewards\n"
        "  • View the global leaderboard"
    ),
    'travel': (
        "🗺️ Travel:\n"
        "  • 8 regions to explore\n"
        "  • Different Pokemon spawn in each region\n"
        "  • 20% chance of random world events\n"
        "  • Events include: treasure, wild rescue, legendary sighting, merchant, ambush"
    ),
    'settings': (
        "⚙️ Settings:\n"
        "  • 25 themes to choose from\n"
        "  • Adjust animation speed\n"
        "  • Change UI border styles\n"
        "  • Customize HUD and bar styles\n"
        "  • Personalize your experience"
    ),
}

def get_game_hint(text):
    """Answer game-related questions."""
    text = text.lower()
    
    for key, hint in GAME_HINTS.items():
        if key in text:
            return hint
    
    # Common question patterns
    if 'how do i' in text or 'how to' in text:
        if 'catch' in text: return GAME_HINTS['catch']
        if 'fuse' in text or 'fusion' in text: return GAME_HINTS['fuse']
        if 'gym' in text: return GAME_HINTS['gym']
        if 'elite' in text: return GAME_HINTS['elite']
        if 'tower' in text: return GAME_HINTS['tower']
        if 'boss' in text or 'raid' in text: return GAME_HINTS['boss']
        if 'heal' in text: return GAME_HINTS['heal']
        if 'shop' in text or 'buy' in text: return GAME_HINTS['shop']
        if 'daycare' in text or 'breed' in text: return GAME_HINTS['daycare']
        if 'pokedex' in text: return GAME_HINTS['pokedex']
        if 'cloud' in text or 'save' in text or 'account' in text: return GAME_HINTS['cloud']
        if 'ranked' in text or 'pvp' in text or 'gts' in text: return GAME_HINTS['ranked']
        if 'travel' in text: return GAME_HINTS['travel']
        if 'setting' in text: return GAME_HINTS['settings']
    
    if 'what is' in text or 'what are' in text:
        if 'fusion' in text: return GAME_HINTS['fuse']
        if 'gym' in text: return GAME_HINTS['gym']
        if 'elite' in text: return GAME_HINTS['elite']
        if 'tower' in text: return GAME_HINTS['tower']
        if 'boss' in text: return GAME_HINTS['boss']
        if 'heal ticket' in text: return GAME_HINTS['heal']
        if 'daycare' in text: return GAME_HINTS['daycare']
        if 'pokedex' in text: return GAME_HINTS['pokedex']
    
    if 'help' in text or 'guide' in text or 'tutorial' in text:
        return (
            "🎮 Game Guide:\n"
            "  Start by catching Pokemon in the wild!\n"
            "  Battle in the Arena for coins\n"
            "  Challenge Gyms to earn badges\n"
            "  Fuse Pokemon for powerful combinations\n"
            "  Climb the Battle Tower for trophies\n"
            "  Fight Boss Raids for legendary rewards\n"
            "  Use the Daycare to breed new Pokemon\n"
            "  Save to cloud to keep progress safe\n"
            "  Ask me about any specific feature!"
        )
    
    return None
