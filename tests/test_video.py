import time
import pytest
from selenium.webdriver.common.by import By
from pages.HomePage import HomePage

"""This test case checks the play-pause functionality and availability of that attribute"""


@pytest.mark.usefixtures("setup_and_teardown")
class TestVideo:
    def test_video(self):
        home_page = HomePage(self.driver)
        time.sleep(5)
        home_page.click_cancel()  # click on the cancel button for accept/decline cookies section
        home_page.hover_video()  # hover over the video
        home_page.click_video()  # click on the video to play it
        home_page.hover_and_pause_video()  # hover over the video to display attributes and click on pause button
        assert self.driver.find_element(By.XPATH, home_page.pause_button_1).is_displayed()
        time.sleep(2)

