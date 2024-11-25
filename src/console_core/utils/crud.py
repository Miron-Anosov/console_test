"""Simple CRUD."""

import json
import logging
from pathlib import Path

from src.models.book import Book, InvalidInputBookData

logger = logging.getLogger(__name__)


class BookCRUD:
    """Simple CRUD for books."""

    OUT_PATH = Path(__file__).parent
    OUT_PATH.mkdir(exist_ok=True, parents=True)
    OUT_PATH = OUT_PATH.absolute()
    FILE_PATH = OUT_PATH / "books.json"

    def _read_books(self) -> list:
        """Read data from JSON-file."""
        try:
            with open(self.FILE_PATH, "r", encoding="utf-8") as file:
                logger.debug("Reading books from JSON-file.")
                return json.load(file)
        except FileNotFoundError:
            logger.error(f"File {self.FILE_PATH} not found.")
            return []
        except json.JSONDecodeError:
            logger.error("Invalid JSON file.")
            raise ValueError("File brake or incorrect.")

    def _save_books(self, books: list) -> None:
        """Save list of books in JSON-file."""
        with open(self.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(
                books, file, ensure_ascii=False, indent=4  # type: ignore
            )
        logger.debug("Books saved.")

    def add_book_input_data(self, book_data: dict) -> str | None:
        """Add book input."""
        try:
            book = Book(**book_data).to_dict()
            books = self._read_books()
            book["id"] = max((book_["id"] for book_ in books), default=0) + 1

            books.append(book)
            self._save_books(books)
            logger.debug("Books added.")

        except InvalidInputBookData as e:
            logger.error(e)
            return str(e)

        return None

    def delete_book_by_id(self, book_id: str | int) -> str | None:
        """Delete book by id."""
        try:
            books = self._read_books()
            updated_books = [book for book in books if book["id"] != book_id]

            if len(books) == len(updated_books):
                logger.debug("Books not deleted.")
                raise InvalidInputBookData(f"Book not found by ID {book_id} ")

            self._save_books(updated_books)
        except InvalidInputBookData as e:
            logger.error(e)
            return str(e)
        return None

    def find_book_by_part_info(self, look_for_data: str) -> list[str] | str:
        """Find book by part info."""
        books = self._read_books()
        if not books:
            return []
        return [
            Book(
                _id=book["id"],
                title=book["title"],
                author=book["author"],
                year=book["year"],
                status=book["status"],
            ).__str__()
            for book in books
            if look_for_data.lower() in book["title"].lower()
            or look_for_data.lower() in book["author"].lower()
            or look_for_data.lower() in book["year"]
        ]

    def select_all_books(self) -> list[str]:
        """Select all books."""
        books = self._read_books()
        if not books:
            return []
        return [
            Book(
                _id=book["id"],
                title=book["title"],
                author=book["author"],
                year=book["year"],
                status=book["status"],
            ).__str__()
            for book in books
        ]

    def update_status_book(
        self, book_id: str | int, status: str
    ) -> str | None:
        """Update book status."""
        try:
            books = self._read_books()

            for book in books:
                if book["id"] == book_id:
                    book["status"] = status
                    self._save_books(books)
                    return None

            logger.debug("Book updated status.")

            raise InvalidInputBookData(f"Book not found by ID {book_id}.")
        except InvalidInputBookData as e:
            logger.error(e)
            return str(e)
