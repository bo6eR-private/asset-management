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
    """Проверяет, что заголовок страницы 'Выдачи имущества'."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    h1 = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert h1.text == "Выдачи имущества", f"Ожидался заголовок 'Выдачи имущества', а найден '{h1.text}'"


def test_three_issues_displayed(driver):
    """Проверяет, что в таблице отображается 3 выдачи."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
    assert len(rows) == 3, f"Ожидалось 3 выдачи, а найдено {len(rows)}"


def test_create_issue_button_exists(driver):
    """Проверяет наличие кнопки '+ Оформить выдачу'."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    create_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Оформить выдачу')]")
    assert create_button.is_displayed(), "Кнопка '+ Оформить выдачу' должна быть отображена"
