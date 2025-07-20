import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # load .env file if present

DATABASE_URL = os.getenv("DATABASE_URL")

def create_table():
    conn = psycopg2.connect(DATABASE_URL)

    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS quiz_history (
            id SERIAL PRIMARY KEY,
            topic TEXT NOT NULL,
            level TEXT NOT NULL,
            score INTEGER NOT NULL,
            total INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    cur.close()
    
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS quiz_history (
            id SERIAL PRIMARY KEY,
            topic TEXT NOT NULL,
            level TEXT NOT NULL,
            score INTEGER NOT NULL,
            total INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    
    conn.close()
    print("✅ Table created successfully")

if __name__ == "__main__":
    create_table()
