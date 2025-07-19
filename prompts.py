# prompts.py

TOPIC_TEMPLATES = {
    "Grammar": "Generate {n} general grammar multiple-choice questions for a {level} English learner.",
    "Tenses": "Create {n} multiple-choice questions about English verb tenses for a {level} learner.",
    "Prepositions": "Write {n} fill-in-the-blank questions using prepositions. Provide 3 options and mark the correct one. Difficulty: {level}.",
    "Articles": "Generate {n} multiple-choice questions about English articles (a, an, the) for a {level} student.",
}

def build_prompt(topic: str, level: str, num_questions: int) -> str:
    topic_instruction = TOPIC_TEMPLATES.get(topic, TOPIC_TEMPLATES["Grammar"]).format(n=num_questions, level=level)
    
    return f"""
You are a quiz generator for English language learners.

{topic_instruction}

Each question must follow *exactly* this format:

Q1: [question text]  
A) [Option A]  
B) [Option B]  
C) [Option C]  
Answer: [Correct letter]

Separate each question with **a blank line**. Only output the quiz. No explanations.
"""
