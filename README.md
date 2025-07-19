# Quizcraft - AI-Powered English Grammar Quiz App

An intelligent English grammar quiz application built with **Streamlit** that generates personalized quizzes using AI. The app creates engaging, adaptive quizzes based on user-selected grammar topics and difficulty levels.

## Features

- **AI-Powered Quiz Generation**: Creates dynamic grammar quizzes using advanced language models
- **Topic Selection**: Choose from various grammar topics (tenses, parts of speech, punctuation, etc.)
- **Difficulty Levels**: Adaptive difficulty settings for different skill levels
- **Interactive Interface**: Clean, user-friendly Streamlit interface
- **Real-time Feedback**: Immediate scoring and explanations
- **Progress Tracking**: Monitor your grammar improvement over time

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd streamlit-grammar-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
```bash
# Create a .env file and add your OpenAI API key
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default web browser. Select your preferred grammar topic and difficulty level to start generating personalized quizzes.

## Configuration

The app uses the following configuration files:
- `config.py`: Application settings and constants
- `prompts.py`: AI prompt templates for quiz generation
- `generator.py`: Quiz generation logic
- `parser.py`: Response parsing utilities

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Hugging Face Spaces Configuration

This app is configured for deployment on Hugging Face Spaces:

---
title: Quizcraft
emoji: 🚀
colorFrom: yellow
colorTo: gray
sdk: gradio
sdk_version: 5.38.0
app_file: app.py
pinned: false
license: mit
short_description: AI-powered English grammar quiz app built with **Streamlit**
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

