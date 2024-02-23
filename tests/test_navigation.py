import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.HomePage import HomePage

"""This test case is for a basic navigation functionality 
We are checking the successful navigation to the resources page"""


@pytest.mark.usefixtures("setup_and_teardown")
class TestNav:
    def test_nav(self):
        home_page = HomePage(self.driver)
        element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, home_page.hover_search_resources_field)))
        if element:
            home_page.hover_on_resources_section()  # hover over resource section on the home page
            home_page.click_on_resources_section()  # select All Resources
            # after successful navigation
            assert self.driver.find_element(By.XPATH, home_page.resource_landing_text_field).text.__eq__(
                home_page.resources_landing_expected_text)
