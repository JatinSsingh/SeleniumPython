from selenium import webdriver
import time


class attribute:

    def test(self):
        driver = webdriver.Chrome(executable_path='/Users/Jatin Singh/Downloads/chromedriver')
        driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
        driver.maximize_window()

        attribut = driver.find_elements_by_css_selector("div[id='checkbox-example'] input[type='checkbox']")

        for attributes in attribut:
         print(attributes.get_attribute('value'))
         attributes.click()
         time.sleep(2)

         radio = driver.find_elements_by_css_selector("div[id='radio-btn-example'] input[name='radioButton']")
         radio[2].click()


o = attribute()
o.test()
