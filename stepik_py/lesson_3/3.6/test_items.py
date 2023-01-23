import time

import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link_pass(browser):
    button_text = '.btn-add-to-basket'
    browser.get(link)
    try:
        browser.find_element(By.CSS_SELECTOR, button_text)
    except NoSuchElementException:
        assert False, 'Item is not available'
    time.sleep(30)
