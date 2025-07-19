# app.py
import streamlit as st
from generator import generate_quiz
import time
import os


key = os.getenv("OPENAI_API_KEY")

if key:
    st.success("✅ OPENAI_API_KEY is set!")
else:
    st.error("❌ OPENAI_API_KEY is NOT set. Check Secrets in Hugging Face.")


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
            user_input = st.radio(f"Your answer for Q{i+1}", ["A", "B", "C"], key=f"q{i}")
            st.session_state["answers"][i] = {
                "user": user_input,
                "correct": answer_part.strip()[0]
            }
        except Exception as e:
            st.warning(f"⚠️ Question {i+1} couldn't be parsed. Try generating again.")

    if st.button("Submit All Answers"):
        score = 0
        for ans in st.session_state["answers"].values():
            if ans["user"] == ans["correct"]:
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
                st.info(f"✅ Correct answer: {ans['correct']}")

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
