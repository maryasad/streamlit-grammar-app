# generator.py
import os
import openai
from dotenv import load_dotenv
from config import OPENAI_API_KEY
from prompts import build_prompt

load_dotenv()  # 👈 ensures .env is loaded in dev and test too
FAKE_MODE = os.getenv("FAKE_MODE") == "true"

openai.api_key = OPENAI_API_KEY

def generate_quiz(topic: str, level: str, num_questions: int) -> str:
    prompt = build_prompt(topic, level, num_questions)
    
    if FAKE_MODE:
        return (
            f"Q1: What is correct for '{topic}' at {level} level?\n"
            f"A) Option 1\nB) Option 2\nC) Option 3\nAnswer: B"
        )
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        content = response.choices[0].message.content
        if content is not None:
            return content.strip()
        else:
            return ""
    except Exception as e:
        print(f"❌ OpenAI error: {e}")
        return ""
