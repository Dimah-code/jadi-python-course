from mylibrary.library import Library

lib = Library()

print(lib.add_book("Python", "Jamilah"))
print(lib.add_book("Ricky and morty", "Sima"))
print(lib.add_book("Kafka", "sima"))
print(lib.add_book("Kafka", "asghar"))
print(lib.add_book("1984", "Goerge Orvell"))

lib.show_books()

print(lib.search_book("Kafka"))

print(lib.remove_book("Mold"))

print(lib.add_book("Linux", "Linus"))

lib.show_books()
