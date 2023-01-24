from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest
import numpy as np


@pytest.mark.parametrize('num', np.array(range(10)))
def test_guest_can_add_product_to_basket(browser, num):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + str(num)
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_basket()
    page.click_on_button_basket()
    page.solve_quiz_and_get_code()
    page.must_be_equal_prices()
    page.must_be_equal_names()
