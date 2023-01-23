import time, math
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from lesson6_step4 import function

if __name__ == '__main__':
    link = "http://suninjuly.github.io/find_link_text"

    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/huge_form.html")
        elements = browser.find_elements(By.XPATH, "//input")
        for element in elements:
            element.send_keys("Мой ответ")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()
