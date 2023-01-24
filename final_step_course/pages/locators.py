from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main >h1")
    PRICE = (By.CSS_SELECTOR, ".product_main >p.price_color")
    ALLERT_NAME = (By.CSS_SELECTOR, "#messages div:first-child strong")
    ALLERT_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
