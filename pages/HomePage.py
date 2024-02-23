import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    hover_search_resources_field = '//*[@id="gatsby-focus-wrapper"]/div/div[1]/div/div/div[2]/div[3]/div[1]'
    click_search_resources_field = '//*[@id="gatsby-focus-wrapper"]/div/div[1]/div/div/div[2]/div[3]/div[2]/a[1]'
    resource_landing_text_field = "//div[@class='resources-intro']/h2"
    resources_landing_expected_text = "Resource Center"

    watch_demo_field = "//div[@class='header-desktop-buttons hide-on-mobile']/a[1]"
    cancel_cookies_button = "//button[@id='rcc-confirm-button']"

    hover_video_field_1 = '//*[@class="logo-carousel"]/div[2]/div[1]/div[1]/span[1]'
    click_video_1 = "//*[@class='logo-carousel']/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]"

    hover_video_after_play_1 = "(//div[@class='w-bottom-bar-middle w-css-reset'])[3]"
    click_video_after_play_1 = "(//div[@class='w-bottom-bar-left w-css-reset'])[3]"

    pause_button_1 = "(//div[@class='w-bottom-bar-left w-css-reset'])[3]"

    def hover_on_resources_section(self):
        a = ActionChains(self.driver)
        m = self.driver.find_element(By.XPATH, self.hover_search_resources_field)
        time.sleep(4)
        # hover over element
        a.move_to_element(m).perform()

    def click_on_resources_section(self):
        self.driver.find_element(By.XPATH, self.click_search_resources_field).click()

    def click_on_watch_demo_section(self):
        self.driver.find_element(By.XPATH, self.watch_demo_field).click()

    def click_cancel(self):
        self.driver.find_element(By.XPATH, self.cancel_cookies_button).click()

    def hover_video(self):
        a = ActionChains(self.driver)
        m = self.driver.find_element(By.XPATH, self.hover_video_field_1)
        time.sleep(5)
        # hover over element
        a.move_to_element(m).perform()
        time.sleep(5)

    def click_video(self):
        self.driver.find_element(By.XPATH,self.click_video_1).click()
        time.sleep(2)

    def hover_and_pause_video(self):
        a = ActionChains(self.driver)
        n = self.driver.find_element(By.XPATH, self.hover_video_after_play_1)
        a.move_to_element(n).perform()
        self.driver.find_element(By.XPATH, self.click_video_after_play_1).click()







