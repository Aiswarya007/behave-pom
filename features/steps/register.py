from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.AccountSuccessPage import AccountSuccessPage
from features.pages.HomePage import HomePage
from features.pages.RegistePage import RegisterPage
from utilities import EmailWithTimeStampGenerator


# def before_scenario(context):
#     context.driver = webdriver.Chrome()
#     context.driver.maximize_window()
#     context.driver.get("https://tutorialsninja.com/demo/")
#
#
# def after_scenario(context):
#     context.driver.quit()

@given('I navigate to Register Page')
def step_impl(context):
    # context.driver = webdriver.Chrome()
    # context.driver.maximize_window()
    # context.driver.get("https://tutorialsninja.com/demo/")
    context.home_page = HomePage(context.driver)
    # context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    # context.driver.find_element(By.LINK_TEXT, "Register").click()
    context.home_page.click_on_my_account()
    # context.home_page.select_register_option()
    context.register_page = context.home_page.select_register_option()


# @when('I enter details into mandatory fields')
# def step_impl(context):
#     # context.register_page = RegisterPage(context.driver)
#     # context.driver.find_element(By.ID, "input-firstname").send_keys("Aiswarya")
#     # context.driver.find_element(By.ID, "input-lastname").send_keys("J")
#     context.register_page.enter_first_name("Aiswarya")
#     context.register_page.enter_last_name("J")
#     time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
#     new_email = "amotoori" + time_stamp + "@gmail.com"
#     # context.driver.find_element(By.ID, "input-email").send_keys(new_email)
#     # context.driver.find_element(By.ID, "input-telephone").send_keys("123456789")
#     # context.driver.find_element(By.ID, "input-password").send_keys("12345")
#     # context.driver.find_element(By.ID, "input-confirm").send_keys("12345")
#     context.register_page.enter_email(new_email)
#     context.register_page.enter_telephone("123456789")
#     context.register_page.enter_password("12345")
#     context.register_page.enter_password_confirm("12345")
@when('I enter below details into mandatory fields')
def step_impl(context):
    for row in context.table:
        # context.register_page = RegisterPage(context.driver)
        # context.driver.find_element(By.ID, "input-firstname").send_keys("Aiswarya")
        # context.driver.find_element(By.ID, "input-lastname").send_keys("J")
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        # time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        # new_email = "amotoori" + time_stamp + "@gmail.com"
        new_email = EmailWithTimeStampGenerator.get_new_email_with_timestamp()
        # context.driver.find_element(By.ID, "input-email").send_keys(new_email)
        # context.driver.find_element(By.ID, "input-telephone").send_keys("123456789")
        # context.driver.find_element(By.ID, "input-password").send_keys("12345")
        # context.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        context.register_page.enter_email(new_email)
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_password_confirm(row["password"])


@when('I select Privacy Policy option')
def step_impl(context):
    context.register_page.select_privacy_policy()
    # context.driver.find_element(By.NAME, "agree").click()


@when('I click on Continue button')
def step_impl(context):
    # context.register_page.click_on_continue_button()
    context.account_success_page = context.register_page.click_on_continue_button()
    # context.driver.find_element(By.XPATH, "//input[@value='Continue']").click()


@then('Account should get created')
def step_impl(context):
    # expected_text = "Your Account Has Been Created!"
    # account_success_page = AccountSuccessPage(context.driver)
    # assert account_success_page.display_status_of_account_created_heading(expected_text)
    assert context.account_success_page.display_status_of_account_created_heading("Your Account Has Been Created!")
    # assert context.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_text)
    # context.driver.quit()


# @when('I enter details into all fields')
# def step_impl(context):
#     # context.driver.find_element(By.ID, "input-firstname").send_keys("Aiswarya")
#     # context.driver.find_element(By.ID, "input-lastname").send_keys("J")
#     # time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
#     # new_email = "amotoori" + time_stamp + "@gmail.com"
#     # context.driver.find_element(By.ID, "input-email").send_keys(new_email)
#     # context.driver.find_element(By.ID, "input-telephone").send_keys("123456789")
#     # context.driver.find_element(By.ID, "input-password").send_keys("12345")
#     # context.driver.find_element(By.ID, "input-confirm").send_keys("12345")
#     # context.driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='1']").click()
#     # context.register_page = RegisterPage(context.driver)
#     context.register_page.enter_first_name("Aiswarya")
#     context.register_page.enter_last_name("J")
#     time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
#     new_email = "amotoori" + time_stamp + "@gmail.com"
#     context.register_page.enter_email(new_email)
#     context.register_page.enter_telephone("123456789")
#     context.register_page.enter_password("12345")
#     context.register_page.enter_password_confirm("12345")
#     context.register_page.select_yes_newsletter_option()

