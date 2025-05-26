import os
import sqlite3

def seed():
    db_path = os.path.join(os.path.dirname(__file__), "../../articles.db")
    schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    with open(schema_path, "r") as f:
        cursor.executescript(f.read())

    # Insert authors
    cursor.execute("INSERT INTO authors (name) VALUES (?)", ("John Doe",))  # ID 1
    cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Jane Smith",))  # ID 2
    cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Bob",))  # ID 3

    # Insert magazines
    cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Tech Weekly", "Technology"))  # ID 1
    cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Health Monthly", "Health"))  # ID 2

    # Insert articles
    # John Doe (3 articles in Tech Weekly)
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", ("AI in 2025", 1, 1))
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", ("Quantum Leap", 1, 1))
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", ("Future of Tech", 1, 1))

    # Jane Smith (1 article in Health Monthly)
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", ("Wellness Trends", 2, 2))

    # Bob (1 article in Tech Weekly)
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", ("Cybersecurity Basics", 3, 1))

    connection.commit()
    connection.close()

if __name__ == "__main__":
    seed()
