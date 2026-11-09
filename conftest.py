import pytest
from playwright.sync_api import Page


@pytest.fixture(autouse=True)
def block_telemetry(page: Page):
    # Эти служебные запросы сайта не нужны для проверки входа и корзины.
    page.route("https://events.backtrace.io/**", lambda route: route.abort())
