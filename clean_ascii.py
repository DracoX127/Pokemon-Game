"""
Legacy cleanup helper for ascii_art.py.

The game depends on the sprite dictionary and named art constants in ascii_art.py.
This script used to rewrite that file at import time, which could break runtime
imports. It is now intentionally guarded and non-destructive.
"""


def clean_ascii_art():
    print("clean_ascii.py is disabled to protect required game art assets.")


if __name__ == "__main__":
    clean_ascii_art()
