from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_on_button_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.ADD_BUTTON_BASKET)
        button_basket.click()

    def should_be_button_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON_BASKET), "Button is not present"

    def must_be_equal_names(self):
        name_product = self.get_name()
        name_in_allert = self.browser.find_element(*ProductPageLocators.ALLERT_NAME).text
        assert name_product == name_in_allert, "Names of products not equal"

    def must_be_equal_prices(self):
        price_product = self.get_full_price()
        price_in_allert = self.browser.find_element(*ProductPageLocators.ALLERT_PRICE).text
        assert price_product == price_in_allert, "Price of products not equal"

    def get_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_full_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE).text

    def get_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE).text.split(' ')[0]
