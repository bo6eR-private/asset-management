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
    """Проверяет заголовок страницы 'Отчёты'."""
    driver.get(TEST_URL)

    headings = driver.find_elements(By.TAG_NAME, "h1")
    assert headings, "На странице отсутствует заголовок <h1>"

    assert headings[0].text == "Отчёты", (
        f"Ожидался заголовок 'Отчёты', "
        f"а найден '{headings[0].text}'"
    )

def test_four_report_cards_exist(driver):
    """Проверяет, что есть 4 карточки доступных отчётов."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "card")))
    
    cards = driver.find_elements(By.CSS_SELECTOR, ".card-body h5")
    report_titles = [card.text for card in cards]
    
    assert len(report_titles) == 4, f"Ожидалось 4 карточки отчётов, а найдено {len(report_titles)}"
    
    expected_titles = ["Отчёт по имуществу", "Отчёт по сотрудникам", "Отчёт по выдачам", "Отчёт по возвратам"]
    for title in expected_titles:
        assert title in report_titles, f"Отсутствует карточка с заголовком '{title}'"


def test_export_section_exists(driver):
    """Проверяет, что есть секция 'Экспорт' с кнопками."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Экспорт" in body_text, "Должна быть секция 'Экспорт'"
    
    export_buttons = driver.find_elements(By.CSS_SELECTOR, "button")
    button_texts = [btn.text for btn in export_buttons]
    
    assert "Экспорт в PDF" in button_texts, "Должна быть кнопка 'Экспорт в PDF'"
    assert "Экспорт в Excel" in button_texts, "Должна быть кнопка 'Экспорт в Excel'"