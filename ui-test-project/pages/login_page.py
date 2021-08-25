from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    USERNAME_FIELD_ID = "sign-in-email"
    PASSWORD_FIELD_ID = "sign-in-passowrd"
    LOGIN_BUTTON_CLASS = "Button__StyledButton-sc-193vxdm-2"
    ERROR_MESSAGE_ID = "sign-in-email-helper"

    def login(self, username, password):
        self.write_in_element(By.ID, self.USERNAME_FIELD_ID, username)
        self.write_in_element(By.ID, self.PASSWORD_FIELD_ID, password)
        self.click_in_element(By.CLASS_NAME, self.LOGIN_BUTTON_CLASS)

    def find_error_message(self):
        return self.wait_element_visibility(By.ID, self.ERROR_MESSAGE_ID).text
