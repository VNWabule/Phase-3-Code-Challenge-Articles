# Phase-3-Code-Challenge-Articles
This project models a publishing system with Articles, Authors, and Magazines using Python and SQLite. It demonstrates working with relational databases, writing SQL schema and seed scripts, and performing queries through Python classes.

---

## Features
- Authors can write multiple articles.
- Articles belong to one magazine.
- Magazines have multiple articles from different authors.
- Uses Python classes to wrap database operations with raw SQL.

---

## Setup Instructions

1. **Clone the Repository**
    ```bash
    git clone git@github.com:VNWabule/Phase-3-Code-Challenge-Articles.git
    cd Phase-3-Code-Challenge-Articles

2. **Install Dependencies**
     ```bash
    pipenv install pytest sqlite3

3. **Activate the Virtual Environment**
    ```bash
    pipenv shell

4. **Seed the Database**
    ```bash
    python lib/db/seed.py

5. **View Database Content**
    ```bash
    python lib/debug.py

---

## How to Access the CLI

1. Make sure you've seeded the database before using the CLI
   ```bash
   python lib/db/seed.py
2. Run the CLI tool using the -m flag
   ```bash
   python -m lib.cli

   
