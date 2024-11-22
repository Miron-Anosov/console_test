"""Console color text formatter."""

COLORS = {
    "red": "\033[91m",
    "blue": "\033[94m",
    "yellow": "\033[93m",
    "cyan": "\033[96m",
    "underline": "\033[4m",
    "green": "\033[92m",
    "bright_green": "\033[32;1m",
    "reset": "\033[0m",
}


class FormatterColorText:
    """Formats text with colors for console output."""

    def __init__(self, text: str = ""):
        """Initialize the formatter.

        Args:
            text (str): The text to format. Defaults to an empty string.
        """
        self.text = text
        self._color_code = COLORS["reset"]

    def __call__(self, text: str) -> "FormatterColorText":
        """Set new text to format.

        Args:
            text (str): The text to format.

        Returns:
            FormatterColorText: The current instance.
        """
        self.text = text
        return self

    def yellow(self) -> "FormatterColorText":
        """Set yellow color."""
        self._color_code = COLORS["yellow"]
        return self

    def cyan(self) -> "FormatterColorText":
        """Set cyan color."""
        self._color_code = COLORS["cyan"]
        return self

    def green(self) -> "FormatterColorText":
        """Set green color."""
        self._color_code = COLORS["green"]
        return self

    def red(self) -> "FormatterColorText":
        """Set red color."""
        self._color_code = COLORS["red"]
        return self

    def blue(self) -> "FormatterColorText":
        """Set blue color."""
        self._color_code = COLORS["blue"]
        return self

    def underline(self) -> "FormatterColorText":
        """Set underline style."""
        self._color_code = COLORS["underline"]
        return self

    def bright_green(self) -> "FormatterColorText":
        """Set bright green color."""
        self._color_code = COLORS["bright_green"]
        return self

    def reset(self) -> "FormatterColorText":
        """Reset color to default."""
        self._color_code = COLORS["reset"]
        return self

    def build_text(self) -> str:
        """Get the formatted text.

        Returns:
            str: The text with applied color or style.
        """
        return f"{self._color_code}{self.text}{COLORS['reset']}"
