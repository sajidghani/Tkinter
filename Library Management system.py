class Library:
    def __init__(self):
        # Initialize an empty list to store the books in the library
        self.books = []

    def add_book(self, book_name):
        # Add a book to the library
        self.books.append(book_name)
        print(f"'{book_name}' has been added to the library.")

    def remove_book(self, book_name):
        # Remove a book from the library if it exists
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"'{book_name}' has been removed from the library.")
        else:
            print(f"'{book_name}' is not available in the library.")

    def search_book(self, book_name):
        # Search for a book in the library
        if book_name in self.books:
            print(f"'{book_name}' is available in the library.")
        else:
            print(f"'{book_name}' is not available in the library.")

    def display_books(self):
        # Display all books in the library
        if self.books:
            print("Books currently available in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("The library is empty.")


# Example usage of the Library class

library = Library()

# Add books to the library
library.add_book("The Great Gatsby")
library.add_book("1984")
library.add_book("To Kill a Mockingbird")

# Display all books in the library
library.display_books()

# Search for a book
library.search_book("1984")
library.search_book("Moby Dick")

# Remove a book
library.remove_book("1984")
library.remove_book("The Catcher in the Rye")

# Display updated list of books
library.display_books()
