"""
Pokemon Game AI Chatbot - Rule-Based Foundation
NO API keys, NO LLM downloads. Pure Python rule-based responses.
"""

import re
import math
import random
from AI.responses import get_greeting, get_goodbye, get_fallback
from AI.knowledge_base import (
    solve_math, get_physics_help, get_science_fact,
    get_game_hint, get_element_info, get_biology_fact,
    get_astronomy_fact
)

class PokemonChatbot:
    """Rule-based chatbot for the Pokemon Game."""
    
    def __init__(self):
        self.name = "PokéBot"
        self.greeted = False
        self.conversation_count = 0
    
    def process(self, user_input):
        """Process user input and return a response."""
        if not user_input:
            return "🤔 Say something!"
        
        self.conversation_count += 1
        text = user_input.strip().lower()
        
        # Check for greetings
        if self._is_greeting(text):
            self.greeted = True
            return get_greeting(self.conversation_count)
        
        # Check for goodbyes
        if self._is_goodbye(text):
            self.greeted = False
            return get_goodbye()
        
        # Check for thanks
        if self._is_thanks(text):
            return random.choice([
                "You're welcome! ",
                "Happy to help, Trainer! ⚡",
                "Anytime! That's what I'm here for! 💪",
                "No problem! Keep training! 🏆"
            ])
        
        # Check for math
        math_result = solve_math(text)
        if math_result:
            return math_result
        
        # Check for physics
        physics_result = get_physics_help(text)
        if physics_result:
            return physics_result
        
        # Check for science
        if self._ask_science(text):
            return get_science_fact()
        
        # Check for element info
        element_result = get_element_info(text)
        if element_result:
            return element_result
        
        # Check for biology
        if self._ask_biology(text):
            return get_biology_fact()
        
        # Check for astronomy
        if self._ask_astronomy(text):
            return get_astronomy_fact()
        
        # Check for game hints
        hint_result = get_game_hint(text)
        if hint_result:
            return hint_result
        
        # Check for identity
        if self._ask_identity(text):
            return random.choice([
                f"I'm {self.name}, your Pokemon Game assistant! 🤖",
                f"I'm {self.name}! I know math, science, and Pokemon stuff! ⚡",
                f"Name's {self.name}. I'm here to help you on your journey! 🎮"
            ])
        
        # Check for capabilities
        if self._ask_capabilities(text):
            return (
                f"I can help with:\n"
                f"  🧮 Math: '2+2', 'sqrt(16)', '15% of 200'\n"
                f"  ⚛️ Physics: 'force formula', 'what is velocity'\n"
                f"  🔬 Science: 'science fact', 'tell me about carbon'\n"
                f"  🧬 Biology: 'biology fact', 'what is DNA'\n"
                f"  🌌 Astronomy: 'astronomy fact', 'tell me about Mars'\n"
                f"  🎮 Game hints: 'how to catch', 'what is fusion'\n"
                f"   Pokemon: 'tell me about pikachu'"
            )
        
        # Check for jokes/fun
        if self._ask_joke(text):
            return random.choice([
                "Why did the Pokemon go to school? To improve its Poké-dex! 📚",
                "What do you call a frozen Pikachu? A Pika-freeze! ❄️",
                "Why don't Pokemon ever get lost? They always follow their Nosepass! 🧭",
                "What's a Pokemon's favorite subject? Shock-onomics! ⚡💰😂",
                "Why did Charizard fail the exam? It couldn't handle the heat! 🔥😄"
            ])
        
        # Fallback
        return get_fallback(text)
    
    def _is_greeting(self, text):
        greetings = ['hi', 'hello', 'hey', 'yo', 'sup', 'what\'s up', 'howdy',
                     'greetings', 'good morning', 'good afternoon', 'good evening',
                     'hola', 'bonjour', 'konichiwa']
        return any(g in text for g in greetings)
    
    def _is_goodbye(self, text):
        goodbyes = ['bye', 'goodbye', 'see ya', 'see you', 'later', 'farewell',
                    'cya', 'gtg', 'gotta go', 'leaving', 'exit', 'quit chat']
        return any(g in text for g in goodbyes)
    
    def _is_thanks(self, text):
        thanks = ['thanks', 'thank you', 'thx', 'ty', 'appreciate', 'cheers']
        return any(t in text for t in thanks)
    
    def _ask_science(self, text):
        return any(w in text for w in ['science fact', 'science trivia', 'random science',
                                        'tell me science', 'science knowledge'])
    
    def _ask_biology(self, text):
        return any(w in text for w in ['biology fact', 'biology', 'dna', 'cell',
                                        'evolution', 'organism', 'living thing'])
    
    def _ask_astronomy(self, text):
        return any(w in text for w in ['astronomy', 'space', 'planet', 'star',
                                        'mars', 'jupiter', 'moon', 'sun', 'galaxy',
                                        'universe', 'black hole', 'nebula'])
    
    def _ask_identity(self, text):
        return any(w in text for w in ['who are you', 'what are you', 'your name',
                                        'what is your name', 'introduce'])
    
    def _ask_capabilities(self, text):
        return any(w in text for w in ['what can you do', 'help me', 'capabilities',
                                        'what do you know', 'features', 'commands'])
    
    def _ask_joke(self, text):
        return any(w in text for w in ['joke', 'funny', 'laugh', 'humor',
                                        'tell me a joke', 'make me laugh'])
