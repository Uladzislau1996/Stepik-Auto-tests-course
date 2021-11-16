import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# создаю функцию
driver = webdriver.Chrome()

# открываю сайт
driver.get('http://suninjuly.github.io/explicit_wait2.html')

# ищу кнопку которую необходимо нажать
button = driver.find_element_by_id('book')



# говорим Selenium проверять в течение 12 секунд, пока кнопка не найдется необходимый текст
price = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
    )
button.click()

# ищу x
element = driver.find_element_by_id('input_value')
x = element.text

# вначале скрипта считаю математическую функцию для x и присваеваю ответ новой переменной
y = calc(x)

# вставляю x в поле для ввода
field = driver.find_element_by_id('answer')
field.send_keys(y)

# нажимаю на кнопку submit
submit = driver.find_element_by_id('solve')
submit.click()

# Выхожу из скрипта
exit()



