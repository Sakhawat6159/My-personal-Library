import json
import os

class LibraryManager:
    def __init__(self, filename='library.json'):
        self.filename = filename
        self.load_library()

    def load_library(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.library = json.load(file)
        else:
            self.library = []

    def save_library(self):
        with open(self.filename, 'w') as file:
            json.dump(self.library, file, indent=4)

    def add_book(self, title, author, year, genre, read_status=False):
        book = {
            'title': title,
            'author': author,
            'year': year,
            'genre': genre,
            'read_status': read_status
        }
        self.library.append(book)
        self.save_library()

    def remove_book(self, title):
        self.library = [book for book in self.library if book['title'] != title]
        self.save_library()

    def search_books(self, query):
        return [book for book in self.library if query.lower() in book['title'].lower() or query.lower() in book['author'].lower()]

    def view_library(self):
        return self.library

    def mark_as_read(self, title):
        for book in self.library:
            if book['title'] == title:
                book['read_status'] = True
                self.save_library()
                break

    def statistics(self):
        total_books = len(self.library)
        read_books = len([book for book in self.library if book['read_status']])
        return total_books, read_books

if __name__ == "__main__":
    manager = LibraryManager()
    # Example usage
    manager.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
    print(manager.view_library())
