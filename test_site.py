
import pytest
from selenium import webdriver #импортируем браузер
from selenium.webdriver.common.by import By #импортируем функционал поиска по элементам страницы
from selenium.webdriver.support.wait import WebDriverWait


#импортируем вебдрайвер для запуска браузера

@pytest.fixture() #вводим фикстуру (но зачем?)
def driver(): #задаем предусловие (функцию) для открытия браузера
    driver = webdriver.Chrome() #обращаемся к вебдрайверу и вызываем Хром
    driver.maximize_window()  # задается открытие полного окна в браузере как настройка
    driver.implicitly_wait(5)
    yield driver # разделение создания ресурса (в данном случае, веб-драйвера) и его очистки после завершения теста
    driver.close()

def test_open_s6(driver):
    driver.get ("https://www.demoblaze.com/") #обращаемся к открытой ранее сессии браузера drive и через get открываем ссылку
    galaxy_s6 = driver.find_element(By.LINK_TEXT, 'Samsung galaxy s6') #вызываем функцию поиска (по тексту)
    #+ вводим переменную galaxy_s6, в нее будет подставляться найденный результат
    galaxy_s6.click() #выбрали действие (клик) с найденным элементом (ссылкой)
    title = driver.find_element(By.XPATH,'//h2[text() = "Samsung galaxy s6" ]') #проверяем, что заголовок содержит
    # указанный текст. "//" — это означает, что поиск будет выполнен для всего документа (всех уровней) и найдётся любой элемент,
    # соответствующий критериям.
    # "h2" — это тег HTML, который мы ищем. В данном случае это заголовок (тег <h2>).
    # [text() = "Samsung galaxy s6"] — это условие, что мы ищем элемент (ссылку),
    # текстовое содержимое которого точно соответствует строке "Samsung galaxy s6".
    assert title.text == 'Samsung galaxy s6' #проверяем, что заголовок соответствует ОР

