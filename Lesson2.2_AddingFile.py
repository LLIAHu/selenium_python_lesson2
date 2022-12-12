import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    f_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('Neo')
    # ввели имя

    l_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Mr.Anderson')
    # ввели фамилию

    ema_il = browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('hucker_neo@matrix.smit')
    # ввели емаил

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = 'BioNeo.txt'
    file_path = os.path.join(current_dir, file_name)
    # добавление файла в переменную пас

    add_file = browser.find_element(By.ID, 'file').send_keys(file_path)
    # добавили файл

    button = browser.find_element(By.CLASS_NAME, 'btn').click()
    # нажали субмит
    time.sleep(10)


finally:
    browser.quit()



