# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/selects1.html")

# Ищем num1
num1 = driver.find_element_by_id("num1")
n1 = num1.text


# Ищем num2
num2 = driver.find_element_by_id("num2")
n2 = num2.text


# Считает anwser
anwser = str(int(n1) + int(n2))


# Ищем элемент в списке равный anwser
from selenium.webdriver.support.ui import Select
drop = Select(driver.find_element_by_id('dropdown'))
drop.select_by_value(anwser) # ищем элемент с текстом "Python"

# Нажимаю кнопку "Submit"
submit = driver.find_element_by_class_name('btn')
submit.click()

exit()
