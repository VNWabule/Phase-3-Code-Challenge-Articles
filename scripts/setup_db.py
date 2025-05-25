from lib.db.connection import get_connection

def setup():
    conn = get_connection()
    with open("lib/db/schema.sql") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    setup()
