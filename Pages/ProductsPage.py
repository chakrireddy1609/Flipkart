from selenium.webdriver.common.by import By

from Pages.SelectedProductPage import SelectedProductPage


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver

    count_of_results = (By.XPATH, "//img[@class='_396cs4 _3exPp9']")
    click_product_button = (By.XPATH, "//img[@alt='IAIR Wired Earphone with in-Built Mic (H7_White) Wired Headset']")

    def assert_count(self):
        count = self.driver.find_elements(*ProductsPage.count_of_results)
        assert count != 0

    def click_product(self):
        self.driver.find_element(*ProductsPage.click_product_button).click()
        selectedproductspage = SelectedProductPage(self.driver)
        return selectedproductspage