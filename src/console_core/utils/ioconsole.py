"""Navigation class for console interface."""

import logging
import os
from dataclasses import dataclass
from functools import partial
from typing import Callable

from src.console_core.utils.console_navigator import PointMenuPositions
from src.console_core.utils.coollors_text import FormatterColorText

logger = logging.getLogger(__name__)


class ConsoleOutput:
    """Handles console output for navigation menus."""

    def __init__(
        self, printer: FormatterColorText, version: str | None = None
    ):
        """
        Initialize ConsoleOutput.

        Args:
            printer: Formatter for colored text.
            version: Application version.
        """
        self._version: str = "0.0.1" if version is None else version
        self._printer = printer

    @staticmethod
    def _clear_screen():
        """Clear the console screen."""
        os.system("cls" if os.name == "nt" else "clear")

    def _exit_text(self) -> str:
        """Generate exit menu text."""
        return self._printer("0.exit").blue().build_text()

    def _back_text(self) -> str:
        """Generate back menu text."""
        return self._printer("9.back").blue().build_text()

    def _screen_footer(
        self,
        invite_text: str | None = None,
        call_screen: Callable | None = None,
    ) -> None:
        """
        Make footer in the menu.

        Args:
            invite_text: Instruction for the user.
            call_screen: Function to call before footer.
        """
        invite_text = invite_text or "Make a choice:"
        if call_screen and callable(call_screen):
            call_screen()

        output = self._printer(invite_text).blue().build_text()
        print(self._under_separator())
        print(f"{self._exit_text():^35}{self._back_text()}")
        print(self._separator())
        print(output)

    def _full_time_screen(self) -> Callable:
        """Make decorator to clear and prepare screen."""

        def decorator(func: Callable) -> Callable:
            def wrapper(*args, **kwargs):
                self._clear_screen()
                self._header_screen()
                func(*args, **kwargs)

            return wrapper

        return decorator

    def _separator(self) -> str:
        """Generate a separator line."""
        return self._printer("=" * 45).yellow().build_text()

    def _under_separator(self) -> str:
        """Generate an underline separator."""
        return self._printer("_" * 45).yellow().build_text()

    def _header_screen(self) -> None:
        """Make header with application info."""
        header_text = f"Console util v:{self._version}"
        header_view = self._printer(f"{header_text:^40}").yellow().build_text()
        print(header_view, self._separator(), sep="\n")

    def main_menu_screen(
        self, invite_text_miss_button: bool | None = None
    ) -> None:
        """
        Make the main menu.

        Args:
            invite_text_miss_button: Show message for invalid input.
        """

        @self._full_time_screen()
        def _main_menu():
            logger.debug("Call main menu")
            menu_items = self._generate_menu_items()
            print(self._make_menu_data(menu_items))

        _main_menu()

        # invite_msg = None
        # if invite_text_miss_button:
        #     invite_msg = (
        #         self._printer("Enter a value from the list above:")
        #         .red()
        #         .build_text()
        #     )

        self._screen_footer(
            # invite_text=invite_msg
        )

    def _generate_menu_items(self) -> tuple:
        """Generate menu items for main menu."""
        return (
            self._printer("1.Add book").blue().build_text(),
            self._printer("2.Del book by ID").blue().build_text(),
            self._printer("3.Find book").blue().build_text(),
            self._printer("4.Select all").blue().build_text(),
            self._printer("5.Update status book").blue().build_text(),
        )

    @staticmethod
    def _make_menu_data(data: tuple) -> str:
        """Format menu items for display."""
        text_to_display = ""
        for index, text in enumerate(data, 1):
            if index % 2 != 0 and index == len(data):
                text_to_display = "".join((text_to_display, f"{text:^55}"))
            elif index % 2 != 0:
                text_to_display = "".join((text_to_display, f"{text:^35}"))
            else:
                text_to_display = "".join((text_to_display, f"{text}\n"))

        return text_to_display.rstrip("\n")

    def exit_menu_screen(self) -> None:
        """Make the exit message."""
        logger.debug("Call exit menu")
        self._clear_screen()
        exit_screen = (
            self._printer("Program exited successfully").blue().build_text()
        )
        print(exit_screen)

    def add_book_screen(self) -> None:
        """Make the add book screen."""

        @self._full_time_screen()
        def _add_book():
            logger.debug("call add book")
            screen_instruction = (
                self._printer(
                    "Enter the information about "
                    "the book by filling out three forms:"
                )
                .underline()
                .build_text()
            )
            self._form_book(screen_instruction=screen_instruction)

        _add_book()

    def _generate_input_instruction_forms(self) -> tuple:
        """Generate input instructions for book forms."""
        return (
            self._printer("1.Author").underline().build_text(),
            self._printer("2.Title").underline().build_text(),
            self._printer("3.Year").underline().build_text(),
        )

    def _form_book(self, screen_instruction: str) -> None:
        """Make the form for entering book details."""
        forms = " ".join(
            form for form in self._generate_input_instruction_forms()
        )
        output_text = f"{screen_instruction}\n{forms}"
        print(output_text)

    def add_book_successful_screen(self) -> None:
        """Make the success screen after adding a book."""
        logger.debug("call add book successful screen.")
        success_screen = (
            self._printer("Successful added book").bright_green().build_text()
        )
        print(f"{success_screen:^45}")

    def add_book_failed_screen(self, msg: str) -> None:
        """Make the failure screen after an unsuccessful book addition."""
        logger.debug("call add book failed screen.")
        failed_screen = self._printer(f"Failed: {msg}").red().build_text()
        print(f"{failed_screen:^45}")

    def delete_book_by_id_screen(self, msg: bool | None = None) -> None:
        """Make the screen for deleting a book by ID."""

        @self._full_time_screen()
        def _delete_book_by_id():
            logger.debug("call delete book by ID screen")
            if msg:
                screen_instruction = (
                    self._printer("Enter valid book ID miss integer.")
                    .red()
                    .build_text()
                )
            else:
                screen_instruction = (
                    self._printer("Enter exist book ID:")
                    .underline()
                    .build_text()
                )
            print(screen_instruction)

        _delete_book_by_id()
        if msg:
            print(self._separator())

    def delete_book_successful(self) -> None:
        """Make the success screen after deleting a book."""
        logger.debug("call delete book successful screen.")
        success_screen = (
            self._printer("Successful deleted book")
            .bright_green()
            .build_text()
        )
        print(f"{success_screen:^45}")

    def delete_book_failed_screen(self, msg: str) -> None:
        """Make the failure screen after an unsuccessful book deletion."""
        logger.debug("call delete book screen")
        failed_screen = self._printer(f"Failed: {msg}").red().build_text()
        print(f"{failed_screen:^45}")

    def find_book_screen(self, msg_err: str | None = None) -> None:
        """Make the screen for searching a book."""

        @self._full_time_screen()
        def _find_book():
            logger.debug("call find book screen")
            screen_instruction = (
                self._printer(
                    "Enter the information for look for "
                    "the book by filling out one from three forms:"
                )
                .underline()
                .build_text()
            )

            self._form_book(screen_instruction=screen_instruction)

            if msg_err:
                print(self._printer(msg_err).red().build_text())

        _find_book()
        print(self._separator())

    def find_book_successful(self, books: list[str]) -> None:
        """Make the success screen after finding a book."""
        logger.debug("call find book successful screen.")
        success_screen = self._printer("Found:").bright_green().build_text()
        screen_books = "\n".join(
            (self._printer(book).bright_green().build_text() for book in books)
        )
        print(f"{success_screen:^45}")
        print(f"{screen_books:^45}")

    def update_book_screen_id(self, msg_err: bool | None = None):
        """Make the screen for updating a book by ID."""
        logger.debug("call update book ID screen.")
        self.delete_book_by_id_screen(msg=msg_err)

    def _generate_status(self) -> tuple:
        """Generate the options for book status update."""
        return (
            self._printer("1.в наличии").blue().build_text(),
            self._printer("2.выдана").blue().build_text(),
        )

    def update_book_screen_status(self, msg_err: str | None = None):
        """Make the screen for updating a book's status."""
        logger.debug("call update book status screen.")

        @self._full_time_screen()
        def _update_book_status():
            screen_instruction = (
                self._printer("Choice new status book:")
                .underline()
                .build_text()
            )
            text_update_menu = self._make_menu_data(self._generate_status())

            msg_except = ""

            if msg_err:
                msg_except = self._printer(msg_err).red().build_text()

            text_update_menu = (
                text_update_menu
                if msg_err is None
                else f"{text_update_menu}\n{msg_except}"
            )

            print(f"{screen_instruction:^45}")
            print(f"{text_update_menu:^45}")

        _update_book_status()
        print(self._separator())

    def update_book_successful_screen(self) -> None:
        """Make the screen the delete book successful."""
        logger.debug("call successful update book successful screen.")
        success_screen = (
            self._printer("Successful update book status")
            .bright_green()
            .build_text()
        )
        print(f"{success_screen:^45}")

    def update_book_failed_screen(self, msg: str) -> None:
        """Make the screen the delete book failed."""
        logger.debug("call fail update book status screen")
        failed_screen = self._printer(f"Failed: {msg}").red().build_text()
        print(f"{failed_screen:^45}")

    def back_menu_context_info_helper(self) -> None:
        """Make the screen back menu context."""
        logger.debug("call back menu context menu text.")
        instruction = (
            self._printer("Use exists interactive menu with: ")
            .underline()
            .build_text()
        )
        menu = (
            self._printer("1.Add book").underline().build_text(),
            self._printer("2.Del book by ID").underline().build_text(),
            self._printer("3.Find book").underline().build_text(),
            self._printer("4.Select all").underline().build_text(),
            self._printer("5.Update status book").underline().build_text(),
        )
        points_menu = " ".join(
            self._printer(form).reset().build_text() for form in menu
        )

        screen_all_text = f"{instruction}\n{points_menu}"
        print(screen_all_text)

    def back_menu_screen(
        self,
        call_screen: Callable | None = None,
    ) -> None:
        """Make the screen back menu text."""

        @self._full_time_screen()
        def _back_menu():
            logger.debug("call back menu screen")

            self._screen_footer(call_screen=call_screen)

        _back_menu()


