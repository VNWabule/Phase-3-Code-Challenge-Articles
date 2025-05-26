import sys
from lib.models.author import Author
from lib.models.magazine import Magazine

def list_authors():
    authors = Author.all()
    if not authors:
        print("No authors found.")
    for author in authors:
        print(f"- {author.name}")

def list_magazines():
    magazines = Magazine.all()
    if not magazines:
        print("No magazines found.")
    for mag in magazines:
        print(f"- {mag.name} ({mag.category})")

def show_top_publisher():
    mag_id = input("Enter magazine ID: ")
    try:
        mag = Magazine.find_by_id(int(mag_id))
        if mag:
            top_author = mag.top_publisher()
            if top_author:
                print(f"Top publisher for '{mag.name}' is {top_author.name}")
            else:
                print("No articles found for this magazine.")
        else:
            print("Magazine not found.")
    except ValueError:
        print("Please enter a valid numeric ID.")

def main_menu():
    while True:
        print("\nWelcome to the Magazine CLI!")
        print("1. List all authors")
        print("2. List all magazines")
        print("3. Show top publisher for a magazine")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_authors()
        elif choice == "2":
            list_magazines()
        elif choice == "3":
            show_top_publisher()
        elif choice == "4":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
