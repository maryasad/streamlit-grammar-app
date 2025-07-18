# 🧠 AI Grammar Quiz App

An interactive, AI-powered English grammar quiz app built with **Streamlit**. This app generates real-time multiple-choice grammar questions using OpenAI's GPT model and provides instant feedback to help learners practice their English in a fun and intelligent way.

![app-screenshot](./screenshot.png)

---

## ✨ Features

- ✅ AI-generated grammar quiz questions
- ✅ Beginner, Intermediate, and Advanced levels
- ✅ Topics like Tenses, Prepositions, Articles, and more
- ✅ Interactive UI with answer validation
- ✅ Real-time quiz generation via GPT-3.5
- ✅ Automatic CI checks via GitHub Actions
- ✅ Easy to extend (add explanations, scoring history, voice input, etc.)

---

## 🛠 Tech Stack

| Layer      | Technology         |
|------------|--------------------|
| Frontend   | Streamlit          |
| Backend    | Python (OpenAI API)|
| Language Model | GPT-3.5-turbo |
| Environment | `venv`            |
| CI/CD      | GitHub Actions     |
| Hosting    | *Streamlit Community Cloud (optional)* |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/maryasad/streamlit-grammar-app.git
cd streamlit-grammar-app
```

### 2. Set up virtual environment
```bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```
### 3. Install dependencies
```bash
Copy
Edit
pip install -r requirements.txt
```
### 4. Add your OpenAI API key
Create a .env file in the root:

env
Copy
Edit
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
### 5. Run the app
```bash
Copy
Edit
streamlit run app.py
```
### ⚙️ Continuous Integration
This project uses GitHub Actions to run CI checks on each push to main:

✅ Python syntax checks via flake8

✅ Dependency installation test

✅ Code cleanliness for Streamlit app

CI configuration is defined in .github/workflows/test.yml.

### 📌 Planned Features
 GPT-generated explanations for answers

 Persian (Farsi) translation toggle

 Text-to-speech for pronunciation

 Score tracking over time

 Auto-deploy via Streamlit Cloud


```
/app
  ├── main.py            ← Streamlit entry
  ├── generator.py       ← AI quiz logic
  ├── prompts.py         ← prompt templates
  ├── parser.py          ← answer extraction/cleanup
  └── config.py          ← API keys/env loader

```

