import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_quiz(topic="grammar", level="beginner", n_questions=3):
    try:
        prompt = f"""
        Generate {n_questions} multiple choice English grammar questions for {level} learners about {topic}.
        Each question must have 3 options and show the correct answer.
        Format like:
        Q: What is the correct form of the verb?
        A) Go
        B) Goes
        C) Going
        Answer: B
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"❌ OpenAI Error: {e}")
        return None
