from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element(By.ID, "peopleRule")
    # находим радиобатон ПИПЛ
    people_checked = people_radio.get_attribute('checked')
    # проверяем у радиобатона наличие атрибута 'checked'
    print("value of people radio: ", people_checked)
    assert people_checked is not None


    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of people robots: ", robots_checked)
    assert robots_checked is None


    submit_button = browser.find_element(By.CLASS_NAME, 'btn')
    submit_checked = submit_button.get_attribute('disabled')
    print("value of submit button:", submit_checked)
    assert submit_checked is None


    time.sleep(13)
    submit_checked = submit_button.get_attribute('disabled')
    print("value uf submit button after 10 sec:", submit_checked)
    assert submit_checked is not None
        

finally:

    browser.quit()