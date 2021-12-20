import os
import pytest
from selenium import webdriver


DRIVERS = os.path.expanduser("~/Desktop/drivers")


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera", "safari"])
    parser.addoption("--url", action="store", default="http://demo-opencart.ru/")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    driver = None

    if _browser == "chrome":
        option = webdriver.ChromeOptions()
        if headless:
            option.headless = True
        driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver", options=option)
    elif _browser == "firefox":
        option = webdriver.FirefoxOptions()
        if headless:
            option.headless = True
        driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver", options=option)
    elif _browser == "opera":
        driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")
    elif _browser == "safari":
        driver = webdriver.Safari()

    if maximized:
        driver.maximize_window()

    def final():
        driver.quit()
    driver.implicitly_wait(3)

    request.addfinalizer(final)

    return driver
