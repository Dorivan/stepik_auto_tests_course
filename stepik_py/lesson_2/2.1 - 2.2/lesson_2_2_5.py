import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def calc(x): return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        link = "https://SunInJuly.github.io/execute_script.html"
        browser.get(link)
        button = browser.find_element_by_tag_name("button")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()

        #browser = webdriver.Chrome()
        ##first = int(browser.find_element(By.ID, first).text)
        #second = int(browser.find_element(By.ID, second).text)
        #select = Select(browser.find_element(By.ID, select_id))
        #select.select_by_value(str(first + second))

        #button = browser.find_element(By.XPATH, "//button[@type='submit']")
        #button.click()

    finally:
        time.sleep(5)
        browser.quit()
