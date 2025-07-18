# app/generator.py
import openai
from app.config import OPENAI_API_KEY
from app.prompts import build_prompt

openai.api_key = OPENAI_API_KEY

def generate_quiz(topic: str, level: str, num_questions: int) -> str:
    prompt = build_prompt(topic, level, num_questions)

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
