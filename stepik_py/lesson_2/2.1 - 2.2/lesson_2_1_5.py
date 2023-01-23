import time, math
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By


def calc(x): return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == '__main__':
    link = "https://suninjuly.github.io/math.html"
    x = "input_value"
    result = "answer"
    robot_cb = "[for='robotCheckbox']"
    robot_rb = "[for='robotsRule']"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        x_element = browser.find_element(By.ID, x).text
        y = calc(x_element)
        input2 = browser.find_element(By.ID, result)
        input2.send_keys(y)

        people_radio = browser.find_element(By.ID, "peopleRule")
        people_checked = people_radio.get_attribute("checked")
        print("value of people radio: ", people_checked)
        assert people_checked is not None, "People radio is not selected by default"

        option1 = browser.find_element(By.CSS_SELECTOR, robot_cb)
        option1.click()
        option2 = browser.find_element(By.CSS_SELECTOR, robot_rb)
        option2.click()

        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

    finally:
        time.sleep(5)
        browser.quit()
