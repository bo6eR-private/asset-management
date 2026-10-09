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


def test_asset_title_displayed(driver):
    """Проверить, что на странице отображается заголовок с названием имущества."""


def test_inventory_number_displayed(driver):
    """Проверить, что отображается инвентарный номер."""


def test_history_has_three_records(driver):
    """Проверить, что в истории операций 3 записи."""


def test_responsible_section_exists(driver):
    """Проверить, что есть секция 'Текущий ответственный'."""


def test_action_buttons_present(driver):
    """Проверить наличие кнопок действий."""
