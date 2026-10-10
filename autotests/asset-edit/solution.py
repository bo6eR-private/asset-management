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
    """Проверяет, что заголовок страницы 'Изменение имущества'."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    h1 = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert h1.text == "Изменение имущества", f"Ожидался заголовок 'Изменение имущества', а найден '{h1.text}'"

def test_inventory_number_is_readonly(driver):
    """Проверяет, что поле инвентарного номера имеет атрибут readonly."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    inv_input = driver.find_element(By.ID, "inventoryNumber")
    readonly_attr = inv_input.get_attribute("readonly")
    assert readonly_attr is not None, "Поле инвентарного номера должно быть readonly"

def test_responsible_section_exists(driver):
    """Проверяет, что есть карточка 'Текущий ответственный'."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    headers = driver.find_elements(By.CLASS_NAME, "card-header")
    responsible_header = None
    for header in headers:
        if "Текущий ответственный" in header.text:
            responsible_header = header
            break
    
    assert responsible_header is not None, "Должна быть карточка 'Текущий ответственный'"