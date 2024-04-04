from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from features.pages.AccountSuccessPage import AccountSuccessPage
from features.pages.BasePage import BasePage


# class RegisterPage:
class RegisterPage(BasePage):

    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    password_confirm_field_id = "input-confirm"
    privacy_policy_option_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    yes_radio_option_xpath = "//input[@name='newsletter'][@value='1']"
    duplicate_email_warning_xpath = "//div[@id='account-register']/div[1]"
    privacy_policy_warning_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_warning_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_warning_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_warning_xpath = "//input[@id='input-password']/following-sibling::div"

    def enter_first_name(self, first_name_text):
        self.type_into_element("first_name_field_id", self.first_name_field_id, first_name_text)
        # self.driver.find_element(By.ID, self.first_name_field_id).send_keys(first_name_text)

    def enter_last_name(self, last_name_text):
        self.type_into_element("last_name_field_id", self.last_name_field_id, last_name_text)
        # self.driver.find_element(By.ID, self.last_name_field_id).send_keys(last_name_text)

    def enter_email(self, email_text):
        self.type_into_element("email_field_id", self.email_field_id, email_text)
        # self.driver.find_element(By.ID, self.email_field_id).send_keys(email_text)

    def enter_telephone(self, telephone_text):
        self.type_into_element("telephone_field_id", self.telephone_field_id, telephone_text)
        # self.driver.find_element(By.ID, self.telephone_field_id).send_keys(telephone_text)

    def enter_password(self, password_text):
        self.type_into_element("password_field_id", self.password_field_id, password_text)
        # self.driver.find_element(By.ID, self.password_field_id).send_keys(password_text)

    def enter_password_confirm(self, password_confirm_text):
        self.type_into_element("password_confirm_field_id", self.password_confirm_field_id, password_confirm_text)
        # self.driver.find_element(By.ID, self.password_confirm_field_id).send_keys(password_confirm_text)

    def select_privacy_policy(self):
        self.click_on_element("privacy_policy_option_name", self.privacy_policy_option_name)
        # self.driver.find_element(By.NAME, self.privacy_policy_option_name).click()

    def click_on_continue_button(self):
        self.click_on_element("continue_button_xpath", self.continue_button_xpath)
        # self.driver.find_element(By.XPATH, self.continue_button_xpath).click()
        return AccountSuccessPage(self.driver)

    def select_yes_newsletter_option(self):
        self.click_on_element("yes_radio_option_xpath", self.yes_radio_option_xpath)
        # self.driver.find_element(By.XPATH, self.yes_radio_option_xpath).click()

    def display_status_of_duplicate_email_warning(self, expected_warning_text):
        return self.retrieved_element_text_contains("duplicate_email_warning_xpath", self.duplicate_email_warning_xpath,
                                                    expected_warning_text)
        # return self.driver.find_element(By.XPATH, self.duplicate_email_warning_xpath).text.__contains__(expected_warning_text)

    def display_status_of_all_warning_messages(self, expected_privacy_warning, expected_first_name_warning, expected_last_name_warning,
                                               expected_email_warning, expected_telephone_warning, expected_password_warning):
        privacy_status = self.retrieved_element_text_contains("privacy_policy_warning_xpath", self.privacy_policy_warning_xpath,
                                                              expected_privacy_warning)
        first_name_status = self.retrieved_element_text_equals("first_name_warning_xpath", self.first_name_warning_xpath,
                                                               expected_first_name_warning)
        last_name_status = self.retrieved_element_text_equals("last_name_warning_xpath", self.last_name_warning_xpath,
                                                              expected_last_name_warning)
        email_status = self.retrieved_element_text_equals("email_warning_xpath", self.email_warning_xpath, expected_email_warning)
        telephone_status = self.retrieved_element_text_equals("telephone_warning_xpath", self.telephone_warning_xpath,
                                                              expected_telephone_warning)
        password_status = self.retrieved_element_text_equals("password_warning_xpath", self.password_warning_xpath,
                                                             expected_password_warning)
        # privacy_status = self.driver.find_element(By.XPATH, self.privacy_policy_warning_xpath).text.__contains__(expected_privacy_warning)
        # first_name_status = self.driver.find_element(By.XPATH, self.first_name_warning_xpath).text.__eq__(expected_first_name_warning)
        # last_name_status = self.driver.find_element(By.XPATH, self.last_name_warning_xpath).text.__eq__(expected_last_name_warning)
        # email_status = self.driver.find_element(By.XPATH, self.email_warning_xpath).text.__eq__(expected_email_warning)
        # telephone_status = self.driver.find_element(By.XPATH, self.telephone_warning_xpath).text.__eq__(expected_telephone_warning)
        # password_status = self.driver.find_element(By.XPATH, self.password_warning_xpath).text.__eq__(expected_password_warning)

        # if privacy_status and first_name_status and last_name_status and email_status and telephone_status and password_status:
        #     return True
        # else:
        #     return False

        return self.return_and_status(privacy_status, first_name_status, last_name_status, email_status, telephone_status, password_status)
