"""Achievement System: 35 milestones to track player progress."""

from ui_core import (
    RESET, BOLD, DIM, BRIGHT_WHITE, BRIGHT_CYAN, BRIGHT_YELLOW,
    BRIGHT_GREEN, BRIGHT_RED, BRIGHT_MAGENTA,
    crazy_input, clear_screen, fancy_header
)

ACHIEVEMENTS = [
    {"id":1, "name":"First Step",      "desc":"Catch your first Pokemon.", "icon":"🐣", "category":"catch", "threshold":1, "reward":{"type":"coins","value":50}},
    {"id":2, "name":"Collector",       "desc":"Catch 10 Pokemon.",         "icon":"📦", "category":"catch", "threshold":10, "reward":{"type":"coins","value":200}},
    {"id":3, "name":"Pokemon Master",  "desc":"Catch 30 Pokemon.",         "icon":"🏆", "category":"catch", "threshold":30, "reward":{"type":"coins","value":500}},
    {"id":4, "name":"Professor's Apprentice","desc":"Catch 50 Pokemon.",  "icon":"🎓", "category":"catch", "threshold":50, "reward":{"type":"trophies","value":100}},
    {"id":5, "name":"Living Dex",      "desc":"Catch 100 Pokemon.",        "icon":"📚", "category":"catch", "threshold":100, "reward":{"type":"trophies","value":500}},
    {"id":6, "name":"Gym Challenger",  "desc":"Win your first Gym badge.", "icon":"🥇", "category":"badges", "threshold":1, "reward":{"type":"coins","value":300}},
    {"id":7, "name":"Badge Collector", "desc":"Win 4 Gym badges.",         "icon":"🎖️", "category":"badges", "threshold":4, "reward":{"type":"trophies","value":200}},
    {"id":8, "name":"Champion",        "desc":"Win all 8 Gym badges.",     "icon":"👑", "category":"badges", "threshold":8, "reward":{"type":"trophies","value":1000}},
    {"id":9, "name":"Elite Challenger","desc":"Defeat your first Elite Four member.","icon":"⚔️","category":"elite_four","threshold":1,"reward":{"type":"coins","value":500}},
    {"id":10,"name":"League Champion", "desc":"Defeat all 5 Elite Four members.","icon":"🏆","category":"elite_four","threshold":5,"reward":{"type":"trophies","value":2000}},
    {"id":11,"name":"Rookie Trainer",  "desc":"Reach level 10 with any Pokemon.","icon":"⭐","category":"level","threshold":10,"reward":{"type":"coins","value":100}},
    {"id":12,"name":"Veteran Trainer", "desc":"Reach level 50 with any Pokemon.","icon":"🌟","category":"level","threshold":50,"reward":{"type":"trophies","value":300}},
    {"id":13,"name":"Legendary Trainer","desc":"Reach level 100 with any Pokemon.","icon":"💫","category":"level","threshold":100,"reward":{"type":"trophies","value":1000}},
    {"id":14,"name":"Breeder",         "desc":"Evolve 5 Pokemon.",         "icon":"🥚", "category":"evolve","threshold":5, "reward":{"type":"coins","value":200}},
    {"id":15,"name":"Evolution Expert","desc":"Evolve 20 Pokemon.",        "icon":"🧬", "category":"evolve","threshold":20, "reward":{"type":"trophies","value":500}},
    {"id":16,"name":"Mad Scientist",   "desc":"Create 3 fusion Pokemon.",  "icon":"🔬", "category":"fusion","threshold":3, "reward":{"type":"coins","value":300}},
    {"id":17,"name":"Genetic Engineer","desc":"Create 10 fusion Pokemon.", "icon":"🧪", "category":"fusion","threshold":10, "reward":{"type":"trophies","value":500}},
    {"id":18,"name":"Explorer",        "desc":"Visit 3 different regions.","icon":"🗺️", "category":"explore","threshold":3, "reward":{"type":"coins","value":150}},
    {"id":19,"name":"World Traveler",  "desc":"Visit all regions.",        "icon":"🌍", "category":"explore","threshold":8, "reward":{"type":"trophies","value":300}},
    {"id":20,"name":"Millionaire",     "desc":"Accumulate 10,000 coins.",  "icon":"💰", "category":"money","threshold":10000,"reward":{"type":"trophies","value":200}},
    {"id":21,"name":"Tycoon",          "desc":"Accumulate 100,000 coins.", "icon":"💎", "category":"money","threshold":100000,"reward":{"type":"trophies","value":1000}},
    {"id":22,"name":"Tower Rookie",    "desc":"Reach round 5 in Battle Tower.","icon":"🗼","category":"tower","threshold":5, "reward":{"type":"coins","value":200}},
    {"id":23,"name":"Tower Veteran",   "desc":"Reach round 25 in Battle Tower.","icon":"🏛️","category":"tower","threshold":25,"reward":{"type":"trophies","value":500}},
    {"id":24,"name":"Tower Legend",    "desc":"Reach round 100 in Battle Tower.","icon":"🏯","category":"tower","threshold":100,"reward":{"type":"trophies","value":2000}},
    {"id":25,"name":"Shiny Hunter",    "desc":"Catch your first Shiny Pokemon.","icon":"✨","category":"shiny","threshold":1,"reward":{"type":"coins","value":500}},
    {"id":26,"name":"Shiny Collector", "desc":"Catch 5 Shiny Pokemon.",   "icon":"🌟",  "category":"shiny","threshold":5, "reward":{"type":"trophies","value":1000}},
    {"id":27,"name":"Slayer",          "desc":"Defeat 50 wild Pokemon.",  "icon":"⚔️",  "category":"defeats","threshold":50,"reward":{"type":"coins","value":300}},
    {"id":28,"name":"Butcher",         "desc":"Defeat 200 wild Pokemon.", "icon":"💀",  "category":"defeats","threshold":200,"reward":{"type":"trophies","value":500}},
    {"id":29,"name":"Shopaholic",      "desc":"Buy 20 items from the shop.","icon":"🛒", "category":"shop","threshold":20,"reward":{"type":"coins","value":200}},
    {"id":30,"name":"Gambler",         "desc":"Buy 100 items from the shop.","icon":"🎰","category":"shop","threshold":100,"reward":{"type":"trophies","value":300}},
    {"id":31,"name":"Jogger",          "desc":"Use the Travel option 10 times.","icon":"🏃","category":"travel","threshold":10,"reward":{"type":"coins","value":100}},
    {"id":32,"name":"Marathon Runner", "desc":"Use the Travel option 50 times.","icon":"🏅","category":"travel","threshold":50,"reward":{"type":"trophies","value":200}},
    {"id":33,"name":"Bug Squasher",    "desc":"Complete 5 Bug Hunt rounds.","icon":"🐛", "category":"bug_hunt","threshold":5,"reward":{"type":"coins","value":300}},
    {"id":34,"name":"Bug Exterminator","desc":"Complete 25 Bug Hunt rounds.","icon":"🧹","category":"bug_hunt","threshold":25,"reward":{"type":"trophies","value":500}},
    {"id":35,"name":"Quest Beginner",  "desc":"Complete 3 quests.",        "icon":"📋", "category":"quests","threshold":3,"reward":{"type":"coins","value":200}},
]


