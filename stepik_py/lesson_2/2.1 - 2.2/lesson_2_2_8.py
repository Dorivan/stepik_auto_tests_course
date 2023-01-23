import time
import os
from selenium import webdriver

from selenium.webdriver.common.by import By

if __name__ == '__main__':
    link = "http://suninjuly.github.io/file_input.html"
    value1 = "[name='firstname']"
    value2 = "[name='lastname']"
    value3 = "[name='email']"
    file = "file"
    file_name = os.path.abspath(os.path.dirname(__file__)) + '\\test.txt'
    print(file_name)
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, value1)
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, value2)
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, value3)
        input3.send_keys("Email")
        file_acc = browser.find_element(By.ID, file)
        file_acc.send_keys(file_name)
        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
    finally:
        time.sleep(5)
        browser.quit()
