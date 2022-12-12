import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    troll_button = browser.find_element(By.CLASS_NAME, 'trollface').click()
    new_page = browser.window_handles[1]

    browser.switch_to.window(new_page)


    time.sleep(2)


    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer_form = browser.find_element(By.ID, 'answer').send_keys(y)
    sub_button = browser.find_element(By.TAG_NAME, 'button').click()



finally:
    time.sleep(5)

    browser.quit()
