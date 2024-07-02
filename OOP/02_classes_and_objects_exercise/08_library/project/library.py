from typing import List, Dict
from project.user import User

class Library:

    def __init__(self):
        self.user_records: List[User] = [] # List of objects
        self.books_available: Dict[str: List[str]] = {} # Dict of {author: [available_books]}
        self.rented_books: Dict[str: Dict[str: int]] = {} # Dict of {username: {book_names: days_to_return: int}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        for record in self.rented_books.values():

            if book_name in record:
                days = record[book_name]
                return f'The book "{book_name}" is already rented and will be available in {days} days!'

        for author, books in self.books_available.items():
            if book_name in books:
                user.books.append(book_name)
                self.books_available.pop(book_name)
                self.rented_books[user.username][book_name] = days_to_return

                return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, user: User) -> str:
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            self.rented_books[user.username].remove(book_name)

        return f"{user.username} doesn't have this book in his/her records!"



