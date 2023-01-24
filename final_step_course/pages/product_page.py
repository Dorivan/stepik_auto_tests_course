from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_on_button_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.ADD_BUTTON_BASKET)
        button_basket.click()

    def should_be_button_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON_BASKET), "Button is not present"
