from lib.db.connection import get_connection

class Author:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    @classmethod
    def all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        rows = cursor.execute("SELECT * FROM authors").fetchall()
        return [cls(id=row[0], name=row[1]) for row in rows]
    
    def __repr__(self):
        return f"<Author {self.id}: {self.name}>"

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            return cls(*row)

    def articles(self):
        from lib.models.article import Article 
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        rows = cursor.fetchall()
        return [Article(*row) for row in rows]

    def magazines(self):
        from lib.models.magazine import Magazine 
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON a.magazine_id = m.id
            WHERE a.author_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        return [Magazine(*row) for row in rows]

    def add_article(self, magazine, title):
        from lib.models.article import Article
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                       (title, self.id, magazine.id))
        conn.commit()
        return Article.find_by_title(title)

    def topic_areas(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.category FROM magazines m
            JOIN articles a ON a.magazine_id = m.id
            WHERE a.author_id = ?
        """, (self.id,))
        return [row[0] for row in cursor.fetchall()]
    
    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        row = cursor.execute("SELECT * FROM authors WHERE name = ?", (name,)).fetchone()
        if row:
            return cls(id=row[0], name=row[1])
        return None
    
    @classmethod
    def top_author(cls):
        conn = get_connection()
        cursor = conn.cursor()
        row = cursor.execute("""
            SELECT authors.*, COUNT(articles.id) as article_count
            FROM authors
            JOIN articles ON authors.id = articles.author_id
            GROUP BY authors.id
            ORDER BY article_count DESC
            LIMIT 1
        """).fetchone()
        if row:
            return cls(id=row[0], name=row[1])
        return None


