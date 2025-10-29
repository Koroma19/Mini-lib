# demo.py
from operators import BookItem, LibraryCenter

# Create book objects
book1 = BookItem("The Journey of Life", "mohamed kamara", "1234577777", 5)
book2 = BookItem("The Great Adventure", "Harper Lee", "9876543210", 3)

# Create a library
main_library = LibraryCenter("City Public Library")

# Add books
main_library.register_book(book1)
main_library.register_book(book2)

# Display available books
print("=== Available Books ===")
for book in main_library.available_books():
    print(book)

# Borrow books
print("\n=== Borrowing ===")
print(main_library.lend_book("1234567890123"))
print(main_library.lend_book("1234567890123"))

# Try to borrow until none left
for _ in range(5):
    print(main_library.lend_book("1234567890123"))

# Return a book
print("\n=== Returning ===")
print(main_library.accept_return("1234567890123"))

# Search book
print("\n=== Search Result ===")
search_result = main_library.search_by_title("The Journey of Life")

if isinstance(search_result, str):
    print(search_result)
else:
    for code, info in search_result:
        print(f"ISBN: {code} | {info}")

# Display final available books
print("\n=== Final Stock ===")
for book in main_library.available_books():
    print(book)
