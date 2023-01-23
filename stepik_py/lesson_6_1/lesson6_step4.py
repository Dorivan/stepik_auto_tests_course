import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    # link = "http://suninjuly.github.io/simple_form_find_task.html"  # Step 4
    link = "http://suninjuly.github.io/find_xpath_form"
    value1 = "input"  # "//input[@name='first_name']"
    value2 = "last_name"  # "//input[@name='last_name']"
    value3 = "form-control.city"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.TAG_NAME, value1)
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, value2)
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, value3)
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()
