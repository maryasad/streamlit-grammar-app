# # tests/test_quiz_generator.py
# import sys
# import os
# sys.path.append(os.path.abspath("."))  # 👈 Add this

from unittest.mock import patch
from app.generator import generate_quiz

@patch("app.generator.openai.ChatCompletion.create")
def test_generate_quiz(mock_create):
    mock_create.return_value = {
        "choices": [
            {
                "message": {
                    "content": "Q: What is the correct form of the verb?\nA) Go\nB) Goes\nC) Going\nAnswer: B"
                }
            }
        ]
    }
    quiz = generate_quiz("Tenses", "Beginner", 3)
    assert quiz is not None
    assert "Answer: B" in quiz
