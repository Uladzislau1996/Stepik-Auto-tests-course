# Функция которая считает значение x
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/get_attribute.html")

# Ищем сундук
box = driver.find_element_by_id("treasure")

# Ищем атрибут x
x = box.get_attribute("valuex")

# Присваиваем y значение которая подсчиталая функция
y = calc(x)

# Вводим значение x в текстовое поле
input1 = driver.find_element_by_id("answer")
input1.send_keys(y)

# Отмечаю checkbox я робот
option1 = driver.find_element_by_id("robotCheckbox")
option1.click()

# Отмечаю radiobutton "правило робота"
option2 = driver.find_element_by_id("robotsRule")
option2.click()

# Нажимаю кнопку "Submit"
submit = driver.find_element_by_class_name('btn')
submit.click()

exit()

