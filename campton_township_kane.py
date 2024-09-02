import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time
import requests


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.camptontownship.com/main/Assessor/Online_Database/requestpin_form4.htm")
    list1 = ['08-25-252-015','08-25-276-001','08-25-276-002','08-25-277-002']
    for i in list1:

        page.get_by_role("textbox").click()
        page.get_by_role("textbox").fill(i)
        page.get_by_role("button", name="Submit PIN").click()
        time.sleep(5)
        # page.goto("https://www.camptontownship.com/main/Assessor/Online_Database/requestpin_response4.asp")

        html_content = page.content()
        with open(fr'C:\Users\swintern4\PycharmProjects\Webscraping\Campton\set3\{i}.html', 'w', encoding='utf-8') as file:
            file.write(html_content)

        time.sleep(2)
        print(i)
        page.get_by_role("link", name="Click here to request another").click()

        time.sleep(3)




        # ---------------------
        # context.close()
        # browser.close()


with sync_playwright() as playwright:
    run(playwright)