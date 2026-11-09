import os
from urllib.parse import unquote, urlsplit

import pytest
from playwright.sync_api import Page


@pytest.fixture(autouse=True)
def block_third_party_telemetry(page: Page):
    # Сторонняя телеметрия сайта не нужна для проверки входа и корзины.
    page.route("https://events.backtrace.io/**", lambda route: route.abort())


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    # В некоторых средах интернет доступен только через системный прокси.
    # На обычном компьютере без этих переменных настройки не меняются.
    args = dict(browser_type_launch_args)
    address = os.environ.get("HTTPS_PROXY") or os.environ.get("HTTP_PROXY")
    if address:
        parts = urlsplit(address)
        server = f"{parts.scheme}://{parts.hostname}"
        if parts.port:
            server += f":{parts.port}"
        proxy = {"server": server}
        if parts.username:
            proxy["username"] = unquote(parts.username)
        if parts.password:
            proxy["password"] = unquote(parts.password)
        args["proxy"] = proxy
    return args
