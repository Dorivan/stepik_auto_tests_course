import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAbs(unittest.TestCase):
    variables = [
        {
            'selector': ".first_class > input",
            'value': "Ivan",
            'By': By.CSS_SELECTOR
        },
        {
            'selector': "[placeholder='Input your last name']",
            'value': "Petrov",
            'By': By.CSS_SELECTOR
        },
        {
            'selector': "//input[contains(@placeholder,'email')]",
            'value': "Email",
            'By': By.XPATH
        },
        {
            'selector': "//button[@type='submit']",
            'value': None,
            'By': By.XPATH
        },
        {
            'selector': "h1",
            'value': None,
            'By': By.TAG_NAME
        }
    ]
    time_remaining = 2

    def body_of_tests(self, link):
        try:
            browser = webdriver.Chrome()
            for i in range(len(self.variables) - 2):
                browser.find_element(
                    self.variables[i]['By'], self.variables[i]['selector']).send_keys(
                    self.variables[i]['value']
                )

            browser.find_element(
                self.variables[3]['By'], self.variables[3]['selector']).click()

            welcome_text = WebDriverWait(browser, self.time_remaining).until(
                EC.element_to_be_clickable((
                    self.variables[4]['By'], self.variables[4]['selector']))
            ).text

            self.assertEqual(
                "Congratulations! You have successfully registered!", welcome_text,
                "Text is not Equal")
        finally:
            browser.quit()

    def test_first_link(self):
        self.body_of_tests('http://suninjuly.github.io/registration1.html')

    def test_second_link(self):
        self.body_of_tests('http://suninjuly.github.io/registration2.html')


if __name__ == "__main__":
    unittest.main()
