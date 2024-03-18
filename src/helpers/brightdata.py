from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from decouple import config
from urllib.parse import urljoin, urlparse


SBR_WEBDRIVER = config('SBR_WEBDRIVER', default=None)


def scrape(url=None, body_only=True, solve_captcha=False, wait_seconds=0):
    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    html = ""
    url = urljoin(url, urlparse(url).path)
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print(f'Connected! Navigating to {url}')
        driver.get(url)
        if wait_seconds > 0:
            driver.implicitly_wait(wait_seconds)
        if solve_captcha:
            solve_res = driver.execute('executeCdpCommand', {
                'cmd': 'Captcha.waitForSolve',
                'params': {'detectTimeout': 10000},
            })
            print('Captcha solve status:', solve_res['value']['status'])
        print('Navigated! Scraping page content...')
        html = driver.page_source
        if body_only:
            body = driver.find_element(By.TAG_NAME, "body")
            html = body.get_attribute('innerHTML')
    return html