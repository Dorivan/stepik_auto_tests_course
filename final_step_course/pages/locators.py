from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "[name='registration-email']")
    PASSWORD_FIELD_1 = (By.CSS_SELECTOR, "[name='registration-password1']")
    PASSWORD_FIELD_2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    CONFIRM_REGISTRATION = (By.CSS_SELECTOR, "[name = 'registration_submit']")


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
    BASKET_BUTTON = (By.XPATH, "//a[contains(@href, 'basket') and @class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    SHOPPING_LIST = (By.CSS_SELECTOR, ".row > p")
    MESSAGE_IN_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    