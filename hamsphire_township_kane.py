import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://www.hampshiretownship.com/Online_Database/requestpin_form4.htm")
    list1 = ['01-21-426-030','01-28-252-006','01-28-252-007','01-28-252-008']
    for i in list1:

        page.get_by_role("textbox").click()
        page.get_by_role("textbox").fill(i)
        page.get_by_role("cell", name="Submit PIN", exact=True).click()
        time.sleep(3)
        html_content = page.content()
        with open(fr'C:\Users\swintern4\PycharmProjects\Webscraping\Hamsphire\set1\{i}.html', 'w', encoding='utf-8') as file:
            file.write(html_content)

        time.sleep(5)
        print(i)
        page.get_by_role("link", name="Click here to request another").click()

        # ---------------------
        # context.close()
        # browser.close()


with sync_playwright() as playwright:
    run(playwright)
