"""Console runner for the book utility."""

import logging

from src.console_core.utils.console_navigator import PointMenuPositions
from src.console_core.utils.front import ConsoleFront

logger = logging.getLogger(__name__)


class ConsoleRunner:
    """Manages console navigation and operations."""

    def __init__(self, console: ConsoleFront):
        """Initialize ConsoleRunner.

        Args:
            console (ConsoleFront): Console interface for user interaction.
        """
        self.console: ConsoleFront = console
        self.cursor = PointMenuPositions.MAIN_MENU
        self.last_cursor = PointMenuPositions.MAIN_MENU

    def run(self):
        """Start the console runner loop."""
        logger.info("Running the utility book.")

        while True:
            match self.cursor:
                case PointMenuPositions.MAIN_MENU:
                    self.last_cursor = self.cursor
                    self.cursor = self.console.main_menu()
                case PointMenuPositions.ADD_BOOK_MENU:
                    call_screen = self.console.add_book()
                    self.cursor = self.console.back_menu(call_screen)
                case PointMenuPositions.DELETE_BOOK_MENU:
                    call_screen = self.console.delete_book()
                    self.cursor = self.console.back_menu(call_screen)
                case PointMenuPositions.FIND_BOOK_MENU:
                    call_screen = self.console.find_book()
                    self.cursor = self.console.back_menu(call_screen)
                case PointMenuPositions.SELECT_BOOK_MENU:
                    call_screen = self.console.select_all_book()
                    self.cursor = self.console.back_menu(call_screen)
                case PointMenuPositions.UPDATE_BOOK_MENU:
                    call_screen = self.console.update_book_status()
                    self.cursor = self.console.back_menu(call_screen)
                case PointMenuPositions.EXIT_MENU:
                    self.console.exit_console()
                case PointMenuPositions.BACK_MENU:
                    self.cursor = PointMenuPositions.MAIN_MENU
                case _:
                    logger.debug("Default case: returning to main menu.")
                    call_screen = self.console.back_menu_halper_screen()
                    self.cursor = self.console.back_menu(call_screen)
