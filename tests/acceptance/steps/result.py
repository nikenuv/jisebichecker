from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import Client


# @given('I am on Report Checked Manuscript Page')
# def step_impl(context):
#     context.client = Client()
#     context.browser = webdriver.Chrome()
#     context.browser.get(
#         'http://127.0.0.1:8000/manuscripts/report/RQEHek6PGA.docx')


@given('I press View Full Report button')
def step_impl(context):
    view_report_button = context.browser.find_element(
        By.ID, "full-view")
    view_report_button.click()


@then('I should be on Full Report Page')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:8000/manuscripts/report/RQEHek6PGA.docx/full', f"Expected Full Report page, but got {
        context.browser.current_url}"
