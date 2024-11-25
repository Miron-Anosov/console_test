# type: ignore
"""First test."""

from datetime import datetime

import pytest

from src.models.book import Book, InvalidInputBookData


@pytest.mark.all
@pytest.mark.book
@pytest.mark.unit
def test_init_book() -> None:
    """Positive test init book."""
    book = Book(author="Author", title="Title", year="1990")
    assert book.__str__()
    assert book.__repr__()
    assert book.author == "Author"
    assert book.title == "Title"
    assert book.year == "1990"


@pytest.mark.all
@pytest.mark.book
@pytest.mark.unit
def test_init_book_with_author_incorrect() -> None:
    """Negative test init book with author."""
    with pytest.raises(InvalidInputBookData):
        Book(author="Au", title="Title", year="1990")


@pytest.mark.all
@pytest.mark.book
@pytest.mark.unit
def test_init_book_with_very_long_title() -> None:
    """Negative test init book with very long title."""
    title = "Title" * 61  # len max 300
    with pytest.raises(InvalidInputBookData):
        Book(author="Author", title=title, year="1990")


@pytest.mark.all
@pytest.mark.book
@pytest.mark.unit
def test_init_book_with_very_long_author_name() -> None:
    """Negative test init book with very long author name."""
    author = "Author" * 6  # len max 30
    with pytest.raises(InvalidInputBookData):
        Book(author=author, title="Title", year="1990")


@pytest.mark.all
@pytest.mark.book
@pytest.mark.unit
def test_init_book_with_future_year() -> None:
    """Negative test init book with future year."""
    year = datetime.now().year + 1
    with pytest.raises(InvalidInputBookData):
        Book(author="Author", title="Title", year=year)


@pytest.mark.all
@pytest.mark.book
@pytest.mark.unit
def test_init_book_with_invalid_year() -> None:
    """Negative test init book with invalid year."""
    year = "Одна тысяча девятьсот девяностый"
    with pytest.raises(InvalidInputBookData):
        Book(author="Author", title="Title", year=year)


@pytest.mark.all
@pytest.mark.book
@pytest.mark.unit
def test_init_book_with_title_incorrect() -> None:
    """Negative test init book with title."""
    with pytest.raises(ValueError):
        Book(author="Author", title="Ti", year="1990")


@pytest.mark.all
@pytest.mark.book
@pytest.mark.unit
def test_init_book_with_invalid_val() -> None:
    """Negative test init book with invalid val."""
    with pytest.raises(InvalidInputBookData):
        Book(author="Author", title=None, year="1990")  # type: ignore


@pytest.mark.all
@pytest.mark.book
@pytest.mark.unit
def test_init_book_with_year_too_many_integers() -> None:
    """Negative test init book with invalid val."""
    with pytest.raises(InvalidInputBookData):
        Book(author="Author", title="Ti", year="19900")


@pytest.mark.all
@pytest.mark.book
@pytest.mark.unit
def test_init_book_with_invalid_year_is_empty() -> None:
    """Negative test init book with invalid val."""
    with pytest.raises(InvalidInputBookData):
        Book(author="Author", title="Ti", year="")


@pytest.mark.all
@pytest.mark.book
@pytest.mark.unit
def test_init_book_without_init_param() -> None:
    """Negative test init book with title."""
    with pytest.raises(TypeError):
        Book(title="Title", year="1990")  # type: ignore

    with pytest.raises(TypeError):
        Book(title="Title", year="1990")  # type: ignore

    with pytest.raises(TypeError):
        Book(title="Title", author="Author")  # type: ignore


@pytest.mark.all
@pytest.mark.book
@pytest.mark.unit
def test_book_to_json() -> None:
    """Negative test to_json method."""
    book = Book(author="Author", title="Title", year="1990")
    jbook = book.to_json()
    assert jbook != {}


@pytest.mark.all
@pytest.mark.book
@pytest.mark.unit
def test_book_from_json() -> None:
    """Positive test from_json method."""
    book = Book(author="Author", title="Title", year="1990")
    assert len(book.to_json()) != 0


@pytest.mark.all
@pytest.mark.book
@pytest.mark.unit
def test_book_from_dict() -> None:
    """Positive test from_dict method."""
    book = Book(author="Author", title="Title", year="1990")
    assert len(book.to_dict()) != 0
