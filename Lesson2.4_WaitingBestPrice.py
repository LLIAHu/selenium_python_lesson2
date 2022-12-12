from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # идем по ссылке

    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button = browser.find_element(By.ID, 'book')
    button.click()
    # инициируем ожидание

    x_elem = browser.find_element(By.ID, 'input_value')
    x = x_elem.text
    y = calc(x)
    # высчитываем мат функцию

    browser.execute_script("window.scrollBy(0, 300);")
    # инициируем скролл страницы

    math_func = browser.find_element(By.ID, 'answer').send_keys(y)
    # вводим полученное значение математической функции в поле ввода

    sub_but = browser.find_element(By.ID, 'solve').click()
    # жмакаем на субмит


finally:
    time.sleep(3)
    browser.quit()


 29.023153138776507