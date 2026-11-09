# Лабораторная работа 5

Автоматизированное UI-тестирование SauceDemo на Python, pytest и Playwright.

## Проверки

1. Отображение логина, пароля и кнопки входа.
2. Успешный вход и переход на `inventory.html`.
3. Добавление Sauce Labs Backpack: индикатор `1`, название и количество в корзине.
4. Отказ входа с неправильным паролем и текст ошибки.

В заданиях 4 и 5 методички приведена одна и та же функция, поэтому она добавлена один раз. Каждый тест получает отдельный контекст браузера от pytest-playwright.

## Запуск в Windows PowerShell

Открой PowerShell в папке проекта. Нужен Python 3.12; для запуска команд активация окружения не требуется.

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

Первый тест отдельно:

```powershell
.\.venv\Scripts\python.exe -m pytest -v test_login.py::test_login_page_is_displayed
```

Отчёт HTML, XML и снимки:

```powershell
.\.venv\Scripts\python.exe -m pytest -v test_login.py --screenshot on --tracing retain-on-failure --html reports/report.html --self-contained-html --junitxml reports/results.xml
```

## GitHub Actions

Workflow находится в `.github/workflows/tests.yml`. Запускается при `push`, `pull_request` и вручную (`workflow_dispatch`). Он устанавливает Python 3.12, зависимости и Chromium, запускает тесты и сохраняет результаты на 14 дней. Для записи в репозиторий workflow не запрашивает прав.

В `conftest.py` есть поддержка стандартных переменных `HTTPS_PROXY` и `HTTP_PROXY`. Если они не заданы, Playwright запускается с обычными настройками. Проверка сертификатов не отключается.

В тестовом браузере блокируются запросы сторонней телеметрии `events.backtrace.io`. Все проверки интерфейса выполняются на настоящем SauceDemo.

## Демонстрация ошибки в заданиях 7 и 11

1. Сначала выполни исправный набор тестов.
2. В `test_login.py` измени только константу `EXPECTED_INVENTORY_URL`: замени `inventory.html` на `incorrect.html`.
3. Запусти тесты. Проверка успешного входа должна завершиться `FAILED`: ожидается `incorrect.html`, но открыт `inventory.html`.
4. Закоммить изменение и отправь его в GitHub, дождись завершения Actions.
5. Верни в константе `inventory.html`, повтори запуск, коммит и отправку.
6. Дождись успешного CI. Итоговый код должен содержать правильный адрес.

## Первое размещение

Создай пустой репозиторий GitHub и выполни в папке проекта команды, подставив его настоящий URL:

```powershell
git init -b main
git add .
git commit -m "Add automated UI tests and GitHub Actions"
git remote add origin https://github.com/ИМЯ/РЕПОЗИТОРИЙ.git
git push -u origin main
```

В коммиты не добавляются `.venv`, кеши и результаты прогонов. Если репозиторий и коммиты уже созданы, повторять `git init` и добавление `origin` не нужно.
