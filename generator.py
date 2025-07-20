# generator.py
import os
import openai
from dotenv import load_dotenv
from config import OPENAI_API_KEY
from prompts import build_prompt

load_dotenv()  # Load .env file

# Function to check fake mode
def is_fake_mode():
    return os.getenv("FAKE_MODE", "").lower() == "true"

openai.api_key = OPENAI_API_KEY

def generate_quiz(topic: str, level: str, num_questions: int) -> str:
    prompt = build_prompt(topic, level, num_questions)
    
    if is_fake_mode():
        return (
            f"Q1: What is correct for '{topic}' at {level} level?\n"
            f"A) Option 1\nB) Option 2\nC) Option 3\nAnswer: B\n\n"
            f"Q2: Another sample question about {topic}?\n"
            f"A) First option\nB) Second option\nC) Third option\nAnswer: A"
        )
    
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        content = response.choices[0].message.content
        print("🔍 Generated Content:\n", content)
        return content.strip() if content else ""
    except Exception as e:
        print(f"❌ OpenAI error: {e}")
        return ""


