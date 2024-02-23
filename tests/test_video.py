import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.HomePage import HomePage

"""This test case checks the play-pause functionality and availability of that attribute"""


@pytest.mark.usefixtures("setup_and_teardown")
class TestVideo:
    def test_video(self):
        home_page = HomePage(self.driver)
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, home_page.cancel_cookies_button)))
        if element:
            home_page.click_cancel()  # click on the cancel button for accept/decline cookies section
            home_page.hover_video()  # hover over the video
            home_page.click_video()  # click on the video to play it
            home_page.hover_and_pause_video()  # hover over the video to display attributes and click on pause button
            assert self.driver.find_element(By.XPATH, home_page.pause_button_1).is_displayed()
            time.sleep(2)



