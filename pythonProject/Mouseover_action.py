from selenium import webdriver
import time
from selenium.webdriver import ActionChains


class window:

    def method(self):

        driver = webdriver.Chrome(executable_path='/Users/Jatin Singh/Downloads/chromedriver')
        driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
        driver.maximize_window()
        time.sleep(1)

        action = ActionChains(driver)
        mouseHover = driver.find_element_by_id("mousehover")
        mouseHover.click()
        action.move_to_element(mouseHover).perform()
        time.sleep(2)

        hoverList = driver.find_element_by_link_text("Reload")
        action.move_to_element(hoverList).click().perform()

        driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
        driver.maximize_window()
        time.sleep(2)

        action1 = ActionChains(driver)
        rightClick = driver.find_element_by_xpath("//input[@name='confirmation']")
        action1.context_click(rightClick).perform()
        time.sleep(2)
        doubleClick = driver.find_element_by_xpath("//input[@id='double-click']")
        action1.double_click(doubleClick).perform()
        time.sleep(2)

        switchAlert = driver.switch_to.alert
        assert "You double clicked me!!!, You got to be kidding me" == switchAlert.text
        switchAlert.accept()


o = window()
o.method()
