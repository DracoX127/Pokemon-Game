"""
╔══════════════════════════════════════════════════╗
║  🔥 CRAZY STYLE ENGINE 🔥                       ║
║  Wild colors, animations, and text effects       ║
║  for the most INSANE terminal experience ever!   ║
╚══════════════════════════════════════════════════╝
"""
import random
import time
import sys
import os
from settings import GAME_SETTINGS

# ═══════════════════════════════════════════
# ANSI ESCAPE CODES
# ═══════════════════════════════════════════

# Reset
RESET = "\033[0m"

# Text styles
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
REVERSE = "\033[7m"
STRIKETHROUGH = "\033[9m"

# Regular colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Bright colors
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# Background colors
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"
BG_BRIGHT_RED = "\033[101m"
BG_BRIGHT_GREEN = "\033[102m"
BG_BRIGHT_YELLOW = "\033[103m"
BG_BRIGHT_BLUE = "\033[104m"
BG_BRIGHT_MAGENTA = "\033[105m"
BG_BRIGHT_CYAN = "\033[106m"

# Color lists for random selection
ALL_COLORS = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, BRIGHT_RED, BRIGHT_GREEN,
              BRIGHT_YELLOW, BRIGHT_BLUE, BRIGHT_MAGENTA, BRIGHT_CYAN, BRIGHT_WHITE]

FIRE_COLORS = [RED, BRIGHT_RED, YELLOW, BRIGHT_YELLOW]
WATER_COLORS = [BLUE, BRIGHT_BLUE, CYAN, BRIGHT_CYAN]
GRASS_COLORS = [GREEN, BRIGHT_GREEN, YELLOW, BRIGHT_YELLOW]
ELECTRIC_COLORS = [YELLOW, BRIGHT_YELLOW, BRIGHT_WHITE]
PSYCHIC_COLORS = [MAGENTA, BRIGHT_MAGENTA, BRIGHT_CYAN]

# ═══════════════════════════════════════════
# 256-COLOR AND TRUE COLOR SUPPORT
# ═══════════════════════════════════════════

def rgb(r, g, b):
    """Create a true color (24-bit) foreground color."""
    return f"\033[38;2;{r};{g};{b}m"

def bg_rgb(r, g, b):
    """Create a true color (24-bit) background color."""
    return f"\033[48;2;{r};{g};{b}m"

def rainbow_char(char, index):
    """Color a single character with rainbow colors based on position."""
    colors_cycle = [
        (255, 0, 0), (255, 127, 0), (255, 255, 0),
        (0, 255, 0), (0, 0, 255), (75, 0, 130), (148, 0, 211)
    ]
    r, g, b = colors_cycle[index % len(colors_cycle)]
    return f"{rgb(r, g, b)}{char}{RESET}"

# ═══════════════════════════════════════════
# TEXT EFFECTS
# ═══════════════════════════════════════════

def rainbow_text(text):
    """Make text cycle through rainbow colors character by character."""
    result = ""
    color_idx = 0
    for char in text:
        if char == " ":
            result += char
        else:
            result += rainbow_char(char, color_idx)
            color_idx += 1
    return result

def random_color_text(text):
    """Color each character a random color."""
    result = ""
    for char in text:
        if char == " ":
            result += char
        else:
            result += f"{random.choice(ALL_COLORS)}{char}"
    return result + RESET

def gradient_text(text, start_rgb, end_rgb):
    """Create a smooth gradient across text."""
    result = ""
    length = max(len(text.replace(" ", "")), 1)
    color_idx = 0
    for char in text:
        if char == " ":
            result += char
        else:
            ratio = color_idx / max(length - 1, 1)
            r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * ratio)
            g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * ratio)
            b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * ratio)
            result += f"{rgb(r, g, b)}{char}"
            color_idx += 1
    return result + RESET

def neon_glow(text, color_rgb):
    """Make text look like it has a neon glow."""
    r, g, b = color_rgb
    dim_r, dim_g, dim_b = r // 3, g // 3, b // 3
    return f"{BOLD}{rgb(r, g, b)}{bg_rgb(dim_r, dim_g, dim_b)} {text} {RESET}"

def glitch_text(text):
    """Make text look glitchy with random symbols inserted."""
    glitch_chars = "░▒▓█▀▄▌▐│┤╡╢╖╕╣║╗╝╜╛┐└┴┬├─┼╞╟╚╔╩╦╠═╬"
    result = ""
    for char in text:
        if random.random() < 0.15:
            result += f"{random.choice(ALL_COLORS)}{random.choice(glitch_chars)}{RESET}"
        result += f"{random.choice(ALL_COLORS)}{char}{RESET}"
    return result

def wave_text(text):
    """Add wave-like Unicode decorations."""
    waves = "〰️～∿≋"
    return f"{'～' * 3} {rainbow_text(text)} {'～' * 3}"

def sparkle_text(text):
    """Add sparkle emojis around text."""
    sparkles = ["✨", "💫", "⭐", "🌟", "✴️", "🔥", "💥", "⚡"]
    left = random.choice(sparkles)
    right = random.choice(sparkles)
    return f"{left} {rainbow_text(text)} {right}"

def fire_text(text):
    """Make text look like it's on fire."""
    result = ""
    for char in text:
        if char == " ":
            result += char
        else:
            result += f"{BOLD}{random.choice(FIRE_COLORS)}{char}"
    return result + RESET

def electric_text(text):
    """Make text look electric/lightning."""
    result = ""
    for char in text:
        if char == " ":
            result += char
        else:
            result += f"{BOLD}{random.choice(ELECTRIC_COLORS)}{char}"
    return result + RESET

