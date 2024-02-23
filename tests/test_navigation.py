import time
import pytest
from selenium.webdriver.common.by import By
from pages.HomePage import HomePage

"""This test case is for a basic navigation functionality 
We are checking the successful navigation to the resources page"""


@pytest.mark.usefixtures("setup_and_teardown")
class TestNav:
    def test_nav(self):
        home_page = HomePage(self.driver)
        time.sleep(5)
        home_page.hover_on_resources_section()  # hover over resource section on the home page
        home_page.click_on_resources_section()  # select All Resources
        time.sleep(10)
        # after successful navigation
        assert self.driver.find_element(By.XPATH, home_page.resource_landing_text_field).text.__eq__(
            home_page.resources_landing_expected_text)
