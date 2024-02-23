from selenium.webdriver.common.by import By


class WatchDemo:
    def __init__(self, driver):
        self.driver = driver

    fname_field = "//input[@id='FirstName']"
    body_field = "//body"
    fname_error_msg_field = "//*[@id='ValidMsgFirstName']"
    expected_error_msg = "This field is required."

    def click_on_fname(self):
        self.driver.find_element(By.XPATH, self.fname_field).click()

    def click_on_body(self):
        self.driver.find_element(By.XPATH, self.body_field).click()
