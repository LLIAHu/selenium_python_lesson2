from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'https://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)
    # открыли браузер
    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    # нашли и посчитали математическую функцию
    answer_form = browser.find_element(By.ID, 'answer')
    answer_form.send_keys(y)
    # ввели в поле ответа найденное значение
    check_box = browser.find_element(By.ID, 'robotCheckbox')
    check_box.click()
    # кликаем чекбокс ЯРобот
    radio_button = browser.find_element(By.ID, 'robotsRule')
    radio_button.click()
    # кликаем радиобатон РоботыРулят(Нет)
    submit_button = browser.find_element(By.CLASS_NAME, 'btn')
    submit_button.click()
    # нажал на кнопку Субмит




finally:

    time.sleep(10)
    browser.quit()

