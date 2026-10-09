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
    """Проверяет, что на странице отображается заголовок с названием имущества."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    # Проверяем наличие h1
    h1 = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert h1.text == "Lenovo ThinkPad T14", f"Ожидался заголовок 'Lenovo ThinkPad T14', а найден '{h1.text}'"


def test_inventory_number_displayed(driver):
    """Проверяет, что отображается инвентарный номер."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    # Проверяем, что есть текст с инвентарным номером
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "INV-0001" in body_text, "Инвентарный номер INV-0001 должен быть отображён"


def test_history_has_three_records(driver):
    """Проверяет, что в истории операций 3 записи."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    # Находим таблицу истории
    rows = driver.find_elements(By.CSS_SELECTOR, ".table tbody tr")
    assert len(rows) == 3, f"Ожидалось 3 записи в истории, а найдено {len(rows)}"


def test_responsible_section_exists(driver):
    """Проверяет, что есть секция 'Текущий ответственный'."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    # Проверяем наличие карточки с заголовком "Текущий ответственный"
    headers = driver.find_elements(By.CLASS_NAME, "card-header")
    responsible_header = None
    for header in headers:
        if "Текущий ответственный" in header.text:
            responsible_header = header
            break
    
    assert responsible_header is not None, "Должна быть карточка 'Текущий ответственный'"


def test_action_buttons_present(driver):
    """Проверяет наличие кнопок действий."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    # Проверяем наличие карточки с действиями
    actions_card = driver.find_elements(By.CLASS_NAME, "card")
    actions_section = None
    for card in actions_card:
        header = card.find_element(By.CLASS_NAME, "card-header")
        if "Действия" in header.text:
            actions_section = card
            break
    
    assert actions_section is not None, "Должна быть карточка 'Действия'"
    
    # Проверяем наличие кнопок
    buttons = actions_section.find_elements(By.TAG_NAME, "button")
    button_links = actions_section.find_elements(By.TAG_NAME, "a")
    total_actions = len(buttons) + len(button_links)
    assert total_actions == 3, f"Ожидалось 3 кнопки действий, а найдено {total_actions}"
    
    # Проверяем текст кнопки "Оформить выдачу"
    issue_button = None
    for btn in button_links:
        if "Оформить выдачу" in btn.text:
            issue_button = btn
            break
    
    assert issue_button is not None, "Должна быть кнопка 'Оформить выдачу'"
