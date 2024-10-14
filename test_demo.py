from random import choice #здесь мы ипортировали из модуля import функцию choice

my_list = ['text', 'one', 'two ']
print(choice(my_list)) #применили импортированную функцию choice к переменной (списку) my_list



#первая тестовая функция
def test_demo1():
    assert 1 == 1 #assert - условие, "Сообщение об ошибке" (проверка истинности выражений)
def test_demo2(before_after):
    assert 2 == 2



# пре- и постусловия
import pytest
@pytest.fixture() #декоратором "@" задаем предусловие
def before_after():
    print("Before test") #предусловие
    yield None # в этом месте располагается тело автотеста
    print("\nAfter test") #постусловие "\n" - перенос строки


