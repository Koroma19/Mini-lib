# operators.py

class BookItem:
    """Represents a single book in the library."""
    def __init__(self, name, writer, code, copies):
        self.name = name
        self.writer = writer
        self.code = code
        self.copies = copies
        self.available = copies

    def info(self):
        """Return book information."""
        return f"Title: {self.name}, Author: {self.writer}, ISBN: {self.code}, Available: {self.available}/{self.copies}"

    def borrow(self):
        """Borrow a book (reduce available count)."""
        if self.available > 0:
            self.available -= 1
            return True
        return False

    def give_back(self):
        """Return a borrowed book (increase available count)."""
        if self.available < self.copies:
            self.available += 1
            return True
        return False

    def update_isbn(self, new_code):
        """Update the book’s ISBN after validation."""
        if len(new_code) == 13 and new_code.isdigit():
            self.code = new_code
        else:
            print("Error: ISBN must be 13 digits.")

    def change_copies(self, new_total):
        """Reset total and available copies."""
        if new_total > 0:
            self.copies = new_total
            self.available = new_total
        else:
            print("Invalid number of copies.")


class LibraryCenter:
    """Handles library operations such as add, search, borrow, and return."""
    def __init__(self, library_name):
        self.library_name = library_name
        self.collection = {}

    def register_book(self, book):
        """Add a new book to the collection."""
        self.collection[book.code] = book

    def delete_book(self, code):
        """Remove a book from the collection."""
        if code in self.collection:
            del self.collection[code]
        else:
            print("Book not found in the system.")

    def search_by_title(self, name):
        """Search for a book by title."""
        matches = [(book.code, book.info()) for book in self.collection.values() if book.name.lower() == name.lower()]
        return matches if matches else "No matching titles found."

    def available_books(self):
        """Return list of books that are currently available."""
        stock = [book.info() for book in self.collection.values() if book.available > 0]
        return stock if stock else "No books available."

    def lend_book(self, code):
        """Borrow a book by ISBN."""
        if code in self.collection:
            if self.collection[code].borrow():
                return f"'{self.collection[code].name}' has been borrowed."
            else:
                return f"No more copies of '{self.collection[code].name}' left."
        return "Book not found."

    def accept_return(self, code):
        """Return a book by ISBN."""
        if code in self.collection:
            if self.collection[code].give_back():
                return f"'{self.collection[code].name}' successfully returned."
            else:
                return f"All copies of '{self.collection[code].name}' are already in stock."
        return "Book not found."
