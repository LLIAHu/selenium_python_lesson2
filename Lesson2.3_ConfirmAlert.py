import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, 'btn').click()

    alert = browser.switch_to.alert
    alert.accept()

    x_elem = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_elem.text
    y = calc(x)
    time.sleep(2)

    answer_form = browser.find_element(By.ID, 'answer')
    answer_form.send_keys(y)

    sub_button = browser.find_element(By.CLASS_NAME, 'btn-primary').click()

finally:
    time.sleep(10)
    browser.quit()

