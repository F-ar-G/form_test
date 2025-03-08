import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def setup():
    # Настройка Chrome
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.get("https://practice-automation.com/form-fields/")
    yield driver
    driver.quit()


def fill_form(driver, name, password, email):
    wait = WebDriverWait(driver, 10)

    # Заполняем поле "Имя"
    name_field = wait.until(EC.element_to_be_clickable((By.ID, "name-input")))
    name_field.clear()
    name_field.send_keys(name)

    # Заполняем поле "Пароль"
    password_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']")))
    password_field.clear()
    password_field.send_keys(password)

    # Выбор напитков (Milk и Coffee)
    drink_values = ["Milk", "Coffee"]
    for drink_value in drink_values:
        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"input[type='checkbox'][value='{drink_value}']")))
        if not checkbox.is_selected():
            driver.execute_script("arguments[0].click();", checkbox)

    # Выбор любимого цвета (Yellow)
    favorite_color_value = "Yellow"
    color_radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"input[type='radio'][value='{favorite_color_value}']")))
    driver.execute_script("arguments[0].click();", color_radio)

    # Выбор из выпадающего списка "Do you like automation?"
    automation_dropdown = Select(wait.until(EC.element_to_be_clickable((By.ID, "automation"))))
    automation_dropdown.select_by_value("yes")

    # Заполнение Email
    email_field = wait.until(EC.element_to_be_clickable((By.ID, "email")))
    driver.execute_script("arguments[0].scrollIntoView(true);", email_field)  # Прокрутка
    email_field.clear()
    email_field.send_keys(email)

    # Подсчет инструментов
    ul_element = wait.until(EC.presence_of_element_located((By.XPATH, "//form/ul")))
    tools = ul_element.find_elements(By.TAG_NAME, "li")
    li_count = len(tools)

    # Ввод количества инструментов в текстовое поле "message"
    message_field = wait.until(EC.element_to_be_clickable((By.ID, "message")))
    message_field.send_keys(f"Инструментов: {li_count}")

    # Выбор самого длинного инструмента
    if tools:
        max_tool = max(tools, key=lambda tool: len(tool.text))
        message_field.send_keys(f" Инструмент: {max_tool.text}")

    # Клик по кнопке "Отправить"
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)

    time.sleep(3)


@pytest.mark.parametrize("name, password, email", [
    ("Test User", "password123", "test@example.com")
])
def test_fill_form(setup, name, password, email):
    driver = setup
    fill_form(driver, name, password, email)

    # Проверка появления алерта с текстом
    time.sleep(2)
    alert = driver.switch_to.alert
    assert "Message received" in alert.text
    alert.accept()  # Закрываем алерт