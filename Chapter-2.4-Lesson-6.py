# Скачиваю Webdriver
from selenium import webdriver

# Присваеваю функцию для переменной
driver = webdriver.Chrome()

#открываю страницу
driver.get('http://suninjuly.github.io/cats.html')

#выполняю команду 
driver.find_element_by_id("button")