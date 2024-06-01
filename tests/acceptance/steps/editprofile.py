from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import Client


@given('I am on Logged In Homepage')
def step_impl(context):

    context.client = Client()
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    
    context.browser.get('http://127.0.0.1:8000/accounts/login')

    # Example: Use Selenium to fill in form fields
    username_input = context.browser.find_element(By.ID, 'username')
    username_input.send_keys('testing')

    password_input = context.browser.find_element(By.ID, 'password1')
    password_input.send_keys('88888888')

    login = context.browser.find_element(By.ID, 'loginbutton')
    login.click()

    context.browser.get('http://127.0.0.1:8000/logged/')

@when('I press User Profile button')
def step_impl(context):
    user_profile_button = context.browser.find_element(By.XPATH, '/html/body/nav/div/div/a')
    user_profile_button.click()

@when('i press Edit Profile button')
def step_impl(context):
    user_profile_button = context.browser.find_element(By.ID, 'edit-profile')
    user_profile_button.click()
    

@then('i should be on Edit Profile Page')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:8000/accounts/editProfile/', f"Expected Edit Profile page, but got {context.browser.current_url}"


@when('I enter a new email and username in the Edit Profile fields')
def step_impl(context):
    context.Register_data = {
        'new_email': 'ammarqorni@gmail.com', 'new_username': 'alqorni'}
    context.browser.get('http://127.0.0.1:8000/accounts/editProfile/')

    email_input = context.browser.find_element(By.ID, 'new_email')
    username_input = context.browser.find_element(By.ID, 'new_username')

    email_input.send_keys(context.Register_data['new_email'])
    username_input.send_keys(context.Register_data['new_username'])


@when('I press Save button')
def step_impl(context):
    save_button = context.browser.find_element(By.XPATH, '/html/body/div/div/form/button')
    save_button.click()
