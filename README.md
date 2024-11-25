# Консольное приложение для работы с книгами

Это консольная утилита для управления книгами, предоставляющая функционал для добавления, удаления, поиска и обновления информации о книгах. Программа использует интерфейс командной строки для взаимодействия с пользователем и предоставляет простой способ работать с базой данных книг.

## Основные возможности

1. **Главное меню**:
   - В главном меню пользователь может выбрать одно из доступных действий:
     - Добавить книгу
     - Удалить книгу
     - Найти книгу
     - Просмотреть все книги
     - Обновить статус книги
     - Выйти из программы

2. **Добавление книги**:
   - Пользователь может ввести данные для новой книги (название, автор, год выпуска) и сохранить её в базе данных.

3. **Удаление книги**:
   - Для удаления книги необходимо ввести её ID. После успешного удаления, книга удаляется из базы данных.

4. **Поиск книги**:
   - Программа позволяет искать книги по части информации (автор, название, год выпуска).

5. **Просмотр всех книг**:
   - Пользователь может увидеть список всех книг, сохранённых в базе данных.

6. **Обновление статуса книги**:
   - Программа позволяет изменять статус книги (например, "в наличии" или "выдана").

7. **Выход из программы**:
   - Завершение работы программы.

## Установка

- Для выполнения основного кода нет требуются дополнительные зависимости за исключением предустановлено языка python = "^3.12".
- Копируем код:
```shell
git clone https://github.com/Miron-Anosov/console_test.git
```
- Запуск основного кода из корневой директории программы:
```shell
python -m src
```

- Для установки тестовых зависимостей и линтеров используйте [Poetry](https://python-poetry.org/). В корне проекта выполните следующие команды:

1. Установите зависимости:

```shell
poetry install
```

- Активируйте виртуальную среду:
```shell
poetry shell
```

- Запустите тесты с отчетом в консоли:
```shell
 poetry run pytest --cov=src --cov-report=term-missing
```
- Или можно просто посмотреть последние результаты тестов в отчете в директории  `htmlcov` запустив в своем браузере
[index.html](htmlcov/index.html)
###
#### Вы так же можете воспользоваться pip для установки зависимостей тестов:
- Создаем окружение:
```shell
python -m .venv venv
```
- Активируем:
```shell
source .venv/bin/activate
```
- Устанавливаем зависимости:
````shell
python -m pip install -r requirements.txt
````
- Запускаем тесты с отчетом в консоли:
```shell
coverage run -m pytest -v -s && coverage report --show-missing
```


Структура проекта

Проект состоит из нескольких модулей, каждый из которых отвечает за конкретную часть функционала:
```
src/
├── console_core/         # Основные модули для работы с консолью
│   ├── console.py        # Запуск программы
│   ├── utils/            # Утилиты (CRUD, ввод/вывод, навигация)
│   ├── ioconsole.py      # Модуль для ввода/вывода данных в консоль
│   ├── crud.py           # Логика работы с данными книг
│   ├── front.py          # Основной интерфейс для взаимодействия с пользователем
│   └── console_navigator.py # Навигация по меню
├── models/               # Модели данных
│   └── book.py           # Модель книги
├── tests/                # Тесты
│   └── unit/             # Юнит-тесты
├── pyproject.toml        # Конфигурация проекта
└── README.md             # Этот файл
```
Зависимости

При написании программы использовались следующие библиотеки:

    pytest: для тестирования
    black, flake8, isort: для форматирования кода и проверки стиля
    mypy: для проверки типов
    pre-commit: для настройки хуков
    poetry: для управления зависимостями