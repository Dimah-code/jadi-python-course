"""
Library Manager Program
"""

from typing import List, Dict


class Library:
    """
    A class to manage a collection of books.

    Attributes:
        books (list): A list of dictionaries where each dictionary
                      contains 'title' and 'author' keys.
    """

    def __init__(self) -> None:
        """Initialize the library with an empty book list."""
        self.books: List[Dict[str, str]] = []

    def add_book(self, title: str, author: str) -> str:
        """
        Add a book to the library.

        Args:
            title (str): Title of the book.
            author (str): Author of the book.

        Returns:
            str: A success message.
        """
        self.books.append({"title": title, "author": author})
        return f"Book '{title}' by {author} added!"

    def remove_book(self, title: str) -> str:
        """
        Remove a book by its title.

        Args:
            title (str): Title of the book to remove.

        Returns:
            str: A success or failure message.
        """
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                return f"Book '{title}' removed!"
        return f"No book found with title '{title}'."

    def search_book(self, title: str) -> List[Dict[str, str]]:
        """
        Search for books by title.

        Args:
            title (str): Title of the book to search.

        Returns:
            list: A list of matching books with their title and author.
        """
        return [book for book in self.books if book["title"] == title]

    def show_books(self) -> None:
        """
        Print all books in the library.

        Returns:
            None
        """
        if not self.books:
            print("No books available.")
            return

        for book in self.books:
            print(f"Title: {book['title']}, Author: {book['author']}")


def main() -> None:
    """
    Run the library management system with a simple menu.
    """
    library = Library()

    print("\n--- Library Menu ---")
    while True:

        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search a book")
        print("4. List all books")
        print("0. Exit")

        option = input("Choose an option: ")

        if option == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            print(library.add_book(title, author))
        elif option == "2":
            title = input("Enter book's title: ")
            print(library.remove_book(title))
        elif option == "3":
            title = input("Enter book's title: ")
            matches = library.search_book(title)
            if matches:
                for book in matches:
                    print(f"Found -> Title: {book['title']}, Author: {book['author']}")
            else:
                print("No matches found.")
        elif option == "4":
            library.show_books()
        elif option == "0":
            print("Program Closed")
            break
        else:
            print("Invalid option! Choose 1, 2, 3, 4, or 0.")


if __name__ == "__main__":
    main()
