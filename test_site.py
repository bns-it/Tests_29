
import pytest
from selenium import webdriver #импортируем браузер
from selenium.webdriver.common.by import By #импортируем функционал поиска по элементам страницы
#импортируем вебдрайвер для запуска браузера

@pytest.fixture() #вводим фикстуру (но зачем?)
def driver(): #задаем предусловие (функцию) для открытия браузера
    driver = webdriver.Chrome() #обращаемся к вебдрайверу и вызываем Хром
    yield driver
    driver.maximize_window() #задается открытие полного окна в браузере как настройка

def test_open_s6(driver):
    driver.get ("https://www.demoblaze.com/") #обращаемся к открытой ранее сессии браузера drive и через get открываем ссылку
    galaxy_s6 = driver.find_element(By.LINK_TEXT, 'Samsung galaxy s6') #вызывае функцию поиска (по тексту)
    #+ вводим переменную galaxy_s6, в нее будет подставляться найденный результат
    galaxy_s6.click() #выбрали действие (клик) с найденным элементом
    title = driver.find_element(By.CSS_SELECTOR) #проверяем, что заголовок содержит указанный текст
