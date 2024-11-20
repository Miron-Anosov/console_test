"""First test."""

import pytest

from src.models.book import Book


@pytest.mark.all
def test_init_book() -> None:
    """Positive test init book."""
    book = Book(author="Author", title="Title", year="1990")
    assert book.author == "Author"
