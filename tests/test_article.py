import pytest
from lib.models.article import Article
from lib.db.connection import get_connection

def setup_function():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT
        );
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author_id INTEGER,
            magazine_id INTEGER,
            FOREIGN KEY(author_id) REFERENCES authors(id),
            FOREIGN KEY(magazine_id) REFERENCES magazines(id)
        );

        DELETE FROM articles;
        DELETE FROM magazines;
        DELETE FROM authors;

        INSERT INTO authors (id, name) VALUES (1, 'Alice');
        INSERT INTO magazines (id, name, category) VALUES (1, 'Tech Today', 'Technology');
        INSERT INTO articles (id, title, author_id, magazine_id) 
        VALUES (1, 'AI and the Future', 1, 1);
    """)
    conn.commit()
    conn.close()


def teardown_function():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript("""
        DELETE FROM articles;
        DELETE FROM magazines;
        DELETE FROM authors;
    """)
    conn.commit()
    conn.close()

def test_article_find_by_id():
    article = Article.find_by_id(1)
    assert article.title == "AI and the Future"

def test_article_find_by_title():
    article = Article.find_by_title("AI and the Future")
    assert article.author_id == 1
    assert article.magazine_id == 1

def test_article_author_and_magazine():
    article = Article.find_by_id(1)
    assert article.author().name == "Alice"
    assert article.magazine().name == "Tech Today"

def test_pytest_usage():
    with pytest.raises(AttributeError):
        article = Article.find_by_id(1)
        article.non_existent_method()
