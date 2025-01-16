from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.HomePage import HomePage
from features.pages.SearchPage import SearchPage


# def before_scenario(context):
#     context.driver = webdriver.Chrome()
#     context.driver.maximize_window()
#     context.driver.get("https://tutorialsninja.com/demo/")
#
#
# def after_scenario(context):
#     context.driver.quit()


@given('I got navigated to Home Page')
def step_impl(context):
    # context.driver = webdriver.Chrome()
    # context.driver.maximize_window()
    # context.driver.get("https://tutorialsninja.com/demo/
    # nothing to change here, coz no locators are here, but can do if required
    # expected_title = "Your Store"
    context.home_page = HomePage(context.driver)
    # assert context.home_page.check_home_page_title(expected_title)
    assert context.home_page.check_home_page_title("Your Store")
    # assert context.driver.title.__eq__(expected_title)



# @when('I enter valid product into the Search box field')
# def step_impl(context):
#     context.home_page.enter_product_into_search_box_field("HP")
#     # context.driver.find_element(By.NAME, "search").send_keys("HP")
@when('I enter valid product say "{product}" into the Search box field')
def step_impl(context, product):
    context.home_page.enter_product_into_search_box_field(product)
    # context.driver.find_element(By.NAME, "search").send_keys("HP")


@when('I click on Search button')
def step_impl(context):
    context.search_page = context.home_page.click_on_search_button()
    # context.home_page.click_on_search_button()
    # context.driver.find_element(By.XPATH, "//div[@id='search']//button").click()


@then('Proper message should be displayed in Search results')
def step_impl(context):
    # expected_text = "There is no product that matches the search criteria."
    # search_page = SearchPage(context.driver)
    # assert search_page.display_status_of_message(expected_text)
    # assert context.search_page.display_status_of_message("There is no product that matches the search criteria.")
    assert context.search_page.display_status_of_message("There is no product that matches the search criteria.abc")
    # assert context.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(
    #     expected_text)
    # context.driver.quit()


@when('I dont enter anything into Search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box_field("")
    # context.driver.find_element(By.NAME, "search").send_keys("")


@then('Valid product should get displayed in Search results')
def step_impl(context):
    # search_page = SearchPage(context.driver)
    # assert search_page.display_status_of_product()
    assert context.search_page.display_status_of_product()
    # assert context.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    # context.driver.quit()


# @when('I enter invalid product into the Search box field')
# def step_impl(context):
#     context.home_page.enter_product_into_search_box_field("Honda")
#     # context.driver.find_element(By.NAME, "search").send_keys("Honda")

@when('I enter invalid product say "{product}" into the Search box field')
def step_impl(context, product):
    context.home_page.enter_product_into_search_box_field(product)
    # context.driver.find_element(By.NAME, "search").send_keys("Honda")
