import sqlite3
import hashlib

DB_NAME = "password_history.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS passwords(
            hash TEXT UNIQUE
        )
    """)

    conn.commit()
    conn.close()


def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def password_exists(password):
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    password_hash = hash_password(password)

    cursor.execute(
        "SELECT * FROM passwords WHERE hash=?",
        (password_hash,)
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None


def save_password(password):
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    password_hash = hash_password(password)

    try:
        cursor.execute(
            "INSERT INTO passwords(hash) VALUES(?)",
            (password_hash,)
        )
        conn.commit()
    except:
        pass

    conn.close()
