from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from django.test import Client


@given('I am on Sign In Page')
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()
    context.browser.get('http://127.0.0.1:8000/accounts/login')

@when('I fill in "username" wih new username "testing_new"')
def step_impl(context):
    email_input = context.browser.find_element(By.ID, 'username')
    email_input.send_keys("testing_new")

@when("i fill all field in Sign In Form with existing account")
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/accounts/login')

    # Example: Use Selenium to fill in form fields
    username_input = context.browser.find_element(By.ID, 'username')
    username_input.send_keys('taufiqul')

    password_input = context.browser.find_element(By.ID, 'password')
    password_input.send_keys('88888888')

@when("i fill all field in Sign In Page with username and password without register")
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/accounts/login')

    # Example: Use Selenium to fill in form fields
    username_input = context.browser.find_element(By.ID, 'username')
    username_input.send_keys('randomizeaksdakjsdnknads')

    password_input = context.browser.find_element(By.ID, 'password')
    password_input.send_keys('88888888')

@when("I press Login button")
def step_impl(context):
    # Example: Use Selenium to click the SignIn button
    login = context.browser.find_element(By.ID, 'loginbutton')
    login.click()

@then("the response should contain Invalid Credentials")
def step_impl(context):
    assert "Invalid Credentials" in context.browser.page_source, f"Expected 'Invalid Credentials' not in page source, but got {context.browser.page_source}"

@then("I should be on Homepage")
def step_impl(context):
    # Implement code to check if the current page is the Search
    context.browser.get('http://127.0.0.1:8000/logged/')
    assert context.browser.current_url == 'http://127.0.0.1:8000/logged/', f"Expected Logged Homepage, but got {context.browser.current_url}"

@then("I should be on Login Page")
def step_impl(context):
    # Implement code to check if the current page is the SignIn page
    assert context.browser.current_url == 'http://127.0.0.1:8000/accounts/login/', f"Expected Login page, but got {context.browser.current_url}"
