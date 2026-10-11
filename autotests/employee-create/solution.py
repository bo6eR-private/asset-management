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
    """Проверяет, что заголовок страницы 'Добавление сотрудника'."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    h1 = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert h1.text == "Добавление сотрудника", f"Ожидался заголовок 'Добавление сотрудника', а найден '{h1.text}'"


def test_submit_button_exists(driver):
    """Проверяет наличие кнопки 'Добавить сотрудника'."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Добавить сотрудника')]")
    assert submit_button.is_displayed(), "Кнопка 'Добавить сотрудника' должна быть отображена"


def test_cancel_button_exists(driver):
    """Проверяет наличие кнопки 'Отмена'."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    cancel_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Отмена')]")
    assert cancel_button.is_displayed(), "Кнопка 'Отмена' должна быть отображена"
