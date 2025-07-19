# prompts.py

TOPIC_TEMPLATES = {
    "Grammar": "Generate {n} general grammar MCQs for a {level} English learner.",
    "Tenses": "Create {n} multiple-choice questions about English verb tenses for a {level} learner.",
    "Prepositions": "Write {n} fill-in-the-blank questions using prepositions. Provide 3 options and mark the correct one. Difficulty: {level}.",
    "Articles": "Generate {n} MCQs about English articles (a, an, the) suitable for a {level} student.",
}

def build_prompt(topic: str, level: str, num_questions: int) -> str:
    template = TOPIC_TEMPLATES.get(topic, TOPIC_TEMPLATES["Grammar"])
    return template.format(n=num_questions, level=level)
