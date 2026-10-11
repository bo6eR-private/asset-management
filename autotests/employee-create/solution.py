import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TEST_URL = os.getenv("TEST_URL")
SELENIUM = os.getenv("SELENIUM_HUB")

@pytest.fixture(scope="module")
def driver():
    """Создаёт экземпляр браузера Chrome перед тестами и закрывает после."""
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,800")
    driver = webdriver.Remote(SELENIUM, options=options)
    yield driver
    driver.quit()


def test_page_title_is_correct(driver):
    """Проверяет заголовок страницы 'Добавление сотрудника'."""
    driver.get(TEST_URL)

    headings = driver.find_elements(By.TAG_NAME, "h1")
    assert headings, "На странице отсутствует заголовок <h1>"

    actual_title = headings[0].text.strip()
    expected_title = "Добавление сотрудника"

    assert actual_title == expected_title, (
        f"Неверный заголовок: ожидался '{expected_title}', "
        f"получен '{actual_title}'"
    )


def test_submit_button_exists(driver):
    """Проверяет наличие кнопки 'Добавить сотрудника'."""
    driver.get(TEST_URL)

    buttons = driver.find_elements(
        By.XPATH,
        "//button[contains(normalize-space(.), 'Добавить сотрудника')]"
    )

    assert buttons, "Кнопка «Добавить сотрудника» отсутствует на странице"
    assert buttons[0].is_displayed(), (
        "Кнопка «Добавить сотрудника» не отображается"
    )


def test_cancel_button_exists(driver):
    """Проверяет наличие ссылки 'Отмена'."""
    driver.get(TEST_URL)

    cancel_links = driver.find_elements(
        By.XPATH,
        "//a[contains(normalize-space(.), 'Отмена')]"
    )

    assert cancel_links, "Ссылка «Отмена» отсутствует на странице"
    assert cancel_links[0].is_displayed(), (
        "Ссылка «Отмена» не отображается"
    )