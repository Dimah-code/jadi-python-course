from mylibrary.library import Library

library = Library()

print(library.add_book("Python", "Jamilah"))
print(library.add_book("Ricky and morty", "Sima"))
print(library.add_book("Kafka", "sima"))
print(library.add_book("Kafka", "asghar"))
print(library.add_book("1984", "Goerge Orvell"))

library.show_books()

print(library.search_book("Kafka"))

print(library.remove_book("Mold"))

print(library.add_book("Linux", "Linus"))

library.show_books()
