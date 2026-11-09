from playwright.sync_api import Page, expect


BASE_URL = "https://www.saucedemo.com/"
# В заданиях 7 и 11 временно меняем inventory.html на incorrect.html.
EXPECTED_INVENTORY_URL = "https://www.saucedemo.com/inventory.html"


def test_login_page_is_displayed(page: Page):
    # Задание 2. Проверяем форму входа.
    page.goto(BASE_URL)
    expect(page.locator('[data-test="username"]')).to_be_visible()
    expect(page.locator('[data-test="password"]')).to_be_visible()
    expect(page.locator('[data-test="login-button"]')).to_be_visible()


def test_successful_login(page: Page):
    # Задание 3. Вход с правильными данными.
    page.goto(BASE_URL)
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    expect(page).to_have_url(EXPECTED_INVENTORY_URL)
    expect(page.locator('[data-test="inventory-container"]')).to_be_visible()


def test_add_product_to_cart(page: Page):
    # Задания 4 и 5 в методичке одинаковые, поэтому тест один.
    page.goto(BASE_URL)
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    expect(page.locator('[data-test="inventory-container"]')).to_be_visible()

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("1")

    # Открываем корзину и проверяем добавленный товар.
    page.locator('[data-test="shopping-cart-link"]').click()
    expect(page).to_have_url(BASE_URL + "cart.html")
    cart_item = page.locator('[data-test="cart-list"]').locator(
        '[data-test="inventory-item"]'
    )
    expect(cart_item).to_have_count(1)
    expect(cart_item.locator('[data-test="inventory-item-name"]')).to_have_text(
        "Sauce Labs Backpack"
    )
    expect(cart_item.locator('[data-test="item-quantity"]')).to_have_text("1")


def test_login_with_invalid_password(page: Page):
    # Задание 6. Вход с неправильным паролем.
    page.goto(BASE_URL)
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("wrong_password")
    page.locator('[data-test="login-button"]').click()

    error = page.locator('[data-test="error"]')
    expect(error).to_be_visible()
    expect(error).to_contain_text("Username and password do not match")
    expect(page).to_have_url(BASE_URL)
