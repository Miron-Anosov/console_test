"""Book model."""

import abc
import json
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class InvalidInputBookData(ValueError):
    """Validation error for invalid input."""

    pass


class ValidString(abc.ABC):
    """Abstract base class for validating strings."""

    MAX_LENGTH: int
    MIN_LENGTH: int
    NOT_VALUE_MSG: str
    INCORRECT_VALUE_MSG: str
    INCORRECT_LENGTH_MSG: str

    def __get__(self, instance, owner) -> str:
        """Return instance."""
        return self.value

    def __set__(self, instance, value: str) -> None:
        """Validate common string."""
        if not isinstance(value, str):
            logger.debug(self.INCORRECT_VALUE_MSG)
            raise InvalidInputBookData(self.INCORRECT_VALUE_MSG)

        if len(value) < self.MIN_LENGTH or len(value) > self.MAX_LENGTH:
            raise InvalidInputBookData(self.INCORRECT_LENGTH_MSG)

        self.value = value


class ValidTitle(ValidString):
    """Title validation descriptor."""

    MAX_LENGTH = 300
    MIN_LENGTH = 3
    NOT_VALUE_MSG = "Значение должно быть заполнено"
    INCORRECT_VALUE_MSG = "Не корректное значение."
    INCORRECT_LENGTH_MSG = (
        f"Название должно содержать не менее {MIN_LENGTH}"
        f" и не более {MAX_LENGTH} символов."
    )


class ValidAuthor(ValidString):
    """Author validation descriptor."""

    MAX_LENGTH = 30
    MIN_LENGTH = 3
    NOT_VALUE_MSG = "Значение должно быть заполнено."
    INCORRECT_VALUE_MSG = "Не корректное значение."
    INCORRECT_LENGTH_MSG = (
        f"ИМЯ автора должно содержать не менее {MIN_LENGTH}"
        f" и не более {MAX_LENGTH} символов включая пробелы."
    )


class ValidYear:
    """Year descriptor."""

    MAX_YEAR = datetime.now().year
    INCORRECT_YEAR_MSG = "Значение должно быть положительным"
    INCORRECT_VALUE_MSG = "Значение должны быть числом."
    INCORRECT_YEAR_FUTURE_MSG = (
        "Дата не может иметь " "значение превышающее текущее."
    )

    def __get__(self, instance, owner) -> str:
        """Return year."""
        return self.value

    def __set__(self, instance, value: int | str) -> None:
        """Validate year."""
        try:
            value = int(value)
        except ValueError:
            logger.debug(self.INCORRECT_VALUE_MSG)
            raise InvalidInputBookData(self.INCORRECT_VALUE_MSG)

        if value > self.MAX_YEAR:
            logger.debug(self.INCORRECT_YEAR_FUTURE_MSG)
            raise InvalidInputBookData(self.INCORRECT_YEAR_FUTURE_MSG)

        value = str(value)

        self.value = value


class Book:
    """Book model."""

    _id_counter = 0
    DEFAULT_STATUS = "В наличии."

    title = ValidTitle()
    author = ValidAuthor()
    year = ValidYear()

    def __init__(self, title: str, author: str, year: int | str):
        """Init new book."""
        self.title = title
        self.author = author
        self.year = year
        self.status: str = self.DEFAULT_STATUS
        self.__class__._id_counter += 1
        self._id = self._id_counter

    def __str__(self):
        """Return book info."""
        return (
            f"{self._id} {self.title} {self.author}"
            f" {self.year} {self.status}"
        )

    def __repr__(self):
        """Return book info."""
        return (
            f"<{self.__class__.__name__}: ("
            f"id={self._id}, title={self.title}, "
            f"author={self.author}, year={self.year})> "
        )

    def to_json(self):
        """Return book Json."""
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=4)

    def to_dict(self):
        """Return book Dict."""
        return dict(
            id=self._id,
            title=self.title,
            author=self.author,
            year=self.year,
            status=self.status,
        )