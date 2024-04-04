from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from features.pages.AccountPage import AccountPage
from features.pages.BasePage import BasePage


# class LoginPage:
class LoginPage(BasePage):

    # def __init__(self, driver :WebDriver):
    #     self.driver = driver

    def __init__(self, driver):
        super().__init__(driver)

    email_address_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@id='account-login']/div[1]"

    def enter_email_address(self, email_text):
        self.type_into_element("email_address_field_id", self.email_address_field_id, email_text)
        # self.driver.find_element(By.ID, self.email_address_field_id).send_keys(email_text)

    def enter_password(self, password_text):
        self.type_into_element("password_field_id", self.password_field_id, password_text)
        # self.driver.find_element(By.ID, self.password_field_id).send_keys(password_text)

    def click_on_login_button(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)
        # self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        return AccountPage(self.driver)

    def display_status_of_warning_message(self, expected_warning_text):
        return self.retrieved_element_text_contains("warning_message_xpath", self.warning_message_xpath, expected_warning_text)
        # return self.driver.find_element(By.XPATH, self.warning_message_xpath).text.__contains__(expected_warning_text)