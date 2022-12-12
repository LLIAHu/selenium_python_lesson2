from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    # нашли и посчитали математическую функцию
    browser.execute_script("window.scrollBy(0, 100);")

    answer_form = browser.find_element(By.ID, 'answer').send_keys(y)

    check_box = browser.find_element(By.ID, 'robotCheckbox')
    check_box.click()

    radio_button = browser.find_element(By.ID, 'robotsRule')
    radio_button.click()

    submit_button = browser.find_element(By.CLASS_NAME, 'btn')
    submit_button.click()

    time.sleep(10)



finally:
    browser.quit()