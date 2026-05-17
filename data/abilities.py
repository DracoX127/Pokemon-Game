"""Ability System: 71 abilities with battle engine hooks and full 483-pokemon + form mapping."""

import random
from ui_core import ability_activation

ABILITY_ACTIVATION_TEXT = {
    "Overgrow":"Overgrow! Grass power surges!","Blaze":"Blaze! Fire rages hotter!","Torrent":"Torrent! Water swells!",
    "Swarm":"Swarm! Bug power multiplies!","Intimidate":"Intimidate cuts the foe's power!","Static":"Static shocks the attacker!",
    "Poison Point":"Poison Point stings the attacker!","Flame Body":"Flame Body burns the attacker!","Cute Charm":"Cute Charm infatuates!",
    "Guts":"Guts boosts strength!","Adaptability":"Adaptability boosts STAB power!","Sand Veil":"Sand Veil boosts evasion!",
    "Snow Cloak":"Snow Cloak boosts evasion!","Sand Rush":"Sand Rush doubles speed!","Slush Rush":"Slush Rush doubles speed!",
    "Swift Swim":"Swift Swim doubles speed in rain!","Chlorophyll":"Chlorophyll doubles speed in sun!",
    "Sand Stream":"Sand Stream whips up a sandstorm!","Drought":"Drought intensifies the sun!","Drizzle":"Drizzle brings rain!",
    "Snow Warning":"Snow Warning summons hail!","Sturdy":"Sturdy holds on!","Levitate":"Levitate provides Ground immunity!",
    "Flash Fire":"Flash Fire absorbs the Fire!","Water Absorb":"Water Absorb restores HP!","Volt Absorb":"Volt Absorb restores HP!",
    "Thick Fat":"Thick Fat reduces damage!","Heatproof":"Heatproof reduces Fire damage!","Moxie":"Moxie boosts DM!",
    "Synchronize":"Synchronize shares the status!","Natural Cure":"Natural Cure heals on switch!",
    "Lightning Rod":"Lightning Rod draws the move!","Serene Grace":"Serene Grace doubles effects!",
    "Magic Guard":"Magic Guard blocks passive damage!","Clear Body":"Clear Body prevents stat reduction!",
    "Marvel Scale":"Marvel Scale boosts defense!","Pressure":"Pressure exerts pressure!",
    "Poison Heal":"Poison Heal restores HP!","Shed Skin":"Shed Skin sheds the status!",
    "Rough Skin":"Rough Skin damages the attacker!","Iron Barbs":"Iron Barbs damages the attacker!",
    "Justified":"Justified raises DM!","Weak Armor":"Weak Armor raises speed!","Mold Breaker":"Mold Breaker negates abilities!",
    "Unnerve":"Unnerve prevents berries!","Sand Force":"Sand Force boosts power!",
    "Gale Wings":"Gale Wings gives priority!","Toxic Boost":"Toxic Boost raises DM!",
    "Solar Power":"Solar Power boosts but burns!","Dry Skin":"Dry Skin reacts to elements!",
    "Sheer Force":"Sheer Force adds power!","Huge Power":"Huge Power doubles DM!","Pure Power":"Pure Power doubles DM!",
    "Technician":"Technician boosts weak moves!","Iron Fist":"Iron Fist boosts punches!","Sand Veil":"Sand Veil boosts evasion!",
    "Sand Rush":"Sand Rush doubles speed!","Steadfast":"Steadfast raises speed from flinching!",
    "Sniper":"Sniper boosts critical hits!","Tinted Lens":"Tinted Lens boosts resisted moves!",
    "Compound Eyes":"Compound Eyes boosts accuracy!","Insomnia":"Insomnia prevents sleep!",
    "Vital Spirit":"Vital Spirit prevents sleep!","Immunity":"Immunity prevents poison!",
    "Oblivious":"Oblivious prevents infatuation!","Own Tempo":"Own Tempo prevents confusion!",
    "Water Veil":"Water Veil prevents burns!","Magma Armor":"Magma Armor prevents freezing!",
    "Battle Armor":"Battle Armor blocks critical hits!","Shell Armor":"Shell Armor blocks critical hits!",
    "Inner Focus":"Inner Focus prevents flinching!","Limber":"Limber prevents paralysis!",
    "Hyper Cutter":"Hyper Cutter prevents DM reduction!","Big Pecks":"Big Pecks prevents defense reduction!",
    "Suction Cups":"Suction Cups prevents forced switching!","Sticky Hold":"Sticky Hold prevents item theft!",
    "Soundproof":"Soundproof blocks sound moves!","Filter":"Filter reduces super-effective damage!",
    "Solid Rock":"Solid Rock reduces super-effective damage!","Wonder Guard":"Wonder Guard blocks non-effective!",
    "Shadow Tag":"Shadow Tag traps the foe!","Magic Bounce":"Magic Bounce reflects the move!",
    "Prankster":"Prankster adds priority!","Regenerator":"Regenerator restores HP!",
    "Cursed Body":"Cursed Body disables the move!","Mega Launcher":"Mega Launcher boosts the pulse!",
    "Strong Jaw":"Strong Jaw crunches down!","Tough Claws":"Tough Claws dig in!",
    "Merciless":"Merciless strikes a weak point!","Steelworker":"Steelworker fortifies!",
    "Water Bubble":"Water Bubble protects and boosts!",
}

