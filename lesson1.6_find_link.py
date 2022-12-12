import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    lnk = browser.find_element(By.LINK_TEXT, "224592")
    lnk.click()
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Andrej")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Sharychev")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Moscow")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(15)
    browser.quit()

