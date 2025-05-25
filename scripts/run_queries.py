import sqlite3

def run():
    conn = sqlite3.connect('articles.db')
    cursor = conn.cursor()

    # Create tables if they don't exist
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS magazines (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author_id INTEGER,
        magazine_id INTEGER,
        FOREIGN KEY(author_id) REFERENCES authors(id),
        FOREIGN KEY(magazine_id) REFERENCES magazines(id)
    );
    """)

    # Clear existing data and insert seed data
    cursor.executescript("""
    DELETE FROM articles;
    DELETE FROM magazines;
    DELETE FROM authors;

    INSERT INTO authors (id, name) VALUES (1, 'Alice');
    INSERT INTO magazines (id, name, category) VALUES (1, 'Tech Today', 'Technology');
    INSERT INTO articles (id, title, author_id, magazine_id) VALUES (1, 'AI and the Future', 1, 1);
    """)

    conn.commit()

    # Verify by selecting articles
    cursor.execute("SELECT id, title, author_id, magazine_id FROM articles;")
    articles = cursor.fetchall()

    print("Current articles in the database:")
    for article in articles:
        print(article)

    conn.close()

if __name__ == "__main__":
    run()
