"""Front module of console."""

import logging
import sys
from collections.abc import Callable
from functools import partial

from src.console_core.utils.console_navigator import PointMenuPositions
from src.console_core.utils.coollors_text import FormatterColorText
from src.console_core.utils.crud import BookCRUD
from src.console_core.utils.ioconsole import ConsoleInput, ConsoleOutput

logger = logging.getLogger(__name__)


class ConsoleFront:
    """Main console worker."""

    def __init__(
        self,
        screener: "ConsoleOutput",
        io_cls: "ConsoleInput",
        crud: "BookCRUD",
    ) -> None:
        """Initialize dependencies."""
        self._screener = screener
        self._io = io_cls
        self._crud = crud

    def main_menu(self, invite_text_miss_button: bool | None = None) -> int:
        """Show main menu and get user input."""
        logger.debug("event main menu screener called.")
        while True:
            self._screener.main_menu_screen()
            cursor = self._io.menu_input()
            try:
                cursor = int(cursor)
            except ValueError:
                logger.debug(
                    "event main menu screener called with wrong message."
                )
                self._screener.main_menu_screen(
                    invite_text_miss_button=invite_text_miss_button
                )
            else:
                return PointMenuPositions.GET_MENU_BY_KEY.get(
                    str(cursor), PointMenuPositions.BACK_MENU_HELPER
                )

    def add_book(self) -> Callable:
        """Call controller to add a new book."""
        logger.debug("event add book called.")
        self._screener.add_book_screen()
        book = self._io.add_book_input_data()
        error = self._crud.add_book_input_data(book)

        if not error:
            return self._screener.add_book_successful_screen
        else:
            call = partial(self._screener.add_book_failed_screen, error)
            return call

    def back_menu(self, call_screen: Callable | None = None) -> int | str:
        """Return to the previous menu."""
        logger.debug("event back menu screener called.")
        self._screener.back_menu_screen(call_screen=call_screen)

        return PointMenuPositions.GET_MENU_BY_KEY.get(
            self._io.menu_input(),
            PointMenuPositions.BACK_MENU_HELPER,
        )

    def delete_book(self) -> Callable:
        """Call controller to delete a book."""
        logger.debug("event delete book called.")
        fail = None
        while True:
            self._screener.delete_book_by_id_screen(msg=fail)
            book_id = self._io.book_by_id()
            try:
                book_id = int(book_id)
                error = self._crud.delete_book_by_id(book_id=book_id)

                if not error:
                    return self._screener.delete_book_successful
                else:
                    result_action = partial(
                        self._screener.delete_book_failed_screen, error
                    )
                    return result_action

            except ValueError:
                logger.debug(
                    "event delete book screener called with wrong message."
                )
                fail = True

    def find_book(self):
        """Call controller to find a book."""
        logger.debug("event find book called.")
        self._screener.find_book_screen()
        position_key = None
        not_break = True
        text_error = "Use ony 1, 2, 3 position"

        while not_break:
            find_book_form_position = self._io.menu_input()

            try:
                position_key = int(find_book_form_position)
                if position_key not in PointMenuPositions.FORMS_FIND_POSITION:
                    raise ValueError(text_error)
                else:
                    not_break = False
            except ValueError as e:
                logger.debug(e)
                self._screener.find_book_screen(msg_err=text_error)
        else:
            find_value = self._io.find_book_input_data(
                position_form=position_key
            )
            books_or_str_err = self._crud.find_book_by_part_info(
                look_for_data=find_value
            )

            if isinstance(books_or_str_err, list):
                found_books = partial(
                    self._screener.find_book_successful, books_or_str_err
                )
                return found_books
            if isinstance(books_or_str_err, str):
                result_action = partial(
                    self._screener.delete_book_failed_screen, books_or_str_err
                )
                return result_action

    def select_all_book(self) -> Callable:
        """Call controller to select all books."""
        logger.debug("event select all book called.")
        all_books = self._crud.select_all_books()
        return partial(self._screener.find_book_successful, all_books)

    def update_book_status(self) -> Callable:
        """Call controller to update book status."""
        logger.debug("event update book status called.")

        fail_id = None
        while True:
            self._screener.update_book_screen_id(msg_err=fail_id)
            book_id = self._io.book_by_id()
            try:
                book_id = int(book_id)
            except ValueError:
                logger.debug(
                    "event update book ID screener called with wrong message."
                )
                fail_id = True

            else:

                num_status = 0
                fail_status = None
                not_break = True
                while not_break:
                    self._screener.update_book_screen_status(
                        msg_err=fail_status
                    )
                    num_status = self._io.menu_input()
                    try:
                        num_status = int(num_status)
                        if (
                            num_status
                            not in PointMenuPositions.STATUS_POSITION_CHOICES
                        ):
                            raise ValueError()
                    except ValueError:
                        logger.debug(
                            "event update book ID"
                            " screener called with wrong message."
                        )
                        fail_status = "Use ony 1 or 2 position please."

                    else:
                        not_break = False

                else:
                    status = (
                        PointMenuPositions.STATUS_ACTIVE
                        if num_status == PointMenuPositions.STATUS_ACTIVE
                        else PointMenuPositions.STATUS_NOT_ACTIVE
                    )
                    error = self._crud.update_status_book(
                        book_id=book_id, status=status
                    )
                    if not error:
                        return self._screener.update_book_successful_screen
                    else:
                        result_action = partial(
                            self._screener.update_book_failed_screen, error
                        )
                        return result_action

    def exit_console(self) -> None:
        """Exit the console."""
        logger.debug("event exit called.")
        self._screener.exit_menu_screen()
        sys.exit(0)

    def back_menu_halper_screen(self) -> Callable:
        """Show helper screen for wrong input."""
        logger.debug("event back menu with wrong screener called.")
        return self._screener.back_menu_context_info_helper


def make_front_console():
    """Return console front worker."""
    printer = FormatterColorText()
    io = ConsoleInput(printer=printer)
    crud = BookCRUD()
    screener = ConsoleOutput(printer=printer)

    return ConsoleFront(
        screener=screener,
        io_cls=io,
        crud=crud,
    )
