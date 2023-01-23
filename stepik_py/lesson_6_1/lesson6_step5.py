import time, math
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from lesson6_step4 import function

if __name__ == '__main__':
    link = "http://suninjuly.github.io/find_link_text"

    try:
        browser = webdriver.Chrome()
        browser.get(link)
        code = str(math.ceil(math.pow(math.pi, math.e)*10000))
        link = browser.find_element(By.LINK_TEXT, code)
        link.click()

        function(browser)

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()
