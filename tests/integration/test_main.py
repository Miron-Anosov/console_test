# type: ignore
"""Test main module."""

import pytest

from src.__main__ import main


@pytest.mark.all
@pytest.mark.main
def test_main_run(mocker) -> None:
    """Positive test init main function."""
    mocker.patch("src.main.ConsoleRunner.run", return_value=None)
    assert main() is None


@pytest.mark.all
@pytest.mark.main
@pytest.mark.integration
def test_main_with_input(monkeypatch) -> None:
    """Test main function with mocked input."""
    # Подменяем input, чтобы вместо ввода возвращалось '0'
    inputs = iter(["0"])  # Симулируем ввод команды выхода
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Перехватываем SystemExit, чтобы тест завершился корректно
    with pytest.raises(SystemExit) as exc_info:
        main()

    # Проверяем, что код выхода равен 0
    assert exc_info.value.code == 0


@pytest.mark.all
@pytest.mark.main
@pytest.mark.integration
@pytest.mark.parametrize(
    "script, inputs, expected_exit_code",
    [
        ("main_menu_and_exit", ["0"], 0),  # Сценарий выхода из главного меню
        (
            "main_menu_miss_&&_back_menu_and_exit",
            ["99", "0"],
            0,
        ),  # Сценарий выхода из главного меню
        (
            "invalid_input_then_exit",
            ["invalid", "0"],
            0,
        ),  # Некорректный ввод, затем выход
        ("keyboard_interrupt", ["^C"], 1),  # Симуляция прерывания
        (
            "main_menu_and_select_all_and_exit",
            ["4", "0"],
            0,
        ),  # Сценарий отображения всех книг
        (
            "main_menu_add_new_book_and_exit",
            ["1", "Иисус-младенец", "Есенин", "1918", "0"],
            0,
        ),  # Сценарий добавления книги
        (
            "main_menu_add_new_book_invalid_title_and_exit",
            ["1", "И", "Есенин", "1918", "0"],
            0,
        ),  # Сценарий добавления книги с невалидными Title
        (
            "main_menu_&&_find_book_by_auth_&&_and_exit",
            ["3", "1", "Есенин", "9", "0"],
            0,
        ),  # Сценарий поиск книг по автору
        (
            "main_menu_&&_find_book_by_title_with_error_&&_and_exit",
            ["3", "0", "2", "Иисус-младенец", "9", "0"],
            0,
        ),  # Сценарий поиск книг по заголовку с ошибкой выбора типа поиска
        (
            "main_menu_&&_find_book_by_empty_title_&&_and_exit",
            ["3", "2", " ", "9", "0"],
            0,
        ),  # Сценарий поиск книг по пустому заголовку
        (
            "main_menu_&&_find_book_by_year_&&_and_exit",
            ["3", "3", "1918", "9", "0"],
            0,
        ),  # Сценарий поиск книг по дате выпуска
        (
            "main_menu_&&_find_book_by_year_and_err_&&_and_exit",
            ["3", "4", "3", "1918", "9", "0"],
            0,
        ),  # Сценарий поиск книг по дате выпуска с ошибкой выбора
        (
            "main_menu_&&_new_status_book_by_id_&&_and_exit",
            ["5", "4", "1", "9", "0"],
            0,
        ),  # Сценарий изменения статуса книги по ID
        (
            "main_menu_&&_new_status_book_by_id_&&_and_exit",
            ["5", "4", "2", "9", "0"],
            0,
        ),  # Сценарий изменения статуса книги по ID
        (
            "main_menu_&&_new_status_try_again_book_by_id_&&_and_exit",
            ["5", "4", "3", "2", "9", "0"],
            0,
        ),  # Сценарий изменения статуса книги по ID
        (
            "main_menu_&&_new_status_book_by_string_id_&&_and_exit",
            ["5", "string", "1", "2", "9", "0"],
            0,
        ),  # Сценарий изменения статуса книги по string-ID
        (
            "main_menu_&&_new_status_book_by_invalid_id_&&_and_exit",
            ["5", "0", "1", "9", "0"],
            0,
        ),  # Сценарий изменения статуса книги по несуществующему ID
        (
            "main_menu_&&_del_book_by_id_&&_and_exit",
            ["2", "4", "9", "0"],
            0,
        ),  # Сценарий удаления книги по ID
        (
            "main_menu_&&_del_book_by_id_2_&&_and_exit",
            ["2", "4", "9", "0"],
            0,
        ),  # Сценарий удаления книги по ID которую уже удалили
        (
            "main_menu_&&_del_book_by_id_err_&&_and_exit",
            ["2", "invalid", "9", "0"],
            0,
        ),  # Сценарий удаления книги по ID c ошибкой
    ],
)
def test_main_with_input_and_match(
    monkeypatch, script, inputs, expected_exit_code
) -> None:
    """Parameterized test for main function with multiple scenarios."""
    # Подменяем input на последовательность вводов
    mock_inputs = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(mock_inputs))

    # Перехватываем SystemExit, чтобы тест завершился корректно
    with pytest.raises(SystemExit) as exc_info:
        match script:
            case "main_menu_and_exit":
                main()
            case "main_menu_miss_&&_back_menu_and_exit":
                main()
            case "invalid_input_then_exit":
                main()
            case "keyboard_interrupt":
                # Для KeyboardInterrupt эмулируем исключение
                monkeypatch.setattr(
                    "builtins.input",
                    lambda _: (_ for _ in ()).throw(KeyboardInterrupt),
                )
                main()
            case "main_menu_and_select_all_and_exit":
                main()
            case "main_menu_add_new_book_and_exit":
                main()
            case "main_menu_add_new_book_invalid_title_and_exit":
                main()
            case "main_menu_add_new_book_invalid_auth_and_exit":
                main()
            case "main_menu_&&_find_book_by_auth_&&_and_exit":
                main()
            case "main_menu_&&_find_book_by_title_&&_and_exit":
                main()
            case "main_menu_&&_find_book_by_empty_title_&&_and_exit":
                main()
            case "main_menu_&&_find_book_by_year_&&_and_exit":
                main()
            case "main_menu_&&_find_book_by_year_and_err_&&_and_exit":
                main()
            case "main_menu_&&_find_book_by_title_with_error_&&_and_exit":
                main()
            case "main_menu_&&_new_status_book_by_id_&&_and_exit":
                main()
            case "main_menu_&&_del_book_by_id_&&_and_exit":
                main()
            case "main_menu_&&_new_status_book_by_invalid_id_&&_and_exit":
                main()
            case "main_menu_&&_new_status_book_by_string_id_&&_and_exit":
                main()
            case "main_menu_&&_new_status_try_again_book_by_id_&&_and_exit":
                main()
            case "main_menu_&&_del_book_by_id_2_&&_and_exit":
                main()
            case "main_menu_&&_del_book_by_id_err_&&_and_exit":
                main()
            case _:
                pytest.fail(f"Unknown script.: {script}")

    # Проверяем, что код выхода совпадает с ожидаемым
    assert exc_info.value.code == expected_exit_code
