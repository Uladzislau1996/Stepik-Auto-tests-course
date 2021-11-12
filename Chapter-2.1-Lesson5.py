import math

def calc(x):
  return str(num1 + num2)

import math

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/math.html")

# Ищем x
x_element = driver.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

# Вводим значение x в текстовое поле
input1 = driver.find_element_by_id("answer")
input1.send_keys(y)

# Отмечаю checkbox я не робот
option1 = driver.find_element_by_css_selector("[for='robotCheckbox']")
option1.click()

# Отмечаю radiobutton "я не робот"
option2 = driver.find_element_by_css_selector("[for='robotsRule']")
option2.click()

# Нажимаю кнопку "Submit"
submit = driver.find_element_by_class_name('btn')
submit.click()

exit()

