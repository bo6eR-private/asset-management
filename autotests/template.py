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


def test_assets_list_displays_all_items(driver):
    """TC-001: Проверить, что на странице отображается список имущества с инвентарным номером, названием, категорией, состоянием и статусом."""


def test_search_by_name(driver):
    """TC-002: Проверить поиск имущества по названию."""


def test_search_by_inventory_number(driver):
    """TC-003: Проверить поиск по инвентарному номеру."""


def test_search_nonexistent_asset(driver):
    """TC-004: Проверить поиск несуществующего имущества."""


def test_filter_by_category(driver):
    """TC-005: Проверить фильтрацию по категории."""


def test_filter_by_status(driver):
    """TC-006: Проверить фильтрацию по статусу."""


def test_open_asset_card(driver):
    """TC-007: Проверить открытие карточки имущества."""
