# # tests/test_quiz_generator.py
# import sys
# import os
# sys.path.append(os.path.abspath("."))  # 👈 Add this

from quiz_generator import generate_quiz

def test_generate_quiz():
    quiz = generate_quiz("Grammar", "Beginner", 3)
    assert quiz is not None
    assert isinstance(quiz, str)
    assert "Answer:" in quiz
