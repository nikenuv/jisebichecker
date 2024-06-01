from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from django.test import Client
from django.db import connection, migrations


@given('I am on Register Page')
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()
    context.browser.get('http://127.0.0.1:8000/accounts/register/')

@when('I fill in "email" wih new email "testing@gmail.com"')
def step_impl(context):
    email_input = context.browser.find_element(By.ID, 'email')
    email_input.send_keys("testing@gmail.com")

@when('I fill in "username" wih new username "testing"')
def step_impl(context):
    uname_input = context.browser.find_element(By.ID, 'username')
    uname_input.send_keys("testing")

@when('I fill in "password" wih "88888888"')
def step_impl(context):
    pw_input = context.browser.find_element(By.ID, 'password1')
    pw_input.send_keys("88888888")

@when('I fill in "confirm_password" with "88888888"')
def step_impl(context):
    cpw_input = context.browser.find_element(By.ID, 'password2')
    cpw_input.send_keys("88888888")

@when('I fill in "confirm_password" with "88888889"')
def step_impl(context):
    cpw_input = context.browser.find_element(By.ID, 'password2')
    cpw_input.send_keys("88888889")


# @when('I fill Register Form with an already existing username')
# def step_impl(context):
#     context.Register_data = {'email': 'qorni@gmail.com', 'username': 'marr',
#                              'password1': 'ammar123', 'password2': 'ammar123'}
#     context.browser.get('http://127.0.0.1:8000/accounts/register/')

#     email_input = context.browser.find_element(By.ID, 'email')
#     username_input = context.browser.find_element(By.ID, 'username')
#     password_input = context.browser.find_element(By.ID, 'password1')
#     confirm_password_input = context.browser.find_element(
#         By.ID, 'password2')

#     email_input.send_keys(context.Register_data['email'])
#     username_input.send_keys(context.Register_data['username'])
#     password_input.send_keys(context.Register_data['password1'])
#     confirm_password_input.send_keys(context.Register_data['password2'])

@when('I fill in "email" wih new email "testing1@gmail.com"')
def step_impl(context):
    email_input = context.browser.find_element(By.ID, 'email')
    email_input.send_keys("testing1@gmail.com")

@when('I fill in "username" wih existing username "testing"')
def step_impl(context):
    uname_input = context.browser.find_element(By.ID, 'username')
    uname_input.send_keys("testing")

@when('I press Sign Up button')
def step_impl(context):
    signup_button = context.browser.find_element(By.ID, 'regist-btn')
    signup_button.click()


@then('I should be on SignIn Page')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:8000/accounts/login/', f"Expected SignIn page, but got {context.browser.current_url}"


@then('the response should contain Password does not match')
def step_impl(context):
    assert "Passwords do not match" in context.browser.page_source, f"Expected 'Passwords do not match' not in page source, but got {context.browser.page_source}"


@then('the response should contain Username already exists')
def step_impl(context):
    alert_element = context.browser.find_element(By.CLASS_NAME, 'alert-danger')

    # Assert that the alert is displayed
    assert alert_element.is_displayed(), "Expected 'alert-danger' to be displayed, but it is not"

    # Assert that the alert text contains "Username is taken"
    assert "Username is taken" in alert_element.text, "Expected 'Username is taken' in the alert text, but it is not"


@then('I should be on Register Page')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:8000/accounts/register/', f"Expected signup page, but got {context.browser.current_url}"
