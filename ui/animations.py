"""
Advanced animation and visual effects engine.
Matrix rain, particle explosions, loading bars, weather, screen transitions.
"""
import random
import time
import sys
import os
from crazy_style import *
from settings import GAME_SETTINGS

def delay_sleep(seconds):
    """Wrapper for sleep that multiplies by the user's animation speed setting."""
    speed = GAME_SETTINGS.get("animation_speed")
    if speed > 0:
        time.sleep(seconds * speed)


# ═══════════════════════════════════════════
# LOADING ANIMATIONS
# ═══════════════════════════════════════════

def pokeball_loading(message="Loading", duration=2.0):
    """Animated pokeball loading spinner."""
    frames = ["⚪", "🔴", "⚪", "⚫"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        frame = frames[i % len(frames)]
        dots = "." * ((i % 3) + 1)
        spaces = " " * (3 - len(dots))
        sys.stdout.write(f"\r  {frame} {BOLD}{BRIGHT_CYAN}{message}{dots}{spaces}{RESET}")
        sys.stdout.flush()
        delay_sleep(0.25)
        i += 1
    sys.stdout.write(f"\r  ✅ {BOLD}{BRIGHT_GREEN}{message}... Done!{' ' * 10}{RESET}\n")


def progress_bar_animated(label="Progress", total=20, duration=1.5):
    """Animated progress bar with colors."""
    for i in range(total + 1):
        ratio = i / total
        filled = int(total * ratio)
        empty = total - filled

        if ratio > 0.7:
            bar_color = BRIGHT_GREEN
            fill_char = "█"
        elif ratio > 0.4:
            bar_color = BRIGHT_YELLOW
            fill_char = "▓"
        else:
            bar_color = BRIGHT_RED
            fill_char = "▒"

        bar = f"{bar_color}{fill_char * filled}{DIM}{'░' * empty}{RESET}"
        percent = f"{BOLD}{bar_color}{int(ratio * 100):3d}%{RESET}"
        sys.stdout.write(f"\r  {BOLD}{BRIGHT_WHITE}{label}{RESET} [{bar}] {percent}")
        sys.stdout.flush()
        delay_sleep(duration / total)
    print()


def spinner_animation(message="Processing", duration=1.5):
    """Classic spinner animation with colors."""
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    colors = [BRIGHT_RED, BRIGHT_YELLOW, BRIGHT_GREEN, BRIGHT_CYAN, BRIGHT_BLUE, BRIGHT_MAGENTA]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        color = colors[i % len(colors)]
        frame = frames[i % len(frames)]
        sys.stdout.write(f"\r  {color}{frame}{RESET} {BOLD}{BRIGHT_WHITE}{message}{RESET}")
        sys.stdout.flush()
        delay_sleep(0.08)
        i += 1
    sys.stdout.write(f"\r  {BRIGHT_GREEN}✓{RESET} {BOLD}{BRIGHT_WHITE}{message}{RESET}{' ' * 5}\n")


def battle_loading():
    """Battle-themed loading animation."""
    frames = [
        f"  {BRIGHT_RED}⚔️  Preparing for battle...{RESET}",
        f"  {BRIGHT_YELLOW}⚡ Charging energy...{RESET}",
        f"  {BRIGHT_CYAN}🌀 Focusing power...{RESET}",
        f"  {BRIGHT_MAGENTA}🔮 Reading opponent...{RESET}",
        f"  {BRIGHT_GREEN}✨ Ready to fight!{RESET}",
    ]
    for frame in frames:
        sys.stdout.write(f"\r{frame}{' ' * 20}")
        sys.stdout.flush()
        delay_sleep(0.4)
    print()


# ═══════════════════════════════════════════
# MATRIX RAIN EFFECT
# ═══════════════════════════════════════════

def matrix_rain(duration=2.0, width=50, density=0.3):
    """Terminal matrix rain effect."""
    chars = "ポケモン0123456789ABCDEFabcdef@#$%^&*(){}[]|/\\"
    columns = [0] * width
    end_time = time.time() + duration

    while time.time() < end_time:
        line = ""
        for col in range(width):
            if random.random() < density:
                columns[col] = random.randint(3, 8)
            if columns[col] > 0:
                brightness = min(255, columns[col] * 40)
                char = random.choice(chars)
                line += f"{rgb(0, brightness, 0)}{char}{RESET}"
                columns[col] -= 1
            else:
                line += " "
        print(f"  {line}")
        delay_sleep(0.05)


def matrix_text_reveal(text, delay=0.05):
    """Reveal text through matrix-style scrambling."""
    result = list(" " * len(text))
    scramble_chars = "ポケモンアイウエオカキクケコ0123456789@#$%"
    revealed = set()

    for step in range(len(text) * 3):
        for i in range(len(text)):
            if i in revealed:
                continue
            if random.random() < 0.1 + (step / (len(text) * 3)) * 0.3:
                result[i] = text[i]
                revealed.add(i)
            else:
                result[i] = random.choice(scramble_chars)

        display = ""
        for i, char in enumerate(result):
            if i in revealed:
                display += f"{BRIGHT_GREEN}{char}{RESET}"
            else:
                display += f"{rgb(0, random.randint(50, 150), 0)}{char}{RESET}"

        sys.stdout.write(f"\r  {display}")
        sys.stdout.flush()
        time.sleep(delay)

        if len(revealed) == len(text):
            break

    sys.stdout.write(f"\r  {BOLD}{BRIGHT_GREEN}{text}{RESET}{' ' * 10}\n")


# ═══════════════════════════════════════════
# PARTICLE EFFECTS (TEXT-BASED)
# ═══════════════════════════════════════════

def explosion_effect(intensity=3):
    """Text-based explosion effect."""
    explosion_frames = [
        ["        💥        "],
        ["      💥💥💥      "],
        ["    💥💥💥💥💥    ",
         "      💥💥💥      ",
         "    💥💥💥💥💥    "],
        ["  💥💥💥💥💥💥💥  ",
         "    💥🔥🔥🔥💥    ",
         "  💥🔥🔥🔥🔥🔥💥  ",
         "    💥🔥🔥🔥💥    ",
         "  💥💥💥💥💥💥💥  "],
        ["💥💥💥💥💥💥💥💥💥",
         "💥🔥🔥🔥🔥🔥🔥🔥💥",
         "💥🔥💛💛💛💛💛🔥💥",
         "💥🔥🔥🔥🔥🔥🔥🔥💥",
         "💥💥💥💥💥💥💥💥💥"],
        ["  💨  💨    💨  💨  ",
         "    💨    💨    💨  ",
         "  💨    💨    💨    ",
         "    💨  💨  💨      "],
        ["    💨      💨      ",
         "        💨          ",
         "  💨          💨    "],
    ]
    for frame in explosion_frames[:intensity + 4]:
        for line in frame:
            print(f"  {line}")
        delay_sleep(0.15)
        # Move cursor up to overwrite
        sys.stdout.write(f"\033[{len(frame)}A")
        sys.stdout.flush()
    # Print final frame normally
    for line in explosion_frames[-1]:
        print(f"  {line}")


def sparkle_burst(duration=1.0, width=40):
    """Sparkle burst animation."""
    sparkles = "✨💫⭐🌟✴️💥⚡🔥"
    end_time = time.time() + duration

    while time.time() < end_time:
        line = ""
        for _ in range(width):
            if random.random() < 0.15:
                line += random.choice(sparkles)
            else:
                line += " "
        print(f"  {line}")
        delay_sleep(0.08)


def damage_shake(text, shakes=5):
    """Shake text left and right to simulate damage."""
    for i in range(shakes):
        offset = "  " if i % 2 == 0 else ""
        color = BRIGHT_RED if i % 2 == 0 else RED
        sys.stdout.write(f"\r{offset}{color}{BOLD}{text}{RESET}{' ' * 10}")
        sys.stdout.flush()
        delay_sleep(0.08)
    sys.stdout.write(f"\r  {BRIGHT_RED}{BOLD}{text}{RESET}{' ' * 10}\n")


# ═══════════════════════════════════════════
# WEATHER EFFECTS
# ═══════════════════════════════════════════

def rain_effect(lines=5, width=50):
    """Rainy weather visual."""
    for _ in range(lines):
        line = ""
        for _ in range(width):
            if random.random() < 0.1:
                line += f"{BRIGHT_BLUE}│{RESET}"
            elif random.random() < 0.05:
                line += f"{BLUE}╎{RESET}"
            else:
                line += " "
        print(f"  {line}")


def snow_effect(lines=5, width=50):
    """Snowy weather visual."""
    flakes = "❄️❅❆*·.。"
    for _ in range(lines):
        line = ""
        for _ in range(width):
            if random.random() < 0.08:
                line += f"{BRIGHT_WHITE}{random.choice(flakes)}{RESET}"
            else:
                line += " "
        print(f"  {line}")


def fire_effect(lines=4, width=40):
    """Fire weather/environment visual."""
    fire_chars = "🔥▓▒░"
    for row in range(lines):
        line = ""
        for _ in range(width):
            if random.random() < 0.2 - (row * 0.04):
                if random.random() < 0.3:
                    line += "🔥"
                else:
                    color = random.choice(FIRE_COLORS)
                    line += f"{color}{random.choice(fire_chars[1:])}{RESET}"
            else:
                line += " "
        print(f"  {line}")


def electric_storm(lines=4, width=50):
    """Electric storm visual."""
    for _ in range(lines):
        line = ""
        for _ in range(width):
            if random.random() < 0.08:
                line += f"{BRIGHT_YELLOW}⚡{RESET}"
            elif random.random() < 0.05:
                line += f"{YELLOW}╪{RESET}"
            else:
                line += " "
        print(f"  {line}")


# ═══════════════════════════════════════════
# SCREEN TRANSITIONS
# ═══════════════════════════════════════════

def wipe_transition(width=50, char="█"):
    """Screen wipe transition effect."""
    for i in range(width):
        bar = f"{BRIGHT_WHITE}{char * i}{RESET}"
        sys.stdout.write(f"\r  {bar}")
        sys.stdout.flush()
        delay_sleep(0.01)
    print()
    for i in range(width):
        bar = f"{DIM}{char * (width - i)}{RESET}"
        sys.stdout.write(f"\r  {bar}")
        sys.stdout.flush()
        delay_sleep(0.01)
    print()


def fade_transition(lines=3, width=50):
    """Fade in/out transition."""
    shades = "░▒▓█▓▒░"
    for shade in shades:
        line = shade * width
        color = random.choice(ALL_COLORS)
        print(f"  {color}{line}{RESET}")
        delay_sleep(0.05)


def pokeball_transition(width=50):
    """Pokeball-themed transition."""
    half = width // 2
    # Top half (red)
    for i in range(3):
        pad = " " * (half - i - 1)
        fill = "█" * (2 * i + 1)
        print(f"  {pad}{BRIGHT_RED}{fill}{RESET}")
    # Middle line
    print(f"  {BRIGHT_WHITE}{'═' * width}{RESET}")
    # Center ball
    center_pad = " " * (half - 1)
    print(f"  {center_pad}{BRIGHT_WHITE}(●){RESET}")
    print(f"  {BRIGHT_WHITE}{'═' * width}{RESET}")
    # Bottom half (white)
    for i in range(2, -1, -1):
        pad = " " * (half - i - 1)
        fill = "█" * (2 * i + 1)
        print(f"  {pad}{BRIGHT_WHITE}{fill}{RESET}")


# ═══════════════════════════════════════════
# BATTLE ANIMATIONS
# ═══════════════════════════════════════════

def animate_attack_sequence(attacker, defender, damage, is_crit=False):
    """Animate an attack sequence from the player."""
    print()
    # Wind-up
    sys.stdout.write(f"  {BOLD}{BRIGHT_CYAN}{attacker}{RESET} prepares to strike")
    for _ in range(3):
        sys.stdout.write(f"{BRIGHT_YELLOW}.{RESET}")
        sys.stdout.flush()
        delay_sleep(0.1)
    print()

    # Dynamic cinematic sequence trigger
    if is_crit:
        # Critical hits guarantee a full legendary blast sequence!
        anim_idx = random.randint(0, 59)
        globals()[f"cinematic_sequence_{anim_idx}"](duration=0.9)
    elif random.random() < 0.35:
        # Standard attacks have a chance of elemental visualization
        anim_idx = random.randint(0, 59)
        globals()[f"cinematic_sequence_{anim_idx}"](duration=0.7)
    else:
        # Legacy fast attack sequence
        attack_chars = ">>>💨💥"
        for i in range(len(attack_chars)):
            spaces = " " * (i * 3)
            sys.stdout.write(f"\r  {spaces}{BRIGHT_RED}{attack_chars[i]}{RESET}")
            sys.stdout.flush()
            delay_sleep(0.04)
        print()

    # Impact
    if is_crit:
        damage_shake(f"💥💥💥 CRITICAL HIT! 💥💥💥", shakes=8)
        print(f"  {BOLD}{BRIGHT_YELLOW}⚡⚡⚡ {damage} DAMAGE! ⚡⚡⚡{RESET}")
    else:
        damage_shake(f"💥 HIT! 💥", shakes=4)
        print(f"  {BOLD}{BRIGHT_RED}💥 {damage} damage to {defender}!{RESET}")
    print()


def animate_enemy_attack_sequence(attacker, defender, damage):
    """Animate an attack sequence from the enemy."""
    print()
    sys.stdout.write(f"  {BOLD}{BRIGHT_RED}{attacker}{RESET} is attacking")
    for _ in range(3):
        sys.stdout.write(f"{RED}.{RESET}")
        sys.stdout.flush()
        delay_sleep(0.1)
    print()

    if random.random() < 0.3:
        anim_idx = random.randint(0, 59)
        globals()[f"cinematic_sequence_{anim_idx}"](duration=0.7)
    else:
        attack_chars = "<<<💨💥"
        for i in range(len(attack_chars)):
            spaces = " " * (30 - (i * 3))
            sys.stdout.write(f"\r  {spaces}{BRIGHT_RED}{attack_chars[i]}{RESET}")
            sys.stdout.flush()
            delay_sleep(0.04)
        print()

    damage_shake(f"💢 {attacker.upper()} STRUCK! 💢", shakes=4)
    print(f"  {BOLD}{BRIGHT_RED}💔 {damage} damage to {defender}!{RESET}")
    print()


def animate_catch_attempt(success):
    """Animate a pokeball throw and catch attempt."""
    # Throw animation
    positions = [5, 15, 25, 35]
    for pos in positions:
        line = " " * pos + "⚪"
        sys.stdout.write(f"\r  {line}{' ' * (40 - pos)}")
        sys.stdout.flush()
        delay_sleep(0.15)

    print()
    # Wiggle
    for i in range(3):
        wiggle = "  " if i % 2 == 0 else ""
        sys.stdout.write(f"\r  {' ' * 33}{wiggle}⚪ *wiggle*")
        sys.stdout.flush()
        delay_sleep(0.5)

    print()
    if success:
        print(f"  {' ' * 33}{BRIGHT_GREEN}✨ *CLICK!* ✨{RESET}")
    else:
        print(f"  {' ' * 33}{BRIGHT_RED}💥 *BREAK!* 💥{RESET}")
    print()


def animate_heal(pokemon_name, heal_amount):
    """Animate healing effect."""
    hearts = ["❤️ ", "❤️ ❤️ ", "❤️ ❤️ ❤️ ", "❤️ ❤️ ❤️ ❤️ ", "❤️ ❤️ ❤️ ❤️ ❤️ "]
    for i, h in enumerate(hearts):
        brightness = int(100 + (i * 35))
        sys.stdout.write(f"\r  {rgb(0, brightness, 0)}{h} Healing {pokemon_name}...{RESET}{' ' * 10}")
        sys.stdout.flush()
        delay_sleep(0.3)
    print()
    print(f"  {BOLD}{BRIGHT_GREEN}✨ +{heal_amount} HP restored!{RESET}")


def animate_level_up(pokemon_name, new_level):
    """Animate level up sequence."""
    print()
    # Stars rising
    for i in range(5):
        stars = "⭐" * (i + 1)
        pad = " " * (10 - i)
        sys.stdout.write(f"\r  {pad}{BRIGHT_YELLOW}{stars}{RESET}")
        sys.stdout.flush()
        delay_sleep(0.2)
    print()

    # Flash the name
    for i in range(6):
        if i % 2 == 0:
            sys.stdout.write(f"\r  {BOLD}{BRIGHT_YELLOW}{REVERSE} {pokemon_name.upper()} IS NOW LEVEL {new_level}! {RESET}")
        else:
            sys.stdout.write(f"\r  {BOLD}{BRIGHT_CYAN} {pokemon_name.upper()} IS NOW LEVEL {new_level}! {RESET}")
        sys.stdout.flush()
        delay_sleep(0.2)
    print()


def animate_money_earned(amount):
    """Animate earning money."""
    coins = ""
    for i in range(min(amount // 30, 10)):
        coins += "💰"
        sys.stdout.write(f"\r  {coins} +{amount} coins!")
        sys.stdout.flush()
        delay_sleep(0.1)
    print()


# ═══════════════════════════════════════════
# FANCY TEXT DISPLAYS
# ═══════════════════════════════════════════

def stat_card(name, hp, maxhp, dm, xp, maxxp, lvl, speed=None, ability=None, hold_item=None):
    """Display a full stat card for a pokemon."""
    width = 35
    name_display = name.upper()
    type_icon = random.choice(["🔥", "💧", "🌿", "⚡", "🔮", "👻", "🐉", "🪨", "✨"])

    print(f"  {BOLD}{BRIGHT_CYAN}╔{'═' * width}╗{RESET}")
    print(f"  {BOLD}{BRIGHT_CYAN}║{RESET} {type_icon} {BOLD}{BRIGHT_WHITE}{name_display:^{width - 6}}{RESET} {type_icon} {BOLD}{BRIGHT_CYAN}║{RESET}")
    ab_display = f"Ab: {ability or '—'}"
    item_display = f"Item: {hold_item or '—'}"
    print(f"  {BOLD}{BRIGHT_CYAN}║{RESET} {DIM}{ab_display:<{width//2}}{item_display:>{width//2}}{RESET} {BOLD}{BRIGHT_CYAN}║{RESET}")
    print(f"  {BOLD}{BRIGHT_CYAN}╠{'═' * width}╣{RESET}")

    # HP bar
    hp_ratio = max(0, min(1, hp / maxhp))
    hp_filled = int(20 * hp_ratio)
    hp_empty = 20 - hp_filled
    hp_color = BRIGHT_GREEN if hp_ratio > 0.6 else (BRIGHT_YELLOW if hp_ratio > 0.3 else BRIGHT_RED)
    
    # Custom bar styles
    bar_style = GAME_SETTINGS.get("hp_bar_style")
    if bar_style == "symbols":
        hp_str = f"{hp_color}{'=' * hp_filled}{DIM}{'-' * hp_empty}{RESET}"
    elif bar_style == "emoji":
        hp_str = f"{hp_color}{'🟩' * (hp_filled//2)}{DIM}{'⬛' * (hp_empty//2)}{RESET}"
    elif bar_style == "abstract":
        hp_str = f"{hp_color}{'~' * hp_filled}{DIM}{'.' * hp_empty}{RESET}"
    else: # blocks
        hp_str = f"{hp_color}{'█' * hp_filled}{DIM}{'░' * hp_empty}{RESET}"

    print(f"  {BOLD}{BRIGHT_CYAN}║{RESET}  ❤️  HP [{hp_str}] {hp_color}{hp}/{maxhp}{RESET}{'':<{20 - len(str(hp)) - len(str(maxhp))}} {BOLD}{BRIGHT_CYAN}║{RESET}")

    # XP bar
    xp_ratio = max(0, min(1, xp / maxxp))
    xp_filled = int(20 * xp_ratio)
    xp_empty = 20 - xp_filled
    xp_style = GAME_SETTINGS.get("xp_bar_style")
    if xp_style == "symbols":
        xp_str = f"{BRIGHT_CYAN}{'#' * xp_filled}{DIM}{'-' * xp_empty}{RESET}"
    elif xp_style == "emoji":
        xp_str = f"{BRIGHT_CYAN}{'🟦' * (xp_filled//2)}{DIM}{'⬛' * (xp_empty//2)}{RESET}"
    elif xp_style == "abstract":
        xp_str = f"{BRIGHT_CYAN}{'*' * xp_filled}{DIM}{'.' * xp_empty}{RESET}"
    else:
        xp_str = f"{BRIGHT_CYAN}{'▰' * xp_filled}{DIM}{'▱' * xp_empty}{RESET}"

    print(f"  {BOLD}{BRIGHT_CYAN}║{RESET}  ⭐ XP [{xp_str}] {BRIGHT_CYAN}{xp}/{maxxp}{RESET}{'':<{20 - len(str(xp)) - len(str(maxxp))}} {BOLD}{BRIGHT_CYAN}║{RESET}")

    # Stats
    print(f"  {BOLD}{BRIGHT_CYAN}║{RESET}  ⚔️  DMG: {BOLD}{BRIGHT_RED}{dm:>5}{RESET}{'':>{width - 18}} {BOLD}{BRIGHT_CYAN}║{RESET}")
    print(f"  {BOLD}{BRIGHT_CYAN}║{RESET}  🌟 LVL: {BOLD}{BRIGHT_YELLOW}{lvl:>5}{RESET}{'':>{width - 18}} {BOLD}{BRIGHT_CYAN}║{RESET}")
    if speed is not None:
        print(f"  {BOLD}{BRIGHT_CYAN}║{RESET}  🏃 SPD: {BOLD}{BRIGHT_CYAN}{speed:>5}{RESET}{'':>{width - 18}} {BOLD}{BRIGHT_CYAN}║{RESET}")
    print(f"  {BOLD}{BRIGHT_CYAN}╚{'═' * width}╝{RESET}")


def battle_hud(your_name, your_hp, your_maxhp, your_dm,
               enemy_name, enemy_hp, enemy_maxhp, enemy_dm,
               your_status=None, enemy_status=None, weather="Clear",
               your_stages=None, enemy_stages=None, turn=0,
               messages=None, your_ability=None, your_item=None,
               enemy_ability=None):
    """Display a battle HUD with both pokemon stats, status, weather, turn counter, and recent messages."""
    width = 60
    hud_style = GAME_SETTINGS.get("battle_hud_style")
    
    # Weather display
    weather_icons = {"Rain": "🌧️", "Sun": "☀️", "Sandstorm": "🌪️", "Hail": "❄️", "Acid Rain": "🧪", "Solar Flare": "💥"}
    w_icon = weather_icons.get(weather, "🌤️")
    
    # Border
    if hud_style == "modern":
        border_top = f"  {BOLD}{BRIGHT_WHITE}┌{'─' * width}┐{RESET}"
        border_bot = f"  {BOLD}{BRIGHT_WHITE}└{'─' * width}┘{RESET}"
    else:
        border_top = f"  {BOLD}{BRIGHT_YELLOW}{'═' * width}{RESET}"
        border_bot = border_top

    if border_top: print(border_top)

    # Header with turn counter and weather
    turn_tag = f"[Turn {turn}]" if turn else ""
    weather_line = f"{w_icon}  {weather.upper()}  {w_icon}"
    header = f"{weather_line}  {DIM}{turn_tag}{RESET}"
    print(f"  {BOLD}{BRIGHT_CYAN}{header.center(width)}{RESET}")

    # Names and Status
    y_stat = f" {BRIGHT_MAGENTA}[{your_status}]{RESET}" if your_status else ""
    e_stat = f" {BRIGHT_MAGENTA}[{enemy_status}]{RESET}" if enemy_status else ""
    
    name_line = f"{your_name.upper()}{y_stat}  vs  {enemy_name.upper()}{e_stat}"
    print(f"  {BOLD}{BRIGHT_WHITE}{name_line.center(width)}{RESET}")

    # Your pokemon
    your_ratio = max(0, min(1, your_hp / your_maxhp))
    your_filled = int(20 * your_ratio)
    your_empty = 20 - your_filled
    your_color = BRIGHT_GREEN if your_ratio > 0.6 else (BRIGHT_YELLOW if your_ratio > 0.3 else BRIGHT_RED)

    # Enemy pokemon
    enemy_ratio = max(0, min(1, enemy_hp / enemy_maxhp))
    enemy_filled = int(20 * enemy_ratio)
    enemy_empty = 20 - enemy_filled
    enemy_color = BRIGHT_GREEN if enemy_ratio > 0.6 else (BRIGHT_YELLOW if enemy_ratio > 0.3 else BRIGHT_RED)

    # Custom bars
    y_bar = f"{your_color}{'█' * your_filled}{DIM}{'░' * your_empty}{RESET}"
    e_bar = f"{enemy_color}{'█' * enemy_filled}{DIM}{'░' * enemy_empty}{RESET}"

    print(f"  {your_color}{your_hp:>4}/{your_maxhp:<4}{RESET} [{y_bar}]")
    print(f"  {enemy_color}{enemy_hp:>4}/{enemy_maxhp:<4}{RESET} [{e_bar}]")

    # Ability and held item info
    info_parts = []
    if your_ability: info_parts.append(f"⚡{your_ability}")
    if your_item: info_parts.append(f"🎒{your_item}")
    if enemy_ability: info_parts.append(f"👾{enemy_ability}")
    if info_parts:
        print(f"  {DIM}{' | '.join(info_parts)}{RESET}")

    if your_stages or enemy_stages:
        def format_stages(stages):
            if not stages:
                return ""
            parts = []
            for stat, val in stages.items():
                if val > 0:
                    parts.append(f"{stat.upper()}+{val}")
                elif val < 0:
                    parts.append(f"{stat.upper()}{val}")
            return " ".join(parts) if parts else ""
        y_stage_str = format_stages(your_stages)
        e_stage_str = format_stages(enemy_stages)
        if y_stage_str or e_stage_str:
            stage_line = f"{y_stage_str:30}  {e_stage_str:30}"
            print(f"  {BRIGHT_CYAN}{stage_line}{RESET}")

    if border_bot: print(border_bot)

    # Recent messages area
    if messages:
        for msg in messages[-3:]:
            print(f"  {msg}")


def shop_item_card(name, cost, hp, dm, index):
    """Display a fancy shop item card."""
    owned = "💰"
    print(f"  {BOLD}{BRIGHT_CYAN}┌{'─' * 30}┐{RESET}")
    print(f"  {BOLD}{BRIGHT_CYAN}│{RESET} {BOLD}{BRIGHT_WHITE}{index}. {rainbow_text(name):<25} {BOLD}{BRIGHT_CYAN}│{RESET}")
    print(f"  {BOLD}{BRIGHT_CYAN}│{RESET}   {BOLD}{BRIGHT_YELLOW}{owned} Cost: {cost:<18}{RESET} {BOLD}{BRIGHT_CYAN}│{RESET}")
    print(f"  {BOLD}{BRIGHT_CYAN}│{RESET}   {BOLD}{BRIGHT_GREEN}❤️  HP: {hp:<19}{RESET} {BOLD}{BRIGHT_CYAN}│{RESET}")
    print(f"  {BOLD}{BRIGHT_CYAN}│{RESET}   {BOLD}{BRIGHT_RED}⚔️  DM: {dm:<19}{RESET} {BOLD}{BRIGHT_CYAN}│{RESET}")
    print(f"  {BOLD}{BRIGHT_CYAN}└{'─' * 30}┘{RESET}")


def fancy_header(text, emoji="⚡", width=50):
    """Display a fancy section header."""
    print()
    print(f"  {BOLD}{random.choice(ALL_COLORS)}{'━' * width}{RESET}")
    centered = f"{emoji}  {text}  {emoji}"
    pad_total = width - len(centered)
    left_pad = pad_total // 2
    right_pad = pad_total - left_pad
    print(f"  {BOLD}{random.choice(ALL_COLORS)}{' ' * left_pad}{rainbow_text(centered)}{' ' * right_pad}{RESET}")
    print(f"  {BOLD}{random.choice(ALL_COLORS)}{'━' * width}{RESET}")
    print()


def countdown(seconds=3):
    """Dramatic countdown."""
    for i in range(seconds, 0, -1):
        size = seconds - i + 1
        color = [BRIGHT_RED, BRIGHT_YELLOW, BRIGHT_GREEN][min(i - 1, 2)]
        sys.stdout.write(f"\r  {color}{BOLD}{'█' * size} {i} {'█' * size}{RESET}{' ' * 20}")
        sys.stdout.flush()
        delay_sleep(0.8)
    sys.stdout.write(f"\r  {BOLD}{BRIGHT_GREEN}{'█' * (seconds + 1)} GO! {'█' * (seconds + 1)}{RESET}{' ' * 20}\n")


def victory_celebration(lines=5, width=40):
    """Victory confetti animation."""
    confetti = "🎉🎊✨💫⭐🌟🏆💎🎯🥇"
    for _ in range(lines):
        line = ""
        for _ in range(width):
            if random.random() < 0.12:
                line += random.choice(confetti)
            else:
                line += " "
        print(f"  {line}")
        delay_sleep(0.1)


def defeat_rain(lines=5, width=40):
    """Defeat sad rain animation."""
    for _ in range(lines):
        line = ""
        for _ in range(width):
            if random.random() < 0.1:
                line += f"{BLUE}💧{RESET}"
            elif random.random() < 0.05:
                line += f"{DIM}│{RESET}"
            else:
                line += " "
        print(f"  {line}")
        delay_sleep(0.1)
# ═══════════════════════════════════════════
# SUBTLE BATTLE EFFECTS
# ═══════════════════════════════════════════

def ability_activation(ability_name, pokemon_name):
    sys.stdout.write(f"\r  {BRIGHT_CYAN}[ {ability_name} of {pokemon_name}! ]{RESET}")
    sys.stdout.flush()
    delay_sleep(0.3)

def type_effectiveness_flash(effectiveness):
    if effectiveness > 1.0:
        for _ in range(2):
            sys.stdout.write(f"\r  {BRIGHT_YELLOW}{'💥' * 5} SUPER EFFECTIVE! {'💥' * 5}{RESET}")
            sys.stdout.flush()
            delay_sleep(0.1)
            sys.stdout.write(f"\r  {' ' * 50}")
            sys.stdout.flush()
            delay_sleep(0.1)
    elif effectiveness == 0.0:
        for _ in range(2):
            sys.stdout.write(f"\r  {DIM}💨 Not very effective...💨{RESET}")
            sys.stdout.flush()
            delay_sleep(0.15)

def weather_indicator(weather, duration=0.5):
    icons = {"Rain":"🌧️","Sun":"☀️","Sandstorm":"🌪️","Hail":"❄️","Acid Rain":"🧪","Solar Flare":"💥"}
    icon = icons.get(weather, "🌤️")
    end = time.time() + duration
    while time.time() < end:
        sys.stdout.write(f"\r  {BRIGHT_CYAN}{icon} {weather.upper()} {icon}{RESET}")
        sys.stdout.flush()
        delay_sleep(0.08)

def item_flash(item_name):
    sys.stdout.write(f"\r  {BRIGHT_YELLOW}✨ {item_name} activated! ✨{RESET}")
    sys.stdout.flush()
    delay_sleep(0.3)

def stage_change_flash(pokemon_name, stat, direction, stages):
    if stages > 0:
        sys.stdout.write(f"\r  {BRIGHT_GREEN}⬆ {pokemon_name}'s {stat.upper()} rose!{RESET}")
    else:
        sys.stdout.write(f"\r  {BRIGHT_RED}⬇ {pokemon_name}'s {stat.upper()} fell!{RESET}")
    sys.stdout.flush()
    delay_sleep(0.3)

def recoil_flash(pokemon_name, amount):
    sys.stdout.write(f"\r  {BRIGHT_RED}💥 {pokemon_name} took {amount} recoil damage!{RESET}")
    sys.stdout.flush()
    delay_sleep(0.3)

def healing_flash(pokemon_name, amount):
    sys.stdout.write(f"\r  {BRIGHT_GREEN}❤️ {pokemon_name} restored {amount} HP!{RESET}")
    sys.stdout.flush()
    delay_sleep(0.3)

# ═══════════════════════════════════════════
# MASSIVE CINEMATIC EFFECTS
# ═══════════════════════════════════════════

def hyper_speed_warp(duration=2.0, width=50):
    """Star Wars style hyper-speed warp effect."""
    end_time = time.time() + duration
    stars = [(random.randint(0, width-1), random.uniform(0.1, 1.0)) for _ in range(30)]
    
    while time.time() < end_time:
        line = [" "] * width
        for i in range(len(stars)):
            pos, speed = stars[i]
            line[int(pos)] = f"{BRIGHT_WHITE}━{RESET}"
            stars[i] = (pos + speed * 3, speed * 1.5) # accelerate outward
            
            if stars[i][0] >= width or stars[i][0] < 0:
                stars[i] = (random.randint(width//2 - 5, width//2 + 5), random.uniform(-0.5, 0.5))
        
        print(f"  {''.join(line)}")
        delay_sleep(0.04)

def black_hole_transition(width=50):
    """Sucks the screen into a central point."""
    center = width // 2
    for radius in range(center, -1, -2):
        line = " " * (center - radius) + f"{BRIGHT_MAGENTA}🌀{'═' * (radius * 2)}🌀{RESET}"
        sys.stdout.write(f"\r  {line}{' ' * 20}")
        sys.stdout.flush()
        delay_sleep(0.05)
    print(f"\r  {' ' * center}{BOLD}{BRIGHT_MAGENTA}💥 VOID 💥{RESET}{' ' * 20}")
    delay_sleep(0.5)

def elemental_storm(lines=6, width=50):
    """Combines fire, water, electric, and grass effects."""
    elements = [
        (FIRE_COLORS, "🔥"),
        (WATER_COLORS, "💧"),
        (ELECTRIC_COLORS, "⚡"),
        (GRASS_COLORS, "🌿")
    ]
    for _ in range(lines):
        line = ""
        for _ in range(width):
            if random.random() < 0.15:
                palette, icon = random.choice(elements)
                line += f"{random.choice(palette)}{icon}{RESET}"
            else:
                line += " "
        print(f"  {line}")
        delay_sleep(0.08)

def laser_show(duration=2.0, width=50):
    """Crazy colorful laser beams."""
    end_time = time.time() + duration
    chars = "＼／│─"
    while time.time() < end_time:
        line = ""
        for _ in range(width):
            if random.random() < 0.2:
                line += f"{random.choice(ALL_COLORS)}{BOLD}{random.choice(chars)}{RESET}"
            else:
                line += " "
        print(f"  {line}")
        delay_sleep(0.06)

# ═══════════════════════════════════════════
# EVOLUTION ANIMATION
# ═══════════════════════════════════════════

def dna_evolution_sequence(old_name, new_name):
    """Plays an epic DNA helix spinning animation for evolution."""
    print()
    wipe_transition(width=50)
    
    # Pulsing pre-evolution text
    for i in range(6):
        color = BRIGHT_WHITE if i % 2 == 0 else DIM
        sys.stdout.write(f"\r  {color}What? {old_name.upper()} is evolving!{RESET}{' '*10}")
        sys.stdout.flush()
        delay_sleep(0.4)
    print("\n")
    
    # DNA Helix Animation
    helix = [
        "  {c1}🧬  🔴{c2}══════{c3}🔵  🧬",
        "  {c1}🧬   🔴{c2}════{c3}🔵   🧬",
        "  {c1}🧬    🔴{c2}══{c3}🔵    🧬",
        "  {c1}🧬     🔴{c3}🔵     🧬",
        "  {c1}🧬    🔵{c2}══{c3}🔴    🧬",
        "  {c1}🧬   🔵{c2}════{c3}🔴   🧬",
        "  {c1}🧬  🔵{c2}══════{c3}🔴  🧬"
    ]
    
    # Spin the helix and speed it up
    spins = 20
    for i in range(spins):
        speed_factor = max(0.02, 0.15 - (i * 0.008))
        c1 = random.choice([BRIGHT_MAGENTA, BRIGHT_CYAN, BRIGHT_WHITE])
        c2 = DIM
        c3 = random.choice([BRIGHT_RED, BRIGHT_BLUE, BRIGHT_YELLOW])
        
        sys.stdout.write(f"\r{helix[i % len(helix)].format(c1=c1, c2=c2, c3=c3)}{' '*10}")
        sys.stdout.flush()
        delay_sleep(speed_factor)
        
    print("\n")
    
    # Flash explosion
    for _ in range(3):
        print(f"  {BG_BRIGHT_WHITE}{BLACK}{' '*50}{RESET}")
        delay_sleep(0.1)
        print(f"  {' '*50}")
        delay_sleep(0.1)
        
    sparkle_burst(duration=1.5, width=45)
    
    # Final Reveal
    text = f"CONGRATULATIONS! Your {old_name.capitalize()} evolved into {new_name.upper()}!"
    print(f"\n  {BOLD}{BRIGHT_GREEN}✨ {text} ✨{RESET}\n")
    delay_sleep(1.0)


def mega_evolution_animation(pokemon_name, mega_form):
    """Plays an epic Mega Evolution sequence with DNA symbols and light bursts."""
    print()
    fancy_header(f"MEGA EVOLUTION!", emoji="🧬", width=50)
    print(f"  {BOLD}{BRIGHT_WHITE}The Key Stone reacts with {pokemon_name.upper()}'s Mega Stone!{RESET}")
    print()
    delay_sleep(0.8)
    
    # Rising particles/DNA helix
    helix = [
        "  {c1}🧬  🔴{c2}═══{c3}🔵  🧬",
        "  {c1}🧬   🔴{c2}═{c3}🔵   🧬",
        "  {c1}🧬    🔴🔵    🧬",
        "  {c1}🧬   🔵{c2}═{c3}🔴   🧬",
        "  {c1}🧬  🔵{c2}═══{c3}🔴  🧬"
    ]
    for i in range(12):
        c1 = BRIGHT_MAGENTA
        c2 = DIM
        c3 = BRIGHT_CYAN
        sys.stdout.write(f"\r{helix[i % len(helix)].format(c1=c1, c2=c2, c3=c3)}{' '*10}")
        sys.stdout.flush()
        delay_sleep(0.08)
    print("\n")
    
    # Blast/Flash
    sparkle_burst(duration=1.2, width=50)
    for _ in range(2):
        sys.stdout.write(f"\r  {REVERSE}{BOLD}{BRIGHT_YELLOW}✨🧬 MEGA EVOLUTION EXPLOSION! 🧬✨{RESET}")
        sys.stdout.flush()
        delay_sleep(0.15)
        sys.stdout.write(f"\r  {' '*50}")
        sys.stdout.flush()
        delay_sleep(0.15)
        
    print()
    text = f"{pokemon_name.upper()} has Mega Evolved into {mega_form.upper()}!"
    print(f"  {BOLD}{BRIGHT_YELLOW}✨ {text} ✨{RESET}")
    print()
    delay_sleep(1.0)


def z_move_animation(pokemon_name, z_move_name, z_crystal):
    """Plays a high-energy Z-Power concentration and strike animation."""
    print()
    fancy_header(f"Z-POWER ACTIVATE!", emoji="⚡", width=50)
    print(f"  {BOLD}{BRIGHT_WHITE}{pokemon_name.upper()} surrounds itself with Z-Power using {z_crystal}!{RESET}")
    print()
    delay_sleep(0.8)
    
    # Charging energy
    for i in range(8):
        bars = "█" * (i + 1)
        dots = "." * (8 - i - 1)
        sys.stdout.write(f"\r  {BRIGHT_YELLOW}⚡ CHARGING Z-POWER: [{bars}{dots}] {int((i+1)/8*100)}%{RESET}")
        sys.stdout.flush()
        delay_sleep(0.12)
    print("\n")
    
    # Laser warp/Hyper speed warp
    hyper_speed_warp(duration=1.0, width=50)
    
    # Big strike reveal
    print(f"\n  {REVERSE}{BOLD}{BRIGHT_YELLOW}💥💥💥 {z_move_name.upper()} 💥💥💥{RESET}")
    sparkle_burst(duration=1.0, width=50)
    print()
    delay_sleep(1.0)


def gigantamax_animation(pokemon_name):
    """Plays a colossal growth and Gigantamax storm cloud animation."""
    print()
    fancy_header(f"GIGANTAMAX!", emoji="👹", width=50)
    print(f"  {BOLD}{BRIGHT_WHITE}{pokemon_name.upper()} is growing to colossal proportions!{RESET}")
    print()
    delay_sleep(0.8)
    
    # Crimson storm clouds
    clouds = [
        "       ☁️        ",
        "     ☁️☁️☁️      ",
        "   ☁️☁️☁️☁️☁️    ",
        " ☁️🔴🔴🔴🔴🔴☁️  ",
        "👹👹👹👹👹👹👹👹"
    ]
    for c in clouds:
        print(f"  {BRIGHT_RED}{c}{RESET}")
        delay_sleep(0.2)
    print()
    
    # Shake
    damage_shake(f"⚡ Colossal Red Storm swirls around the arena! ⚡", shakes=6)
    print()
    text = f"{pokemon_name.upper()} has Gigantamaxed!"
    print(f"  {BOLD}{BRIGHT_RED}👹 {text} 👹{RESET}")
    print()
    delay_sleep(1.0)

