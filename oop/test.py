# test.py
from operators import BookItem, LibraryCenter

# Create books
b1 = BookItem("Intro to AI", "Andrew Ng", "1112223334445", 4)
b2 = BookItem("Deep Learning", "Ian Goodfellow", "2223334445556", 2)

# Create library
lib = LibraryCenter("Tech Library")

# Add books
lib.register_book(b1)
lib.register_book(b2)

# List available books
print("=== Current Stock ===")
for item in lib.available_books():
    print(item)

# Borrow book
print("\n=== Borrow Test ===")
print(lib.lend_book("1112223334445"))
print(lib.lend_book("1112223334445"))

# Return book
print("\n=== Return Test ===")
print(lib.accept_return("1112223334445"))

# Search by title
print("\n=== Search Test ===")
print(lib.search_by_title("Intro to AI"))
