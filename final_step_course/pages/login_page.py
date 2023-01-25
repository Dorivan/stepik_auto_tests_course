from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def register_new_user(self, email, passwd):
        self.go_to_login_page()
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        passwd_1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_1)
        passwd_1.send_keys(passwd)
        passwd_2 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_2)
        passwd_2.send_keys(passwd)
        self.browser.find_element(*LoginPageLocators.CONFIRM_REGISTRATION).click()
