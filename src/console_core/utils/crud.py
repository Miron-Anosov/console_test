"""Simple CRUD."""

import logging

from src.models.book import Book, InvalidInputBookData

logger = logging.getLogger(__name__)


class BookCRUD:
    """Simple CRUD for books."""

    @staticmethod
    def add_book_input_data(book_data: dict) -> str | None:
        """Add book input."""
        try:
            book = Book(**book_data)
            print(book)
        except InvalidInputBookData as e:
            logger.error(e)
            return str(e)

        return None

        # todo пишем в файл.

    @staticmethod
    def delete_book_by_id(book_id: str | int) -> str | None:
        """Delete book by id."""
        try:
            print(book_id)
        except InvalidInputBookData as e:
            logger.error(e)
            return str(e)
        return None

    @staticmethod
    def find_book_by_part_info(look_for_data: str) -> list[str] | str:
        """Find book by part info."""
        try:
            print(look_for_data)
            return [
                Book(
                    title="Collection", author="Pushkin", year="1990"
                ).__str__()
            ]
        except InvalidInputBookData as e:
            logger.error(e)
            return str(e)

    @staticmethod
    def select_all_books() -> list[str]:
        """Select all books."""
        return [
            Book(title="Collection", author="Pushkin", year="1990").__str__(),
            Book(
                title="WAR and Peace", author="Tolstoy", year="1991"
            ).__str__(),
        ]

    @staticmethod
    def update_status_book(book_id: str | int, status: str) -> str | None:
        """Update book status."""
        print(book_id, status)
        try:
            return None
        except InvalidInputBookData as e:
            logger.error(e)
            return str(e)
