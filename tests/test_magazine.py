import pytest
from lib.models.magazine import Magazine
from lib.models.author import Author
from lib.models.article import Article
from lib.db.connection import get_connection

def setup_function():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript("""
        DELETE FROM articles;
        DELETE FROM magazines;
        DELETE FROM authors;
        INSERT INTO authors (id, name) VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Carol');
        INSERT INTO magazines (id, name, category) VALUES (1, 'Tech Today', 'Technology');
        INSERT INTO articles (id, title, author_id, magazine_id) VALUES 
            (1, 'AI and the Future', 1, 1),
            (2, 'Quantum Computing', 1, 1),
            (3, '5G Explained', 2, 1),
            (4, 'Machine Learning', 2, 1),
            (5, 'Cybersecurity', 2, 1),
            (6, 'IoT Trends', 3, 1);
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

def test_articles():
    mag = Magazine.find_by_id(1)
    articles = mag.articles()
    assert len(articles) == 6
    assert all(isinstance(article, Article) for article in articles)

def test_contributors():
    mag = Magazine.find_by_id(1)
    authors = mag.contributors()
    assert len(authors) == 3
    assert all(isinstance(author, Author) for author in authors)

def test_article_titles():
    mag = Magazine.find_by_id(1)
    titles = mag.article_titles()
    assert "AI and the Future" in titles
    assert len(titles) == 6

def test_contributing_authors():
    mag = Magazine.find_by_id(1)
    contributors = mag.contributing_authors()
    names = [a.name for a in contributors]
    assert "Bob" in names
    assert "Alice" not in names 

def test_top_publisher():
    mag = Magazine.find_by_id(1)
    top_author = mag.top_publisher()
    assert top_author.name == "Bob"
    assert isinstance(top_author, Author)


def test_pytest_usage():
    with pytest.raises(AttributeError):
        mag = Magazine.find_by_id(1)
        mag.non_existent_method()
