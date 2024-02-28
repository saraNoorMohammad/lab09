import unittest
from book_manager import Book, BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.manager = BookManager()
        self.book1 = Book("1234567890", "Book 1", "Author 1")
        self.book2 = Book("0987654321", "Book 2", "Author 2")
        # Add setup for test books here

    def test_add_book(self):
        # Test adding a book to the manager
        self.manager.add_book(self.book1)
        self.assertIn(self.book1, self.manager.books)

    def test_add_duplicate_book(self):
        # Test adding a book with a duplicate ISBN
        self.manager.add_book(self.book1)
        self.manager.add_book(self.book1)
        self.assertEqual(len(self.manager.books), 1)

    def test_remove_book(self):
        # Test removing a book from the manager
        self.manager.add_book(self.book1)
        self.manager.remove_book("1234567890")
        self.assertNotIn(self.book1, self.manager.books)

    def test_list_books(self):
        # Test listing all books in the manager
        self.manager.add_book(self.book1)
        self.manager.add_book(self.book2)
        books = self.manager.list_books()
        self.assertEqual(len(books), 2)
        self.assertIn(self.book1, books)
        self.assertIn(self.book2, books)

if __name__ == '__main__':
    unittest.main()