class AchievementManager:
    def __init__(self):
        self.unlocked = set()
        self.counters = {}

    def get_counter(self, key):
        return self.counters.get(key, 0)

    def increment(self, key, amount=1):
        self.counters[key] = self.get_counter(key) + amount
        return self.check(key)

    def check(self, key):
        results = []
        for a in ACHIEVEMENTS:
            if a["id"] in self.unlocked:
                continue
            if a["category"] != key:
                continue
            current = self.counters.get(key, 0)
            if current >= a["threshold"]:
                self.unlocked.add(a["id"])
                results.append(a)
        return results

    def hook_catch(self, is_shiny=False):
        results = []
        c = self.increment("catch")
        results.extend(c)
        if is_shiny:
            results.extend(self.increment("shiny"))
        return results

    def hook_defeat(self):
        return self.increment("defeats")

    def hook_badge(self, count):
        return self.check("badges")

    def hook_elite_four(self, count):
        return self.check("elite_four")

    def hook_level(self, level):
        old = self.counters.get("level", 0)
        if level > old:
            self.counters["level"] = level
        return self.check("level")

    def hook_evolve(self):
        return self.increment("evolve")

    def hook_fusion(self):
        return self.increment("fusion")

    def hook_explore(self, regions_visited):
        self.counters["explore"] = regions_visited
        return self.check("explore")

    def hook_money(self, amount):
        self.counters["money"] = amount
        return self.check("money")

    def hook_tower(self, record):
        self.counters["tower"] = record
        return self.check("tower")

    def hook_shop(self):
        return self.increment("shop")

    def hook_travel(self):
        return self.increment("travel")

    def hook_bug_hunt(self):
        return self.increment("bug_hunt")

    def hook_quest(self):
        return self.increment("quests")

    def show_menu(self):
        while True:
            clear_screen()
            fancy_header("ACHIEVEMENTS", "🏅", 50)
            total = len(ACHIEVEMENTS)
            done = len(self.unlocked)
            print(f"  {BOLD}{BRIGHT_WHITE}Progress: {done}/{total} ({done*100//total if total else 0}%){RESET}\n")
            for a in ACHIEVEMENTS:
                unlocked = a["id"] in self.unlocked
                icon = "✅" if unlocked else "⬜"
                name_style = BRIGHT_GREEN if unlocked else DIM
                desc_style = BRIGHT_WHITE if unlocked else DIM
                print(f"  {icon} {name_style}{a['icon']} {a['name']:<22}{RESET} {desc_style}{a['desc']:<40}{RESET}")
            print(f"\n  {DIM}Total: {done}/{total} achievements unlocked{RESET}")
            print()
            r = crazy_input("Press Enter to go back")
            if r.lower() == "q":
                break
            break
        clear_screen()

    def to_dict(self):
        return {
            "unlocked": list(self.unlocked),
            "counters": dict(self.counters),
        }

    @classmethod
    def from_dict(cls, data):
        m = cls()
        m.unlocked = set(data.get("unlocked", []))
        m.counters = dict(data.get("counters", {}))
        return m


achievement_manager = AchievementManager()
