import time, math
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    link = "http://suninjuly.github.io/registration1.html"
    value1 = "//input[contains(@placeholder,'first')]"
    value2 = "//input[contains(@placeholder,'last')]"
    value3 = "//input[contains(@placeholder,'email')]"
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, value1)
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, value2)
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, value3)
        input3.send_keys("Smolensk")
        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()
