from selenium import webdriver
import time


class suggest():

    def test(self):
        driver = webdriver.Chrome(executable_path='/Users/Jatin Singh/Downloads/chromedriver')
        driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
        driver.maximize_window()

        sugest = driver.find_element_by_id('autosuggest')
        sugest.send_keys('ind')
        time.sleep(2)

        country = driver.find_elements_by_xpath("//ul[@id='ui-id-1']//a")
        for countries in country:
            if countries.text == "India":
                countries.click()
                time.sleep(2)
                break

o = suggest()
o.test()
