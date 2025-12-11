import sqlite3
import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DB_DIR, "test_users.db")

def test_anonymization():
    if not os.path.exists(DB_PATH):
        print(f"Database not found at {DB_PATH}")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT name, email FROM users')
    users = cursor.fetchall()
    conn.close()

    if not users:
        print("No users found in the database")
        sys.exit(1)

    name_pattern = re.compile(r"Anonym Användare \d+")
    email_pattern = re.compile(r"anonym_\d+@example\.local")

    failed = False
    for name, email in users:
        if not name_pattern.fullmatch(name):
            print(f"FAIL: Name not anonymized -> {name}")
            failed = True
        if not email_pattern.fullmatch(email):
            print(f"FAIL: Email not anonymized -> {email}")
            failed = True

    if failed:
        sys.exit(1)
    else:
        print("PASS: All names and emails are anonymized")

if __name__ == "__main__":
    test_anonymization()
