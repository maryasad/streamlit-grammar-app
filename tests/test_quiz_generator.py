# tests/test_generator.py
from unittest.mock import patch
from generator import generate_quiz

@patch("generator.openai.chat.completions.create")
def test_generate_quiz(mock_create):
    mock_create.return_value = {
        "choices": [{"message": {"content": "Q1: What is correct?\nA) Foo\nB) Bar\nC) Baz\nAnswer: B"}}]
    }

    quiz = generate_quiz("Grammar", "Beginner", 1)
    # basic assertions to make sure the quiz format is as expected
    assert isinstance(quiz, str)
    assert "Q1" in quiz
    assert "Answer: B" in quiz
