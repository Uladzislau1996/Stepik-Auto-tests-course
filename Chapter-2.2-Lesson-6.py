# Функция которая считает значение x
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Скачиваю библиоткеу
from selenium import webdriver

# создаю функцию для обращения к webdriver
driver = webdriver.Chrome()

# открываю сайт
driver.get('http://SunInJuly.github.io/execute_script.html')

# ищу x
element = driver.find_element_by_id('input_value')
x = element.text

# вначале скрипта считаю математическую функцию для x и присваеваю ответ новой переменной
y = calc(x)

# скролю страницу вниз
scroll = driver.find_element_by_class_name("btn")
driver.execute_script("return arguments[0].scrollIntoView(true);", scroll)

# ищу текстовое поле и вставляю туда ответ
input = driver.find_element_by_id('answer')
input.send_keys(y)

# скролю страницу вниз
scroll = driver.find_element_by_class_name("btn")
driver.execute_script("return arguments[0].scrollIntoView(true);", scroll)

# выбираю чекбокс я робот
checkbox = driver.find_element_by_css_selector("[for='robotCheckbox']")
checkbox.click()

# выбираю радиобаттон правило роботов
radio = driver.find_element_by_css_selector("[for='robotsRule']")
radio.click()

# Нажимаю кнопку "Submit"
button = driver.find_element_by_class_name('btn')
button.click()

# Закрываю окно браузера
exit()