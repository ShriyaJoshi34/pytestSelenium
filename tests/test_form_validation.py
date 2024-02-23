import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from pages.WatchDemo import WatchDemo

"""This test case checks the error message displayed when data is not entered in required field"""

@pytest.mark.usefixtures("setup_and_teardown")
class TestForm:
    def test_form_val(self):
        home_page = HomePage(self.driver)
        form_val = WatchDemo(self.driver)

        home_page.click_on_watch_demo_section()  # select watch demo from home page
        time.sleep(5)
        # to generate error message click on first name
        form_val.click_on_fname()
        # click outside the first name field without entering data
        form_val.click_on_body()
        # click on the first name field again and check for the error message displayed
        form_val.click_on_fname()
        time.sleep(2)
        assert self.driver.find_element(By.XPATH,form_val.fname_error_msg_field).text.__eq__(form_val.expected_error_msg)


        # self.driver.find_element(By.XPATH,"//div[@class='header-desktop-buttons hide-on-mobile']/a[1]").click()
        # time.sleep(5)
        # self.driver.find_element(By.XPATH,"//input[@id='FirstName']").click()
        # self.driver.find_element(By.XPATH,"//body").click()
        # self.driver.find_element(By.XPATH,"//input[@id='FirstName']").click()
        # time.sleep(3)
        # expected_error_msg = "This field is required."
        # assert self.driver.find_element(By.XPATH,"//*[@id='ValidMsgFirstName']").text.__eq__(expected_error_msg)



