"""Battle Log: message queuing, turn tracking, and scrollable history."""

import sys
from crazy_style import (
    RESET, BOLD, DIM, BRIGHT_WHITE, BRIGHT_CYAN, BRIGHT_YELLOW,
    BRIGHT_GREEN, BRIGHT_RED, BRIGHT_MAGENTA,
    crazy_input, clear_screen
)


class BattleLog:
    """Collects battle messages and provides a scrollable history view."""

    def __init__(self):
        self.messages = []
        self.turn = 0

    def next_turn(self):
        self.turn += 1
        msg = f"[Turn {self.turn}] {'─' * 40}"
        self.messages.append(msg)

    def add(self, msg, style=None):
        if style:
            self.messages.append(f"{style}{msg}{RESET}")
        else:
            self.messages.append(msg)

    def log(self, msg, style=None):
        if style:
            styled = f"{style}{msg}{RESET}"
            self.messages.append(styled)
            print(styled)
        else:
            self.messages.append(msg)
            print(msg)

    def add_separator(self):
        self.messages.append(f"  {DIM}{'·' * 50}{RESET}")

    def get_recent(self, count=4):
        return self.messages[-count:] if self.messages else []

    def show_history(self, per_page=15):
        offset = len(self.messages)
        while offset > 0:
            clear_screen()
            start = max(0, offset - per_page)
            page = self.messages[start:offset]
            print(f"  {BOLD}{BRIGHT_WHITE}═══ BATTLE HISTORY (Turn {self.turn}) ═══{RESET}\n")
            for msg in page:
                if msg.startswith("[Turn"):
                    print(f"  {BOLD}{BRIGHT_CYAN}{msg}{RESET}")
                else:
                    print(f"  {msg}")
            print(f"\n  {DIM}Showing {start+1}–{offset} of {len(self.messages)}{RESET}")
            r = crazy_input("  [N]ext / [P]rev / [Q]uit: ").lower()
            if r == "n":
                offset = start
            elif r == "p":
                offset = min(len(self.messages), offset + per_page)
            else:
                break
        clear_screen()

    def clear(self):
        self.messages.clear()
        self.turn = 0


battle_log = BattleLog()
