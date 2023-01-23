import time
import os
import math
from selenium import webdriver

from selenium.webdriver.common.by import By


def calc(x): return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == '__main__':
    link = "http://suninjuly.github.io/cats.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element(By.ID, "button")
        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
    finally:
        time.sleep(5)
        browser.quit()