ABILITIES = {
    "Overgrow":    {"name":"Overgrow","desc":"Powers up Grass moves when HP is low.","trigger":"low_hp","type":"Grass","mult":1.5},
    "Blaze":       {"name":"Blaze","desc":"Powers up Fire moves when HP is low.","trigger":"low_hp","type":"Fire","mult":1.5},
    "Torrent":     {"name":"Torrent","desc":"Powers up Water moves when HP is low.","trigger":"low_hp","type":"Water","mult":1.5},
    "Swarm":       {"name":"Swarm","desc":"Powers up Bug moves when HP is low.","trigger":"low_hp","type":"Bug","mult":1.5},
    "Intimidate":  {"name":"Intimidate","desc":"Lowers the foe's DM on entry.","trigger":"on_entry","effect":"lower_dm","stages":-1},
    "Static":      {"name":"Static","desc":"30% chance to paralyze on contact.","trigger":"on_contact","effect":"Paralyze","chance":0.3},
    "Poison Point":{"name":"Poison Point","desc":"30% chance to poison on contact.","trigger":"on_contact","effect":"Poison","chance":0.3},
    "Flame Body":  {"name":"Flame Body","desc":"30% chance to burn on contact.","trigger":"on_contact","effect":"Burn","chance":0.3},
    "Cute Charm":  {"name":"Cute Charm","desc":"30% chance to infatuate on contact.","trigger":"on_contact","effect":"Infatuate","chance":0.3},
    "Guts":        {"name":"Guts","desc":"Boosts DM when statused.","trigger":"status_boost","stat":"dm","mult":1.5},
    "Adaptability":{"name":"Adaptability","desc":"Powers up same-type moves.","trigger":"stab","mult":2.0},
    "Sand Veil":   {"name":"Sand Veil","desc":"Boosts evasiveness in sandstorm.","trigger":"weather","weather":"Sandstorm","evasion":1.25},
    "Snow Cloak":  {"name":"Snow Cloak","desc":"Boosts evasiveness in hail.","trigger":"weather","weather":"Hail","evasion":1.25},
    "Sand Rush":   {"name":"Sand Rush","desc":"Doubles Speed in sandstorm.","trigger":"weather_speed","weather":"Sandstorm","mult":2.0},
    "Slush Rush":  {"name":"Slush Rush","desc":"Doubles Speed in hail.","trigger":"weather_speed","weather":"Hail","mult":2.0},
    "Swift Swim":  {"name":"Swift Swim","desc":"Doubles Speed in rain.","trigger":"weather_speed","weather":"Rain","mult":2.0},
    "Chlorophyll": {"name":"Chlorophyll","desc":"Doubles Speed in sun.","trigger":"weather_speed","weather":"Sun","mult":2.0},
    "Sand Stream": {"name":"Sand Stream","desc":"Summons a sandstorm on entry.","trigger":"on_entry","effect":"weather","weather":"Sandstorm"},
    "Drought":     {"name":"Drought","desc":"Summons harsh sun on entry.","trigger":"on_entry","effect":"weather","weather":"Sun"},
    "Drizzle":     {"name":"Drizzle","desc":"Summons rain on entry.","trigger":"on_entry","effect":"weather","weather":"Rain"},
    "Snow Warning":{"name":"Snow Warning","desc":"Summons hail on entry.","trigger":"on_entry","effect":"weather","weather":"Hail"},
    "Sturdy":      {"name":"Sturdy","desc":"Survives OHKO from full HP.","trigger":"survive","condition":"full_hp"},
    "Levitate":    {"name":"Levitate","desc":"Immune to Ground moves.","trigger":"immunity","type":"Ground"},
    "Flash Fire":  {"name":"Flash Fire","desc":"Immune to Fire, boosts own Fire.","trigger":"immunity_boost","type":"Fire","mult":1.5},
    "Water Absorb":{"name":"Water Absorb","desc":"Immune to Water, restores HP.","trigger":"immunity_heal","type":"Water","heal_ratio":0.25},
    "Volt Absorb": {"name":"Volt Absorb","desc":"Immune to Electric, restores HP.","trigger":"immunity_heal","type":"Electric","heal_ratio":0.25},
    "Thick Fat":   {"name":"Thick Fat","desc":"Halves Fire and Ice damage.","trigger":"damage_reduction","types":["Fire","Ice"],"mult":0.5},
    "Heatproof":   {"name":"Heatproof","desc":"Halves Fire damage.","trigger":"damage_reduction","types":["Fire"],"mult":0.5},
    "Moxie":       {"name":"Moxie","desc":"Boosts DM after fainting a foe.","trigger":"on_ko","stat":"dm","stages":1},
    "Synchronize": {"name":"Synchronize","desc":"Passes burn/poison/paralyze to the attacker.","trigger":"on_statused","chance":1.0},
    "Natural Cure":{"name":"Natural Cure","desc":"Cures status on switching out.","trigger":"on_switch_out"},
    "Lightning Rod":{"name":"Lightning Rod","desc":"Draws Electric moves, boosts DM.","trigger":"redirect","type":"Electric","stat":"dm","stages":1},
    "Serene Grace":{"name":"Serene Grace","desc":"Doubles secondary effect chances.","trigger":"effect_chance","mult":2.0},
    "Magic Guard": {"name":"Magic Guard","desc":"Takes no passive damage from weather/status/recoil.","trigger":"passive_immunity"},
    "Clear Body":  {"name":"Clear Body","desc":"Prevents stat reduction from foes.","trigger":"protect_stages"},
    "Marvel Scale":{"name":"Marvel Scale","desc":"Boosts defense when statused.","trigger":"status_boost","stat":"def","mult":1.5},
    "Pressure":    {"name":"Pressure","desc":"Enemy moves cost 2 PP.","trigger":"pp_pressure"},
    "Poison Heal": {"name":"Poison Heal","desc":"Heals when poisoned instead of taking damage.","trigger":"status_heal","status":"Poison","heal_ratio":0.125},
    "Shed Skin":   {"name":"Shed Skin","desc":"30% chance to cure status each turn.","trigger":"on_turn_cure","chance":0.3},
    "Rough Skin":  {"name":"Rough Skin","desc":"Damages attacker on contact.","trigger":"on_contact_damage","ratio":0.125},
    "Iron Barbs":  {"name":"Iron Barbs","desc":"Damages attacker on contact.","trigger":"on_contact_damage","ratio":0.125},
    "Justified":   {"name":"Justified","desc":"Boosts DM when hit by Dark moves.","trigger":"hit_by_type","type":"Dark","stat":"dm","stages":1},
    "Weak Armor":  {"name":"Weak Armor","desc":"Raises Speed, lowers defense when hit.","trigger":"on_hit_physical","speed_stages":2,"def_stages":-1},
    "Mold Breaker":{"name":"Mold Breaker","desc":"Ignores target's ability.","trigger":"ignore_ability"},
    "Unnerve":     {"name":"Unnerve","desc":"Prevents foe from using berries.","trigger":"prevent_berry"},
    "Sand Force":  {"name":"Sand Force","desc":"Boosts Rock/Ground/Steel in sandstorm.","trigger":"weather_boost","weather":"Sandstorm","types":["Rock","Ground","Steel"],"mult":1.3},
    "Gale Wings":  {"name":"Gale Wings","desc":"Gives Flying moves priority at full HP.","trigger":"priority","type":"Flying","condition":"full_hp"},
    "Toxic Boost": {"name":"Toxic Boost","desc":"Boosts DM when poisoned.","trigger":"status_boost","status":"Poison","stat":"dm","mult":1.5},
    "Solar Power": {"name":"Solar Power","desc":"Boosts DM in sun but loses HP each turn.","trigger":"weather_trade","weather":"Sun","stat":"dm","mult":1.5,"damage_ratio":0.125},
    "Dry Skin":    {"name":"Dry Skin","desc":"Immune to Water, heals in rain, hurt by Fire.","trigger":"complex_weather","heal_weather":"Rain","heal_ratio":0.125,"weak_type":"Fire"},
    "Sheer Force": {"name":"Sheer Force","desc":"Boosts move power but removes secondary effects.","trigger":"sheer_force","mult":1.3},
    "Huge Power":  {"name":"Huge Power","desc":"Doubles the Pokemon's DM stat.","trigger":"stat_double","stat":"dm","mult":2.0},
    "Pure Power":  {"name":"Pure Power","desc":"Doubles the Pokemon's DM stat.","trigger":"stat_double","stat":"dm","mult":2.0},
    "Technician":  {"name":"Technician","desc":"Boosts moves with 60 or less base power.","trigger":"weak_move_boost","power_threshold":60,"mult":1.5},
    "Iron Fist":   {"name":"Iron Fist","desc":"Boosts punching moves.","trigger":"type_category_boost","category":"punch","mult":1.2},
    "Steadfast":   {"name":"Steadfast","desc":"Raises Speed each time the Pokemon flinches.","trigger":"on_flinch","stat":"speed","stages":1},
    "Sniper":      {"name":"Sniper","desc":"Boosts critical hit damage.","trigger":"crit_boost","mult":2.25},
    "Tinted Lens": {"name":"Tinted Lens","desc":"Doubles damage for not-very-effective moves.","trigger":"tinted_lens","mult":2.0},
    "Compound Eyes":{"name":"Compound Eyes","desc":"Boosts move accuracy by 30%.","trigger":"accuracy_boost","mult":1.3},
    "Insomnia":    {"name":"Insomnia","desc":"Prevents sleep.","trigger":"status_immunity","status":"Sleep"},
    "Vital Spirit": {"name":"Vital Spirit","desc":"Prevents sleep.","trigger":"status_immunity","status":"Sleep"},
    "Immunity":    {"name":"Immunity","desc":"Prevents poisoning.","trigger":"status_immunity","status":"Poison"},
    "Oblivious":   {"name":"Oblivious","desc":"Prevents infatuation.","trigger":"status_immunity","status":"Infatuate"},
    "Own Tempo":   {"name":"Own Tempo","desc":"Prevents confusion.","trigger":"status_immunity","status":"Confuse"},
    "Water Veil":  {"name":"Water Veil","desc":"Prevents burns.","trigger":"status_immunity","status":"Burn"},
    "Magma Armor": {"name":"Magma Armor","desc":"Prevents freezing.","trigger":"status_immunity","status":"Freeze"},
    "Battle Armor":{"name":"Battle Armor","desc":"Blocks critical hits.","trigger":"block_crit"},
    "Shell Armor": {"name":"Shell Armor","desc":"Blocks critical hits.","trigger":"block_crit"},
    "Inner Focus": {"name":"Inner Focus","desc":"Prevents flinching.","trigger":"status_immunity","status":"Flinch"},
    "Limber":      {"name":"Limber","desc":"Prevents paralysis.","trigger":"status_immunity","status":"Paralyze"},
    "Hyper Cutter":{"name":"Hyper Cutter","desc":"Prevents DM reduction.","trigger":"protect_stat","stat":"dm"},
    "Big Pecks":   {"name":"Big Pecks","desc":"Prevents defense reduction.","trigger":"protect_stat","stat":"def"},
    "Suction Cups":{"name":"Suction Cups","desc":"Prevents forced switching.","trigger":"block_switch"},
    "Sticky Hold": {"name":"Sticky Hold","desc":"Prevents item theft.","trigger":"block_item_theft"},
    "Soundproof":  {"name":"Soundproof","desc":"Blocks sound-based moves.","trigger":"block_type","type":"Sound"},
    "Filter":      {"name":"Filter","desc":"Reduces super-effective damage.","trigger":"damage_reduction","types":["__super_effective__"],"mult":0.75},
    "Solid Rock":  {"name":"Solid Rock","desc":"Reduces super-effective damage.","trigger":"damage_reduction","types":["__super_effective__"],"mult":0.75},
    "Wonder Guard":{"name":"Wonder Guard","desc":"Only super-effective moves hit.","trigger":"wonder_guard"},
    "Motor Drive": {"name":"Motor Drive","desc":"Immune to Electric, raises Speed.","trigger":"immunity_boost_speed","type":"Electric","speed_stages":1},
    "Shadow Tag":"Shadow Tag traps the foe!","Magic Bounce":"Magic Bounce reflects the move!",
    "Prankster":"Prankster adds priority!","Regenerator":"Regenerator restores HP!",
    "Sap Sipper":  {"name":"Sap Sipper","desc":"Immune to Grass, boosts DM.","trigger":"immunity_boost","type":"Grass","stat":"dm","stages":1},
    "Storm Drain": {"name":"Storm Drain","desc":"Draws Water moves, boosts DM.","trigger":"redirect_boost","type":"Water","stat":"dm","stages":1},
    "Shadow Tag":  {"name":"Shadow Tag","desc":"Prevents the foe from switching out.","trigger":"block_switch"},
    "Magic Bounce":{"name":"Magic Bounce","desc":"Reflects status moves back to the user.","trigger":"reflect_status"},
    "Prankster":   {"name":"Prankster","desc":"Gives priority to status moves.","trigger":"status_priority"},
    "Regenerator": {"name":"Regenerator","desc":"Restores 1/3 max HP when switching out.","trigger":"on_switch_out","heal_ratio":1/3},
    "Cursed Body": {"name":"Cursed Body","desc":"30% chance to disable a move on contact.","trigger":"on_contact","effect":"Disable","chance":0.3},
    "Mega Launcher":{"name":"Mega Launcher","desc":"Boosts aura/pulse moves by 50%.","trigger":"aura_boost","mult":1.5},
    "Strong Jaw":  {"name":"Strong Jaw","desc":"Boosts biting moves by 50%.","trigger":"bite_boost","mult":1.5},
    "Tough Claws": {"name":"Tough Claws","desc":"Boosts contact moves by 30%.","trigger":"contact_boost","mult":1.3},
    "Merciless":   {"name":"Merciless","desc":"Always crits on poisoned targets.","trigger":"crit_on_poisoned"},
    "Steelworker": {"name":"Steelworker","desc":"Boosts Steel moves by 50%.","trigger":"type_boost","type":"Steel","mult":1.5},
    "Water Bubble":{"name":"Water Bubble","desc":"Halves Fire damage, boosts Water moves.","trigger":"water_bubble","boost_mult":2.0,"reduce_mult":0.5},
}

