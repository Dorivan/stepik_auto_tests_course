import time, math
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    link = "http://suninjuly.github.io/registration1.html"
    value1 = ".first_class > input"
    value2 = "[placeholder='Input your last name']"
    value3 = "//input[contains(@placeholder,'email')]"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, value1)
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, value2)
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, value3)
        input3.send_keys("Email")
        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text
    finally:
        time.sleep(5)
        browser.quit()
