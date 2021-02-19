from selenium.webdriver.common.by import By


class Checkbutton:

    def __init__(self, driver):
        self.driver = driver

    Button = (By.XPATH, "//button[@class='btn btn-success']")

    def shopItem2(self):
        return self.driver.find_element(*Checkbutton.Button)

    Suggestions = (By.XPATH, "//input[@id='country']")

    def shopItem3(self):
        return self.driver.find_element(*Checkbutton.Suggestions)

    Autosuggests = (By.XPATH, "//div[@class='suggestions']//a")

    def shopItem9(self):
        return self.driver.find_elements(*Checkbutton.Autosuggests)

    AutoSuggest = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    def shopItem4(self):
        return self.driver.find_element(*Checkbutton.AutoSuggest)

    Purchasee = (By.XPATH, "//input[@class='btn btn-success btn-lg']")

    def shopItem5(self):
        return self.driver.find_element(*Checkbutton.Purchasee)

    SuccessText = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def shopItem8(self):
        return self.driver.find_element(*Checkbutton.SuccessText)
