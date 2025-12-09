import sqlite3
import os
import time

# ----------------------------
# Databasinställningar
# ----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "data")  # mappen för databasen
DB_PATH = os.path.join(DB_DIR, "test_users.db")

# Se till att mappen finns
os.makedirs(DB_DIR, exist_ok=True)


# ----------------------------
# Initiera databasen
# ----------------------------
def init_database():
    """Initialize the database and create users table."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Skapa tabell
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    # Lägg till testanvändare om tabellen är tom
    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]

    if count == 0:
        test_users = [
            ('Anna Andersson', 'anna@test.se'),
            ('Bo Bengtsson', 'bo@test.se')
        ]
        cursor.executemany('INSERT INTO users (name, email) VALUES (?, ?)', test_users)
        print("Database initialized with test users")
    else:
        print(f"Database already contains {count} users")

    conn.commit()
    conn.close()


# ----------------------------
# Visa användare
# ----------------------------
def display_users():
    """Display all users in the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    if users:
        print("\nCurrent users in database:")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
    else:
        print("\nNo users found in database.")

    conn.close()


# ----------------------------
# GDPR-funktioner
# ----------------------------
def clear_test_data():
    """GDPR Action 1: Clear all test data."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM users')
    conn.commit()
    conn.close()

    print("All test data has been cleared (GDPR compliant)")


def anonymize_data():
    """GDPR Action 2: Anonymize user data."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('UPDATE users SET name = "Anonym Användare"')
    conn.commit()
    conn.close()

    print("All user names have been anonymized (GDPR compliant)")


# ----------------------------
# Huvudprogram
# ----------------------------
if __name__ == "__main__":
    init_database()
    display_users()

    # Håll "containern" igång för test
    print("\nContainer is running. Press Ctrl+C to exit.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down...")


