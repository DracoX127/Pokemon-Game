"""
Advanced Tactical AI Engine: Personas, decision trees, trash talk, and predictive battle logic.
"""

import random
import sys
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if os.path.basename(BASE_DIR) == "core":
    BASE_DIR = os.path.dirname(BASE_DIR)
for subdir in ["core", "data", "utils", "ui"]:
    full = os.path.join(BASE_DIR, subdir)
    if full not in sys.path:
        sys.path.insert(0, full)

from moves_data import MOVES, get_effectiveness

# ══════════════════════════════════════════════════════════════════════════════
# AI PERSONA DEFINITIONS
# ══════════════════════════════════════════════════════════════════════════════

AI_PERSONAS = {
    "Hyper-Offense": {
        "name": "Hyper-Offense",
        "emoji": "⚔️",
        "color_tag": "BRIGHT_RED",
        "description": "All-out attacker. Prioritizes maximum damage above all else.",
        "weights": {"damage": 0.85, "status": 0.05, "heal": 0.00, "switch": 0.05, "debuff": 0.05},
        "aggression": 0.95,
        "switch_threshold": 0.15,
        "heal_threshold": 0.10,
        "risk_tolerance": 0.80,
    },
    "Trickster": {
        "name": "Trickster",
        "emoji": "🎭",
        "color_tag": "BRIGHT_MAGENTA",
        "description": "Unpredictable. Loves status moves, switches, and mind games.",
        "weights": {"damage": 0.30, "status": 0.35, "heal": 0.05, "switch": 0.20, "debuff": 0.10},
        "aggression": 0.50,
        "switch_threshold": 0.40,
        "heal_threshold": 0.30,
        "risk_tolerance": 0.60,
    },
    "Staller": {
        "name": "Staller",
        "emoji": "🛡️",
        "color_tag": "BRIGHT_BLUE",
        "description": "Patient defender. Heals, status, and outlasts opponents.",
        "weights": {"damage": 0.15, "status": 0.30, "heal": 0.30, "switch": 0.15, "debuff": 0.10},
        "aggression": 0.20,
        "switch_threshold": 0.50,
        "heal_threshold": 0.60,
        "risk_tolerance": 0.20,
    },
    "Gambler": {
        "name": "Gambler",
        "emoji": "🎲",
        "color_tag": "BRIGHT_YELLOW",
        "description": "High-risk, high-reward. Random plays, loves crits and OHKOs.",
        "weights": {"damage": 0.50, "status": 0.15, "heal": 0.05, "switch": 0.15, "debuff": 0.15},
        "aggression": 0.70,
        "switch_threshold": 0.30,
        "heal_threshold": 0.20,
        "risk_tolerance": 0.95,
    },
    "Tactical": {
        "name": "Tactical",
        "emoji": "🧠",
        "color_tag": "BRIGHT_CYAN",
        "description": "Balanced strategist. Adapts to the situation intelligently.",
        "weights": {"damage": 0.45, "status": 0.20, "heal": 0.15, "switch": 0.10, "debuff": 0.10},
        "aggression": 0.60,
        "switch_threshold": 0.30,
        "heal_threshold": 0.40,
        "risk_tolerance": 0.50,
    },
    "Bully": {
        "name": "Bully",
        "emoji": "😈",
        "color_tag": "BRIGHT_RED",
        "description": "Targets weaknesses relentlessly. Exploits type disadvantages.",
        "weights": {"damage": 0.70, "status": 0.10, "heal": 0.05, "switch": 0.05, "debuff": 0.10},
        "aggression": 0.85,
        "switch_threshold": 0.20,
        "heal_threshold": 0.15,
        "risk_tolerance": 0.70,
    },
    "Support": {
        "name": "Support",
        "emoji": "💚",
        "color_tag": "BRIGHT_GREEN",
        "description": "Team player. Buffs allies, debuffs enemies, and provides utility.",
        "weights": {"damage": 0.20, "status": 0.25, "heal": 0.25, "switch": 0.10, "debuff": 0.20},
        "aggression": 0.30,
        "switch_threshold": 0.35,
        "heal_threshold": 0.50,
        "risk_tolerance": 0.30,
    },
}

