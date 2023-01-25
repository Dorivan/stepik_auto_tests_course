from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time


def test_empty_basket_and_current_url(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    basket_page.should_be_message_in_basket()


def test_basket_with_items(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_button_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.go_to_basket()
    basket_page.should_be_not_empty_basket()
