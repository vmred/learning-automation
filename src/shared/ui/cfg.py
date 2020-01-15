import os
from selene import config, browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

config.browser_name = os.getenv('browser', 'chrome')
config.timeout = 60

timeout = config.timeout
browser = browser


def get_chrome_options():
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--window-size=1920x1080')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return options


def set_chrome_driver():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                              options=get_chrome_options(),
                              desired_capabilities=config.desired_capabilities)
    browser.set_driver(driver)


set_chrome_driver()
