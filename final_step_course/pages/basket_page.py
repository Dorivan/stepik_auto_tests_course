from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_not_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.SHOPPING_LIST), \
            "Basket is empty, but should be not"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.SHOPPING_LIST), \
            "Basket is not empty, but should be"

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url

    def should_be_message_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_IN_BASKET), \
            "Message is not present"