class ConsoleInput:
    """Class for handling console input operations."""

    def __init__(self, printer: FormatterColorText) -> None:
        """
        Init the ConsoleInput class.

        Args:
            printer (FormatterColorText): An object responsible for
            formatting text for console output.
        """
        self._printer = printer
        self._book_forms = self._make_book_forms()

    def _make_book_forms(self):
        """
        Create input forms for gathering book data.

        Returns:
            InputForms: An object with predefined methods for
            entering book data.
        """
        author_text = self._printer("Author > ").blue().build_text()
        title_text = self._printer("Title > ").blue().build_text()
        year_text = self._printer("Year > ").blue().build_text()

        author = partial(input, author_text)
        title = partial(input, title_text)
        year = partial(input, year_text)

        @dataclass()
        class InputForms:
            """Helper class for book input forms."""

            author_form = author
            title_form = title
            year_form = year

        return InputForms

    def menu_input(self) -> str:
        """
        Input for selecting a menu option.

        Returns:
            str: The user-entered menu option.
        """
        input_ = self._printer("> ").blue().build_text()
        return input(input_)

    def add_book_input_data(self) -> dict[str, str]:
        """
        Collect data for adding a new book.

        Returns:
            dict[str, str]: A dictionary containing the book's data.
        """
        book = {
            "author": self._book_forms.author_form(),
            "title": self._book_forms.title_form(),
            "year": self._book_forms.year_form(),
        }

        logger.debug(f"Input data of book: {book}")
        return book

    def book_by_id(self) -> str:
        """
        Prompts the user to enter a book ID.

        Returns:
            str: The entered book ID.
        """
        input_ = self._printer("ID: ").blue().build_text()
        return input(input_)

    def find_book_input_data(self, position_form: int) -> str | None:
        """Give data for finding a book based on the selected form.

        Args:
            position_form (int): The index of the input form.

        Returns:
            str | None: The entered data, or None if the form is invalid.

        Raises:
            ValueError: If an invalid form index is provided.
        """
        match position_form:
            case PointMenuPositions.FORM_FIND_BOOK_AUTH:
                return self._book_forms.author_form()
            case PointMenuPositions.FORM_FIND_BOOK_TITLE:
                return self._book_forms.title_form()
            case PointMenuPositions.FORM_FIND_BOOK_YEAR:
                return self._book_forms.year_form()
            case _:
                raise ValueError(f"Invalid position form {position_form}")
