from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import Client
import os
import time


@given('I am on Report Checked Manuscript Page')
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()
    context.browser.get(
        'http://127.0.0.1:8000/manuscripts/report/RQEHek6PGA.docx')


@when('I press Download button')
def step_impl(context):
    download_button = context.browser.find_element(By.ID, 'download-btn')
    download_button.click()
    time.sleep(5)  # Wait for 5 seconds, adjust as needed


@then('the report file should be downloaded successfully')
def step_impl(context):
    # Assuming the downloaded file will be in the Downloads directory
    download_directory = '"C:/Users/ammar/Downloads"'  # Update this path
    downloaded_file_path = os.path.join(download_directory, 'RQEHek6PGA.docx')

    # Wait for up to 10 seconds until the file is downloaded
    wait_time = 0
    max_wait_time = 10
    while not os.path.exists("C:/Users/ammar/Downloads") and wait_time < max_wait_time:
        time.sleep(1)
        wait_time += 1

    # Check if the file exists
    assert os.path.exists("C:/Users/ammar/Downloads"), f"Expected file '{
        downloaded_file_path}' not found"

    # Additional checks can be added based on your specific requirements
