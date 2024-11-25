"""Core navigation module."""


class PointMenuPositions:
    """Defines constants for menu navigation."""

    # Main menu options
    MAIN_MENU = 1
    ADD_BOOK_MENU = 2
    DELETE_BOOK_MENU = 3
    FIND_BOOK_MENU = 4
    UPDATE_BOOK_MENU = 5
    SELECT_BOOK_MENU = 6

    # Special menu actions
    EXIT_MENU = 0
    BACK_MENU = 9
    BACK_MENU_HELPER = 999

    # Find book form options
    FORM_FIND_BOOK_AUTH = 1
    FORM_FIND_BOOK_TITLE = 2
    FORM_FIND_BOOK_YEAR = 3

    FORMS_FIND_POSITION = (
        FORM_FIND_BOOK_AUTH,
        FORM_FIND_BOOK_TITLE,
        FORM_FIND_BOOK_YEAR,
    )

    # Menu mapping by key
    GET_MENU_BY_KEY = {
        "1": ADD_BOOK_MENU,
        "2": DELETE_BOOK_MENU,
        "3": FIND_BOOK_MENU,
        "4": SELECT_BOOK_MENU,
        "5": UPDATE_BOOK_MENU,
        "9": BACK_MENU,
        "0": EXIT_MENU,
    }

    # Book status choices
    STATUS_POSITION_CHOICES = (1, 2)
    STATUS_ACTIVE = "в наличии"
    STATUS_ACTIVE_NUM = 1
    STATUS_NOT_ACTIVE = "выдана"

    GET_STATUS = {"1": STATUS_ACTIVE, "2": STATUS_NOT_ACTIVE}
