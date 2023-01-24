from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_BUTTON_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main >h1")
    PRICE = (By.CSS_SELECTOR, ".product_main >p.price_color")
    ALLERT_NAME = (By.CSS_SELECTOR, "#messages div:first-child strong")
    ALLERT_PRICE = (By.CLASS_NAME, "alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
