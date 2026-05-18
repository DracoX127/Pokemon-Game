"""
Response templates for Pokemon Chatbot.
Personality: Friendly, Pokemon-themed, helpful.
"""

import random

GREETINGS = [
    "Hey there, Trainer! Welcome! How can I help you today? ",
    "Hello! I'm PokéBot, your game assistant! What's up? ⚡",
    "Hi! Ready to talk Pokemon, math, or science? Ask away! 🎮",
    "Hey! Great to see you! Need help with anything? 💪",
    "Yo, Trainer! What can I do for you today? 🌟",
    "Greetings! I know math, science, and Pokemon stuff. What's on your mind? 🤖",
    "Hello there! Welcome back! How's your Pokemon journey going? 🏆",
    "Hey hey! PokéBot here at your service! What do you need? ⚡",
]

GREETINGS_RETURNING = [
    "Welcome back, Trainer! What can I help with? ",
    "Hey again! Ready for more questions? ⚡",
    "Back so soon? What's on your mind? 🎮",
    "Hello again! Need more help? I'm here! 💪",
]

GOODBYES = [
    "See you later, Trainer! Keep catching 'em all! ⚡",
    "Bye! Good luck on your Pokemon journey! 🏆",
    "Catch you later! Remember to save your game! 💾",
    "Farewell! May your crits be frequent! 🎯",
    "See ya! Don't forget to heal your Pokemon! ❤️",
    "Goodbye! Go catch some shinies! ✨",
    "Later! May the RNG be ever in your favor! 🎲",
    "Bye bye! Train hard and battle harder! 💪",
]

FALLBACKS = [
    "Hmm, I'm not sure about that one! Try asking me about math, physics, science, or Pokemon game hints! 🤔",
    "I don't know that yet, but I'm learning! Try: '2+2', 'what is force', 'science fact', or 'how to catch' 📚",
    "That's beyond my current knowledge! I can help with math, science, physics, and game tips! 🧮",
    "Interesting question! I specialize in math, science, and Pokemon game help. Try asking about those! ⚡",
    "I'm still learning about that! For now, I can solve math, explain physics, share science facts, and give game hints! 🎮",
    "Not sure about that one, Trainer! But I'm great at math problems, science facts, and game strategy! 💡",
]

def get_greeting(count):
    """Get a greeting response."""
    if count > 1:
        return random.choice(GREETINGS_RETURNING)
    return random.choice(GREETINGS)

def get_goodbye():
    """Get a goodbye response."""
    return random.choice(GOODBYES)

def get_fallback(text):
    """Get a fallback response for unknown inputs."""
    response = random.choice(FALLBACKS)
    # Sometimes echo back what they said
    if random.random() < 0.3:
        response += f"\n  You said: \"{text}\" — try rephrasing!"
    return response
