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
    """TC-001: Проверяет, что на странице отображается список имущества с инвентарным номером, названием, категорией, состоянием и статусом."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.presence_of_element_located((By.ID, "assetsTable")))
    
    rows = driver.find_elements(By.CSS_SELECTOR, "#assetsTable tbody tr")
    assert len(rows) == 3, f"Ожидалось 3 записи в таблице, а найдено {len(rows)}"
    
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        assert len(cells) == 6, "В каждой строке должно быть 6 колонок"
        inv_num = cells[0].text
        name = cells[1].text
        category = cells[2].text
        condition = cells[3].text
        status_cell = cells[4]
        
        assert inv_num != "", "Инвентарный номер не должен быть пустым"
        assert name != "", "Название не должно быть пустым"
        assert category != "", "Категория не должна быть пустой"
        assert condition != "", "Состояние не должно быть пустым"
        
        badge = status_cell.find_element(By.TAG_NAME, "span")
        assert badge.is_displayed(), "Бейдж со статусом должен быть отображён"


def test_search_by_name(driver):
    """TC-002: Проверяет поиск имущества по названию."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    search_input = wait.until(EC.presence_of_element_located((By.ID, "searchInput")))
    search_input.clear()
    search_input.send_keys("Lenovo ThinkPad T14")
    
    search_button = driver.find_element(By.ID, "searchButton")
    search_button.click()
    
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#assetsTable tbody tr")) > 0)
    
    rows = driver.find_elements(By.CSS_SELECTOR, "#assetsTable tbody tr")
    assert len(rows) == 1, f"Ожидалось 1 запись после поиска по названию, а найдено {len(rows)}"
    
    name_cell = rows[0].find_elements(By.TAG_NAME, "td")[1]
    assert name_cell.text == "Lenovo ThinkPad T14", "Должна отображаться запись с названием 'Lenovo ThinkPad T14'"


def test_search_by_inventory_number(driver):
    """TC-003: Проверяет поиск по инвентарному номеру."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    search_input = wait.until(EC.presence_of_element_located((By.ID, "searchInput")))
    search_input.clear()
    search_input.send_keys("INV-0001")
    
    search_button = driver.find_element(By.ID, "searchButton")
    search_button.click()
    
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#assetsTable tbody tr")) > 0)
    
    rows = driver.find_elements(By.CSS_SELECTOR, "#assetsTable tbody tr")
    assert len(rows) == 1, f"Ожидалось 1 запись после поиска по инвентарному номеру, а найдено {len(rows)}"
    
    inv_cell = rows[0].find_elements(By.TAG_NAME, "td")[0]
    assert inv_cell.text == "INV-0001", "Должна отображаться запись с инвентарным номером 'INV-0001'"


def test_search_nonexistent_asset(driver):
    """TC-004: Проверяет поиск несуществующего имущества."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    search_input = wait.until(EC.presence_of_element_located((By.ID, "searchInput")))
    search_input.clear()
    search_input.send_keys("INV-9999")
    
    search_button = driver.find_element(By.ID, "searchButton")
    search_button.click()
    
    wait.until(EC.presence_of_element_located((By.ID, "noResults")))
    
    no_results = driver.find_element(By.ID, "noResults")
    assert no_results.is_displayed(), "Должно отображаться сообщение 'Имущество не найдено'"
    
    assert "Имущество не найдено" in no_results.text, "Сообщение должно содержать текст 'Имущество не найдено'"
    
    rows = driver.find_elements(By.CSS_SELECTOR, "#assetsTable tbody tr")
    assert len(rows) == 0, "Таблица должна быть пустой при поиске несуществующего имущества"


def test_filter_by_category(driver):
    """TC-005: Проверяет фильтрацию по категории."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    category_select = wait.until(EC.presence_of_element_located((By.ID, "categoryFilter")))
    category_select.click()
    
    from selenium.webdriver.support.ui import Select
    select = Select(category_select)
    select.select_by_value("computer")
    
    search_button = driver.find_element(By.ID, "searchButton")
    search_button.click()
    
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#assetsTable tbody tr")) > 0)
    
    rows = driver.find_elements(By.CSS_SELECTOR, "#assetsTable tbody tr")
    assert len(rows) == 2, f"Ожидалось 2 записи категории 'Компьютерная техника', а найдено {len(rows)}"
    
    for row in rows:
        category_cell = row.find_elements(By.TAG_NAME, "td")[2]
        assert category_cell.text == "Компьютерная техника", "Все записи должны иметь категорию 'Компьютерная техника'"


def test_filter_by_status(driver):
    """TC-006: Проверяет фильтрацию по статусу."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    status_select = wait.until(EC.presence_of_element_located((By.ID, "statusFilter")))
    status_select.click()
    
    from selenium.webdriver.support.ui import Select
    select = Select(status_select)
    select.select_by_value("stock")
    
    search_button = driver.find_element(By.ID, "searchButton")
    search_button.click()
    
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#assetsTable tbody tr")) > 0)
    
    rows = driver.find_elements(By.CSS_SELECTOR, "#assetsTable tbody tr")
    assert len(rows) == 1, f"Ожидалось 1 запись со статусом 'На складе', а найдено {len(rows)}"
    
    status_cell = rows[0].find_elements(By.TAG_NAME, "td")[4]
    badge = status_cell.find_element(By.TAG_NAME, "span")
    assert "На складе" in badge.text, "Запись должна иметь статус 'На складе'"


def test_open_asset_card(driver):
    """TC-007: Проверяет открытие карточки имущества."""
    driver.get(TEST_URL)
    wait = WebDriverWait(driver, 10)
    
    rows = driver.find_elements(By.CSS_SELECTOR, "#assetsTable tbody tr")
    target_row = None
    for row in rows:
        inv_cell = row.find_elements(By.TAG_NAME, "td")[0]
        if inv_cell.text == "INV-0001":
            target_row = row
            break
    
    assert target_row is not None, "Не найдена запись с инвентарным номером INV-0001"
    
    open_button = target_row.find_element(By.CSS_SELECTOR, "a.btn-outline-primary")
    assert open_button.is_displayed(), "Кнопка 'Открыть' должна быть отображена"
    assert "Открыть" in open_button.text, "Кнопка должна содержать текст 'Открыть'"