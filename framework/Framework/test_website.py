import pytest
from selenium.webdriver.support.select import Select
from Framework.BaseClass import Baseclass
from PageObject.HomePage import Homepage
from TestData.testData import TestData


class Testwebsite(Baseclass):

    def test_website(self, getData):
        log = self.test_logg()
        homepage = Homepage(self.driver)
        log.info("Name is "+getData["Name"])
        homepage.getName().send_keys(getData["Name"])
        log.info("Email is "+getData["Email"])
        homepage.getEmail().send_keys(getData["Email"])
        log.info("Password is "+getData["Password"])
        homepage.getPassword().send_keys(getData["Password"])

        homepage.getCheckbox().click()

        gender = Select(homepage.getGender())
        gender.select_by_visible_text("Male")

        homepage.getRadio().click()

        homepage.getStatus().send_keys("01/01/2000")

        homepage.getSubmit().click()

        tex = homepage.getText().text

        assert ("Success! The Form has been submitted successfully!." in tex)

        self.driver.refresh()

    @pytest.fixture(params=TestData.test_Data)
    def getData(self, request):
        return request.param
