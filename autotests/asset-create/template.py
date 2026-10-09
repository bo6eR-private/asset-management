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
    """Проверить, что заголовок страницы 'Добавление имущества'."""


def test_form_has_required_fields(driver):
    """Проверить, что форма содержит поля: название, инвентарный номер, категория."""


def test_submit_button_exists(driver):
    """Проверить наличие кнопки 'Добавить имущество'."""
