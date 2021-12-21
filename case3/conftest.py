import pytest
from selenium import webdriver
import pytest
import logging


class ValidBrowsers:
    valid_browsers = (
        ["chrome", "edge", "firefox", "ie",
         "opera", "phantomjs", "safari",
         "android", "iphone", "ipad", "remote"])


class Browser:
    GOOGLE_CHROME = "chrome"
    EDGE = "edge"
    FIREFOX = "firefox"
    INTERNET_EXPLORER = "ie"
    OPERA = "opera"
    PHANTOM_JS = "phantomjs"
    SAFARI = "safari"
    ANDROID = "android"
    IPHONE = "iphone"
    IPAD = "ipad"
    REMOTE = "remote"

    VERSION = {
        "chrome": None,
        "edge": None,
        "firefox": None,
        "ie": None,
        "opera": None,
        "phantomjs": None,
        "safari": None,
        "android": None,
        "iphone": None,
        "ipad": None,
        "remote": None
    }

    LATEST = {
        "chrome": None,
        "edge": None,
        "firefox": None,
        "ie": None,
        "opera": None,
        "phantomjs": None,
        "safari": None,
        "android": None,
        "iphone": None,
        "ipad": None,
        "remote": None
    }


def pytest_addoption(parser):
    parser = parser.getgroup('SeleniumBase',
                             'SeleniumBase specific configuration options')
    parser.addoption('--browser',
                     action="store",
                     dest='browser',
                     type=str.lower,
                     choices=ValidBrowsers.valid_browsers,
                     default=Browser.GOOGLE_CHROME,
                     help="""Specifies the web browser to use. Default: Chrome.
                          If you want to use Firefox, explicitly indicate that.
                          Example: (--browser=firefox)""")

@pytest.fixture(scope="session")
def setup(request):

    browser = request.config.getoption("--browser")
    logger = logging.getLogger()
    logger.info(browser)
    driver = None
    if browser == "firefox":
        capabilities = {
            "browserName": "firefox",
            "browserVersion": "95.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }
        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=capabilities)
        driver.maximize_window()
    elif browser == "chrome":
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "95.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=capabilities)
    yield driver
    driver.close()