# ══════════════════════════════════════════════════════════════════════════════
# TRASH TALK DIALOGUE SYSTEM
# ══════════════════════════════════════════════════════════════════════════════

TRASH_TALK = {
    "Hyper-Offense": {
        "intro": [
            "I'll crush you in one hit!",
            "Defense is for cowards. ATTACK!",
            "You won't survive my onslaught!",
            "Time to show you what REAL power looks like!",
            "I don't need strategy — just raw POWER!",
        ],
        "crit": [
            "HA! That's what I call a HIT!",
            "Did you see that?! PURE DESTRUCTION!",
            "CRITICAL! You're already finished!",
            "That's the power of HYPER-OFFENSE!",
            "BOOM! Did that hurt?!",
        ],
        "ko": [
            "Pathetic. One-shot.",
            "Too weak. Next!",
            "Is that all you've got?!",
            "GG. You never stood a chance.",
            "Another one bites the dust!",
        ],
        "low_hp": [
            "I'm not done yet... I'll take you with me!",
            "Even at 1 HP, I hit harder than you!",
            "You think I'm done? THINK AGAIN!",
        ],
        "defeat": [
            "Impossible... my power wasn't enough?!",
            "I... I need MORE ATTACK POWER!",
            "This isn't over! I'll come back stronger!",
        ],
        "switch": [
            "Fresh fighter, fresh pain!",
            "You can't handle my whole team!",
        ],
    },
    "Trickster": {
        "intro": [
            "You never know what I'll do next~",
            "Let's play a little game, shall we?",
            "I love mind games. Hope you're ready!",
            "Surprise is my greatest weapon!",
        ],
        "crit": [
            "Oops! Did that hurt? 😏",
            "Lucky? Or am I just that good?",
            "Hehe, didn't see that coming!",
        ],
        "ko": [
            "Tricked you~ Goodbye!",
            "That was fun! Want to play again?",
            "You fell right into my trap!",
        ],
        "low_hp": [
            "Oh no~ I'm in trouble! ...Or am I?",
            "Time for my backup plan~",
        ],
        "defeat": [
            "You're no fun... I had so many tricks left!",
            "Fine, you win this round. But I'll be back!",
        ],
        "switch": [
            "Switcheroo! Bet you didn't expect THAT!",
            "My team is full of surprises~",
        ],
    },
    "Staller": {
        "intro": [
            "I have all the time in the world.",
            "Patience is my greatest weapon.",
            "You'll tire yourself out before I do.",
            "Let's see who lasts longer~",
        ],
        "crit": [
            "Even I can hit hard when needed.",
            "That was... satisfying.",
        ],
        "ko": [
            "You exhausted yourself. How predictable.",
            "Patience pays off.",
            "Another one worn down.",
        ],
        "low_hp": [
            "I've survived worse. Much worse.",
            "Healing time...",
        ],
        "defeat": [
            "I... ran out of time. Impressive.",
            "You outlasted me. Respect.",
        ],
        "switch": [
            "Let someone else handle this.",
            "Strategic retreat.",
        ],
    },
    "Gambler": {
        "intro": [
            "All or nothing, baby!",
            "Let's roll the dice!",
            "High risk, high reward — that's my style!",
            "Feeling lucky? Because I am!",
        ],
        "crit": [
            "JACKPOT! 🎰",
            "CRIT! Lady Luck is on my side!",
            "BOOM! That's what I'm talking about!",
            "RNG gods bless me!",
        ],
        "ko": [
            "Called it! Lucky shot!",
            "Gambler's intuition never lies!",
            "Hit the jackpot on that one!",
        ],
        "low_hp": [
            "All in! Let's see what happens!",
            "One more roll of the dice!",
        ],
        "defeat": [
            "Bad luck... I'll get 'em next time!",
            "The dice weren't in my favor today.",
            "RNG screwed me. Whatever.",
        ],
        "switch": [
            "New pokemon, new luck!",
            "Let's try my luck with this one!",
        ],
    },
    "Tactical": {
        "intro": [
            "I've analyzed your team. Let's begin.",
            "Strategy beats brute force every time.",
            "I've already calculated 47 possible outcomes.",
            "Let's see how you handle a tactical mind.",
        ],
        "crit": [
            "Calculated. Expected outcome.",
            "Precision strike. As planned.",
        ],
        "ko": [
            "As predicted. Next.",
            "Tactical advantage secured.",
            "Eliminated. Proceeding.",
        ],
        "low_hp": [
            "Recalculating strategy...",
            "Adjusting tactics. Not defeated yet.",
        ],
        "defeat": [
            "My calculations were... off. Interesting.",
            "I'll need to refine my strategy.",
        ],
        "switch": [
            "Optimal switch timing.",
            "Strategic rotation.",
        ],
    },
    "Bully": {
        "intro": [
            "I'm gonna target your weakest link!",
            "You're about to get BULLIED.",
            "I know your type weaknesses. All of them.",
        ],
        "crit": [
            "SUPER EFFECTIVE! Take THAT!",
            "I knew that would crush you!",
            "Weakness exploited! HA!",
        ],
        "ko": [
            "Type advantage. GG.",
            "Too easy. You're just weak.",
            "BULLIED. Next!",
        ],
        "low_hp": [
            "I'm still stronger than you!",
            "Don't count me out yet!",
        ],
        "defeat": [
            "My typing was wrong... impossible!",
            "I'll find your weakness next time!",
        ],
        "switch": [
            "New victim incoming!",
            "Let me bring out the counter!",
        ],
    },
    "Support": {
        "intro": [
            "My team is my strength. Let's go!",
            "I fight for my friends!",
            "Together, we're unstoppable!",
        ],
        "crit": [
            "Even support can hit hard!",
            "That was for my team!",
        ],
        "ko": [
            "For the team! One down!",
            "We did it together!",
        ],
        "low_hp": [
            "My team will carry me!",
            "I won't let them down!",
        ],
        "defeat": [
            "I'm sorry, team... I failed you.",
            "We'll come back stronger together!",
        ],
        "switch": [
            "Tagging in a teammate!",
            "Let someone else shine!",
        ],
    },
}

# ══════════════════════════════════════════════════════════════════════════════
# ADVANCED MOVE ANALYSIS ENGINE
# ══════════════════════════════════════════════════════════════════════════════

def analyze_move_pool(moves_list, ally_stats, defender_type, weather="Clear"):
    """Deep analysis of all available moves with multi-factor scoring."""
    analyzed = []
    
    for m in moves_list:
        data = MOVES.get(m, {"type": "Normal", "power": 40, "category": "Physical", "effect": None, "priority": 0})
        power = data.get("power", 0)
        m_type = data.get("type", "Normal")
        category = data.get("category", "Physical")
        priority = data.get("priority", 0)
        effect = data.get("effect", {})
        
        # Type effectiveness
        eff = get_effectiveness(m_type, defender_type)
        
        # STAB bonus
        is_stab = (m_type == ally_stats.get("type", "Normal"))
        stab_mult = 1.5 if is_stab else 1.0
        
        # Weather boost
        weather_boost = 1.0
        if weather == "Sun" and m_type == "Fire":
            weather_boost = 1.5
        elif weather == "Rain" and m_type == "Water":
            weather_boost = 1.5
        elif weather == "Sandstorm" and m_type in ("Rock", "Ground", "Steel"):
            weather_boost = 1.3
        elif weather == "Hail" and m_type == "Ice":
            weather_boost = 1.5
        
        # Expected damage score
        expected_damage = power * eff * stab_mult * weather_boost
        
        # Status infliction potential
        status_to_inflict = None
        status_value = 0
        if effect and isinstance(effect, dict):
            status_to_inflict = effect.get("status")
            if status_to_inflict and not ally_stats.get("status"):
                # Value depends on status type and defender type
                if status_to_inflict == "Burn" and category == "Physical":
                    status_value = 30  # High value: halves physical attack
                elif status_to_inflict == "Paralyze":
                    status_value = 25  # Medium value: speed reduction
                elif status_to_inflict == "Poison":
                    status_value = 20  # Low-medium: damage over time
                elif status_to_inflict == "Sleep":
                    status_value = 40  # High value: prevents action
                elif status_to_inflict == "Freeze":
                    status_value = 50  # Very high: prevents action entirely
        
        # Healing potential
        heal_ratio = effect.get("heal", 0) if effect and isinstance(effect, dict) else 0
        heal_value = heal_ratio * 100 if heal_ratio > 0 else 0
        
        # Stat change potential
        stat_changes = effect.get("stages", {}) if effect and isinstance(effect, dict) else {}
        stat_change_value = sum(abs(v) * 15 for v in stat_changes.values())
        
        # Priority bonus
        priority_value = priority * 20
        
        # PP consideration
        pp = ally_stats.get("pp", {}).get(m, 0)
        pp_penalty = 0 if pp > 5 else (5 - pp) * 10
        
        # Overall utility score
        utility_score = (
            expected_damage * 0.4 +
            status_value * 0.2 +
            heal_value * 0.15 +
            stat_change_value * 0.1 +
            priority_value * 0.1 +
            (100 if eff > 1.0 else 0) * 0.05 -
            pp_penalty
        )
        
        analyzed.append({
            "name": m,
            "data": data,
            "power": power,
            "type": m_type,
            "category": category,
            "priority": priority,
            "effectiveness": eff,
            "is_stab": is_stab,
            "weather_boost": weather_boost,
            "expected_damage": expected_damage,
            "status_to_inflict": status_to_inflict,
            "status_value": status_value,
            "heal_ratio": heal_ratio,
            "heal_value": heal_value,
            "stat_changes": stat_changes,
            "stat_change_value": stat_change_value,
            "priority_value": priority_value,
            "pp": pp,
            "pp_penalty": pp_penalty,
            "utility_score": utility_score,
            "is_super_effective": eff > 1.0,
            "is_not_very_effective": eff < 1.0 and eff > 0,
            "is_immune": eff == 0,
        })
    
    return analyzed


def predict_switch(enemy_team_dict, current_name):
    """Predict which pokemon the enemy might switch to based on type advantage."""
    candidates = []
    for name, stats in enemy_team_dict.items():
        if name == current_name:
            continue
        if stats.get("hp", 0) <= 0:
            continue
        # Prefer pokemon with higher HP and better typing
        hp_ratio = stats.get("hp", 0) / stats.get("maxhp", 1)
        candidates.append((name, hp_ratio, stats.get("dm", 0)))
    
    if not candidates:
        return None
    
    # Sort by HP ratio, then by damage
    candidates.sort(key=lambda x: (x[1], x[2]), reverse=True)
    return candidates[0][0]


def calculate_threat_level(ally_stats, defender_stats):
    """Calculate how much of a threat the defender is to the ally."""
    threat = 0
    
    # DM comparison
    ally_dm = ally_stats.get("dm", 0)
    defender_dm = defender_stats.get("dm", 0)
    if defender_dm > ally_dm * 1.5:
        threat += 30
    elif defender_dm > ally_dm:
        threat += 15
    
    # Speed comparison
    ally_speed = ally_stats.get("speed", 50)
    defender_speed = defender_stats.get("speed", 50)
    if defender_speed > ally_speed * 1.3:
        threat += 20
    elif defender_speed > ally_speed:
        threat += 10
    
    # HP comparison
    ally_hp_ratio = ally_stats.get("hp", 0) / ally_stats.get("maxhp", 1)
    defender_hp_ratio = defender_stats.get("hp", 0) / defender_stats.get("maxhp", 1)
    if ally_hp_ratio < defender_hp_ratio * 0.5:
        threat += 25
    elif ally_hp_ratio < defender_hp_ratio:
        threat += 10
    
    # Status on ally
    if ally_stats.get("status"):
        threat += 15
    
    return min(threat, 100)


# ══════════════════════════════════════════════════════════════════════════════
# TACTICAL AI DECISION ENGINE
# ══════════════════════════════════════════════════════════════════════════════

def tactical_ai_decide(enemy_stats, ally_stats, enemy_team_dict, current_name,
                       ai_persona="Tactical", weather="Clear", turn_count=0):
    """
    Advanced AI decision engine using persona weights, move analysis,
    threat assessment, and predictive switching.
    
    Returns: (action_type, action_target)
        action_type: "attack", "switch"
        action_target: move_name or pokemon_name
    """
    persona = AI_PERSONAS.get(ai_persona, AI_PERSONAS["Tactical"])
    moves = enemy_stats.get("moves", ["Tackle"])
    hp_ratio = enemy_stats.get("hp", 0) / enemy_stats.get("maxhp", 1)
    
    # Analyze all moves
    analyzed_moves = analyze_move_pool(moves, enemy_stats, ally_stats.get("type", "Normal"), weather)
    
    # Filter out immune moves
    viable_moves = [m for m in analyzed_moves if not m["is_immune"]]
    if not viable_moves:
        viable_moves = analyzed_moves
    
    # Calculate threat level
    threat = calculate_threat_level(enemy_stats, ally_stats)
    
    # Check available teammates
    available_teammates = [n for n in enemy_team_dict
                          if n != current_name and enemy_team_dict[n].get("hp", 0) > 0]
    
    # ─── DECISION TREE ───
    
    # 1. CRITICAL HP: Heal or switch
    if hp_ratio < persona["heal_threshold"] * 0.5:
        heal_moves = [m for m in viable_moves if m["heal_ratio"] > 0]
        if heal_moves:
            best_heal = max(heal_moves, key=lambda x: x["heal_value"])
            return ("attack", best_heal["name"])
        
        if available_teammates and random.random() < persona["switch_threshold"] * 2:
            best_switch = predict_switch(enemy_team_dict, current_name)
            if best_switch:
                return ("switch", best_switch)
    
    # 2. LOW HP: Consider healing or switching
    if hp_ratio < persona["heal_threshold"]:
        heal_moves = [m for m in viable_moves if m["heal_ratio"] > 0]
        if heal_moves and random.random() < persona["weights"]["heal"] * 2:
            best_heal = max(heal_moves, key=lambda x: x["heal_value"])
            return ("attack", best_heal["name"])
        
        if available_teammates and random.random() < persona["switch_threshold"]:
            best_switch = predict_switch(enemy_team_dict, current_name)
            if best_switch:
                return ("switch", best_switch)
    
    # 3. HIGH THREAT: Consider switching to a counter
    if threat > 70 and available_teammates and random.random() < persona["switch_threshold"]:
        # Find a teammate with type advantage over the defender
        defender_type = ally_stats.get("type", "Normal")
        best_counter = None
        best_counter_score = 0
        for name in available_teammates:
            teammate = enemy_team_dict[name]
            teammate_type = teammate.get("type", "Normal")
            eff = get_effectiveness(teammate_type, defender_type)
            if eff > 1.0:
                score = eff * teammate.get("dm", 0) * (teammate.get("hp", 0) / teammate.get("maxhp", 1))
                if score > best_counter_score:
                    best_counter_score = score
                    best_counter = name
        
        if best_counter:
            return ("switch", best_counter)
    
    # 4. STATUS INFLECTION: If ally has no status and we have status moves
    if not ally_stats.get("status") and persona["weights"]["status"] > 0.1:
        status_moves = [m for m in viable_moves if m["status_to_inflict"]]
        if status_moves:
            # Filter out useless statuses
            valid_status = []
            for sm in status_moves:
                inflict = sm["status_to_inflict"]
                opp_type = ally_stats.get("type", "Normal")
                if inflict == "Poison" and "Poison" in opp_type:
                    continue
                if inflict == "Paralyze" and "Electric" in opp_type:
                    continue
                if inflict == "Burn" and "Fire" in opp_type:
                    continue
                valid_status.append(sm)
            
            if valid_status and random.random() < persona["weights"]["status"] * 1.5:
                best_status = max(valid_status, key=lambda x: x["status_value"])
                return ("attack", best_status["name"])
    
    # 5. DEBUFF MOVES
    if persona["weights"]["debuff"] > 0.05:
        debuff_moves = [m for m in viable_moves if m["stat_changes"]]
        if debuff_moves and random.random() < persona["weights"]["debuff"]:
            best_debuff = max(debuff_moves, key=lambda x: x["stat_change_value"])
            return ("attack", best_debuff["name"])
    
    # 6. DAMAGE SELECTION
    if persona["weights"]["damage"] > 0:
        # Hyper-Offense: pure damage
        if ai_persona == "Hyper-Offense":
            damage_moves = [m for m in viable_moves if m["power"] > 0]
            if damage_moves:
                best = max(damage_moves, key=lambda x: x["expected_damage"])
                return ("attack", best["name"])
        
        # Bully: prioritize super-effective moves
        elif ai_persona == "Bully":
            se_moves = [m for m in viable_moves if m["is_super_effective"]]
            if se_moves:
                best = max(se_moves, key=lambda x: x["expected_damage"])
                return ("attack", best["name"])
        
        # Gambler: sometimes go for low-accuracy high-power moves
        elif ai_persona == "Gambler":
            if random.random() < 0.2:
                high_power = [m for m in viable_moves if m["power"] >= 100]
                if high_power:
                    return ("attack", random.choice(high_power)["name"])
        
        # Trickster: random choice among viable moves
        elif ai_persona == "Trickster":
            if random.random() < 0.3:
                return ("attack", random.choice(viable_moves)["name"])
        
        # Tactical/Staller/Support: utility-based selection
        if viable_moves:
            best = max(viable_moves, key=lambda x: x["utility_score"])
            return ("attack", best["name"])
    
    # 7. FALLBACK: Random viable move
    if viable_moves:
        return ("attack", random.choice(viable_moves)["name"])
    
    # 8. DESPERATION: Struggle
    return ("attack", random.choice(moves))


# ══════════════════════════════════════════════════════════════════════════════
# TRASH TALK GENERATOR
# ══════════════════════════════════════════════════════════════════════════════

def get_trash_talk(ai_persona, context):
    """
    Get context-sensitive trash talk dialogue for the AI.
    
    context: "intro", "crit", "ko", "low_hp", "defeat", "switch"
    """
    persona_talk = TRASH_TALK.get(ai_persona, TRASH_TALK["Tactical"])
    messages = persona_talk.get(context, ["..."])
    return random.choice(messages)


def get_persona_emoji(ai_persona):
    """Get the emoji for an AI persona."""
    persona = AI_PERSONAS.get(ai_persona, AI_PERSONAS["Tactical"])
    return persona["emoji"]


def get_persona_description(ai_persona):
    """Get the description for an AI persona."""
    persona = AI_PERSONAS.get(ai_persona, AI_PERSONAS["Tactical"])
    return persona["description"]


def generate_ai_team(team_size, level_range, persona=None):
    """
    Generate an enemy team with a specific AI persona.
    
    Returns: (team_dict, persona_name)
    """
    if persona is None:
        persona = random.choice(list(AI_PERSONAS.keys()))
    
    # This would integrate with the existing team generation
    # For now, return the persona info
    return persona, AI_PERSONAS[persona]
