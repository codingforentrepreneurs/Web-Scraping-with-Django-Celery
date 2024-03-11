from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from decouple import config
from urllib.parse import urljoin, urlparse


SBR_WEBDRIVER = config('SBR_WEBDRIVER', default=None)


def scrape(url=None, solve_captcha=False, wait_seconds=0):
    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    html = ""
    url = urljoin(url, urlparse(url).path)
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print(f'Connected! Navigating to {url}')
        driver.get(url)
        if wait_seconds > 0:
            driver.implicitly_wait(wait_seconds)
        # CAPTCHA handling: If you're expecting a CAPTCHA on the target page, use the following code snippet to check the status of Scraping Browser's automatic CAPTCHA solver
        # print('Waiting captcha to solve...')
        if solve_captcha:
            solve_res = driver.execute('executeCdpCommand', {
                'cmd': 'Captcha.waitForSolve',
                'params': {'detectTimeout': 10000},
            })
            print('Captcha solve status:', solve_res['value']['status'])
        print('Navigated! Scraping page content...')
        html = driver.page_source
    return html