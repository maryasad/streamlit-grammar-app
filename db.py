import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conn


def save_quiz(topic, level, raw_text):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO quizzes (topic, level, content)
        VALUES (%s, %s, %s)
    """, (topic, level, raw_text))
    conn.commit()
    cur.close()
    conn.close()

def get_all_quizzes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, topic, level, content FROM quizzes")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results