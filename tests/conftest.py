import pytest
from selenium import webdriver

from utilities import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    driver = None
    if browser.__eq__("chrome"):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    app_url = ReadConfigurations.read_configuration("basic info","url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
