from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import Client


@when('I press View History button')
def step_impl(context):
    view_history_button = context.browser.find_element(By.ID, 'history-button')
    view_history_button.click()


@then('I should be on History Page')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:8000/manuscripts/history', f"Expected History page, but got {context.browser.current_url}"