@when('I enter below details into all fields')
def step_impl(context):
    for row in context.table:
        # context.driver.find_element(By.ID, "input-firstname").send_keys("Aiswarya")
        # context.driver.find_element(By.ID, "input-lastname").send_keys("J")
        # time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        # new_email = "amotoori" + time_stamp + "@gmail.com"
        # context.driver.find_element(By.ID, "input-email").send_keys(new_email)
        # context.driver.find_element(By.ID, "input-telephone").send_keys("123456789")
        # context.driver.find_element(By.ID, "input-password").send_keys("12345")
        # context.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        # context.driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='1']").click()
        # context.register_page = RegisterPage(context.driver)
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        # time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        # new_email = "amotoori" + time_stamp + "@gmail.com"
        new_email = EmailWithTimeStampGenerator.get_new_email_with_timestamp()
        context.register_page.enter_email(new_email)
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_password_confirm(row["password"])
        context.register_page.select_yes_newsletter_option()


# @when('I enter details into all fields except email field')
# def step_impl(context):
#     # context.driver.find_element(By.ID, "input-firstname").send_keys("Aiswarya")
#     # context.driver.find_element(By.ID, "input-lastname").send_keys("J")
#     # context.driver.find_element(By.ID, "input-telephone").send_keys("123456789")
#     # context.driver.find_element(By.ID, "input-password").send_keys("12345")
#     # context.driver.find_element(By.ID, "input-confirm").send_keys("12345")
#     # context.driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='1']").click()
#     # context.register_page = RegisterPage(context.driver)
#     context.register_page.enter_first_name("Aiswarya")
#     context.register_page.enter_last_name("J")
#     context.register_page.enter_telephone("123456789")
#     context.register_page.enter_password("12345")
#     context.register_page.enter_password_confirm("12345")
#     context.register_page.select_yes_newsletter_option()
@when('I enter details into all fields except email field')
def step_impl(context):
    for row in context.table:
        # context.driver.find_element(By.ID, "input-firstname").send_keys("Aiswarya")
        # context.driver.find_element(By.ID, "input-lastname").send_keys("J")
        # context.driver.find_element(By.ID, "input-telephone").send_keys("123456789")
        # context.driver.find_element(By.ID, "input-password").send_keys("12345")
        # context.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        # context.driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='1']").click()
        # context.register_page = RegisterPage(context.driver)
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_password_confirm(row["password"])
        context.register_page.select_yes_newsletter_option()


@when('I enter existing accounts email into email field')
def step_impl(context):
    context.register_page.enter_email("amotooriapril2023@gmail.com")
    # context.driver.find_element(By.ID, "input-email").send_keys("amotooriapril2023@gmail.com")


@then('Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    # expected_warning = "Warning: E-Mail Address is already registered!"
    # assert context.register_page.display_status_of_duplicate_email_warning(expected_warning)
    assert context.register_page.display_status_of_duplicate_email_warning("Warning: E-Mail Address is already registered!")
    # assert (context.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]")
    #         .text.__contains__(expected_warning))
    # context.driver.quit()


@when('I dont enter anything into the fields')
def step_impl(context):
    # context.driver.find_element(By.ID, "input-firstname").send_keys("")
    # context.driver.find_element(By.ID, "input-lastname").send_keys("")
    # context.driver.find_element(By.ID, "input-email").send_keys("")
    # context.driver.find_element(By.ID, "input-telephone").send_keys("")
    # context.driver.find_element(By.ID, "input-password").send_keys("")
    # context.driver.find_element(By.ID, "input-confirm").send_keys("")

    # context.register_page = RegisterPage(context.driver)
    context.register_page.enter_first_name("")
    context.register_page.enter_last_name("")
    context.register_page.enter_email("")
    context.register_page.enter_telephone("")
    context.register_page.enter_password("")
    context.register_page.enter_password_confirm("")


@then('Proper warning messages for every mandatory fields should be displayed')
def step_impl(context):
    # expected_privacy_policy_warning = "Warning: You must agree to the Privacy Policy!"
    # expected_first_name_warning = "First Name must be between 1 and 32 characters!"
    # expected_last_name_warning = "Last Name must be between 1 and 32 characters!"
    # expected_email_warning = "E-Mail Address does not appear to be valid!"
    # expected_telephone_warning = "Telephone must be between 3 and 32 characters!"
    # expected_password_warning = "Password must be between 4 and 20 characters!"
    #
    # assert context.register_page.display_status_of_all_warning_messages(expected_privacy_policy_warning,
    #                                                                     expected_first_name_warning, expected_last_name_warning,
    #                                                                     expected_email_warning, expected_telephone_warning,
    #                                                                     expected_password_warning)

    assert context.register_page.display_status_of_all_warning_messages("Warning: You must agree to the Privacy Policy!",
                                                                        "First Name must be between 1 and 32 characters!",
                                                                        "Last Name must be between 1 and 32 characters!",
                                                                        "E-Mail Address does not appear to be valid!",
                                                                        "Telephone must be between 3 and 32 characters!",
                                                                        "Password must be between 4 and 20 characters!")

    # assert (context.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]")
    #         .text.__contains__(expected_privacy_policy_warning))
    # assert (context.driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div")
    #         .text.__eq__(expected_first_name_warning))
    # assert (context.driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div")
    #         .text.__eq__(expected_last_name_warning))
    # assert (context.driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div")
    #         .text.__eq__(expected_email_warning))
    # assert (context.driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div")
    #         .text.__eq__(expected_telephone_warning))
    # assert (context.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div")
    #         .text.__eq__(expected_password_warning))

    # context.driver.quit()