def psychic_text(text):
    """Make text look psychic/mystical."""
    result = ""
    for char in text:
        if char == " ":
            result += char
        else:
            result += f"{BOLD}{ITALIC}{random.choice(PSYCHIC_COLORS)}{char}"
    return result + RESET

def crazy_text(text):
    """The CRAZIEST text effect - random everything."""
    styles = [BOLD, ITALIC, UNDERLINE, ""]
    result = ""
    for char in text:
        if char == " ":
            result += char
        else:
            style = random.choice(styles)
            color = random.choice(ALL_COLORS)
            result += f"{style}{color}{char}{RESET}"
    return result

# ═══════════════════════════════════════════
# ANIMATED PRINTING
# ═══════════════════════════════════════════

def typewriter(text, delay=0.03, color=None):
    """Print text with a typewriter effect."""
    if color:
        sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if color:
        sys.stdout.write(RESET)
    print()

def dramatic_print(text, delay=0.05):
    """Print text dramatically with random colors per character."""
    for char in text:
        if char == " ":
            sys.stdout.write(char)
        else:
            sys.stdout.write(f"{random.choice(ALL_COLORS)}{BOLD}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def explode_print(text):
    """Print text with an explosion effect."""
    print(f"\n{BOLD}{BRIGHT_RED}💥💥💥 {fire_text(text)} 💥💥💥{RESET}\n")

def slow_reveal(text, style_func=rainbow_text, delay=0.02):
    """Reveal text character by character with styling."""
    for i in range(1, len(text) + 1):
        sys.stdout.write(f"\r{style_func(text[:i])}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ═══════════════════════════════════════════
# BOX DRAWING & FRAMES
# ═══════════════════════════════════════════

def crazy_box(text, color=BRIGHT_CYAN, width=None):
    """Draw a crazy box around text."""
    lines = text.split('\n') if '\n' in text else [text]
    if width is None:
        width = max(len(line) for line in lines) + 4
    
    top = f"{color}{BOLD}╔{'═' * width}╗{RESET}"
    bottom = f"{color}{BOLD}╚{'═' * width}╝{RESET}"
    
    print(top)
    for line in lines:
        padding = width - len(line) - 2
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"{color}{BOLD}║{RESET} {' ' * left_pad}{rainbow_text(line)}{' ' * right_pad} {color}{BOLD}║{RESET}")
    print(bottom)

def fire_box(text, width=None):
    """Draw a fire-themed box."""
    lines = text.split('\n') if '\n' in text else [text]
    if width is None:
        width = max(len(line) for line in lines) + 4
    
    fire_top = f"{BOLD}{BRIGHT_RED}🔥{'━' * width}🔥{RESET}"
    fire_bottom = f"{BOLD}{BRIGHT_RED}🔥{'━' * width}🔥{RESET}"
    
    print(fire_top)
    for line in lines:
        padding = width - len(line) - 2
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"{BOLD}{BRIGHT_RED}🔥{RESET} {' ' * left_pad}{fire_text(line)}{' ' * right_pad} {BOLD}{BRIGHT_RED}🔥{RESET}")
    print(fire_bottom)

def electric_box(text, width=None):
    """Draw an electric-themed box."""
    lines = text.split('\n') if '\n' in text else [text]
    if width is None:
        width = max(len(line) for line in lines) + 4
    
    print(f"{BOLD}{BRIGHT_YELLOW}⚡{'─' * width}⚡{RESET}")
    for line in lines:
        padding = width - len(line) - 2
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"{BOLD}{BRIGHT_YELLOW}⚡{RESET} {' ' * left_pad}{electric_text(line)}{' ' * right_pad} {BOLD}{BRIGHT_YELLOW}⚡{RESET}")
    print(f"{BOLD}{BRIGHT_YELLOW}⚡{'─' * width}⚡{RESET}")

def battle_frame(left_text, right_text):
    """Draw a battle-style frame."""
    width = 50
    print(f"{BOLD}{BRIGHT_RED}{'⚔️ ' * 13}{RESET}")
    left_styled = fire_text(left_text)
    right_styled = gradient_text(right_text, (0, 100, 255), (255, 0, 100))
    print(f"  {left_styled}  {BOLD}{BRIGHT_WHITE}⚡ VS ⚡{RESET}  {right_styled}")
    print(f"{BOLD}{BRIGHT_RED}{'⚔️ ' * 13}{RESET}")

def hp_bar(current, maximum, length=20, name=""):
    """Display a colored HP bar."""
    ratio = max(0, current / maximum)
    filled = int(length * ratio)
    empty = length - filled
    
    if ratio > 0.6:
        bar_color = BRIGHT_GREEN
    elif ratio > 0.3:
        bar_color = BRIGHT_YELLOW
    else:
        bar_color = BRIGHT_RED
    
    bar = f"{bar_color}{'█' * filled}{DIM}{'░' * empty}{RESET}"
    label = f"{BOLD}{bar_color}{current}/{maximum}{RESET}"
    
    if name:
        print(f"  {BOLD}{BRIGHT_WHITE}{name}{RESET} ❤️  [{bar}] {label}")
    else:
        print(f"  ❤️  [{bar}] {label}")

def xp_bar(current, maximum, length=20, name=""):
    """Display an XP bar."""
    ratio = min(1, max(0, current / maximum))
    filled = int(length * ratio)
    empty = length - filled
    
    bar = f"{BRIGHT_CYAN}{'▰' * filled}{DIM}{'▱' * empty}{RESET}"
    label = f"{BOLD}{BRIGHT_CYAN}{current}/{maximum}{RESET}"
    
    if name:
        print(f"  {BOLD}{BRIGHT_WHITE}{name}{RESET} ⭐ [{bar}] {label}")
    else:
        print(f"  ⭐ [{bar}] {label}")

