import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_open_s6(driver):
    driver.get("https://www.demoblaze.com/")
    # Ждем, пока элемент "Samsung galaxy s6" станет кликабельным и кликаем по нему
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Samsung galaxy s6'))
    ).click()

    # Ждем, пока элемент заголовка появится
    title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Samsung galaxy s6'))
    )

    assert title.text == 'Samsung galaxy s6'
