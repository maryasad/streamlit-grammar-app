# app.py
import streamlit as st
from generator import generate_quiz
import time
import os

st.write("🔍 Environment keys:", list(os.environ.keys()))



# Enable FAKE_MODE on Hugging Face
if "HF_SPACE_ID" in os.environ:
    os.environ["FAKE_MODE"] = "true"

st.warning(os.getenv("FAKE_MODE"))

if os.getenv("FAKE_MODE") == "true":
    st.warning("🚧 Running in demo mode. Real API is disabled.")

# key = os.getenv("OPENAI_API_KEY")

# if key:
#     st.success("✅ OPENAI_API_KEY is set!")
# else:
#     st.error("❌ OPENAI_API_KEY is NOT set. Check Secrets in Hugging Face.")


st.set_page_config(page_title="AI Grammar Quiz", page_icon="🧠", layout="centered")
st.title("🧠 AI Grammar Quiz Generator")
st.write("Test your grammar with quizzes created by AI!")

with st.form("quiz_form"):
    topic = st.selectbox("Choose a topic:", ["Grammar", "Tenses", "Prepositions", "Articles"])
    level = st.selectbox("Select level:", ["Beginner", "Intermediate", "Advanced"])
    num_questions = st.slider("Number of questions", 1, 5, 3)
    submitted = st.form_submit_button("Generate Quiz")

if submitted:
    with st.spinner("Talking to AI..."):
        quiz = generate_quiz(topic, level, num_questions)
        if not quiz:
            st.error("❌ Failed to generate quiz. Please check your API key or try again.")
        else:
            st.session_state["quiz"] = quiz.split("\n\n")
            st.session_state["answers"] = {}  # Reset answers
            st.session_state["submitted"] = False

if "quiz" in st.session_state:
    st.subheader("📝 Your Quiz")
    for i, block in enumerate(st.session_state["quiz"]):
        if not block.strip():
            continue
        try:
            # Safe parsing
            if "Answer:" not in block:
                raise ValueError("Missing 'Answer:'")            
            question_part, answer_part = block.strip().split("Answer:",1)
            question_text = question_part.strip()
            correct_letter = answer_part.strip()[0].upper()
            # Validate the correct letter
            if correct_letter not in ["A", "B", "C"]:
                raise ValueError("Invalid answer format")

            st.markdown(f"**{question_part.strip()}**")
            # Extract options and correct answer
            lines = question_text.strip().split("\n")
            question_line = lines[0]
            options = lines[1:]  # Expects: A) Option 1, B) Option 2, ...

            # Map options to labels
            option_map = {}
            for line in options:
                if line.strip()[:2] in ["A)", "B)", "C)"]:
                    letter = line.strip()[0]
                    text = line.strip()[3:].strip()
                    option_map[text] = letter

            # Show question and clickable options
            st.markdown(f"**{question_line}**")
            user_input_text = st.radio("Choose your answer:", list(option_map.keys()), key=f"q{i}")

            # Save both text and mapped letter
            st.session_state["answers"][i] = {
                "user_letter": option_map[user_input_text],
                "correct_letter": correct_letter,
                "user_text": user_input_text
            }
        except Exception as e:
            st.warning(f"⚠️ Question {i+1} couldn't be parsed. Try generating again.")

    if st.button("Submit All Answers"):
        score = 0
        for ans in st.session_state["answers"].values():
            if ans["user_letter"] == ans["correct_letter"]:
                score += 1
        total = len(st.session_state["answers"])
        if total > 0:
            percent = int((score / total) * 100)
        else:
            percent = 0
        st.success(f"✅ Final Score: {score} / {total}")
        progress_bar = st.progress(0)
        for i in range(percent + 1):
            progress_bar.progress(i)
            time.sleep(0.01)

        for i, ans in st.session_state["answers"].items():
            if st.button(f"Reveal Answer Q{i+1}", key=f"reveal_{i}"):
                st.info(f"✅ Correct answer: {ans['correct_letter']} — {ans['user_text']}")



        # Save to history
        if "history" not in st.session_state:
            st.session_state.history = []
        st.session_state.history.append({
            "topic": topic,
            "level": level,
            "score": score,
            "total": total
        })

# Show history
if "history" in st.session_state and st.session_state.history:
    st.subheader("📜 Quiz History")
    for entry in st.session_state.history:
        st.markdown(f"- **{entry['topic']}** ({entry['level']}) — {entry['score']}/{entry['total']}")

if st.button("🔄 Try Another Quiz"):
    for key in list(st.session_state.keys()):
        # Ensure key is a string before calling string methods
        if (
            isinstance(key, str)
            and (key.startswith("q") or key.startswith("submit_") or key in ["quiz", "answers"])
        ):
            del st.session_state[key]
    st.rerun()
