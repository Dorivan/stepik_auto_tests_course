import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

list_urls = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class Test_login():
    email = 'killer.spy@yandex.ru'
    paswd = 'Nikitosperminov^^1488'

    #@pytest.mark.skip
    def test_login(self, browser):
        link = f"https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, "ember33"))
        )
        browser.find_element(By.ID, "ember33").click()

        login = browser.find_element(By.CSS_SELECTOR, "[name='login']")
        login.send_keys(self.email)
        pass_field = browser.find_element(By.CSS_SELECTOR, "[name='password']")
        pass_field.send_keys(self.paswd)
        browser.find_element(By.CLASS_NAME, "button_with-loader").click()

        span = "//span[text()[contains(., 'загрузка')]]"
        WebDriverWait(browser, 15).until_not(
            EC.presence_of_element_located((By.XPATH, span))
        )
        time.sleep(5)

    # @pytest.mark.skip
    @pytest.mark.parametrize('url', list_urls)
    def test_guest_should_see_login_link(self, browser, url):
        link = f"https://stepik.org/lesson/{url}/step/1"
        browser.get(link)

        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div/textarea"))
        )
        answer = math.log(int(time.time()))
        text_area = browser.find_element(By.XPATH, "//div/textarea")
        text_area.send_keys(str(answer))
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
        time.sleep(25)
        smart_move = 'smart-hints__hint'
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, smart_move))
        )
