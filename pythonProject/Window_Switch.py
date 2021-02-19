from selenium import webdriver
import time


class window:

    def method(self):

        driver = webdriver.Chrome(executable_path='/Users/Jatin Singh/Downloads/chromedriver')
        driver.get("https://the-internet.herokuapp.com/windows")
        driver.maximize_window()
        time.sleep(2)

        link = driver.find_element_by_link_text("Click Here")
        link.click()
        time.sleep(2)

        childWindow = driver.window_handles[1]
        switch = driver.switch_to.window(childWindow)
        childText = driver.find_element_by_tag_name("h3").text
        print(childText)

        againSwitch = driver.switch_to.window(driver.window_handles[0])
        parentText = driver.find_element_by_tag_name("h3").text
        print(parentText)
        time.sleep(2)
        driver.quit()


o = window()
o.method()
