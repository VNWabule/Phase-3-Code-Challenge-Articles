import os
import sqlite3

def debug():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    db_path = os.path.join(project_root, "articles.db")

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    print("\n=== Authors ===")
    for row in cursor.execute("SELECT * FROM authors"):
        print(row)

    print("\n=== Magazines ===")
    for row in cursor.execute("SELECT * FROM magazines"):
        print(row)

    print("\n=== Articles ===")
    for row in cursor.execute("SELECT * FROM articles"):
        print(row)

    connection.close()

if __name__ == "__main__":
    debug()
