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
    """Проверяет, что на странице отображается 3 записи имущества."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located((By.ID, "assetsTable")))

    assetSize = 3;
    rows = driver.find_elements(By.CSS_SELECTOR, "#assetsTable tr")
    assert len(rows) == assetSize, f"Ожидалось { assetSize } записи в таблице, а найдено {len(rows)}"


def test_search_by_name(driver):
    """Проверяет поиск имущества по названию."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    # Вводим название для поиска
    search_input = wait.until(EC.presence_of_element_located((By.ID, "searchInput")))
    search_input.clear()
    search_input.send_keys("Lenovo ThinkPad T14")
    
    # Нажимаем кнопку "Найти"
    search_button = driver.find_element(By.ID, "searchButton")
    search_button.click()
    
    # Ждём обновления таблицы
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#assetsTable tr")) > 0)
    
    # Проверяем, что отображается только одна запись
    rows = driver.find_elements(By.CSS_SELECTOR, "#assetsTable tr")
    assert len(rows) == 1, f"Ожидалось 1 запись после поиска по названию, а найдено {len(rows)}"
    
    # Проверяем, что это именно Lenovo ThinkPad T14
    name_cell = rows[0].find_elements(By.TAG_NAME, "td")[1]
    assert name_cell.text == "Lenovo ThinkPad T14", "Должна отображаться запись с названием 'Lenovo ThinkPad T14'"


def test_filter_by_category(driver):
    """Проверяет фильтрацию по категории."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    # Выбираем категорию "Компьютерная техника"
    category_select = wait.until(EC.presence_of_element_located((By.ID, "categoryFilter")))
    category_select.click()
    
    from selenium.webdriver.support.ui import Select
    select = Select(category_select)
    select.select_by_value("computer")
    
    # Нажимаем кнопку "Найти"
    search_button = driver.find_element(By.ID, "searchButton")
    search_button.click()
    
    # Ждём обновления таблицы
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#assetsTable tr")) > 0)
    
    # Проверяем, что отображаются только записи категории "Компьютерная техника"
    rows = driver.find_elements(By.CSS_SELECTOR, "#assetsTable tr")
    assert len(rows) == 2, f"Ожидалось 2 записи категории 'Компьютерная техника', а найдено {len(rows)}"
    
    # Проверяем, что все записи имеют категорию "Компьютерная техника"
    for row in rows:
        category_cell = row.find_elements(By.TAG_NAME, "td")[2]
        assert category_cell.text == "Компьютерная техника", "Все записи должны иметь категорию 'Компьютерная техника'"


def test_filter_by_status(driver):
    """Проверяет фильтрацию по статусу."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    # Выбираем статус "На складе"
    status_select = wait.until(EC.presence_of_element_located((By.ID, "statusFilter")))
    status_select.click()
    
    from selenium.webdriver.support.ui import Select
    select = Select(status_select)
    select.select_by_value("stock")
    
    # Нажимаем кнопку "Найти"
    search_button = driver.find_element(By.ID, "searchButton")
    search_button.click()
    
    # Ждём обновления таблицы
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#assetsTable tr")) > 0)
    
    # Проверяем, что отображаются только записи со статусом "На складе"
    rows = driver.find_elements(By.CSS_SELECTOR, "#assetsTable tr")
    assert len(rows) == 1, f"Ожидалось 1 запись со статусом 'На складе', а найдено {len(rows)}"
    
    # Проверяем, что запись имеет статус "На складе"
    status_cell = rows[0].find_elements(By.TAG_NAME, "td")[4]
    badge = status_cell.find_element(By.TAG_NAME, "span")
    assert "На складе" in badge.text, "Запись должна иметь статус 'На складе'"


def test_open_button_text(driver):
    """Проверяет, что кнопка имеет текст 'Открыть'."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    # Находим первую кнопку "Открыть"
    rows = driver.find_elements(By.CSS_SELECTOR, "#assetsTable tr")
    assert len(rows) > 0, "В таблице должны быть записи"
    
    open_button = rows[0].find_element(By.CSS_SELECTOR, "a.btn-outline-primary")
    assert open_button.is_displayed(), "Кнопка должна быть отображена"
    assert "Открыть" in open_button.text, "Кнопка должна содержать текст 'Открыть'"
