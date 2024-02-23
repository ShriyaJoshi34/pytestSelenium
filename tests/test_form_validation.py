import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.HomePage import HomePage
from pages.WatchDemo import WatchDemo

"""This test case checks the error message displayed when data is not entered in required field"""


@pytest.mark.usefixtures("setup_and_teardown")
class TestForm:
    def test_form_val(self):
        home_page = HomePage(self.driver)
        form_val = WatchDemo(self.driver)
        element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, home_page.watch_demo_field)))
        if element:
            home_page.click_on_watch_demo_section()  # select watch demo from home page
            time.sleep(5)
            # to generate error message click on first name
            form_val.click_on_fname()
            # click outside the first name field without entering data
            form_val.click_on_body()
            # click on the first name field again and check for the error message displayed
            form_val.click_on_fname()
            time.sleep(2)
            assert self.driver.find_element(By.XPATH, form_val.fname_error_msg_field).text.__eq__(
                form_val.expected_error_msg)

