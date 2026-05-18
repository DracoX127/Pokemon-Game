"""
Pokemon Game AI Chatbot Package
Rule-based chatbot — NO API keys, NO LLM downloads.
"""

from AI.chatbot import PokemonChatbot
from AI.knowledge_base import (
    solve_math, get_physics_help, get_science_fact,
    get_game_hint, get_element_info, get_biology_fact,
    get_astronomy_fact
)
from AI.responses import get_greeting, get_goodbye, get_fallback

__all__ = [
    'PokemonChatbot',
    'solve_math', 'get_physics_help', 'get_science_fact',
    'get_game_hint', 'get_element_info', 'get_biology_fact',
    'get_astronomy_fact',
    'get_greeting', 'get_goodbye', 'get_fallback',
]
