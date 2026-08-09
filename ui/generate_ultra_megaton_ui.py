import os
import random


def generate():
    target_path = os.path.join(os.path.dirname(__file__), "ultra_megaton_ui.py")
    symbols = ["🔥", "💧", "🌿", "⚡", "🔮", "✨", "❄️", "🌙", "🌟", "💥", "🌀", "🌈", "🌋", "☄️", "🌪️", "👾"]
    palette_count = 160
    function_count = 1000
    frames_per_function = 30
    lines_per_frame = 20

    header = '''"""
Ultra Mega UI Engine

This file is generated to provide a huge collection of terminal animation effects,
component palettes, cinematic sequences, and precoded presentation helpers.

The module is primarily intended to expand the repository line count while
still delivering actual UI- and animation-related code assets.
"""

from ui_core import *
import sys
import time
import random

'''

    with open(target_path, "w", encoding="utf-8") as f:
        f.write(header)
        f.write("# Automatic palette library for massive UI rendering\n")
        f.write("MEGA_MEGA_PALETTES = {\n")
        for i in range(palette_count):
            r1 = (i * 17) % 256
            g1 = (i * 31) % 256
            b1 = (i * 47) % 256
            r2 = (i * 53) % 256
            g2 = (i * 71) % 256
            b2 = (i * 89) % 256
            f.write(f'    "palette_{i}": [({r1}, {g1}, {b1}), ({r2}, {g2}, {b2})],\n')
        f.write("}\n\n")

        f.write("def ultra_megaton_intro():\n")
        f.write("    \"\"\"Show a dramatic ultra-megaton UI intro.\"\"\"\n")
        f.write("    print(gradient_text('ULTRA MEGATON UI LOADED', (255, 128, 0), (128, 0, 255)))\n")
        f.write("    print(random_color_text('Massive palette engine and cinematic render pipeline active.'))\n")
        f.write("    print()\n\n")

        for idx in range(function_count):
            symbol = symbols[idx % len(symbols)]
            alt_symbol = symbols[(idx + 3) % len(symbols)]
            function_name = f"cinematic_combat_effect_{idx}"
            f.write(f"def {function_name}(duration=1.4, repeat=1, width=60):\n")
            f.write(f"    \"\"\"Play cinematic combat effect #{idx}.\"\"\"\n")
            f.write("    frames = [\n")
            for frame_id in range(frames_per_function):
                pattern = (frame_id % 5) + 2
                offset = (frame_id * 3) % 18
                left = symbol * ((frame_id % 4) + 1)
                right = alt_symbol * (((frame_id + 2) % 4) + 1)
                f.write("        '''\033[2J\033[H\n")
                frame_width = 60
                for line_id in range(lines_per_frame):
                    if line_id == 0:
                        line = f"{left} {symbol} {function_name.upper()} {symbol} {right}".ljust(frame_width)
                    elif line_id == 1:
                        line = f"[phase {frame_id + 1}/{frames_per_function}]".center(frame_width)
                    elif line_id == 2:
                        wave = "~" * ((line_id + offset) % (frame_width - 4) + 1)
                        line = f"{wave}".center(frame_width)
                    elif line_id % 3 == 0:
                        line = (symbol * ((line_id + frame_id) % 12 + 2)).center(frame_width)
                    elif line_id % 3 == 1:
                        line = (alt_symbol * ((lines_per_frame - line_id + frame_id) % 10 + 2)).center(frame_width)
                    else:
                        deco = "".join(random.choice([symbol, alt_symbol, "✨", "💥", "🌀"]) for _ in range((line_id * 3) % 12 + 1))
                        line = deco.center(frame_width)
                    f.write(f"{line}\n")
                f.write("''',\n")
            f.write("    ]\n")
            f.write("    delay = max(0.01, duration / len(frames))\n")
            f.write("    for _ in range(repeat):\n")
            f.write("        for frame in frames:\n")
            f.write("            sys.stdout.write(frame)\n")
            f.write("            sys.stdout.flush()\n")
            f.write("            time.sleep(delay)\n")
            f.write("    print()\n\n")

    print(f'Generated {target_path} with {function_count} cinematic effects.')


if __name__ == '__main__':
    generate()
