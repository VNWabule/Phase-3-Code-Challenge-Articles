import pytest
from lib.models.author import Author
from lib.models.article import Article
from lib.models.magazine import Magazine
from lib.db.connection import get_connection

def setup_function():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript("""
        DELETE FROM articles;
        DELETE FROM magazines;
        DELETE FROM authors;
        INSERT INTO authors (id, name) VALUES (1, 'Alice'), (2, 'Bob');
        INSERT INTO magazines (id, name, category) VALUES (1, 'Tech Today', 'Technology'), (2, 'Health Weekly', 'Health');
        INSERT INTO articles (id, title, author_id, magazine_id) VALUES 
            (1, 'AI and the Future', 1, 1),
            (2, 'Healthy Living', 1, 2),
            (3, 'Quantum Computing', 1, 1),
            (4, 'Mindfulness', 2, 2);
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

def test_author_articles():
    author = Author.find_by_id(1)
    articles = author.articles()
    assert len(articles) == 3
    assert all(isinstance(article, Article) for article in articles)

def test_author_magazines():
    author = Author.find_by_id(1)
    magazines = author.magazines()
    assert len(magazines) == 2
    assert all(isinstance(mag, Magazine) for mag in magazines)

def test_add_article():
    author = Author.find_by_id(1)
    new_article = author.add_article(Magazine.find_by_id(2), "Sleep Science")
    assert new_article.title == "Sleep Science"
    assert new_article.author_id == 1
    assert new_article.magazine_id == 2

def test_topic_areas():
    author = Author.find_by_id(1)
    topics = author.topic_areas()
    assert set(topics) == {"Technology", "Health"}

def test_pytest_usage():
    with pytest.raises(AttributeError):
        author = Author.find_by_id(1)
        author.non_existent_method()