# ═══════════════════════════════════════════
# DIVIDERS & SEPARATORS
# ═══════════════════════════════════════════

def crazy_divider(width=50):
    """Print a crazy divider line."""
    dividers = [
        lambda: rainbow_text("═" * width),
        lambda: f"{BOLD}{BRIGHT_MAGENTA}{'✦ ' * (width // 2)}{RESET}",
        lambda: gradient_text("━" * width, (255, 0, 0), (0, 0, 255)),
        lambda: f"{BOLD}{BRIGHT_CYAN}{'〜' * (width // 2)}{RESET}",
        lambda: f"{'🔮' * (width // 3)}",
        lambda: fire_text("🔥" + "━" * (width - 2) + "🔥"),
        lambda: f"{BRIGHT_YELLOW}{'⚡' * (width // 2)}{RESET}",
    ]
    print(random.choice(dividers)())

def menu_divider(width=35):
    """Print a menu-style divider."""
    print(gradient_text("─" * width, (255, 100, 0), (0, 200, 255)))

# ═══════════════════════════════════════════
# ASCII ART
# ═══════════════════════════════════════════

POKEBALL_ART = r"""
        ██████████████        
      ██░░░░░░░░░░░░░░██      
    ██░░░░░░░░░░░░░░░░░░██    
  ██░░░░░░░░░░░░░░░░░░░░░░██  
  ██░░░░░░░░░░░░░░░░░░░░░░██  
  ████████████████████████████ 
  ██▓▓▓▓▓▓▓▓██    ██▓▓▓▓▓▓██  
  ██▓▓▓▓▓▓██  ████  ██▓▓▓▓██  
    ██▓▓▓▓██  ████  ██▓▓██    
      ██▓▓▓▓██    ██▓▓██      
        ██████████████        
"""

TITLE_ART = r"""
 ██████╗  ██████╗ ██╗  ██╗███████╗███╗   ███╗ ██████╗ ███╗   ██╗
 ██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝████╗ ████║██╔═══██╗████╗  ██║
 ██████╔╝██║   ██║█████╔╝ █████╗  ██╔████╔██║██║   ██║██╔██╗ ██║
 ██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║
 ██║     ╚██████╔╝██║  ██╗███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
 ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
"""

BATTLE_ART = r"""
     ⚔️  ╔══════════════════════════╗  ⚔️
        ║   ⚡ B A T T L E ! ⚡    ║
     ⚔️  ╚══════════════════════════╝  ⚔️
"""

SHOP_ART = r"""
  ┌─────────────────────────────┐
  │  🏪  P O K É  S H O P  🏪  │
  │    ♦ Buy ♦ Train ♦ Win ♦    │
  └─────────────────────────────┘
"""

HOSPITAL_ART = r"""
  ╔═══════════════════════════════╗
  ║   🏥  P O K É  C E N T E R  ║
  ║      ❤️  Heal Your Team  ❤️   ║
  ╚═══════════════════════════════╝
"""

WIN_ART = r"""
    ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★
    ★                        ★
    ★   🏆  V I C T O R Y ! 🏆  ★
    ★                        ★
    ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★
"""

LOSE_ART = r"""
    ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳
    ╳                        ╳
    ╳   💀  D E F E A T  💀  ╳
    ╳                        ╳
    ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳
"""

CATCH_ART = r"""
    ╔═══════════════════════════╗
    ║  🎉  G O T C H A !  🎉  ║
    ╚═══════════════════════════╝
"""

LEVEL_UP_ART = r"""
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃  🌟 L E V E L  U P ! 🌟  ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

CRIT_ART = r"""
   ╔══════════════════════════════╗
   ║ 💥💥 C R I T I C A L ! 💥💥 ║
   ╚══════════════════════════════╝
