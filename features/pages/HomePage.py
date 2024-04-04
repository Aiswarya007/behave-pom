from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from features.pages.BasePage import BasePage
from features.pages.LoginPage import LoginPage
from features.pages.RegistePage import RegisterPage
from features.pages.SearchPage import SearchPage


# class HomePage:
class HomePage(BasePage):

    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    def __init__(self, driver):
        super().__init__(driver)

    my_account_option_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    search_box_field_name = "search"
    search_button_xpath = "//div[@id='search']//button"
    register_option_link_text = "Register"

    def click_on_my_account(self):
        self.click_on_element("my_account_option_xpath", self.my_account_option_xpath)
        # self.driver.find_element(By.XPATH, self.my_account_option_xpath).click()

    def select_login_option(self):
        self.click_on_element("login_option_link_text", self.login_option_link_text)
        # self.driver.find_element(By.LINK_TEXT, self.login_option_link_text).click()
        return LoginPage(self.driver)

    def check_home_page_title(self, expected_title_text):
        return self.verify_page_title(expected_title_text)
        # return self.driver.title.__eq__(expected_title_text)

    def enter_product_into_search_box_field(self, product_text):
        self.type_into_element("search_box_field_name", self.search_box_field_name, product_text)
        # self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product_text)

    def click_on_search_button(self):
        self.click_on_element("search_button_xpath", self.search_button_xpath)
        # self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        return SearchPage(self.driver)

    def select_register_option(self):
        self.click_on_element("register_option_link_text", self.register_option_link_text)
        # self.driver.find_element(By.LINK_TEXT, self.register_option_link_text).click()
        return RegisterPage(self.driver)