import os
import sqlite3

def seed():
    db_path = os.path.join(os.path.dirname(__file__), "../../articles.db")
    schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    with open(schema_path, "r") as f:
        cursor.executescript(f.read())

    # Seed data
    cursor.execute("INSERT INTO authors (name) VALUES (?)", ("John Doe",))
    cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Jane Smith",))

    cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Tech Weekly", "Technology"))
    cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Health Monthly", "Health"))

    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", ("AI in 2025", 1, 1))
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", ("Wellness Trends", 2, 2))
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", ("Quantum Leap", 1, 1))

    connection.commit()
    connection.close()

if __name__ == "__main__":
    seed()
