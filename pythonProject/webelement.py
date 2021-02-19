from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class clickSendkey():

    def test(self):
        driver = webdriver.Firefox(executable_path='/Users/Jatin Singh/Downloads/geckodriver')
        driver.get('https://google.com/')
        driver.maximize_window()

        texttype = driver.find_element_by_xpath("//input[@type='text']")
        texttype.send_keys('letskodeitselenium')
        time.sleep(3)

        search = driver.find_element_by_xpath("//div[@class='FPdoLc tfB0Bf']//input[@class='gNO89b']")
        search.click()
        time.sleep(3)

        driver.close()

o = clickSendkey()
o.test()
