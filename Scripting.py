# pip install playwright
# playwright install chromium
# playwright codegen

import time
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/search?q=today+date+and+current+time&oq=today+date+and+current+time&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTE0NTAzajBqMqgCALACAQ&sourceid=chrome&ie=UTF-8")
    page1 = context.new_page()
    page1.goto("https://www.google.com/search?q=code+alpha&oq=code+alpha&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDM5OTZqMGoxqAIAsAIB&sourceid=chrome&ie=UTF-8")
    page1.get_by_role("link", name="Elevate Your Career With").click()
    page2 = context.new_page()
    page2.goto("https://www.google.com/search?q=thanks&oq=thanks+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDM1ODJqMGoxqAIAsAIA&sourceid=chrome&ie=UTF-8")
    page2.get_by_label("Filters and topics").get_by_role("link", name="Images").click()

    time.sleep(15)
    # ---------------------

    
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
