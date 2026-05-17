import sys
import os

# Dynamic absolute path injection to allow all nested folders to load in sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
core_dir = os.path.join(BASE_DIR, "core")
sys.path.insert(0, core_dir)

# Delegate boot execution to core/main.py!
import main
