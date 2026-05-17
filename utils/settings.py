import json
import os

SETTINGS_FILE = "settings.json"

DEFAULT_SETTINGS = {
    "theme": "rainbow",               # Options: rainbow, fire, water, grass, electric, psychic, hacker, vaporwave, gold, blood, ice, retro, dark
    "animation_speed": 1.0,           # Multiplier: 0.0 (instant), 0.5 (fast), 1.0 (normal), 2.0 (slow)
    "border_style": "crazy",          # Options: crazy, fire, electric, shadow, double, rounded, dashed, water, grass
    "text_reveal_style": "typewriter",# Options: typewriter, dramatic, slow_reveal, glitch, typing_cursor
    "battle_hud_style": "classic",    # Options: classic, modern, minimal, ascii
    "hp_bar_style": "blocks",         # Options: blocks, symbols, emoji, abstract
    "xp_bar_style": "blocks",         # Options: blocks, symbols, emoji, abstract
    "enable_screen_shake": True,
    "enable_ascii_art": True,
    "enable_particles": True
}

class SettingsManager:
    def __init__(self):
        self.settings = DEFAULT_SETTINGS.copy()
        self.load()

    def load(self):
        if os.path.exists(SETTINGS_FILE):
            try:
                with open(SETTINGS_FILE, 'r') as f:
                    loaded = json.load(f)
                    # Update settings with loaded ones, keeping defaults for missing keys
                    for k, v in loaded.items():
                        if k in self.settings:
                            self.settings[k] = v
            except Exception as e:
                print(f"Error loading settings: {e}")

    def save(self):
        try:
            with open(SETTINGS_FILE, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")

    def get(self, key):
        return self.settings.get(key, DEFAULT_SETTINGS.get(key))

    def set(self, key, value):
        if key in self.settings:
            self.settings[key] = value
            self.save()

    def reset_to_defaults(self):
        self.settings = DEFAULT_SETTINGS.copy()
        self.save()

# Global instance to be imported everywhere
GAME_SETTINGS = SettingsManager()