ABILITY_MAP = {
    "Bulbasaur":"Overgrow","Ivysaur":"Overgrow","Venusaur":"Overgrow","Charmander":"Blaze","Charmeleon":"Blaze","Charizard":"Blaze",
    "Squirtle":"Torrent","Wartortle":"Torrent","Blastoise":"Torrent","Caterpie":"Swarm","Metapod":"Shed Skin","Butterfree":"Compound Eyes",
    "Weedle":"Swarm","Kakuna":"Shed Skin","Beedrill":"Swarm","Pidgey":"Keen Eye","Pidgeotto":"Keen Eye","Pidgeot":"Keen Eye",
    "Rattata":"Guts","Raticate":"Guts","Spearow":"Keen Eye","Fearow":"Keen Eye","Ekans":"Intimidate","Arbok":"Intimidate",
    "Pikachu":"Static","Raichu":"Static","Sandshrew":"Sand Veil","Sandslash":"Sand Veil","Nidoran F":"Poison Point","Nidorina":"Poison Point",
    "Nidoqueen":"Poison Point","Nidoran M":"Poison Point","Nidorino":"Poison Point","Nidoking":"Poison Point","Clefairy":"Magic Guard",
    "Clefable":"Magic Guard","Vulpix":"Flash Fire","Ninetales":"Flash Fire","Jigglypuff":"Cute Charm","Wigglytuff":"Cute Charm",
    "Zubat":"Inner Focus","Golbat":"Inner Focus","Oddish":"Chlorophyll","Gloom":"Chlorophyll","Vileplume":"Chlorophyll",
    "Paras":"Dry Skin","Parasect":"Dry Skin","Venonat":"Tinted Lens","Venomoth":"Tinted Lens","Diglett":"Sand Veil","Dugtrio":"Sand Veil",
    "Meowth":"Technician","Persian":"Technician","Psyduck":"Cloud Nine","Golduck":"Cloud Nine","Mankey":"Anger Point","Primeape":"Anger Point",
    "Growlithe":"Flash Fire","Arcanine":"Flash Fire","Poliwag":"Water Absorb","Poliwhirl":"Water Absorb","Poliwrath":"Water Absorb",
    "Abra":"Synchronize","Kadabra":"Synchronize","Alakazam":"Magic Guard","Machop":"Guts","Machoke":"Guts","Machamp":"Guts",
    "Bellsprout":"Chlorophyll","Weepinbell":"Chlorophyll","Victreebel":"Chlorophyll","Tentacool":"Clear Body","Tentacruel":"Clear Body",
    "Geodude":"Sturdy","Graveler":"Sturdy","Golem":"Sturdy","Ponyta":"Flash Fire","Rapidash":"Flash Fire","Slowpoke":"Oblivious",
    "Slowbro":"Oblivious","Magnemite":"Sturdy","Magneton":"Sturdy","Farfetch'd":"Keen Eye","Doduo":"Early Bird","Dodrio":"Early Bird",
    "Seel":"Thick Fat","Dewgong":"Thick Fat","Grimer":"Stench","Muk":"Stench","Shellder":"Shell Armor","Cloyster":"Shell Armor",
    "Gastly":"Levitate","Haunter":"Levitate","Gengar":"Levitate","Onix":"Sturdy","Drowzee":"Insomnia","Hypno":"Insomnia",
    "Krabby":"Hyper Cutter","Kingler":"Hyper Cutter","Voltorb":"Static","Electrode":"Static","Exeggcute":"Chlorophyll",
    "Exeggutor":"Chlorophyll","Cubone":"Rock Head","Marowak":"Rock Head","Hitmonlee":"Limber","Hitmonchan":"Iron Fist",
    "Lickitung":"Oblivious","Koffing":"Levitate","Weezing":"Levitate","Rhyhorn":"Lightning Rod","Rhydon":"Lightning Rod",
    "Chansey":"Natural Cure","Tangela":"Chlorophyll","Kangaskhan":"Scrappy","Horsea":"Swift Swim","Seadra":"Swift Swim",
    "Goldeen":"Swift Swim","Seaking":"Swift Swim","Staryu":"Natural Cure","Starmie":"Natural Cure","Mr. Mime":"Filter",
    "Scyther":"Swarm","Jynx":"Oblivious","Electabuzz":"Static","Magmar":"Flame Body","Pinsir":"Hyper Cutter",
    "Tauros":"Intimidate","Magikarp":"Swift Swim","Gyarados":"Intimidate","Lapras":"Water Absorb","Ditto":"Limber",
    "Eevee":"Adaptability","Vaporeon":"Water Absorb","Jolteon":"Volt Absorb","Flareon":"Flash Fire","Porygon":"Trace",
    "Porygon2":"Trace","Omanyte":"Swift Swim","Omastar":"Swift Swim","Kabuto":"Swift Swim","Kabutops":"Swift Swim",
    "Aerodactyl":"Pressure","Snorlax":"Thick Fat","Articuno":"Snow Cloak","Zapdos":"Static","Moltres":"Flame Body",
    "Dratini":"Shed Skin","Dragonair":"Shed Skin","Dragonite":"Marvel Scale","Mewtwo":"Pressure","Mew":"Synchronize",
    "Chikorita":"Overgrow","Bayleef":"Overgrow","Meganium":"Overgrow","Cyndaquil":"Blaze","Quilava":"Blaze","Typhlosion":"Blaze",
    "Totodile":"Torrent","Croconaw":"Torrent","Feraligatr":"Torrent","Sentret":"Keen Eye","Furret":"Keen Eye",
    "Hoothoot":"Insomnia","Noctowl":"Insomnia","Ledyba":"Swarm","Ledian":"Swarm","Spinarak":"Swarm","Ariados":"Swarm",
    "Crobat":"Inner Focus","Chinchou":"Volt Absorb","Lanturn":"Volt Absorb","Pichu":"Static","Cleffa":"Magic Guard",
    "Igglybuff":"Cute Charm","Togepi":"Serene Grace","Togetic":"Serene Grace","Togekiss":"Serene Grace","Natu":"Synchronize",
    "Xatu":"Synchronize","Mareep":"Static","Flaaffy":"Static","Ampharos":"Static","Bellossom":"Chlorophyll",
    "Marill":"Thick Fat","Azumarill":"Thick Fat","Sudowoodo":"Sturdy","Politoed":"Water Absorb","Hoppip":"Chlorophyll",
    "Skiploom":"Chlorophyll","Jumpluff":"Chlorophyll","Aipom":"Technician","Sunkern":"Chlorophyll","Sunflora":"Chlorophyll",
    "Yanma":"Compound Eyes","Yanmega":"Compound Eyes","Wooper":"Water Absorb","Quagsire":"Water Absorb","Espeon":"Magic Bounce",
    "Umbreon":"Synchronize","Murkrow":"Insomnia","Honchkrow":"Insomnia","Slowking":"Oblivious","Misdreavus":"Levitate",
    "Mismagius":"Levitate","Unown":"Levitate","Wobbuffet":"Shadow Tag","Girafarig":"Sap Sipper","Pineco":"Sturdy",
    "Forretress":"Sturdy","Dunsparce":"Serene Grace","Gligar":"Sand Veil","Gliscor":"Sand Veil","Steelix":"Sturdy",
    "Snubbull":"Intimidate","Granbull":"Intimidate","Qwilfish":"Poison Point","Scizor":"Swarm","Shuckle":"Sturdy",
    "Heracross":"Guts","Sneasel":"Inner Focus","Weavile":"Pressure","Teddiursa":"Quick Feet","Ursaring":"Guts",
    "Slugma":"Flame Body","Magcargo":"Flame Body","Swinub":"Thick Fat","Piloswine":"Thick Fat","Mamoswine":"Thick Fat",
    "Corsola":"Natural Cure","Remoraid":"Swift Swim","Octillery":"Suction Cups","Delibird":"Vital Spirit",
    "Mantine":"Water Absorb","Skarmory":"Sturdy","Houndour":"Flash Fire","Houndoom":"Flash Fire","Kingdra":"Swift Swim",
    "Phanpy":"Pickup","Donphan":"Sturdy","Porygon-Z":"Adaptability","Stantler":"Intimidate","Smeargle":"Technician",
    "Tyrogue":"Guts","Hitmontop":"Technician","Smoochum":"Oblivious","Elekid":"Static","Magby":"Flame Body",
    "Miltank":"Thick Fat","Blissey":"Natural Cure","Raikou":"Pressure","Entei":"Pressure","Suicune":"Pressure",
    "Larvitar":"Guts","Pupitar":"Shed Skin","Tyranitar":"Sand Stream","Lugia":"Pressure","Ho-Oh":"Pressure","Celebi":"Natural Cure",
    "Treecko":"Overgrow","Grovyle":"Overgrow","Sceptile":"Overgrow","Torchic":"Blaze","Combusken":"Blaze","Blaziken":"Blaze",
    "Mudkip":"Torrent","Marshtomp":"Torrent","Swampert":"Torrent","Poochyena":"Intimidate","Mightyena":"Intimidate",
    "Zigzagoon":"Guts","Linoone":"Guts","Wurmple":"Swarm","Silcoon":"Shed Skin","Beautifly":"Swarm","Cascoon":"Shed Skin",
    "Dustox":"Swarm","Lotad":"Swift Swim","Lombre":"Swift Swim","Ludicolo":"Swift Swim","Seedot":"Chlorophyll",
    "Nuzleaf":"Chlorophyll","Shiftry":"Chlorophyll","Taillow":"Guts","Swellow":"Guts","Wingull":"Keen Eye",
    "Pelipper":"Keen Eye","Ralts":"Synchronize","Kirlia":"Synchronize","Gardevoir":"Trace","Gallade":"Justified",
    "Surskit":"Swift Swim","Masquerain":"Intimidate","Shroomish":"Quick Feet","Breloom":"Quick Feet","Slakoth":"Truant",
    "Vigoroth":"Vital Spirit","Slaking":"Truant","Nincada":"Compound Eyes","Ninjask":"Speed Boost","Shedinja":"Wonder Guard",
    "Whismur":"Soundproof","Loudred":"Soundproof","Exploud":"Soundproof","Makuhita":"Thick Fat","Hariyama":"Thick Fat",
    "Azurill":"Thick Fat","Nosepass":"Sturdy","Probopass":"Sturdy","Skitty":"Cute Charm","Delcatty":"Cute Charm",
    "Sableye":"Stall","Mawile":"Intimidate","Aron":"Sturdy","Lairon":"Sturdy","Aggron":"Sturdy","Meditite":"Pure Power",
    "Medicham":"Pure Power","Electrike":"Static","Manectric":"Static","Plusle":"Plus","Minun":"Minun",
    "Volbeat":"Illuminate","Illumise":"Oblivious","Roselia":"Poison Point","Roserade":"Poison Point","Gulpin":"Sticky Hold",
    "Swalot":"Sticky Hold","Carvanha":"Rough Skin","Sharpedo":"Rough Skin","Wailmer":"Water Veil","Wailord":"Water Veil",
    "Numel":"Simple","Camerupt":"Magma Armor","Torkoal":"Drought","Spoink":"Thick Fat","Grumpig":"Thick Fat",
    "Spinda":"Tangled Feet","Trapinch":"Hyper Cutter","Vibrava":"Levitate","Flygon":"Levitate","Cacnea":"Sand Veil",
    "Cacturne":"Sand Veil","Swablu":"Natural Cure","Altaria":"Natural Cure","Zangoose":"Immunity","Seviper":"Shed Skin",
    "Lunatone":"Levitate","Solrock":"Levitate","Barboach":"Oblivious","Whiscash":"Oblivious","Corphish":"Hyper Cutter",
    "Crawdaunt":"Hyper Cutter","Baltoy":"Levitate","Claydol":"Levitate","Lileep":"Suction Cups","Cradily":"Suction Cups",
    "Anorith":"Swift Swim","Armaldo":"Swift Swim","Feebas":"Swift Swim","Milotic":"Marvel Scale","Castform":"Forecast",
    "Kecleon":"Color Change","Shuppet":"Insomnia","Banette":"Insomnia","Duskull":"Levitate","Dusclops":"Levitate",
    "Dusknoir":"Levitate","Tropius":"Chlorophyll","Chimecho":"Levitate","Absol":"Pressure","Wynaut":"Shadow Tag",
    "Snorunt":"Inner Focus","Glalie":"Inner Focus","Froslass":"Snow Cloak","Spheal":"Thick Fat","Sealeo":"Thick Fat",
    "Walrein":"Thick Fat","Clamperl":"Shell Armor","Huntail":"Swift Swim","Gorebyss":"Swift Swim","Relicanth":"Swift Swim",
    "Luvdisc":"Swift Swim","Bagon":"Rock Head","Shelgon":"Rock Head","Salamence":"Intimidate","Beldum":"Clear Body",
    "Metang":"Clear Body","Metagross":"Clear Body","Regirock":"Sturdy","Regice":"Clear Body","Registeel":"Clear Body",
    "Latias":"Levitate","Latios":"Levitate","Kyogre":"Drizzle","Groudon":"Drought","Rayquaza":"Air Lock",
    "Jirachi":"Serene Grace","Deoxys":"Pressure",
    "Turtwig":"Overgrow","Grotle":"Overgrow","Torterra":"Overgrow","Chimchar":"Blaze","Monferno":"Blaze","Infernape":"Blaze",
    "Piplup":"Torrent","Prinplup":"Torrent","Empoleon":"Torrent","Starly":"Keen Eye","Staravia":"Intimidate","Staraptor":"Intimidate",
    "Bidoof":"Simple","Bibarel":"Simple","Kricketot":"Shed Skin","Kricketune":"Swarm","Shinx":"Intimidate","Luxio":"Intimidate",
    "Luxray":"Intimidate","Budew":"Poison Point","Rhyperior":"Solid Rock","Tangrowth":"Chlorophyll","Electivire":"Motor Drive",
    "Magmortar":"Flame Body","Togekiss":"Serene Grace","Yanmega":"Speed Boost","Leafeon":"Chlorophyll","Glaceon":"Snow Cloak",
    "Gliscor":"Sand Veil","Mamoswine":"Thick Fat","Porygon-Z":"Adaptability","Gallade":"Justified","Probopass":"Sturdy",
    "Dusknoir":"Levitate","Froslass":"Snow Cloak","Rotom":"Levitate","Rotom-Wash":"Levitate","Rotom-Heat":"Levitate",
    "Rotom-Frost":"Levitate","Rotom-Fan":"Levitate","Rotom-Mow":"Levitate","Uxie":"Levitate","Mesprit":"Levitate",
    "Azelf":"Levitate","Dialga":"Pressure","Palkia":"Pressure","Heatran":"Flash Fire","Regigigas":"Slow Start",
    "Giratina":"Pressure","Cresselia":"Levitate","Phione":"Swift Swim","Manaphy":"Swift Swim","Darkrai":"Bad Dreams",
    "Shaymin":"Natural Cure","Arceus":"Multitype",
    "Victini":"Victory Star","Snivy":"Overgrow","Servine":"Overgrow","Serperior":"Overgrow","Tepig":"Blaze",
    "Pignite":"Blaze","Emboar":"Blaze","Oshawott":"Torrent","Dewott":"Torrent","Samurott":"Torrent",
    "Patrat":"Run Away","Watchog":"Illuminate","Lillipup":"Intimidate","Herdier":"Intimidate","Stoutland":"Intimidate",
    "Purrloin":"Unburden","Liepard":"Unburden","Pansage":"Overgrow","Simisage":"Overgrow","Pansear":"Blaze",
    "Simisear":"Blaze","Panpour":"Torrent","Simipour":"Torrent","Munna":"Synchronize","Musharna":"Synchronize",
    "Pidove":"Super Luck","Tranquill":"Super Luck","Unfezant":"Super Luck","Blitzle":"Lightning Rod","Zebstrika":"Lightning Rod",
    "Roggenrola":"Sturdy","Boldore":"Sturdy","Gigalith":"Sturdy","Woobat":"Unaware","Swoobat":"Unaware",
    "Drilbur":"Sand Rush","Excadrill":"Sand Rush","Audino":"Healer","Timburr":"Guts","Gurdurr":"Guts","Conkeldurr":"Guts",
    "Tympole":"Swift Swim","Palpitoad":"Swift Swim","Seismitoad":"Poison Touch","Throh":"Guts","Sawk":"Sturdy",
    "Sewaddle":"Swarm","Swadloon":"Swarm","Leavanny":"Swarm","Venipede":"Poison Point","Whirlipede":"Poison Point",
    "Scolipede":"Poison Point","Cottonee":"Prankster","Whimsicott":"Prankster","Petilil":"Chlorophyll","Lilligant":"Chlorophyll",
    "Basculin":"Adaptability","Sandile":"Intimidate","Krokorok":"Intimidate","Krookodile":"Intimidate","Darumaka":"Hustle",
    "Darmanitan":"Sheer Force","Maractus":"Water Absorb","Dwebble":"Sturdy","Crustle":"Sturdy","Scraggy":"Moxie",
    "Scrafty":"Moxie","Sigilyph":"Magic Guard","Yamask":"Mummy","Cofagrigus":"Mummy","Tirtouga":"Sturdy",
    "Carracosta":"Sturdy","Archen":"Defeatist","Archeops":"Defeatist","Trubbish":"Stench","Garbodor":"Stench",
    "Zorua":"Illusion","Zoroark":"Illusion","Minccino":"Cute Charm","Cinccino":"Cute Charm","Gothita":"Frisk",
    "Gothorita":"Frisk","Gothitelle":"Frisk","Solosis":"Magic Guard","Duosion":"Magic Guard","Reuniclus":"Magic Guard",
    "Ducklett":"Keen Eye","Swanna":"Keen Eye","Vanillite":"Ice Body","Vanillish":"Ice Body","Vanilluxe":"Ice Body",
    "Deerling":"Chlorophyll","Sawsbuck":"Chlorophyll","Emolga":"Static","Karrablast":"Swarm","Escavalier":"Swarm",
    "Foongus":"Effect Spore","Amoonguss":"Effect Spore","Frillish":"Water Absorb","Jellicent":"Water Absorb",
    "Alomomola":"Healer","Joltik":"Compound Eyes","Galvantula":"Compound Eyes","Ferroseed":"Iron Barbs",
    "Ferrothorn":"Iron Barbs","Klink":"Plus","Klang":"Plus","Klinklang":"Plus","Tynamo":"Levitate","Eelektrik":"Levitate",
    "Eelektross":"Levitate","Elgyem":"Synchronize","Beheeyem":"Synchronize","Litwick":"Flash Fire","Lampent":"Flash Fire",
    "Chandelure":"Flash Fire","Axew":"Mold Breaker","Fraxure":"Mold Breaker","Haxorus":"Mold Breaker","Cubchoo":"Snow Cloak",
    "Beartic":"Snow Cloak","Cryogonal":"Levitate","Shelmet":"Shell Armor","Accelgor":"Swarm","Stunfisk":"Static",
    "Mienfoo":"Regenerator","Mienshao":"Regenerator","Druddigon":"Rough Skin","Golett":"Iron Fist","Golurk":"Iron Fist",
    "Pawniard":"Inner Focus","Bisharp":"Inner Focus","Kingambit":"Supreme Overlord","Bouffalant":"Reckless",
    "Rufflet":"Hustle","Braviary":"Defiant","Vullaby":"Overcoat","Mandibuzz":"Overcoat","Heatmor":"Flash Fire",
    "Durant":"Hustle","Deino":"Hustle","Zweilous":"Hustle","Hydreigon":"Levitate","Larvesta":"Flame Body",
    "Volcarona":"Flame Body","Cobalion":"Justified","Terrakion":"Justified","Virizion":"Justified","Tornadus":"Prankster",
    "Thundurus":"Prankster","Reshiram":"Turboblaze","Zekrom":"Teravolt","Landorus":"Sand Force","Kyurem":"Pressure",
    "Meloetta":"Serene Grace","Genesect":"Download",
    "Chespin":"Overgrow","Quilladin":"Overgrow","Chesnaught":"Overgrow","Fennekin":"Blaze","Braixen":"Blaze",
    "Delphox":"Blaze","Froakie":"Torrent","Frogadier":"Torrent","Greninja":"Torrent","Bunnelby":"Pickup",
    "Diggersby":"Huge Power","Fletchling":"Gale Wings","Fletchinder":"Flame Body","Talonflame":"Gale Wings",
    "Scatterbug":"Compound Eyes","Spewpa":"Shed Skin","Vivillon":"Compound Eyes","Litleo":"Rivalry","Pyroar":"Rivalry",
    "Flabebe":"Flower Veil","Floette":"Flower Veil","Florges":"Flower Veil","Skiddo":"Sap Sipper","Gogoat":"Sap Sipper",
    "Pancham":"Iron Fist","Pangoro":"Iron Fist","Furfrou":"Fur Coat","Espurr":"Infiltrator","Meowstic":"Infiltrator",
    "Honedge":"No Guard","Doublade":"No Guard","Aegislash":"Stance Change","Spritzee":"Healer","Aromatisse":"Healer",
    "Swirlix":"Sweet Veil","Slurpuff":"Sweet Veil","Inkay":"Contrary","Malamar":"Contrary","Binacle":"Sniper",
    "Barbaracle":"Sniper","Skrelp":"Poison Point","Dragalge":"Poison Point","Clauncher":"Mega Launcher",
    "Clawitzer":"Mega Launcher","Helioptile":"Dry Skin","Heliolisk":"Dry Skin","Tyrunt":"Strong Jaw",
    "Tyrantrum":"Strong Jaw","Amaura":"Refrigerate","Aurorus":"Refrigerate","Sylveon":"Pixilate",
    "Hawlucha":"Limber","Dedenne":"Cheek Pouch","Carbink":"Clear Body","Goomy":"Sap Sipper","Sliggoo":"Sap Sipper",
    "Goodra":"Sap Sipper","Klefki":"Prankster","Phantump":"Natural Cure","Trevenant":"Natural Cure",
    "Pumpkaboo":"Pickup","Gourgeist":"Pickup","Bergmite":"Ice Body","Avalugg":"Ice Body","Noibat":"Frisk",
    "Noivern":"Frisk","Xerneas":"Fairy Aura","Yveltal":"Dark Aura","Zygarde":"Aura Break",
    "Diancie":"Clear Body","Hoopa":"Magician","Volcanion":"Water Absorb",
    "Rowlet":"Overgrow","Dartrix":"Overgrow","Decidueye":"Overgrow","Litten":"Blaze","Torracat":"Blaze",
    "Incineroar":"Blaze","Popplio":"Torrent","Brionne":"Torrent","Primarina":"Torrent","Pikipek":"Keen Eye",
    "Trumbeak":"Keen Eye","Toucannon":"Keen Eye","Yungoos":"Stakeout","Gumshoos":"Stakeout","Grubbin":"Swarm",
    "Charjabug":"Battery","Vikavolt":"Levitate","Bounsweet":"Leaf Guard","Steenee":"Leaf Guard","Tsareena":"Queenly Majesty",
    "Cutiefly":"Shield Dust","Ribombee":"Shield Dust","Rockruff":"Keen Eye","Lycanroc":"Sand Rush",
    "Wishiwashi":"Schooling","Mareanie":"Merciless","Toxapex":"Merciless","Mudbray":"Stamina","Mudsdale":"Stamina",
    "Dewpider":"Water Bubble","Araquanid":"Water Bubble","Fomantis":"Leaf Guard","Lurantis":"Leaf Guard",
    "Morelull":"Effect Spore","Shiinotic":"Effect Spore","Salandit":"Corrosion","Salazzle":"Corrosion",
    "Stufful":"Fluffy","Bewear":"Fluffy","Bounsweet":"Leaf Guard","Comfey":"Triage","Oranguru":"Telepathy",
    "Passimian":"Receiver","Wimpod":"Wimp Out","Golisopod":"Emergency Exit","Sandygast":"Water Compaction",
    "Palossand":"Water Compaction","Pyukumuku":"Innards Out","Type: Null":"Battle Armor","Silvally":"RKS System",
    "Minior":"Shields Down","Komala":"Comatose","Turtonator":"Shell Armor","Togedemaru":"Iron Barbs",
    "Mimikyu":"Disguise","Bruxish":"Dazzling","Drampa":"Berserk","Dhelmise":"Steelworker",
    "Jangmo-o":"Bulletproof","Hakamo-o":"Bulletproof","Kommo-o":"Bulletproof","Tapu Koko":"Electric Surge",
    "Tapu Lele":"Psychic Surge","Tapu Bulu":"Grassy Surge","Tapu Fini":"Misty Surge","Cosmog":"Unaware",
    "Cosmoem":"Sturdy","Solgaleo":"Full Metal Body","Lunala":"Shadow Shield","Nihilego":"Beast Boost",
    "Buzzwole":"Beast Boost","Pheromosa":"Beast Boost","Xurkitree":"Beast Boost","Celesteela":"Beast Boost",
    "Kartana":"Beast Boost","Guzzlord":"Beast Boost","Necrozma":"Prism Armor","Stakataka":"Beast Boost",
    "Blacephalon":"Beast Boost","Poipole":"Beast Boost","Naganadel":"Beast Boost","Magearna":"Soul-Heart",
    "Marshadow":"Technician","Zeraora":"Volt Absorb",
    "Grookey":"Overgrow","Thwackey":"Overgrow","Rillaboom":"Overgrow","Scorbunny":"Blaze","Raboot":"Blaze",
    "Cinderace":"Blaze","Sobble":"Torrent","Drizzile":"Torrent","Inteleon":"Torrent","Skwovet":"Cheek Pouch",
    "Greedent":"Cheek Pouch","Rookidee":"Unnerve","Corvisquire":"Unnerve","Corviknight":"Mirror Armor",
    "Blipbug":"Swarm","Dottler":"Swarm","Orbeetle":"Swarm","Nickit":"Run Away","Thievul":"Unburden",
    "Yamper":"Ball Fetch","Boltund":"Strong Jaw","Rolycoly":"Steam Engine","Carkol":"Steam Engine",
    "Coalossal":"Steam Engine","Applin":"Ripen","Flapple":"Hustle","Appletun":"Thick Fat",
    "Silicobra":"Sand Spit","Sandaconda":"Sand Spit","Cramorant":"Gulp Missile","Arrokuda":"Swift Swim",
    "Barraskewda":"Swift Swim","Toxel":"Rattled","Toxtricity":"Punk Rock","Sizzlipede":"Flash Fire",
    "Centiskorch":"Flash Fire","Clobbopus":"Limber","Grapploct":"Limber","Sinistea":"Weak Armor",
    "Polteageist":"Weak Armor","Hatenna":"Healer","Hattrem":"Healer","Hatterene":"Magic Bounce",
    "Impidimp":"Prankster","Morgrem":"Prankster","Grimmsnarl":"Prankster","Obstagoon":"Guts",
    "Perrserker":"Tough Claws","Cursola":"Weak Armor","Sirfetch'd":"Steadfast","Mr. Rime":"Screen Cleaner",
    "Runerigus":"Wandering Spirit","Milcery":"Sweet Veil","Alcremie":"Sweet Veil","Falinks":"Battle Armor",
    "Pincurchin":"Electric Surge","Snom":"Shield Dust","Frosmoth":"Ice Scales","Stonjourner":"Power Spot",
    "Eiscue":"Ice Face","Indeedee":"Psychic Surge","Morpeko":"Hunger Switch","Cufant":"Sheer Force",
    "Copperajah":"Sheer Force","Dracozolt":"Volt Absorb","Arctozolt":"Volt Absorb","Dracovish":"Water Absorb",
    "Arctovish":"Water Absorb","Duraludon":"Light Metal","Dragapult":"Clear Body","Zacian":"Intrepid Sword",
    "Zamazenta":"Dauntless Shield","Eternatus":"Pressure","Keldeo":"Justified","Meloetta":"Serene Grace",
    "Genesect":"Download","Zarude":"Leaf Guard","Regieleki":"Transistor","Regidrago":"Dragon's Maw",
    "Glastrier":"Chilling Neigh","Spectrier":"Grim Neigh","Calyrex":"Unnerve","Enamorus":"Cute Charm",
    "Sprigatito":"Overgrow","Floragato":"Overgrow","Meowscarada":"Overgrow","Fuecoco":"Blaze","Crocalor":"Blaze",
    "Skeledirge":"Blaze","Quaxly":"Torrent","Quaxwell":"Torrent","Quaquaval":"Torrent","Lechonk":"Aroma Veil",
    "Oinkologne":"Thick Fat","Tarountula":"Insomnia","Spidops":"Insomnia","Nymble":"Swarm","Lokix":"Swarm",
    "Pawmi":"Static","Pawmo":"Static","Pawmot":"Static","Tandemaus":"Run Away","Maushold":"Technician",
    "Fidough":"Own Tempo","Dachsbun":"Well-Baked Body","Smoliv":"Early Bird","Dolliv":"Early Bird",
    "Arboliva":"Harvest","Squawkabilly":"Intimidate","Nacli":"Sturdy","Naclstack":"Sturdy","Garganacl":"Sturdy",
    "Charcadet":"Flash Fire","Armarouge":"Flash Fire","Ceruledge":"Flash Fire","Tadbulb":"Static","Bellibolt":"Electromorphosis",
    "Wattrel":"Wind Power","Kilowattrel":"Wind Power","Maschiff":"Intimidate","Mabosstiff":"Intimidate",
    "Shroodle":"Unburden","Grafaiai":"Unburden","Bramblin":"Wind Rider","Brambleghast":"Wind Rider",
    "Toedscool":"Mycelium Might","Toedscruel":"Mycelium Might","Klawf":"Anger Shell","Capsakid":"Chlorophyll",
    "Scovillain":"Chlorophyll","Rellor":"Compound Eyes","Rabsca":"Synchronize","Flittle":"Speed Boost",
    "Espathra":"Speed Boost","Tinkatink":"Mold Breaker","Tinkatuff":"Mold Breaker","Tinkaton":"Mold Breaker",
    "Wiglett":"Gooey","Wugtrio":"Gooey","Bombirdier":"Big Pecks","Finizen":"Water Veil","Palafin":"Zero to Hero",
    "Varoom":"Overcoat","Revavroom":"Overcoat","Cyclizar":"Shed Skin","Orthworm":"Earth Eater","Glimmet":"Toxic Debris",
    "Glimmora":"Toxic Debris","Greavard":"Sand Rush","Houndstone":"Sand Rush","Flamigo":"Tangled Feet",
    "Cetoddle":"Thick Fat","Cetitan":"Thick Fat","Veluza":"Sharpness","Dondozo":"Unaware","Tatsugiri":"Commander",
    "Annihilape":"Vital Spirit","Clodsire":"Water Absorb","Farigiraf":"Armor Tail","Dudunsparce":"Serene Grace",
    "Kingambit":"Supreme Overlord","Great Tusk":"Protosynthesis","Scream Tail":"Protosynthesis","Brute Bonnet":"Protosynthesis",
    "Flutter Mane":"Protosynthesis","Slither Wing":"Protosynthesis","Sandy Shocks":"Protosynthesis",
    "Roaring Moon":"Protosynthesis","Iron Treads":"Quark Drive","Iron Moth":"Quark Drive","Iron Hands":"Quark Drive",
    "Iron Jugulis":"Quark Drive","Iron Thorns":"Quark Drive","Iron Bundle":"Quark Drive","Iron Valiant":"Quark Drive",
    "Koraidon":"Orichalcum Pulse","Miraidon":"Hadron Engine",
    # New ability mappings
    "Wobbuffet":"Shadow Tag","Wynaut":"Shadow Tag","Gothita":"Shadow Tag","Gothorita":"Shadow Tag","Gothitelle":"Shadow Tag",
    "Chingling":"Levitate","Chimecho":"Levitate","Bronzor":"Levitate","Bronzong":"Levitate",
    "Absol":"Magic Bounce","Espeon":"Magic Bounce","Xatu":"Magic Bounce","Natu":"Magic Bounce",
    "Riolu":"Prankster","Sableye":"Prankster","Murkrow":"Prankster","Cottonee":"Prankster","Whimsicott":"Prankster",
    "Tornadus":"Prankster","Thundurus":"Prankster","Grapploct":"Prankster",
    "Slowpoke":"Regenerator","Slowbro":"Regenerator","Slowking":"Regenerator","Tangela":"Regenerator",
    "Tangrowth":"Regenerator","Ho-Oh":"Regenerator","Solosis":"Regenerator","Duosion":"Regenerator",
    "Reuniclus":"Regenerator","Amomola":"Regenerator","Mareanie":"Regenerator","Toxapex":"Regenerator",
    "Frillish":"Cursed Body","Jellicent":"Cursed Body","Lampent":"Cursed Body","Chandelure":"Cursed Body",
    "Froslass":"Cursed Body","Dragapult":"Cursed Body",
}

