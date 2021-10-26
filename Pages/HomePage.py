from selenium.webdriver.common.by import By
from Pages.ProductsPage import ProductsPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    close_button = (By.XPATH, "//button[@class='_2KpZ6l _2doB4z']")
    electronics_button = (By.XPATH, "//img[@alt='Electronics']")
    wired_headphones_button = (By.XPATH, "//a[normalize-space()='Wired Headphones']")


    def click_close_button(self):
        return self.driver.find_element(*HomePage.close_button)

    def click_electronics_menu(self):
        return self.driver.find_element(*HomePage.electronics_button)

    def click_wiredheadphones_button(self):
        return self.driver.find_element(*HomePage.wired_headphones_button)

    def cartpage_object(self):
        productspage = ProductsPage(self.driver)
        return productspage



