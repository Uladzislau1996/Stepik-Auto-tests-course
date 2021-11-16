# Скачиваю библиоткеу
from selenium import webdriver

# создаю функцию для обращения к webdriver
driver = webdriver.Chrome()

# открываю сайт
driver.get('http://suninjuly.github.io/file_input.html')

# ищу и заполняю поле firstname
firstname = driver.find_element_by_css_selector("[name='firstname']")
firstname.send_keys('QA')

# ищу и заполняю поле lastname
lastname = driver.find_element_by_css_selector("[name='lastname']")
lastname.send_keys('Vlad')

# ищу и заполняю поле email
email = driver.find_element_by_css_selector("[name='email']")
email.send_keys('Vlad@mail.com')

# ищу кнопку "Выберите файл"
element = driver.find_element_by_css_selector("[name='file']")
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'textfile.txt')           # добавляем к этому пути имя файла 
element.send_keys(file_path)


# нажимаю кнопку "submit"
button = driver.find_element_by_class_name('btn')
button.click()


# Закрываю окно браузера
exit()