import sqlite3
import os

# Hardcoded secret (Vulnerability: Insecure storage of sensitive information)
API_KEY = "sk-1234567890abcdef1234567890abcdef"

def get_user_data(username):
    # SQL Injection (Vulnerability: Improper Neutralization of Special Elements used in an SQL Command)
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    print(f"Executing query: {query}")
    cursor.execute(query)
    return cursor.fetchall()

def dangerous_execution(user_input):
    # Command Injection (Vulnerability: Improper Neutralization of Special Elements used in an OS Command)
    os.system(f"echo {user_input}")

if __name__ == "__main__":
    # Test calls
    print(get_user_data("admin' OR '1'='1"))
    dangerous_execution("; rm -rf /")
