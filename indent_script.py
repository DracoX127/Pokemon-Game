"""
Legacy helper for wrapping the main loop in a crash-save try/except block.

This is not used by the game at runtime. It is kept runnable, but guarded so
importing the module cannot rewrite main.py by accident.
"""


def apply_try_wrapper():
    with open("main.py", "r") as f:
        lines = f.readlines()

    new_lines = []
    for i, line in enumerate(lines):
        if 198 <= i <= 536:  # Indices for lines 199 to 537
            if i == 198:
                new_lines.append("try:\n")
            new_lines.append("    " + line if line.strip() else line)
        else:
            new_lines.append(line)

    except_block = """
except Exception as e:
    print()
    print_art(SAVING_ART, lambda t: glitch_text(t))
    print(f"  {BOLD}{BRIGHT_RED}⚠️ CRASH DETECTED! ⚠️{RESET}")
    print(f"  {DIM}Error: {e}{RESET}")
    print()
    ans = crazy_input("Would you like to save your game before closing? (y/n)")
    if ans.lower() == 'y':
        if save_game(name, pokemon, money, trophies, inventory, location, badges, tower_record, pokedex_seen, pokedex_caught):
            print(f"  {BOLD}{BRIGHT_GREEN}✅ Game saved successfully!{RESET}")
        else:
            print(f"  {BOLD}{BRIGHT_RED}❌ Failed to save!{RESET}")
    sys.exit(1)

"""

    new_lines.insert(538, except_block)

    with open("main.py", "w") as f:
        f.writelines(new_lines)


if __name__ == "__main__":
    apply_try_wrapper()
