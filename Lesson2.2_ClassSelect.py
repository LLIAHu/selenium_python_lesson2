import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = 'http://suninjuly.github.io/selects2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    y = str(int(num1) + int(num2))
    # считаем сумму чисел, чтобы ввести значение в выпадающем списке
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    # находим выпадающий список
    select.select_by_value(y)
    # вводим значение для выбора
    sub_button = browser.find_element(By.CLASS_NAME, 'btn').click()
    # жмакаем на кнопоцьку
finally:

    time.sleep(5)
    browser.quit()


