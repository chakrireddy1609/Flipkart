from selenium.webdriver.common.by import By
from Pages.CheckoutPage import CheckOutPage


class SelectedProductPage:

    def __init__(self, driver):
        self.driver = driver

    text_pincode = (By.CSS_SELECTOR, "#pincodeInputId")
    button_click_check = (By.XPATH, "//span[@class='_2P_LDn']")
    text_delivery_time = (By.XPATH, "//span[@class='_1TPvTK']")
    button_add_to_cart = (By.XPATH, "//button[@class='_2KpZ6l _2U9uOA _3v1-ww']")

    def input_pincode(self):
        return self.driver.find_element(*SelectedProductPage.text_pincode)

    def click_check_pincode(self):
        return self.driver.find_element(*SelectedProductPage.button_click_check)

    def check_delivery_time(self):
        delivery_time = self.driver.find_element(*SelectedProductPage.text_delivery_time)
        print("Delivery time is "+ delivery_time.text)

    def add_to_cart(self):
        self.driver.find_element(*SelectedProductPage.button_add_to_cart).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage
