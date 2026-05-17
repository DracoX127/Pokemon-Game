"""Held Items System: 52 items with battle engine hooks."""

import random
from animations import item_flash, healing_flash

HELD_ITEMS = {
    "Leftovers":    {"name":"Leftovers","desc":"Restores 1/16 max HP each turn.","trigger":"on_turn","effect":"heal","ratio":1/16,"price":2000},
    "Oran Berry":   {"name":"Oran Berry","desc":"Restores 10 HP when HP drops below 50%.","trigger":"on_hp_threshold","effect":"heal","value":10,"condition":"hp_below_50","consumable":True,"price":300},
    "Sitrus Berry": {"name":"Sitrus Berry","desc":"Restores 25% max HP when HP drops below 50%.","trigger":"on_hp_threshold","effect":"heal_ratio","value":0.25,"condition":"hp_below_50","consumable":True,"price":500},
    "Figy Berry":   {"name":"Figy Berry","desc":"Restores 33% max HP when HP drops below 50%.","trigger":"on_hp_threshold","effect":"heal_ratio","value":0.33,"condition":"hp_below_50","consumable":True,"price":400},
    "Iapapa Berry": {"name":"Iapapa Berry","desc":"Restores 33% max HP when HP drops below 25%.","trigger":"on_hp_threshold","effect":"heal_ratio","value":0.33,"condition":"hp_below_25","consumable":True,"price":400},
    "Chesto Berry": {"name":"Chesto Berry","desc":"Cures sleep.","trigger":"on_status","effect":"cure_status","status":"Sleep","consumable":True,"price":400},
    "Rawst Berry":  {"name":"Rawst Berry","desc":"Cures burn.","trigger":"on_status","effect":"cure_status","status":"Burn","consumable":True,"price":400},
    "Pecha Berry":  {"name":"Pecha Berry","desc":"Cures poison.","trigger":"on_status","effect":"cure_status","status":"Poison","consumable":True,"price":400},
    "Cheri Berry":  {"name":"Cheri Berry","desc":"Cures paralysis.","trigger":"on_status","effect":"cure_status","status":"Paralyze","consumable":True,"price":400},
    "Aspear Berry": {"name":"Aspear Berry","desc":"Cures freeze.","trigger":"on_status","effect":"cure_status","status":"Freeze","consumable":True,"price":400},
    "Persim Berry": {"name":"Persim Berry","desc":"Cures confusion.","trigger":"on_status","effect":"cure_status","status":"Confuse","consumable":True,"price":400},
    "Lum Berry":    {"name":"Lum Berry","desc":"Cures any status condition.","trigger":"on_status","effect":"cure_any","consumable":True,"price":600},
    "Leppa Berry":  {"name":"Leppa Berry","desc":"Restores 10 PP to a move when PP reaches 0.","trigger":"on_pp_empty","effect":"restore_pp","value":10,"consumable":True,"price":500},
    "Choice Band":  {"name":"Choice Band","desc":"Boosts DM by 50% but locks to one move.","trigger":"damage_boost","mult":1.5,"restriction":"lock_move","price":3000},
    "Choice Scarf": {"name":"Choice Scarf","desc":"Boosts Speed by 50% but locks to one move.","trigger":"speed_boost","mult":1.5,"restriction":"lock_move","price":3000},
    "Choice Specs": {"name":"Choice Specs","desc":"Boosts DM by 50% but locks to one move.","trigger":"damage_boost_special","mult":1.5,"restriction":"lock_move","price":3000},
    "Life Orb":     {"name":"Life Orb","desc":"Boosts DM by 30% but costs 10% max HP each attack.","trigger":"damage_boost_recoil","mult":1.3,"recoil_ratio":0.1,"price":2500},
    "Expert Belt":  {"name":"Expert Belt","desc":"Boosts super-effective damage by 20%.","trigger":"super_effective_boost","mult":1.2,"price":2000},
    "Focus Sash":   {"name":"Focus Sash","desc":"Survives with 1 HP from full HP.","trigger":"survive","condition":"full_hp","consumable":True,"price":2500},
    "Focus Band":   {"name":"Focus Band","desc":"10% chance to survive a KO.","trigger":"survive_chance","chance":0.1,"consumable":False,"price":1500},
    "Rocky Helmet": {"name":"Rocky Helmet","desc":"Damages attacker for 1/6 max HP on contact.","trigger":"on_contact_damage","ratio":1/6,"price":2000},
    "Assault Vest": {"name":"Assault Vest","desc":"Raises DM but prevents status moves.","trigger":"stat_boost_damage","mult":1.5,"restriction":"no_status","price":2000},
    "Flame Orb":    {"name":"Flame Orb","desc":"Inflicts burn on the holder at end of turn.","trigger":"passive_status","status":"Burn","price":1000},
    "Toxic Orb":    {"name":"Toxic Orb","desc":"Inflicts poison on the holder at end of turn.","trigger":"passive_status","status":"Poison","price":1000},
    "Black Sludge": {"name":"Black Sludge","desc":"Heals 1/16 HP per turn for Poison types, hurts others.","trigger":"conditional_turn","heal_ratio":1/16,"harm_ratio":-1/8,"price":1500},
    "Charcoal":     {"name":"Charcoal","desc":"Boosts Fire moves by 20%.","trigger":"type_boost","type":"Fire","mult":1.2,"price":800},
    "Mystic Water": {"name":"Mystic Water","desc":"Boosts Water moves by 20%.","trigger":"type_boost","type":"Water","mult":1.2,"price":800},
    "Miracle Seed": {"name":"Miracle Seed","desc":"Boosts Grass moves by 20%.","trigger":"type_boost","type":"Grass","mult":1.2,"price":800},
    "Magnet":       {"name":"Magnet","desc":"Boosts Electric moves by 20%.","trigger":"type_boost","type":"Electric","mult":1.2,"price":800},
    "Never-Melt Ice":{"name":"Never-Melt Ice","desc":"Boosts Ice moves by 20%.","trigger":"type_boost","type":"Ice","mult":1.2,"price":800},
    "Black Belt":   {"name":"Black Belt","desc":"Boosts Fighting moves by 20%.","trigger":"type_boost","type":"Fighting","mult":1.2,"price":800},
    "Poison Barb":  {"name":"Poison Barb","desc":"Boosts Poison moves by 20%.","trigger":"type_boost","type":"Poison","mult":1.2,"price":800},
    "Soft Sand":    {"name":"Soft Sand","desc":"Boosts Ground moves by 20%.","trigger":"type_boost","type":"Ground","mult":1.2,"price":800},
    "Sharp Beak":   {"name":"Sharp Beak","desc":"Boosts Flying moves by 20%.","trigger":"type_boost","type":"Flying","mult":1.2,"price":800},
    "Silk Scarf":   {"name":"Silk Scarf","desc":"Boosts Normal moves by 20%.","trigger":"type_boost","type":"Normal","mult":1.2,"price":800},
    "Twisted Spoon":{"name":"Twisted Spoon","desc":"Boosts Psychic moves by 20%.","trigger":"type_boost","type":"Psychic","mult":1.2,"price":800},
    "Silver Powder":{"name":"Silver Powder","desc":"Boosts Bug moves by 20%.","trigger":"type_boost","type":"Bug","mult":1.2,"price":800},
    "Hard Stone":   {"name":"Hard Stone","desc":"Boosts Rock moves by 20%.","trigger":"type_boost","type":"Rock","mult":1.2,"price":800},
    "Spell Tag":    {"name":"Spell Tag","desc":"Boosts Ghost moves by 20%.","trigger":"type_boost","type":"Ghost","mult":1.2,"price":800},
    "Dragon Fang":  {"name":"Dragon Fang","desc":"Boosts Dragon moves by 20%.","trigger":"type_boost","type":"Dragon","mult":1.2,"price":800},
    "Dark Glasses": {"name":"Dark Glasses","desc":"Boosts Dark moves by 20%.","trigger":"type_boost","type":"Dark","mult":1.2,"price":800},
    "Metal Coat":   {"name":"Metal Coat","desc":"Boosts Steel moves by 20%.","trigger":"type_boost","type":"Steel","mult":1.2,"price":800},
    "Fairy Feather":{"name":"Fairy Feather","desc":"Boosts Fairy moves by 20%.","trigger":"type_boost","type":"Fairy","mult":1.2,"price":800},
    "Shell Bell":   {"name":"Shell Bell","desc":"Restores 1/8 of damage dealt.","trigger":"on_attack_heal","ratio":1/8,"price":1500},
    "Wide Lens":    {"name":"Wide Lens","desc":"Boosts accuracy by 10%.","trigger":"accuracy_boost","mult":1.1,"price":1000},
    "Zoom Lens":    {"name":"Zoom Lens","desc":"Boosts accuracy by 20% when holder moves last.","trigger":"conditional_accuracy","mult":1.2,"price":1200},
    "King's Rock":  {"name":"King's Rock","desc":"10% chance to flinch when attacking.","trigger":"effect_add","effect":"Flinch","chance":0.1,"price":1500},
    "Razor Claw":   {"name":"Razor Claw","desc":"Boosts critical hit ratio.","trigger":"crit_boost","price":1500},
    "Scope Lens":   {"name":"Scope Lens","desc":"Boosts critical hit ratio.","trigger":"crit_boost","price":1200},
    "Quick Claw":   {"name":"Quick Claw","desc":"20% chance to move first.","trigger":"priority_chance","chance":0.2,"price":1000},
    "Metronome":    {"name":"Metronome","desc":"Boosts damage for consecutive same move use.","trigger":"consecutive_boost","mult":1.2,"max_stacks":5,"price":1500},
    "Eject Button": {"name":"Eject Button","desc":"Switches out when hit by an attack.","trigger":"on_hit_switch","consumable":True,"price":1500},
    "Air Balloon":  {"name":"Air Balloon","desc":"Gives Ground immunity until hit.","trigger":"ground_immune","condition":"not_hit","price":1500},
    "Eviolite":     {"name":"Eviolite","desc":"Boosts defense for unevolved Pokemon.","trigger":"eviolite_boost","mult":1.5,"price":2500},
    "Safety Goggles":{"name":"Safety Goggles","desc":"Protects from weather damage.","trigger":"weather_protect","price":1500},
    "Heavy-Duty Boots":{"name":"Heavy-Duty Boots","desc":"Protects from hazard damage.","trigger":"hazard_protect","price":1500},
    "Blunder Policy":{"name":"Blunder Policy","desc":"Boosts Speed when the holder misses.","trigger":"on_miss_boost","stat":"speed","stages":2,"consumable":True,"price":1000},
    "Red Card":     {"name":"Red Card","desc":"Forces the foe to switch when holder is hit.","trigger":"force_switch","consumable":True,"price":1500},
    "Charizardite X":{"name":"Charizardite X","desc":"Equip to Charizard to trigger Mega Evolution in combat.","trigger":"mega_stone","target":"charizard","mega_form":"mega charizard x","price":5000},
    "Charizardite Y":{"name":"Charizardite Y","desc":"Equip to Charizard to trigger Mega Evolution in combat.","trigger":"mega_stone","target":"charizard","mega_form":"mega charizard y","price":5000},
    "Venusaurite":  {"name":"Venusaurite","desc":"Equip to Venusaur to trigger Mega Evolution in combat.","trigger":"mega_stone","target":"venusaur","mega_form":"mega venusaur","price":5000},
    "Blastoisinite":{"name":"Blastoisinite","desc":"Equip to Blastoise to trigger Mega Evolution in combat.","trigger":"mega_stone","target":"blastoise","mega_form":"mega blastoise","price":5000},
    "Mewtwonite Y": {"name":"Mewtwonite Y","desc":"Equip to Mewtwo to trigger Mega Evolution in combat.","trigger":"mega_stone","target":"mewtwo","mega_form":"mega mewtwo y","price":10000},
    "Gengarite":    {"name":"Gengarite","desc":"Equip to Gengar to trigger Mega Evolution in combat.","trigger":"mega_stone","target":"gengar","mega_form":"mega gengar","price":5000},
    "Alakazite":    {"name":"Alakazite","desc":"Equip to Alakazam to trigger Mega Evolution in combat.","trigger":"mega_stone","target":"alakazam","mega_form":"mega alakazam","price":5000},
    "Pikashunium Z":{"name":"Pikashunium Z","desc":"Equip to Pikachu to unleash 10,000,000 Volt Thunderbolt Z-Move!","trigger":"z_crystal","target":"pikachu","z_move":"10,000,000 Volt Thunderbolt","price":5000},
    "Firium Z":     {"name":"Firium Z","desc":"Fire Z-Crystal. Unleash Inferno Overdrive Z-Move!","trigger":"z_crystal","type":"Fire","z_move":"Inferno Overdrive","price":3000},
    "Electrium Z":  {"name":"Electrium Z","desc":"Electric Z-Crystal. Unleash Gigavolt Havoc Z-Move!","trigger":"z_crystal","type":"Electric","z_move":"Gigavolt Havoc","price":3000},
    "Waterium Z":   {"name":"Waterium Z","desc":"Water Z-Crystal. Unleash Hydro Vortex Z-Move!","trigger":"z_crystal","type":"Water","z_move":"Hydro Vortex","price":3000},
    "Grassium Z":   {"name":"Grassium Z","desc":"Grass Z-Crystal. Unleash Bloom Doom Z-Move!","trigger":"z_crystal","type":"Grass","z_move":"Bloom Doom","price":3000},
    "Normalium Z":  {"name":"Normalium Z","desc":"Normal Z-Crystal. Unleash Breakneck Blitz Z-Move!","trigger":"z_crystal","type":"Normal","z_move":"Breakneck Blitz","price":3000},
}

BERRY_NAMES = ["Oran Berry","Sitrus Berry","Figy Berry","Iapapa Berry","Chesto Berry","Rawst Berry",
               "Pecha Berry","Cheri Berry","Aspear Berry","Persim Berry","Lum Berry","Leppa Berry"]
TYPE_ITEMS = ["Charcoal","Mystic Water","Miracle Seed","Magnet","Never-Melt Ice","Black Belt","Poison Barb",
              "Soft Sand","Sharp Beak","Silk Scarf","Twisted Spoon","Silver Powder","Hard Stone","Spell Tag",
              "Dragon Fang","Dark Glasses","Metal Coat","Fairy Feather"]
BATTLE_ITEMS = ["Leftovers","Choice Band","Choice Scarf","Choice Specs","Life Orb","Expert Belt",
                "Focus Sash","Focus Band","Rocky Helmet","Assault Vest","Shell Bell","Wide Lens",
                "Zoom Lens","King's Rock","Razor Claw","Scope Lens","Quick Claw","Metronome",
                "Eject Button","Air Balloon","Flame Orb","Toxic Orb","Black Sludge",
                "Eviolite","Safety Goggles","Heavy-Duty Boots","Blunder Policy","Red Card",
                "Charizardite X","Charizardite Y","Venusaurite","Blastoisinite","Mewtwonite Y","Gengarite","Alakazite",
                "Pikashunium Z","Firium Z","Electrium Z","Waterium Z","Grassium Z","Normalium Z"]

