import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Скачиваю Webdriver
from selenium import webdriver

# Присваеваю функцию для переменной
driver = webdriver.Chrome()

# Открываю сайт
driver.get('http://suninjuly.github.io/redirect_accept.html')

# Ищу кнопку и нажимаю на нее
button = driver.find_element_by_class_name('trollface')
button.click()

# Узнаю имя новой вкладки
new_window = driver.window_handles[1]

# Переключаюсь на новую вкладку
driver.switch_to.window(new_window)

# ищу x
element = driver.find_element_by_id('input_value')
x = element.text

# вначале скрипта считаю математическую функцию для x и присваеваю ответ новой переменной
y = calc(x)

# вставляю x в поле для ввода
field = driver.find_element_by_id('answer')
field.send_keys(y)

# нажимаю на кнопку submit
submit = driver.find_element_by_class_name('btn-primary')
submit.click()

# Выхожу из скрипта
exit()


