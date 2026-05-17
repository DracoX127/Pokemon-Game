"""Quest Manager: tracking, progress updates, menu display for 10,000 quests."""

import random
from quest_system import QUESTS
from crazy_style import (
    RESET, BOLD, DIM, BRIGHT_WHITE, BRIGHT_CYAN, BRIGHT_YELLOW,
    BRIGHT_GREEN, BRIGHT_RED, BRIGHT_MAGENTA,
    crazy_input, crazy_int_input, clear_screen
)
from animations import fancy_header
from animations import fancy_header
from animations import fancy_header

DIFFICULTY_COLORS = {"easy": BRIGHT_GREEN, "medium": BRIGHT_YELLOW, "hard": BRIGHT_RED, "expert": BRIGHT_MAGENTA}


class QuestManager:
    def __init__(self):
        self.active = {}
        self.completed = set()
        self.progress = {}

    def assign(self, quest_id):
        if quest_id in self.completed:
            return False
        for q in QUESTS:
            if q["id"] == quest_id:
                self.active[quest_id] = q
                self.progress[quest_id] = 0
                return True
        return False

    def progress_for(self, quest_id, amount=1):
        if quest_id not in self.active:
            return False
        new_val = self.progress.get(quest_id, 0) + amount
        self.progress[quest_id] = new_val
        q = self.active[quest_id]
        if new_val >= q["count"]:
            self.complete(quest_id)
            return "complete"
        return "progress"

    def complete(self, quest_id):
        if quest_id in self.active:
            reward = self.active[quest_id]["reward"]
            self.completed.add(quest_id)
            del self.active[quest_id]
            if quest_id in self.progress:
                del self.progress[quest_id]
            return reward
        return None

    def hook_catch(self, poke_type, name):
        results = []
        for qid in list(self.active.keys()):
            q = self.active[qid]
            if q["type"] == "Catch" and (q["target"] == poke_type or q["target"].lower() in name.lower()):
                result = self.progress_for(qid)
                if result == "complete":
                    results.append((qid, q))
        return results

    def hook_defeat(self, poke_type, name):
        results = []
        for qid in list(self.active.keys()):
            q = self.active[qid]
            if q["type"] == "Defeat" and (q["target"] == poke_type or q["target"].lower() in name.lower()):
                result = self.progress_for(qid)
                if result == "complete":
                    results.append((qid, q))
        return results

    def hook_explore(self, region):
        results = []
        for qid in list(self.active.keys()):
            q = self.active[qid]
            if q["type"] == "Explore" and q["target"] == region:
                result = self.progress_for(qid)
                if result == "complete":
                    results.append((qid, q))
        return results

    def hook_evolve(self, poke_type, name):
        results = []
        for qid in list(self.active.keys()):
            q = self.active[qid]
            if q["type"] == "Evolve" and (q["target"] == poke_type or q["target"].lower() in name.lower()):
                result = self.progress_for(qid)
                if result == "complete":
                    results.append((qid, q))
        return results

    def hook_fuse(self, count=1):
        results = []
        for qid in list(self.active.keys()):
            q = self.active[qid]
            if q["type"] == "Fuse":
                result = self.progress_for(qid, count)
                if result == "complete":
                    results.append((qid, q))
        return results

    def hook_battle_win(self, arena_type="wild"):
        results = []
        for qid in list(self.active.keys()):
            q = self.active[qid]
            if q["type"] == "Battle":
                result = self.progress_for(qid)
                if result == "complete":
                    results.append((qid, q))
        return results

    def hook_tower(self, round_num):
        results = []
        for qid in list(self.active.keys()):
            q = self.active[qid]
            if q["type"] == "Tower" and round_num >= q["count"]:
                result = self.progress_for(qid)
                if result == "complete":
                    results.append((qid, q))
        return results

    def hook_train(self, poke_type, level):
        results = []
        for qid in list(self.active.keys()):
            q = self.active[qid]
            if q["type"] == "Train" and q["target"] == poke_type and level >= q["count"]:
                result = self.progress_for(qid)
                if result == "complete":
                    results.append((qid, q))
        return results

    def get_available(self, count=5):
        pool = [q for q in QUESTS if q["id"] not in self.completed and q["id"] not in self.active]
        random.shuffle(pool)
        return pool[:count]

    def get_display_line(self, qid):
        q = self.active.get(qid)
        if not q:
            q = next((x for x in QUESTS if x["id"] == qid), None)
        if not q:
            return ""
        prog = self.progress.get(qid, 0)
        color = DIFFICULTY_COLORS.get(q["difficulty"], BRIGHT_WHITE)
        status = f"{prog}/{q['count']}" if qid in self.active else "✓"
        return f"  {color}[{q['difficulty'][0].upper()}]{RESET} #{q['id']:>5} {q['type']:8} {q['objective'][:40]:40} {status}"

    def show_menu(self, player_money=0, player_trophies=0):
        while True:
            clear_screen()
            fancy_header("QUEST BOARD", "📋", 50)
            avail = self.get_available(5)
            print(f"\n  {BOLD}{BRIGHT_CYAN}Available Quests:{RESET}")
            for q in avail:
                c = DIFFICULTY_COLORS.get(q["difficulty"], BRIGHT_WHITE)
                print(f"  {c}[{q['difficulty'][0].upper()}]{RESET} {BOLD}{q['id']}.{RESET} {q['type']:8} {q['objective'][:50]}")
                print(f"       🌟 {q['giver']}  🎁 {q['reward_desc']:30}  🌍 {q['region']}")
            if self.active:
                print(f"\n  {BOLD}{BRIGHT_YELLOW}Active Quests:{RESET}")
                for qid in sorted(self.active.keys()):
                    print(self.get_display_line(qid))
            if self.completed:
                print(f"\n  {DIM}Completed: {len(self.completed)} quests{DIM}")
            print(f"\n  {DIM}Total quests: {len(QUESTS)} | Active: {len(self.active)}{RESET}")
            print()
            print(f"  {BOLD}{BRIGHT_WHITE}1-5.{RESET} Accept quest")
            print(f"  {BOLD}{BRIGHT_WHITE}A.{RESET} Auto-accept a random quest")
            print(f"  {BOLD}{DIM}Q.{RESET} Back")
            r = crazy_input("Choose")
            if r.lower() == "q":
                break
            if r.lower() == "a":
                if avail:
                    self.assign(avail[0]["id"])
                    print(f"  {BRIGHT_GREEN}Accepted quest #{avail[0]['id']}!{RESET}")
                    crazy_input("Press Enter to continue")
            else:
                try:
                    idx = int(r) - 1
                    if 0 <= idx < len(avail):
                        self.assign(avail[idx]["id"])
                        print(f"  {BRIGHT_GREEN}Accepted quest #{avail[idx]['id']}!{RESET}")
                        crazy_input("Press Enter to continue")
                except ValueError:
                    pass


quest_manager = QuestManager()
