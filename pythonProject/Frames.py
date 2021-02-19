from selenium import webdriver
import time


class window:

    def method(self):

        driver = webdriver.Chrome(executable_path='/Users/Jatin Singh/Downloads/chromedriver')
        driver.get('https://the-internet.herokuapp.com/iframe')
        driver.maximize_window()
        time.sleep(1)

        switchFrame = driver.switch_to.frame("mce_0_ifr")
        clearText = driver.find_element_by_id("tinymce")
        clearText.clear()
        time.sleep(1)

        writeText = driver.find_element_by_id("tinymce")
        writeText.send_keys("My Name is Jatin Ssingh")
        time.sleep(2)

        switchParent = driver.switch_to.default_content()
        getHeading = driver.find_element_by_tag_name("h3").text
        print(getHeading)


o = window()
o.method()
