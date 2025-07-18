import streamlit as st
from quiz_generator import generate_quiz

st.set_page_config(page_title="AI Grammar Quiz", page_icon="🧠", layout="centered")

st.title("🧠 AI Grammar Quiz Generator")
st.write("Test your grammar with quizzes created by AI!")

topic = st.selectbox("Choose a topic:", ["Grammar", "Tenses", "Prepositions", "Articles"])
level = st.selectbox("Select level:", ["Beginner", "Intermediate", "Advanced"])
num_questions = st.slider("Number of questions", 1, 5, 3)

if st.button("Generate Quiz"):
    with st.spinner("Talking to AI..."):
        quiz = generate_quiz(topic, level, num_questions)
        # Add this to make sure quiz is not None
        if not quiz:
            st.error("❌ Failed to generate quiz. Please check your API key or try again.")
        else:
            st.session_state["quiz"] = quiz.split("\n\n")

if "quiz" in st.session_state:
    st.subheader("📝 Your Quiz")
    score = 0
    for i, block in enumerate(st.session_state["quiz"]):
        if not block.strip():
            continue
        try:
            question_part, answer_part = block.strip().split("Answer:")
            st.markdown(f"**{question_part.strip()}**")
            user_input = st.radio(f"Your answer for Q{i+1}", ["A", "B", "C"], key=f"q{i}")
            correct = answer_part.strip()[0]
            if st.button(f"Submit Answer {i+1}", key=f"submit_{i}"):
                if user_input == correct:
                    st.success("✅ Correct!")
                    score += 1
                else:
                    st.error(f"❌ Wrong. Correct answer: {correct}")
        except Exception:
            st.warning("⚠️ One question couldn't be parsed. Try generating again.")
    st.info(f"Your current score: {score}/{len(st.session_state['quiz'])}")
