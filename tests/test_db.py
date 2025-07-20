import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def test_db_connection_and_data():
    DATABASE_URL = os.getenv("DATABASE_URL")
    assert DATABASE_URL is not None, "❌ DATABASE_URL is not set"

    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    # Check if table exists
    cur.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_name = 'quiz_history'
        );
    """)
    result = cur.fetchone()
    assert result is not None, "❌ Failed to fetch table existence check result"
    table_exists = result[0]
    assert table_exists, "❌ Table 'quiz_history' does not exist"

    # Optional: check if any rows exist
    cur.execute("SELECT COUNT(*) FROM quiz_history;")
    count_result = cur.fetchone()
    assert count_result is not None, "❌ Failed to fetch row count"
    count = count_result[0]
    print(f"✅ Number of rows in quiz_history: {count}")
    assert count >= 0  # At least test that it doesn't crash

    cur.close()
    conn.close()
