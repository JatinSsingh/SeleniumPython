from selenium.webdriver.common.by import By
from PageObject.CheckOutPage import Checkout


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[@href='/angularpractice/shop']")
    name = (By.XPATH, "//div[@class='form-group']/input[@name='name']")
    email = (By.XPATH, "//input[@name='email']")
    password = (By.CSS_SELECTOR, "#exampleInputPassword1")
    checkbox = (By.XPATH, "//input[@id='exampleCheck1']")
    gender = (By.XPATH, "//select[@id='exampleFormControlSelect1']")
    radio = (By.ID, "inlineRadio2")
    status = (By.XPATH, "//input[@type='date']")
    submit = (By.XPATH, "//input[@type='submit']")
    text = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def shopItem(self):
        self.driver.find_element(*Homepage.shop).click()
        prod = Checkout(self.driver)
        return prod

    def getName(self):
        return self.driver.find_element(*Homepage.name)

    def getEmail(self):
        return self.driver.find_element(*Homepage.email)

    def getPassword(self):
        return self.driver.find_element(*Homepage.password)

    def getCheckbox(self):
        return self.driver.find_element(*Homepage.checkbox)

    def getGender(self):
        return self.driver.find_element(*Homepage.gender)

    def getRadio(self):
        return self.driver.find_element(*Homepage.radio)

    def getStatus(self):
        return self.driver.find_element(*Homepage.status)

    def getSubmit(self):
        return self.driver.find_element(*Homepage.submit)

    def getText(self):
        return self.driver.find_element(*Homepage.text)
