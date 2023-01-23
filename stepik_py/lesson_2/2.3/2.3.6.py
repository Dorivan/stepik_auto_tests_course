import time
import os
import math
from selenium import webdriver

from selenium.webdriver.common.by import By


def calc(x): return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == '__main__':
    link = "http://suninjuly.github.io/redirect_accept.html"
    button_1 = "btn-primary"  # Class-name
    value1 = 'input_value'
    value2 = 'answer'

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CLASS_NAME, button_1).click()
        window = browser.window_handles[1]
        browser.switch_to.window(window)
        x_element = browser.find_element(By.ID, value1).text
        y = calc(x_element)
        browser.find_element(By.ID, value2).send_keys(y)
        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
    finally:
        time.sleep(5)
        browser.quit()
