# app/prompts.py
def build_prompt(topic: str, level: str, num_questions: int) -> str:
    return (
        f"Generate {num_questions} multiple-choice grammar questions "
        f"on the topic '{topic}' for a {level} English learner.\n"
        "Each question should have options A, B, and C and show the correct answer clearly like:\n\n"
        "Question: ...\nA) ...\nB) ...\nC) ...\nAnswer: B"
    )
