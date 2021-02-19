import time
from Framework.BaseClass import Baseclass
from PageObject.CheckOutPage import Checkout
from PageObject.ConfirmPage import Checkbutton
from PageObject.HomePage import Homepage


class TestFramework(Baseclass):

    def test_case1(self):
        log = self.test_logg()
        homepage = Homepage(self.driver)
        prod = homepage.shopItem()
        log.info("List of All Mobiles")
        time.sleep(2)

        products = prod.shopItem7()
        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            log.info(productName)
            if productName == "iphone X":
                product.find_element_by_xpath("div/button").click()

        checkButton = Checkout(self.driver)
        checkButton.shopItem1().click()
        time.sleep(1)

        checkoutButton = Checkbutton(self.driver)
        checkoutButton.shopItem2().click()
        time.sleep(2)

        suggestions = Checkbutton(self.driver)
        log.info("Enter the Country Name as Ind")
        suggestions.shopItem3().send_keys("Ind")
        time.sleep(7)

        autosugg = Checkbutton(self.driver)
        autosuggests = autosugg.shopItem9()
        for autosuggest in autosuggests:
            if autosuggest.text == "India":
                autosuggest.click()
                time.sleep(2)
                break

        checkbox = Checkbutton(self.driver)
        checkbox.shopItem4().click()

        purchase = Checkbutton(self.driver)
        purchase.shopItem5().click()
        time.sleep(1)

        succestext = Checkbutton(self.driver)
        successtext = succestext.shopItem8()
        log.info(successtext.text)

        self.driver.get_screenshot_as_file("Screenshot.png")
