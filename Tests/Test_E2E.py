import time

from selenium.webdriver import ActionChains

from Pages.HomePage import HomePage
from Tests.BaseTest import BaseTest


class Test_E2E_addtocart(BaseTest):

    def test_flipkart_addtocart(self):
        log = self.implement_logging()
        homepage = HomePage(self.driver)
        time.sleep(2)
        homepage.click_close_button().click()
        action = ActionChains(self.driver)
        action.move_to_element(homepage.click_electronics_menu()).perform()
        time.sleep(2)
        action.move_to_element(homepage.click_wiredheadphones_button()).click().perform()
        log.info("Clicked on Dynamic Element : Wired Headphones")
        time.sleep(2)
        productspage = homepage.cartpage_object()
        productspage.assert_count()
        time.sleep(2)
        selectedproductspage = productspage.click_product()
        window = self.driver.window_handles
        self.driver.switch_to.window(window[1])
        print(self.driver.title)
        time.sleep(2)
        selectedproductspage.input_pincode().send_keys('500019')
        selectedproductspage.click_check_pincode().click()
        time.sleep(2)
        selectedproductspage.check_delivery_time()
        checkoutpage = selectedproductspage.add_to_cart()
        time.sleep(2)
        checkoutpage.click_place_order().click()