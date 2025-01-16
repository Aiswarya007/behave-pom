from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.AccountPage import AccountPage
from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage
from utilities import EmailWithTimeStampGenerator


# def before_scenario(context):
#     context.driver = webdriver.Chrome()
#     context.driver.maximize_window()
#     context.driver.get("https://tutorialsninja.com/demo/")
#
#
# def after_scenario(context):
#     context.driver.quit()


@given('I navigate to login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    # context.home_page.select_login_option()
    context.login_page = context.home_page.select_login_option()
    # context.driver = webdriver.Chrome()
    # context.driver.maximize_window()
    # context.driver.get("https://tutorialsninja.com/demo/")
    # context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    # context.driver.find_element(By.LINK_TEXT, "Login").click()


# @when('I enter valid email address and valid password into the fields')
@when('I enter valid email address as "{email}" and valid password as "{password}" into the fields')
# def step_impl(context):
def step_impl(context, email, password):
    # context.login_page = LoginPage(context.driver)
    # context.login_page.enter_email_address("amotooriapril2023@gmail.com")
    # context.login_page.enter_password("12345")
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)
    # context.driver.find_element(By.ID, "input-email").send_keys("amotooriapril2023@gmail.com")
    # context.driver.find_element(By.ID, "input-password").send_keys("12345")


@when('I click on login button')
def step_impl(context):
    # context.login_page.click_on_login_button()
    context.account_page = context.login_page.click_on_login_button()
    # context.driver.find_element(By.XPATH, "//input[@value='Login']").click()


@then('I should get logged in')
def step_impl(context):
    # context.account_page = AccountPage(context.driver)
    assert context.account_page.display_status_of_edit_your_account_info_option()
    # assert context.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()
    # context.driver.quit()


# @when('I enter invalid email and valid password into the fields')
# def step_impl(context):
#     # generate invalid email everytime
#     time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
#     invalid_email = "amotoori" + time_stamp + "@gmail.com"
#     # context.login_page = LoginPage(context.driver)
#     context.login_page.enter_email_address(invalid_email)
#     context.login_page.enter_password("12345")
#     # context.driver.find_element(By.ID, "input-email").send_keys(invalid_email)
#     # context.driver.find_element(By.ID, "input-password").send_keys("12345")

# @when('I enter invalid email and valid password into the fields')
# def step_impl(context):
@when('I enter invalid email and valid password say "{password}" into the fields')
def step_impl(context, password):
    # generate invalid email everytime
    # time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    # invalid_email = "amotoori" + time_stamp + "@gmail.com"
    invalid_email = EmailWithTimeStampGenerator.get_new_email_with_timestamp()
    # context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address(invalid_email)
    # context.login_page.enter_password("12345")
    context.login_page.enter_password(password)
    # context.driver.find_element(By.ID, "input-email").send_keys(invalid_email)
    # context.driver.find_element(By.ID, "input-password").send_keys("12345")


@then('I should get a proper warning message')
def step_impl(context):
    # expected_warning = "Warning: No match for E-Mail Address and/or Password."
    # assert context.login_page.display_status_of_warning_message(expected_warning)
    assert context.login_page.display_status_of_warning_message("Warning: No match for E-Mail Address and/or Password.")
    # assert context.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(
    #     expected_warning)
    # context.driver.quit()


# @when('I enter valid email and invalid password into the fields')
# def step_impl(context):
#     # context.login_page = LoginPage(context.driver)
#     context.login_page.enter_email_address("amotooriapril2023@gmail.com")
#     context.login_page.enter_password("1234567")
#     # context.driver.find_element(By.ID, "input-email").send_keys("amotooriapril2023@gmail.com")
#     # context.driver.find_element(By.ID, "input-password").send_keys("1234567")

@when('I enter valid email say "{email}" and invalid password say "{password}" into the fields')
def step_impl(context, email, password):
    # context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)
    # context.driver.find_element(By.ID, "input-email").send_keys("amotooriapril2023@gmail.com")
    # context.driver.find_element(By.ID, "input-password").send_keys("1234567")


# @when('I enter invalid email and invalid password into the fields')
# def step_impl(context):
#     time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
#     invalid_email = "amotoori" + time_stamp + "@gmail.com"
#     # context.login_page = LoginPage(context.driver)
#     context.login_page.enter_email_address(invalid_email)
#     context.login_page.enter_password("1234567")
#     # context.driver.find_element(By.ID, "input-email").send_keys(invalid_email)
#     # context.driver.find_element(By.ID, "input-password").send_keys("1234567")

@when('I enter invalid email and invalid password say "{password}" into the fields')
def step_impl(context, password):
    # time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    # invalid_email = "amotoori" + time_stamp + "@gmail.com"
    invalid_email = EmailWithTimeStampGenerator.get_new_email_with_timestamp()
    # context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password(password)
    # context.driver.find_element(By.ID, "input-email").send_keys(invalid_email)
    # context.driver.find_element(By.ID, "input-password").send_keys("1234567")



@when('I dont enter anything into email and password fields')
def step_impl(context):
    # context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")
    # context.driver.find_element(By.ID, "input-email").send_keys("")
    # context.driver.find_element(By.ID, "input-password").send_keys("")
