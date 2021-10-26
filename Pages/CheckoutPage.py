from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver

    button_place_order = (By.XPATH, "//button[@class='_2KpZ6l _2ObVJD _3AWRsL']")

    def click_place_order(self):
        return self.driver.find_element(*CheckOutPage.button_place_order)