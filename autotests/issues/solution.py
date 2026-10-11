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
    """Проверяет заголовок страницы 'Выдачи имущества'."""
    driver.get(TEST_URL)

    headings = driver.find_elements(By.TAG_NAME, "h1")
    assert headings, "На странице отсутствует заголовок <h1>"

    actual_title = headings[0].text.strip()
    expected_title = "Выдачи имущества"

    assert actual_title == expected_title, (
        f"Ожидался заголовок '{expected_title}', "
        f"а найден '{actual_title}'"
    )


def test_three_issues_displayed(driver):
    """Проверяет, что в таблице отображается 3 выдачи."""
    driver.get(TEST_URL)

    rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
    assert len(rows) == 3, (
        f"Ожидалось 3 выдачи, а найдено {len(rows)}"
    )


def test_create_issue_button_exists(driver):
    """Проверяет наличие ссылки '+ Оформить выдачу'."""
    driver.get(TEST_URL)

    buttons = driver.find_elements(
        By.XPATH,
        "//a[contains(normalize-space(.), 'Оформить выдачу')]"
    )

    assert buttons, "Ссылка «Оформить выдачу» отсутствует на странице"
    assert buttons[0].is_displayed(), (
        "Ссылка «Оформить выдачу» не отображается"
    )