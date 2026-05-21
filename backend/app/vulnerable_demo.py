import sqlite3
import os
import subprocess

# Hardcoded secret resolved: Load from environment variable with a safe placeholder fallback
API_KEY = os.getenv("DEMO_API_KEY", "DEMO_API_KEY_PLACEHOLDER")

def get_user_data(username):
    # SQL Injection resolved: Use parameterized query
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    print(f"Executing query: {query} with param {username}")
    cursor.execute(query, (username,))
    return cursor.fetchall()

def dangerous_execution(user_input):
    # Command Injection resolved: Use subprocess.run without shell=True
    subprocess.run(["echo", user_input], check=True)

if __name__ == "__main__":
    # Test calls
    print(get_user_data("admin' OR '1'='1"))
    dangerous_execution("; rm -rf /")
