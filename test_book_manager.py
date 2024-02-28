import unittest
from book_manager import Book, BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.manager = BookManager()
        # Add setup for test books here

    # Implement test methods here

if __name__ == '__main__':
    unittest.main()
