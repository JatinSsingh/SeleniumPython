from selenium.webdriver.common.by import By


class Checkout:

    def __init__(self, driver):
        self.driver = driver

    Product1 = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def shopItem1(self):
        return self.driver.find_element(*Checkout.Product1)

    Product2 = (By.XPATH, "//div[@class='card h-100']")

    def shopItem7(self):
        return self.driver.find_elements(*Checkout.Product2)
