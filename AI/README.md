# Pokemon Game AI Chatbot

## Current Implementation (Rule-Based)
This is a **100% rule-based chatbot** with NO API keys and NO LLM downloads. Everything runs locally in Python.

### Features
- **Greetings/Goodbyes** — Friendly Pokemon-themed responses
- **Math Solver** — Basic arithmetic, percentages, factorials, square roots, powers
- **Physics Helper** — 14 physics formulas with explanations and examples
- **Science Facts** — 25 random science trivia facts
- **Element Info** — 20 chemical elements with atomic data
- **Biology Facts** — 20 biology knowledge facts
- **Astronomy Facts** — 20 space/astronomy facts
- **Game Hints** — Help for all game features (catching, fusing, gyms, etc.)
- **Jokes** — Pokemon-themed jokes

### Files
| File | Purpose |
|------|---------|
| `chatbot.py` | Main chatbot engine with intent detection |
| `knowledge_base.py` | Math solver, physics, science, game hints |
| `responses.py` | Greeting, goodbye, and fallback templates |

### Future Upgrade Path (When Ready)
To upgrade to a real AI later:
1. Replace `chatbot.py` with an API-based implementation
2. Keep the same `process()` interface
3. Options: OpenAI, Anthropic, local LLM (Ollama), or any chat API
4. The `knowledge_base.py` can serve as fallback when API is unavailable

### Usage
```python
from AI import PokemonChatbot
bot = PokemonChatbot()
response = bot.process("what is 2+2")
print(response)  # "🧮 2 + 2 = 4"
```
