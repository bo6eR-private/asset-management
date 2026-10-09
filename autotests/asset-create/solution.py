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
    """Проверяет, что заголовок страницы 'Добавление имущества'."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    h1 = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert h1.text == "Добавление имущества", f"Ожидался заголовок 'Добавление имущества', а найден '{h1.text}'"


def test_form_has_required_fields(driver):
    """Проверяет, что форма содержит поля: название, инвентарный номер, категория."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    # Проверяем наличие поля названия
    name_input = driver.find_element(By.ID, "assetName")
    assert name_input is not None, "Поле 'Название' должно быть на форме"
    
    # Проверяем наличие поля инвентарного номера
    inv_input = driver.find_element(By.ID, "inventoryNumber")
    assert inv_input is not None, "Поле 'Инвентарный номер' должно быть на форме"
    
    # Проверяем наличие селекта категории
    category_select = driver.find_element(By.ID, "category")
    assert category_select is not None, "Селект 'Категория' должен быть на форме"


def test_submit_button_exists(driver):
    """Проверяет наличие кнопки 'Добавить имущество'."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    assert submit_button is not None, "Кнопка 'Добавить имущество' должна быть на форме"
    assert "Добавить имущество" in submit_button.text, "Кнопка должна содержать текст 'Добавить имущество'"