_TYPE_ABILITIES = {
    "Bug":"Swarm","Dark":"Moxie","Dragon":"Intimidate","Electric":"Static","Fairy":"Cute Charm",
    "Fighting":"Guts","Fire":"Blaze","Flying":"Gale Wings","Ghost":"Levitate","Grass":"Overgrow",
    "Ground":"Sand Veil","Ice":"Snow Cloak","Normal":"Adaptability","Poison":"Poison Point",
    "Psychic":"Synchronize","Rock":"Sturdy","Steel":"Heatproof","Water":"Torrent",
}

def get_ability_for_pokemon(name):
    lookup = name.lower().strip()
    title = lookup.capitalize()
    if title in ABILITY_MAP:
        return ABILITY_MAP[title]
    for key in ABILITY_MAP:
        if key.lower() == lookup:
            return ABILITY_MAP[key]
    return None

def pick_ability_by_type(poke_type, abilities_module=None):
    return _TYPE_ABILITIES.get(poke_type, "Adaptability")

def apply_ability_trigger(ability_name, trigger, pokemon, defender=None, weather=None, move_type=None, attacker=None):
    if not ability_name:
        return {}
    ab = ABILITIES.get(ability_name)
    if not ab:
        return {}
    result = {"messages": [], "damage_mult": 1.0, "defense_mult": 1.0, "speed_mult": 1.0,
              "evasion_mult": 1.0, "heal": 0, "stage_changes": {}, "block": False, "ignore_ability": False}
    hp = pokemon.get("hp", 1)
    maxhp = pokemon.get("maxhp", 1)
    hp_ratio = hp / maxhp if maxhp > 0 else 0

    if trigger == "on_entry":
        if ab.get("trigger") == "on_entry":
            eff = ab.get("effect")
            if eff == "lower_dm" and defender:
                ability_activation(ability_name, pokemon.get("name", "Pokemon"))
                stages = ab.get("stages", -1)
                current = defender.get("stages", {}).get("dm", 0)
                new = max(-6, min(6, current + stages))
                if "stages" not in defender:
                    defender["stages"] = {}
                defender["stages"]["dm"] = new
                direction = "fell" if stages < 0 else "rose"
                result["messages"].append(f"{ability_name}: {defender.get('name','Foe')}'s DM {direction}!")
            elif eff == "weather" and weather is not None:
                ability_activation(ability_name, pokemon.get("name", "Pokemon"))
                result["weather_change"] = ab.get("weather")

    elif trigger == "low_hp":
        if ab.get("trigger") == "low_hp" and hp_ratio < 1/3:
            if move_type == ab.get("type"):
                ability_activation(ability_name, pokemon.get("name", "Pokemon"))
                result["damage_mult"] = ab.get("mult", 1.5)
                result["messages"].append(f"{ability_name} boosted the {move_type} move!")

    elif trigger == "damage_calc":
        raw_type = move_type
        if ab.get("trigger") == "stab" and raw_type == pokemon.get("type"):
            result["damage_mult"] = ab.get("mult", 2.0)
        if ab.get("trigger") == "damage_reduction" and raw_type in ab.get("types", []):
            ability_activation(ability_name, pokemon.get("name", "Pokemon"))
            result["defense_mult"] = ab.get("mult", 0.5)
            result["messages"].append(f"{ability_name} reduced damage!")
        if ab.get("trigger") == "weather_boost" and weather == ab.get("weather") and raw_type in ab.get("types", []):
            ability_activation(ability_name, pokemon.get("name", "Pokemon"))
            result["damage_mult"] = ab.get("mult", 1.3)
            result["messages"].append(f"{ability_name} boosted the {raw_type} move in {weather}!")
        if ab.get("trigger") == "weather_trade" and weather == ab.get("weather"):
            ability_activation(ability_name, pokemon.get("name", "Pokemon"))
            result["damage_mult"] = ab.get("mult", 1.5)

    elif trigger == "on_contact":
        if ab.get("trigger") == "on_contact" and attacker:
            if random.random() < ab.get("chance", 0.3):
                ability_activation(ability_name, pokemon.get("name", "Pokemon"))
                status = ab.get("effect")
                if status and not attacker.get("status"):
                    attacker["status"] = status
                    result["messages"].append(f"{ability_name} inflicted {status} on the attacker!")
        if ab.get("trigger") == "on_contact_damage" and attacker:
            ability_activation(ability_name, pokemon.get("name", "Pokemon"))
            dmg = int(attacker.get("maxhp", 100) * ab.get("ratio", 0.125))
            attacker["hp"] = max(0, attacker.get("hp", 0) - dmg)
            result["messages"].append(f"{ability_name} damaged the attacker!")

    elif trigger == "on_ko":
        if ab.get("trigger") == "on_ko" and ab.get("stat"):
            ability_activation(ability_name, pokemon.get("name", "Pokemon"))
            result["stage_changes"][ab["stat"]] = ab.get("stages", 1)
            result["messages"].append(f"{ability_name}: DM rose!")

    elif trigger == "weather_check":
        if ab.get("trigger") == "weather" and weather == ab.get("weather"):
            result["evasion_mult"] = ab.get("evasion", 1.0)
        if ab.get("trigger") == "weather_speed" and weather == ab.get("weather"):
            result["speed_mult"] = ab.get("mult", 2.0)

    elif trigger == "passive_turn":
        if ab.get("trigger") == "on_turn_cure" and pokemon.get("status"):
            if random.random() < ab.get("chance", 0.3):
                ability_activation(ability_name, pokemon.get("name", "Pokemon"))
                pokemon["status"] = None
                result["messages"].append(f"{ability_name}: Status was cured!")

    return result



