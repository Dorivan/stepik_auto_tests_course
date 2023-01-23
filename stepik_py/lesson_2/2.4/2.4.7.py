from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x): return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == '__main__':
    price_selector = 'price'
    button_book = 'book'
    input_value = 'input_value'
    answer = 'answer'
    browser = webdriver.Chrome()
    try:
        browser.get("http://suninjuly.github.io/explicit_wait2.html")

        WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, price_selector), '$100')
        )
        browser.find_element(By.ID, button_book).click()

        x_element = browser.find_element(By.ID, input_value).text
        y = calc(x_element)
        input2 = browser.find_element(By.ID, answer)
        input2.send_keys(y)

        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
    finally:
        time.sleep(5)
        browser.quit()