def get_type_item(poke_type):
    mapping = {
        "Fire":"Charcoal","Water":"Mystic Water","Grass":"Miracle Seed","Electric":"Magnet",
        "Ice":"Never-Melt Ice","Fighting":"Black Belt","Poison":"Poison Barb","Ground":"Soft Sand",
        "Flying":"Sharp Beak","Psychic":"Twisted Spoon","Bug":"Silver Powder","Rock":"Hard Stone",
        "Ghost":"Spell Tag","Dragon":"Dragon Fang","Dark":"Dark Glasses","Steel":"Metal Coat",
        "Fairy":"Fairy Feather","Normal":"Silk Scarf",
    }
    return mapping.get(poke_type, "Silk Scarf")

def apply_held_item_trigger(item_name, trigger, holder, attacker=None, defender=None, weather=None, move_type=None):
    if not item_name:
        return {}
    item = HELD_ITEMS.get(item_name)
    if not item:
        return {}
    result = {"messages":[],"damage_mult":1.0,"defense_mult":1.0,"speed_mult":1.0,"heal":0,
              "block":False,"consumed":False,"accuracy_mult":1.0,"recoil":0}
    hp = holder.get("hp", 1)
    maxhp = holder.get("maxhp", 1)
    hp_ratio = hp / maxhp if maxhp > 0 else 0

    if trigger == "on_turn" and item.get("trigger") == "on_turn":
        if item.get("effect") == "heal":
            item_flash(item_name)
            heal = int(maxhp * item.get("ratio", 1/16))
            holder["hp"] = min(maxhp, hp + heal)
            result["heal"] = heal
            result["messages"].append(f"{item_name}: Restored {heal} HP!")

    if trigger == "on_hp_threshold" and item.get("trigger") == "on_hp_threshold":
        cond = item.get("condition", "hp_below_50")
        meets = (cond == "hp_below_50" and hp_ratio < 0.5 and hp_ratio > 0) or \
                (cond == "hp_below_25" and hp_ratio < 0.25 and hp_ratio > 0)
        if meets:
            if item.get("effect") == "heal":
                item_flash(item_name)
                heal = item.get("value", 10)
                holder["hp"] = min(maxhp, hp + heal)
                result["heal"] = heal
                result["messages"].append(f"{item_name}: Restored {heal} HP!")
                result["consumed"] = item.get("consumable", False) and item_name in BERRY_NAMES
            elif item.get("effect") == "heal_ratio":
                item_flash(item_name)
                heal = int(maxhp * item.get("value", 0.25))
                holder["hp"] = min(maxhp, hp + heal)
                result["heal"] = heal
                result["messages"].append(f"{item_name}: Restored {heal} HP!")
                result["consumed"] = item.get("consumable", False)

    if trigger == "on_status" and item.get("trigger") == "on_status":
        if holder.get("status"):
            item_flash(item_name)
            if item.get("effect") == "cure_any":
                holder["status"] = None
                result["messages"].append(f"{item_name}: Cured the status condition!")
                result["consumed"] = item.get("consumable", False)
            elif item.get("effect") == "cure_status" and holder.get("status") == item.get("status"):
                holder["status"] = None
                result["messages"].append(f"{item_name}: Cured {item['status']}!")
                result["consumed"] = item.get("consumable", False)

    if trigger == "damage_calc" and move_type:
        if item.get("trigger") == "type_boost" and move_type == item.get("type"):
            result["damage_mult"] = item.get("mult", 1.2)
        if item.get("trigger") == "damage_boost":
            result["damage_mult"] = item.get("mult", 1.5)
        if item.get("trigger") == "damage_boost_recoil":
            result["damage_mult"] = item.get("mult", 1.3)
            result["recoil"] = int(maxhp * item.get("recoil_ratio", 0.1))
        if item.get("trigger") == "super_effective_boost":
            pass

    if trigger == "move_used" and item.get("restriction") == "lock_move" and item.get("locked") is None:
        item["locked"] = True

    if trigger == "accuracy_check":
        if item.get("trigger") == "accuracy_boost":
            result["accuracy_mult"] = item.get("mult", 1.1)

    return result
