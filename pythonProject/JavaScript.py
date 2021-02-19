from selenium import webdriver
import time


class window:

    def method(self):
        driver = webdriver.Chrome(executable_path='/Users/Jatin Singh/Downloads/chromedriver')
        driver.get('https://rahulshettyacademy.com/angularpractice/')
        driver.maximize_window()
        time.sleep(2)

        textName = driver.find_element_by_xpath("//div[@class='form-group']//input[@name='name']")
        textName.send_keys("Jatin Ssingh")
        time.sleep(2)
        # Get Text By Selenium
        getText = driver.find_element_by_xpath("//div[@class='form-group']//input[@name='name']").get_attribute("value")
        print(getText)
        # Get Text By JavaScript
        javaScript = driver.execute_script('return document.getElementsByName("name")[0].value')
        print(javaScript)

        shopButton = driver.find_element_by_xpath('//a[@href="/angularpractice/shop"]')
        driver.execute_script("arguments[0].click();", shopButton)
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)


o = window()
o.method()