"""

def print_title():
    """Print the game title with crazy colors."""
    for line in TITLE_ART.strip().split('\n'):
        print(gradient_text(line, (255, 50, 50), (255, 200, 0)))
    print()
    print(rainbow_text("     ⚡ G O T T A  C A T C H  ' E M  A L L ! ⚡"))
    print()

def print_pokeball():
    """Print the pokeball ASCII art."""
    for line in POKEBALL_ART.strip().split('\n'):
        print(gradient_text(line, (255, 0, 0), (255, 255, 255)))

def print_art(art, style_func=rainbow_text):
    """Print ASCII art with a style function."""
    for line in art.strip().split('\n'):
        print(style_func(line))

# ═══════════════════════════════════════════
# THEMED INPUT PROMPTS
# ═══════════════════════════════════════════

def crazy_input(prompt):
    """A crazy styled input prompt."""
    styled = f"{BOLD}{BRIGHT_CYAN}▸ {rainbow_text(prompt)}{BRIGHT_CYAN} ➤ {RESET}"
    return input(styled)

def crazy_int_input(prompt):
    """A crazy styled integer input prompt."""
    styled = f"{BOLD}{BRIGHT_YELLOW}▸ {rainbow_text(prompt)}{BRIGHT_YELLOW} ➤ {RESET}"
    while True:
        try:
            return int(input(styled))
        except ValueError:
            print(f"  {BOLD}{BRIGHT_RED}❌ Please enter a number!{RESET}")

# ═══════════════════════════════════════════
# SCREEN EFFECTS
# ═══════════════════════════════════════════

def clear_screen():
    """Clear the terminal screen."""
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def screen_flash(color=BG_RED, duration=0.1):
    """Flash the screen with a color."""
    sys.stdout.write(f"{color}{' ' * 80}\n" * 5)
    sys.stdout.flush()
    time.sleep(duration)
    sys.stdout.write(RESET)

def dramatic_pause(seconds=1.0):
    """Add a dramatic pause with dots."""
    for _ in range(3):
        sys.stdout.write(f"{random.choice(ALL_COLORS)}.{RESET}")
        sys.stdout.flush()
        time.sleep(seconds / 3)
    print()

# ═══════════════════════════════════════════
# STAT DISPLAY HELPERS
# ═══════════════════════════════════════════

def stat_label(label, value, color=BRIGHT_WHITE, icon=""):
    """Display a stat with fancy formatting."""
    return f"  {icon} {BOLD}{color}{label}:{RESET} {BOLD}{BRIGHT_YELLOW}{value}{RESET}"

def money_display(amount):
    """Display money with coin emoji and color."""
    return f"{BOLD}{BRIGHT_YELLOW}💰 {amount} coins{RESET}"

def trophy_display(amount):
    """Display trophies with formatting."""
    return f"{BOLD}{BRIGHT_MAGENTA}🏆 {amount} trophies{RESET}"

def pokemon_name_style(name):
    """Style a pokemon name."""
    return f"{BOLD}{BRIGHT_CYAN}{name.upper()}{RESET}"

def enemy_name_style(name):
    """Style an enemy pokemon name."""
    return f"{BOLD}{BRIGHT_RED}{name.upper()}{RESET}"

def player_name_style(name):
    """Style a player name."""
    return gradient_text(name, (255, 215, 0), (255, 100, 0))


# ═══════════════════════════════════════════
# ADVANCED TEXT EFFECTS
# ═══════════════════════════════════════════

def shadow_text(text, shadow_color=(80, 80, 80)):
    """Text with a shadow effect using dim duplicate."""
    shadow = f"{rgb(*shadow_color)}{text}{RESET}"
    main = f"{BOLD}{BRIGHT_WHITE}{text}{RESET}"
    return f"{shadow}\n{main}"

def double_strike_text(text):
    """Double-line bold text for emphasis."""
    top = f"{BOLD}{BRIGHT_WHITE}{text}{RESET}"
    bottom = f"{BOLD}{UNDERLINE}{BRIGHT_YELLOW}{text}{RESET}"
    return f"{top}\n{bottom}"

def morse_style_text(text):
    """Make text look like morse code dots and dashes."""
    morse_map = {
        'a': '·−', 'b': '−···', 'c': '−·−·', 'd': '−··', 'e': '·',
        'f': '··−·', 'g': '−−·', 'h': '····', 'i': '··', 'j': '·−−−',
        'k': '−·−', 'l': '·−··', 'm': '−−', 'n': '−·', 'o': '−−−',
        'p': '·−−·', 'q': '−−·−', 'r': '·−·', 's': '···', 't': '−',
        'u': '··−', 'v': '···−', 'w': '·−−', 'x': '−··−', 'y': '−·−−',
        'z': '−−··', ' ': '   '
    }
    result = ""
    for char in text.lower():
        morse = morse_map.get(char, char)
        result += f"{random.choice(ALL_COLORS)}{morse}{RESET} "
    return result

def hacker_text(text):
    """Green-on-black hacker movie style text."""
    return f"{BOLD}{rgb(0, 255, 0)}{bg_rgb(0, 0, 0)} {text} {RESET}"

def vaporwave_text(text):
    """V A P O R W A V E  aesthetic text."""
    spaced = "  ".join(text.upper())
    result = ""
    colors = [(255, 100, 200), (100, 200, 255), (200, 100, 255), (100, 255, 200)]
    for i, char in enumerate(spaced):
        if char == " ":
            result += char
        else:
            r, g, b = colors[i % len(colors)]
            result += f"{ITALIC}{rgb(r, g, b)}{char}{RESET}"
    return result

def pixel_text(text):
    """Make text look pixelated with block characters."""
    pixel_chars = "▀▁▂▃▄▅▆▇█▉▊▋▌▍▎▏"
    result = ""
    for char in text:
        if char == " ":
            result += "  "
        else:
            result += f"{random.choice(ALL_COLORS)}{random.choice(pixel_chars)}{char}{RESET}"
    return result

def zalgo_text(text, intensity=2):
    """Add zalgo/corrupted unicode combining characters."""
    zalgo_up = ['̍', '̎', '̄', '̅', '̿', '̑', '̆', '̐', '͒', '͗', '͑', '̇', '̈', '̊', '͂', '̓', '̈́', '͊', '͋', '͌']
    zalgo_mid = ['̕', '̛', '̀', '́', '͘', '̡', '̢', '̧', '̨', '̴', '̵', '̶', '͏', '͜', '͝', '͞', '͟', '͠', '͢']
    zalgo_down = ['̖', '̗', '̘', '̙', '̜', '̝', '̞', '̟', '̠', '̤', '̥', '̦', '̩', '̪', '̫', '̬', '̭', '̮', '̯', '̰', '̱']
    result = ""
    for char in text:
        if char == " ":
            result += char
            continue
        result += f"{random.choice(ALL_COLORS)}{char}"
        for _ in range(random.randint(0, intensity)):
            result += random.choice(zalgo_up)
        for _ in range(random.randint(0, intensity)):
            result += random.choice(zalgo_mid)
        for _ in range(random.randint(0, intensity)):
            result += random.choice(zalgo_down)
        result += RESET
    return result

def retro_text(text):
    """Retro 80s neon style text."""
    neon_colors = [(255, 0, 128), (0, 255, 255), (255, 255, 0), (255, 0, 255), (0, 255, 128)]
    result = ""
    for i, char in enumerate(text):
        if char == " ":
            result += char
        else:
            r, g, b = neon_colors[i % len(neon_colors)]
            result += f"{BOLD}{rgb(r, g, b)}{char}{RESET}"
    return result

def blood_text(text):
    """Dripping blood horror text."""
    drips = "̤̤̖̗̘̙̈̈"
    result = ""
    for char in text:
        if char == " ":
            result += char
        else:
            result += f"{BOLD}{rgb(180, 0, 0)}{char}"
            if random.random() < 0.3:
                result += random.choice(['̤', '̖', '̗'])
            result += RESET
    return result

def ice_text(text):
    """Frozen ice crystal text."""
    ice_colors = [(200, 230, 255), (150, 200, 255), (100, 180, 255), (180, 220, 255)]
    result = ""
    for i, char in enumerate(text):
        if char == " ":
            result += char
        else:
            r, g, b = ice_colors[i % len(ice_colors)]
            result += f"{BOLD}{rgb(r, g, b)}{char}{RESET}"
    return result

def gold_text(text):
    """Shiny gold text."""
    gold_colors = [(255, 215, 0), (255, 200, 0), (255, 230, 50), (200, 170, 0), (255, 245, 100)]
    result = ""
    for i, char in enumerate(text):
        if char == " ":
            result += char
        else:
            r, g, b = gold_colors[i % len(gold_colors)]
            result += f"{BOLD}{rgb(r, g, b)}{char}{RESET}"
    return result

def shadow_box(text, width=None):
    """Box with shadow effect."""
    lines = text.split('\n') if '\n' in text else [text]
    if width is None:
        width = max(len(line) for line in lines) + 4

    print(f"  {BOLD}{BRIGHT_WHITE}┌{'─' * width}┐{RESET}")
    for line in lines:
        padding = width - len(line) - 2
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"  {BOLD}{BRIGHT_WHITE}│{RESET} {' ' * left_pad}{rainbow_text(line)}{' ' * right_pad} {BOLD}{BRIGHT_WHITE}│{RESET}{DIM}░{RESET}")
    print(f"  {BOLD}{BRIGHT_WHITE}└{'─' * width}┘{RESET}{DIM}░{RESET}")
    print(f"   {DIM}{'░' * (width + 2)}{RESET}")

def double_box(text, width=None, inner_color=BRIGHT_CYAN, outer_color=BRIGHT_YELLOW):
    """Double-bordered box."""
    lines = text.split('\n') if '\n' in text else [text]
    if width is None:
        width = max(len(line) for line in lines) + 8

    inner_width = width - 4
    print(f"  {outer_color}{BOLD}╔{'═' * width}╗{RESET}")
    print(f"  {outer_color}{BOLD}║{RESET}  {inner_color}{BOLD}┌{'─' * inner_width}┐{RESET}  {outer_color}{BOLD}║{RESET}")
    for line in lines:
        padding = inner_width - len(line) - 2
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"  {outer_color}{BOLD}║{RESET}  {inner_color}{BOLD}│{RESET} {' ' * left_pad}{rainbow_text(line)}{' ' * right_pad} {inner_color}{BOLD}│{RESET}  {outer_color}{BOLD}║{RESET}")
    print(f"  {outer_color}{BOLD}║{RESET}  {inner_color}{BOLD}└{'─' * inner_width}┘{RESET}  {outer_color}{BOLD}║{RESET}")
    print(f"  {outer_color}{BOLD}╚{'═' * width}╝{RESET}")

def rounded_box(text, width=None, color=BRIGHT_MAGENTA):
    """Box with rounded corners."""
    lines = text.split('\n') if '\n' in text else [text]
    if width is None:
        width = max(len(line) for line in lines) + 4

    print(f"  {color}{BOLD}╭{'─' * width}╮{RESET}")
    for line in lines:
        padding = width - len(line) - 2
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"  {color}{BOLD}│{RESET} {' ' * left_pad}{rainbow_text(line)}{' ' * right_pad} {color}{BOLD}│{RESET}")
    print(f"  {color}{BOLD}╰{'─' * width}╯{RESET}")

def dashed_box(text, width=None, color=BRIGHT_GREEN):
    """Box with dashed borders."""
    lines = text.split('\n') if '\n' in text else [text]
    if width is None:
        width = max(len(line) for line in lines) + 4

    dash = "┄" * width
    print(f"  {color}{BOLD}┌{dash}┐{RESET}")
    for line in lines:
        padding = width - len(line) - 2
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"  {color}{BOLD}┊{RESET} {' ' * left_pad}{rainbow_text(line)}{' ' * right_pad} {color}{BOLD}┊{RESET}")
    print(f"  {color}{BOLD}└{dash}┘{RESET}")

def water_box(text, width=None):
    """Water-themed box."""
    lines = text.split('\n') if '\n' in text else [text]
    if width is None:
        width = max(len(line) for line in lines) + 4

    wave = "~" * width
    print(f"  {BOLD}{BRIGHT_BLUE}💧{wave}💧{RESET}")
    for line in lines:
        padding = width - len(line) - 2
        left_pad = padding // 2
        right_pad = padding - left_pad
        inner = gradient_text(line, (0, 100, 255), (0, 200, 255))
        print(f"  {BOLD}{BRIGHT_BLUE}💧{RESET} {' ' * left_pad}{inner}{' ' * right_pad} {BOLD}{BRIGHT_BLUE}💧{RESET}")
    print(f"  {BOLD}{BRIGHT_BLUE}💧{wave}💧{RESET}")

def grass_box(text, width=None):
    """Grass-themed box."""
    lines = text.split('\n') if '\n' in text else [text]
    if width is None:
        width = max(len(line) for line in lines) + 4

    vine = "~" * width
    print(f"  {BOLD}{BRIGHT_GREEN}🌿{vine}🌿{RESET}")
    for line in lines:
        padding = width - len(line) - 2
        left_pad = padding // 2
        right_pad = padding - left_pad
        inner = gradient_text(line, (0, 200, 0), (100, 255, 100))
        print(f"  {BOLD}{BRIGHT_GREEN}🌿{RESET} {' ' * left_pad}{inner}{' ' * right_pad} {BOLD}{BRIGHT_GREEN}🌿{RESET}")
    print(f"  {BOLD}{BRIGHT_GREEN}🌿{vine}🌿{RESET}")

# ═══════════════════════════════════════════
# TABLE DRAWING
# ═══════════════════════════════════════════

def draw_table(headers, rows, color=BRIGHT_CYAN):
    """Draw a formatted table with headers and rows."""
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    # Top border
    border_parts = ["─" * (w + 2) for w in col_widths]
    print(f"  {color}{BOLD}┌{'┬'.join(border_parts)}┐{RESET}")

    # Header
    header_parts = []
    for i, h in enumerate(headers):
        header_parts.append(f" {BOLD}{BRIGHT_YELLOW}{h:<{col_widths[i]}}{RESET} ")
    print(f"  {color}{BOLD}│{RESET}{'│'.join(header_parts)}{color}{BOLD}│{RESET}")

    # Header separator
    print(f"  {color}{BOLD}├{'┼'.join(border_parts)}┤{RESET}")

    # Rows
    for row in rows:
        row_parts = []
        for i, cell in enumerate(row):
            cell_str = str(cell)
            row_parts.append(f" {BRIGHT_WHITE}{cell_str:<{col_widths[i]}}{RESET} ")
        print(f"  {color}{BOLD}│{RESET}{'│'.join(row_parts)}{color}{BOLD}│{RESET}")

    # Bottom border
    print(f"  {color}{BOLD}└{'┴'.join(border_parts)}┘{RESET}")

# ═══════════════════════════════════════════
# BANNER GENERATORS
# ═══════════════════════════════════════════

def banner(text, style="stars", width=50):
    """Generate different style banners."""
    pad_total = width - len(text) - 4
    left_pad = pad_total // 2
    right_pad = pad_total - left_pad

    if style == "stars":
        border = "★ " * (width // 2)
        print(f"  {BRIGHT_YELLOW}{border}{RESET}")
        print(f"  {BRIGHT_YELLOW}★{RESET}{' ' * left_pad} {rainbow_text(text)} {' ' * right_pad}{BRIGHT_YELLOW}★{RESET}")
        print(f"  {BRIGHT_YELLOW}{border}{RESET}")
    elif style == "fire":
        border = "🔥" * (width // 3)
        print(f"  {border}")
        print(f"  🔥{' ' * left_pad} {fire_text(text)} {' ' * right_pad}🔥")
        print(f"  {border}")
    elif style == "electric":
        border = "⚡" * (width // 2)
        print(f"  {BRIGHT_YELLOW}{border}{RESET}")
        print(f"  ⚡{' ' * left_pad} {electric_text(text)} {' ' * right_pad}⚡")
        print(f"  {BRIGHT_YELLOW}{border}{RESET}")
    elif style == "diamond":
        border = "💎 " * (width // 3)
        print(f"  {border}")
        print(f"  💎{' ' * left_pad} {gradient_text(text, (100, 200, 255), (200, 100, 255))} {' ' * right_pad}💎")
        print(f"  {border}")
    elif style == "skull":
        border = "💀 " * (width // 3)
        print(f"  {border}")
        print(f"  💀{' ' * left_pad} {blood_text(text)} {' ' * right_pad}💀")
        print(f"  {border}")

def mega_banner(text, width=55):
    """The ULTIMATE banner with multiple border layers."""
    print()
    print(f"  {gradient_text('█' * width, (255, 0, 0), (0, 0, 255))}")
    print(f"  {gradient_text('█' * width, (255, 50, 0), (0, 50, 255))}")
    pad_total = width - len(text) - 4
    left_pad = pad_total // 2
    right_pad = pad_total - left_pad
    inner = f"  {BOLD}{BRIGHT_WHITE}{BG_RED}{'█' * 2}{RESET}{' ' * left_pad} {crazy_text(text)} {' ' * right_pad}{BOLD}{BRIGHT_WHITE}{BG_RED}{'█' * 2}{RESET}"
    print(inner)
    print(f"  {gradient_text('█' * width, (0, 50, 255), (255, 50, 0))}")
    print(f"  {gradient_text('█' * width, (0, 0, 255), (255, 0, 0))}")
    print()

# ═══════════════════════════════════════════
# ANIMATED TEXT DISPLAYS
# ═══════════════════════════════════════════

def bouncing_text(text, bounces=3, delay=0.1):
    """Text that bounces with indentation."""
    heights = [0, 2, 4, 6, 4, 2, 0]
    for _ in range(bounces):
        for h in heights:
            indent = " " * h
            sys.stdout.write(f"\r  {indent}{random.choice(ALL_COLORS)}{BOLD}{text}{RESET}{' ' * 20}")
            sys.stdout.flush()
            time.sleep(delay)
    print()

def pulsing_text(text, pulses=3, delay=0.15):
    """Text that pulses between bright and dim."""
    for _ in range(pulses):
        sys.stdout.write(f"\r  {DIM}{text}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write(f"\r  {BOLD}{BRIGHT_WHITE}{text}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write(f"\r  {BOLD}{BRIGHT_YELLOW}{text}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def text_explosion(text, delay=0.05):
    """Characters explode outward from center."""
    mid = len(text) // 2
    for radius in range(mid + 1):
        display = list(" " * len(text))
        for i in range(len(text)):
            dist = abs(i - mid)
            if dist <= radius:
                display[i] = text[i]
        line = "".join(display)
        sys.stdout.write(f"\r  {rainbow_text(line)}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def scroll_text(text, width=40, speed=0.05):
    """Scrolling marquee text effect."""
    padded = " " * width + text + " " * width
    for i in range(len(padded) - width):
        window = padded[i:i + width]
        sys.stdout.write(f"\r  {gradient_text(window, (255, 0, 100), (0, 100, 255))}")
        sys.stdout.flush()
        time.sleep(speed)
    print()

def typing_with_cursor(text, delay=0.04):
    """Typewriter with blinking cursor."""
    for i in range(len(text)):
        sys.stdout.write(f"\r  {BRIGHT_GREEN}{text[:i+1]}{BLINK}▋{RESET}{' ' * 5}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(f"\r  {BRIGHT_GREEN}{text}{RESET}{' ' * 5}\n")

# ═══════════════════════════════════════════
# EXTRA DIVIDER STYLES
# ═══════════════════════════════════════════

def wave_divider(width=50):
    """Wavy divider line."""
    wave = ""
    for i in range(width):
        chars = "∿∿∼∼"
        wave += f"{random.choice(ALL_COLORS)}{chars[i % len(chars)]}{RESET}"
    print(f"  {wave}")

def star_divider(width=50):
    """Star-filled divider."""
    stars = ["⭐", "🌟", "✨", "💫", "✴️"]
    line = ""
    for _ in range(width // 3):
        line += random.choice(stars)
    print(f"  {line}")

def arrow_divider(width=50, direction="right"):
    """Arrow-style divider."""
    if direction == "right":
        arrow = "►" * (width // 2)
    else:
        arrow = "◄" * (width // 2)
    print(f"  {gradient_text(arrow, (255, 100, 0), (0, 200, 255))}")

def dot_divider(width=50):
    """Dotted divider with varying sizes."""
    dots = "·•●⬤●•·"
    line = ""
    for i in range(width):
        line += f"{random.choice(ALL_COLORS)}{dots[i % len(dots)]}{RESET}"
    print(f"  {line}")

def rainbow_divider(width=50):
    """Full rainbow gradient divider."""
    print(f"  {gradient_text('━' * width, (255, 0, 0), (148, 0, 211))}")

def zigzag_divider(width=50):
    """Zigzag pattern divider."""
    zag = ""
    for i in range(width):
        if i % 4 < 2:
            zag += f"{random.choice(ALL_COLORS)}╱{RESET}"
        else:
            zag += f"{random.choice(ALL_COLORS)}╲{RESET}"
    print(f"  {zag}")

def emoji_divider(width=50, theme="pokemon"):
    """Themed emoji divider."""
    themes = {
        "pokemon": ["⚡", "🔥", "💧", "🌿", "🐾", "⭐", "💎", "🏆"],
        "battle": ["⚔️", "🛡️", "💥", "⚡", "🔥", "💀", "👊", "🎯"],
        "nature": ["🌿", "🌺", "🌸", "🌼", "🌻", "🌹", "🌷", "🍀"],
        "space": ["🌟", "⭐", "🌙", "☀️", "🪐", "🌌", "✨", "💫"],
    }
    emojis = themes.get(theme, themes["pokemon"])
    line = ""
    for _ in range(width // 3):
        line += random.choice(emojis)
    print(f"  {line}")


# ═══════════════════════════════════════════
# DYNAMIC THEME WRAPPERS
# ═══════════════════════════════════════════

def get_theme_color():
    """Get the primary color for the current theme."""
    theme = GAME_SETTINGS.get("theme")
    if theme == "fire": return BRIGHT_RED
    if theme == "water": return BRIGHT_BLUE
    if theme == "grass": return BRIGHT_GREEN
    if theme == "electric": return BRIGHT_YELLOW
    if theme == "psychic": return BRIGHT_MAGENTA
    if theme == "hacker": return "\033[38;2;0;255;0m" # rgb(0,255,0)
    if theme == "blood": return "\033[38;2;180;0;0m"
    if theme == "gold": return "\033[38;2;255;215;0m"
    if theme == "ice": return "\033[38;2;150;200;255m"
    if theme == "dark": return DIM + WHITE
    if theme == "cyberpunk": return "\033[38;2;255;0;255m" # hot magenta
    if theme == "synthwave": return "\033[38;2;255;100;0m"  # neon orange
    if theme == "sakura": return "\033[38;2;255;182;193m" # cherry pink
    if theme == "obsidian": return "\033[38;2;50;50;50m"   # charcoal
    if theme == "steampunk": return "\033[38;2;212;175;55m" # bronze/gold
    if theme == "aurora": return "\033[38;2;0;255;150m"    # aurora green
    if theme == "blizzard": return "\033[38;2;200;230;255m" # ice blue
    if theme == "emerald": return "\033[38;2;0;200;100m"   # deep emerald
    if theme == "ruby": return "\033[38;2;220;20;60m"      # ruby red
    if theme == "sapphire": return "\033[38;2;15;82;186m"   # sapphire blue
    if theme == "crystal": return "\033[38;2;224;255;255m" # crystal cyan
    if theme == "galaxy": return "\033[38;2;75;0;130m"     # indigo
    return BRIGHT_CYAN # default fallback

def theme_text(text):
    """Apply the currently selected text theme effect."""
    theme = GAME_SETTINGS.get("theme")
    if theme == "rainbow": return rainbow_text(text)
    if theme == "fire": return fire_text(text)
    if theme == "water": return gradient_text(text, (0, 100, 255), (0, 200, 255))
    if theme == "grass": return gradient_text(text, (0, 200, 0), (100, 255, 100))
    if theme == "electric": return electric_text(text)
    if theme == "psychic": return psychic_text(text)
    if theme == "hacker": return hacker_text(text)
    if theme == "vaporwave": return vaporwave_text(text)
    if theme == "gold": return gold_text(text)
    if theme == "blood": return blood_text(text)
    if theme == "ice": return ice_text(text)
    if theme == "retro": return retro_text(text)
    if theme == "dark": return shadow_text(text)
    if theme == "cyberpunk": return gradient_text(text, (255, 0, 128), (0, 255, 255))
    if theme == "synthwave": return gradient_text(text, (255, 100, 0), (128, 0, 255))
    if theme == "sakura": return gradient_text(text, (255, 182, 193), (255, 255, 255))
    if theme == "obsidian": return gradient_text(text, (30, 30, 30), (150, 0, 255))
    if theme == "steampunk": return gradient_text(text, (200, 120, 50), (255, 215, 0))
    if theme == "aurora": return gradient_text(text, (0, 255, 150), (0, 100, 255))
    if theme == "blizzard": return gradient_text(text, (150, 200, 255), (255, 255, 255))
    if theme == "emerald": return gradient_text(text, (0, 150, 50), (100, 255, 150))
    if theme == "ruby": return gradient_text(text, (150, 0, 0), (255, 100, 100))
    if theme == "sapphire": return gradient_text(text, (0, 50, 200), (0, 200, 255))
    if theme == "crystal": return gradient_text(text, (224, 255, 255), (255, 215, 0))
    if theme == "galaxy": return gradient_text(text, (130, 0, 250), (255, 100, 150))
    return rainbow_text(text)

def theme_box(text, width=None):
    """Draw a box using the currently selected border style."""
    style = GAME_SETTINGS.get("border_style")
    if style == "crazy": return crazy_box(text, width=width)
    if style == "fire": return fire_box(text, width=width)
    if style == "electric": return electric_box(text, width=width)
    if style == "shadow": return shadow_box(text, width=width)
    if style == "double": return double_box(text, width=width)
    if style == "rounded": return rounded_box(text, width=width)
    if style == "dashed": return dashed_box(text, width=width)
    if style == "water": return water_box(text, width=width)
    if style == "grass": return grass_box(text, width=width)
    # Map additional premium box widgets dynamically from ultra_mega_ui if matching
    try:
        if style.startswith("box_"):
            box_num = int(style.split("_")[1])
            # Call programmatically from ultra_mega_ui
            return globals()[f"gradient_box_{box_num}"](text, width=width or 50)
    except:
        pass
    return crazy_box(text, width=width)

def theme_divider(width=50):
    """Draw a divider using the currently selected border style."""
    style = GAME_SETTINGS.get("border_style")
    if style == "crazy": return crazy_divider(width)
    if style == "fire": print(fire_text("🔥" + "━" * (width - 2) + "🔥")); return
    if style == "electric": print(f"{BRIGHT_YELLOW}{'⚡' * (width // 2)}{RESET}"); return
    if style == "shadow": return dot_divider(width)
    if style == "double": return rainbow_divider(width)
    if style == "rounded": return wave_divider(width)
    if style == "dashed": return zigzag_divider(width)
    if style == "water": return wave_divider(width)
    if style == "grass": return emoji_divider(width, theme="nature")
    return crazy_divider(width)

def theme_print(text, delay=None):
    """Print text using the selected reveal animation."""
    style = GAME_SETTINGS.get("text_reveal_style")
    
    # Calculate effective delay
    base_delay = delay if delay is not None else 0.03
    effective_delay = base_delay * GAME_SETTINGS.get("animation_speed")
    
    if effective_delay == 0:
        print(f"  {theme_text(text)}")
        return
        
    if style == "typewriter":
        typewriter(f"  {text}", delay=effective_delay)
    elif style == "dramatic":
        dramatic_print(f"  {text}", delay=effective_delay)
    elif style == "slow_reveal":
        slow_reveal(f"  {text}", style_func=theme_text, delay=effective_delay)
    elif style == "glitch":
        print(f"  {glitch_text(text)}")
        time.sleep(effective_delay * 10) # Pause after showing glitch
    elif style == "typing_cursor":
        typing_with_cursor(text, delay=effective_delay)
    else:
        print(f"  {theme_text(text)}")

# Dynamic layout multi-pane panel renderer
def render_panel_grid(panels, width=80):
    """Render multiple text panels side-by-side inside styled boxes."""
    if not panels: return
    num_panels = len(panels)
    col_width = (width - (num_panels * 2)) // num_panels
    
    lines_per_panel = []
    max_lines = 0
    for p in panels:
        p_lines = p.split("\n")
        lines_per_panel.append(p_lines)
        max_lines = max(max_lines, len(p_lines))
        
    border_color = get_theme_color()
    top_border = f"  {border_color}" + " ┌" + "─"*col_width + "┐ " * num_panels + RESET
    print(top_border)
    
    for r in range(max_lines):
        row_str = "  "
        for p_idx in range(num_panels):
            p_lines = lines_per_panel[p_idx]
            cell_content = p_lines[r] if r < len(p_lines) else ""
            display_text = cell_content[:col_width].ljust(col_width)
            row_str += f"{border_color}│{RESET} {display_text} {border_color}│{RESET} "
        print(row_str)
        
    bot_border = f"  {border_color}" + " └" + "─"*col_width + "┘ " * num_panels + RESET
    print(bot_border)

# Expose everything from ultra_mega_ui at the very end of crazy_style to prevent circular import issues
from ultra_mega_ui import *
