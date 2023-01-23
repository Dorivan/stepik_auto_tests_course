import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def calc(x): return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == '__main__':
    link = "http://suninjuly.github.io/selects1.html"
    first = "num1"
    second = "num2"
    select_id = "dropdown"

    try:
        browser = webdriver.Chrome()
        browser.get(link)
        first = int(browser.find_element(By.ID, first).text)
        second = int(browser.find_element(By.ID, second).text)
        select = Select(browser.find_element(By.ID, select_id))
        select.select_by_value(str(first + second))

        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

    finally:
        time.sleep(5)
        browser.quit()
