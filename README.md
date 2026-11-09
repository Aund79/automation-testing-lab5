# Лабораторная работа 5

Тесты для учебного сайта [SauceDemo](https://www.saucedemo.com/). Используются Python, pytest и Playwright.

## Что проверяется

1. Поля логина и пароля и кнопка входа.
2. Вход с правильными данными.
3. Добавление рюкзака в корзину.
4. Ошибка при неправильном пароле.

Задания 4 и 5 в методичке повторяются, поэтому для них один тест.

## Запуск

Нужен Python 3.12. Команды для PowerShell из папки проекта:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m playwright install chromium
.\.venv\Scripts\python.exe -m pytest -v test_login.py
```

Чтобы видеть действия браузера:

```powershell
.\.venv\Scripts\python.exe -m pytest -v --headed --slowmo 700 test_login.py
```

## Проверка CI

После отправки изменений GitHub Actions сам устанавливает зависимости и запускает тесты. Результаты находятся во вкладке Actions.

Для заданий 7 и 11 в `EXPECTED_INVENTORY_URL` временно ставится `incorrect.html`. Тогда тест входа падает, потому что на самом деле открыт `inventory.html`. После проверки нужно вернуть правильный адрес.
