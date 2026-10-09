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


def test_assets_list_displays_three_items(driver):
    """Проверить, что на странице отображается 3 записи имущества."""


def test_search_by_name(driver):
    """Проверить поиск имущества по названию."""


def test_filter_by_category(driver):
    """Проверить фильтрацию по категории."""


def test_filter_by_status(driver):
    """Проверить фильтрацию по статусу."""


def test_open_button_text(driver):
    """Проверить, что кнопка имеет текст 'Открыть'."""
