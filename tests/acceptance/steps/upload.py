from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import Client
from selenium.webdriver.common.keys import Keys
import os, time


@given('I am on Upload Manuscript Page')
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
    context.browser.get("http://127.0.0.1:8000/manuscripts/upload/")


@when('I upload .docx Manuscript file on Upload field')
# def step_impl(context):
#     # Ganti "iframe_id" dengan ID iframe yang benar
#     context.browser.switch_to.frame("iframe_id")
#     file_input = context.browser.find_element(By.ID, 'file')
#     path_file_docx = 'tests/45974 Audia.docx'
#     file_input.send_keys('tests/45974 Audia.docx')
#     context.browser.switch_to.default_content()
def step_when(context):
    current = os.getcwd()
    file_path = current + '\\tests\\45974 Audia.docx'
    file_input = context.browser.find_element(By.ID, 'file')
    # Set the file path in the file input field
    file_input.send_keys(file_path)


@when('I upload .pdf Manuscript file on Upload field')
# def step_impl(context):
#     file_input = context.browser.find_element(By.ID, 'file')
#     path_file_pdf = 'tests/46654 S.pdf'
#     file_input.send_keys('tests/46654 S.pdf')
def step_when(context):
    current = os.getcwd()
    file_path = current + '\\tests\\46654 S.pdf'
    file_input = context.browser.find_element(By.ID, 'file')
    # Set the file path in the file input field
    file_input.send_keys(file_path)


@when('I press Check Now! button')
def step_impl(context):
    check_now_button = context.browser.find_element(By.ID, 'check-now-button')
    check_now_button.click()


@then('I should be on Report Page')
def step_impl(context):
    failed_report_locator = (By.CLASS_NAME, 'report-box-failed')
    success_report_locator = (By.CLASS_NAME, 'report-box-success')

    try:
        WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located(failed_report_locator)
            or EC.presence_of_element_located(success_report_locator)
        )
    except TimeoutError:
        assert False, "Neither 'report-box-failed' nor 'report-box-success' element found on the Report Page"

    assert True, "At least one of the expected elements is present on the Report Page"

@then('I should be on Upload Manuscript Page')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:8000/manuscripts/upload/', f"Expected Upload Manuscript page, but got {context.browser.current_url}"


@then('The response should contain Wrong Uploaded File Type')
def step_impl(context):
    assert "Wrong Uploaded File Type" in context.browser.page_source, f"Expected 'Wrong Uploaded File Type' not in page source, but got {context.browser.page_source}"
