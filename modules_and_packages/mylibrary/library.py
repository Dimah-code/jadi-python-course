class Library():
    books = []
    def __init__(self):
        pass
    
    def add_book(self, title, author):
        Library.books.append({'title': title, 'author': author})
        return f"Book {title} by {author} added!"
    
    def remove_book(self, title):
        Library.books.pop(title in Library.books)
        return f"Book {title} deleted!"
    
    def search_book(self, title):
        
        matches = [book for book in Library.books if book["title"] == title]
        return matches
    def show_books(self):
        print()
        for book in Library.books:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print()


if __name__ == "__main__":
    
    library = Library()
    
    opt = ""
    while opt != "0":
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search a book")
        print("4. List all books")
        print("0. Exit")
        
        opt = input("Choose an option: ")
        
        if opt == "1":
            title = input("Enter a title: ")
            author = input("Enter author: ")
            print(library.add_book(title, author))
        elif opt == "2":
            title = input("Enter book's title: ")
            print(library.remove_book(title))
        elif opt == "3":
            title = input("Enter book's title: ")
            print(library.search_book(title))
        elif opt == "4":
            library.show_books()
        elif opt == "0":
            continue
        else:
            print("Wrong option! (choose 1, 2, 3, 4, 0")
print("Program Closed")