from selenium import webdriver
import time


class attribute:

    def test(self):
        driver = webdriver.Chrome(executable_path='/Users/Jatin Singh/Downloads/chromedriver')
        driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
        driver.maximize_window()

        Text = driver.find_element_by_css_selector('#name')
        Text.send_keys('Jatin Ssingh')
        time.sleep(2)

        btn = driver.find_element_by_id('alertbtn')
        btn.click()
        alert = driver.switch_to.alert
        time.sleep(2)

        print(alert.text)
        alert.accept()
        time.sleep(2)

        # Cancel Test_Script
        Text = driver.find_element_by_css_selector('#name')
        Text.send_keys('Jatin Ssingh')
        time.sleep(2)

        cbtn = driver.find_element_by_id('confirmbtn')
        cbtn.click()
        Alert = driver.switch_to.alert
        time.sleep(2)

        print(Alert.text)
        Alert.dismiss()
        time.sleep(2)
        driver.quit()


o = attribute()
o.test()
