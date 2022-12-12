from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    f_name = browser.find_element(By.CLASS_NAME, "form-control.first")
    f_name.send_keys('Neo')
    l_name = browser.find_element(By.CLASS_NAME, "form-control.second")
    l_name.send_keys('Mr. Anderson')
    email_area = browser.find_element(By.CLASS_NAME, "form-control.third")
    email_area.send_keys('hucker_neo@matrix.smit')
    phone = browser.find_element(By.XPATH, "//label[text()='Phone:']/following-sibling::input")
    phone.send_keys(+79999999999)
    adress = browser.find_element(By.XPATH, "//label[text()='Address:']/following-sibling::input")
    adress.send_keys('USSR')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    time.sleep(3)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()
