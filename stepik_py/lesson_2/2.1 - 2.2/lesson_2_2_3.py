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
        browser.execute_script("document.title='Script executing';")
        browser.execute_script("alert('Robots at work');")

    finally:
        time.sleep(5)
        browser.quit()
