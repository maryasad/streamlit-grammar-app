# tests/test_generator.py
from unittest.mock import patch
from app.generator import generate_quiz

@patch("app.generator.openai.ChatCompletion.create")
def test_generate_quiz(mock_create):
    mock_create.return_value = {
        "choices": [{"message": {"content": "Q1: What is correct?\nA) Foo\nB) Bar\nC) Baz\nAnswer: B"}}]
    }

    quiz = generate_quiz("Grammar", "Beginner", 1)
    assert "Answer: B" in quiz
