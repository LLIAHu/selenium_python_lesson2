from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.TAG_NAME, 'img')
    treasure_checked = treasure.get_attribute('valuex')
    x = treasure_checked
    y = calc(x)
    # нашли и посчитали математическую функцию
    browser.find_element(By.ID, 'answer').send_keys(y)
    # ввели в поле ответа найденное значение
    browser.find_element(By.ID, 'robotCheckbox').click()
    # кликаем чекбокс ЯРобот
    browser.find_element(By.ID, 'robotsRule').click()
    # кликаем радиобатон РоботыРулят(Нет)
    browser.find_element(By.CLASS_NAME, 'btn').click()



finally:
    time.sleep(10)
    browser.quit()


