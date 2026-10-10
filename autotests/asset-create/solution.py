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
    """Проверяет заголовок страницы."""
    driver.get(TEST_URL)

    headings = driver.find_elements(By.TAG_NAME, "h1")
    assert headings, "На странице отсутствует заголовок <h1>"

    actual_title = headings[0].text
    expected_title = "Добавление имущества"

    assert actual_title == expected_title, (
        f"Неверный заголовок. "
        f"Ожидался: '{expected_title}', получен: '{actual_title}'"
    )

def test_form_has_required_fields(driver):
    """Проверяет, что форма содержит поля: название, инвентарный номер, категория."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    name_input = driver.find_elements(By.ID, "assetName")
    assert name_input, "Поле 'Название' должно быть на форме"
    
    inv_input = driver.find_elements(By.ID, "inventoryNumber")
    assert inv_input, "Поле 'Инвентарный номер' должно быть на форме"
    
    category_select = driver.find_elements(By.ID, "category")
    assert category_select, "Селект «Категория» отсутствует на форме"


def test_submit_button_exists(driver):
    """Проверяет наличие кнопки 'Добавить имущество'."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    assert submit_button is not None, "Кнопка 'Добавить имущество' должна быть на форме"
    assert "Добавить имущество" in submit_button.text, "Кнопка должна содержать текст 'Добавить имущество'"