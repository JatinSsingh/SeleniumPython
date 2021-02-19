from selenium import webdriver
import time


class window:

    def method(self):
        driver = webdriver.Chrome(executable_path='/Users/Jatin Singh/Downloads/chromedriver')
        driver.get('https://rahulshettyacademy.com/angularpractice/')
        driver.maximize_window()

        shopButton = driver.find_element_by_xpath('//a[@href="/angularpractice/shop"]')
        shopButton.click()
        time.sleep(2)

        products = driver.find_elements_by_xpath("//div[@class='card h-100']")
        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            if productName == "iphone X":
                product.find_element_by_xpath("div/button").click()

        checkButton = driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']")
        checkButton.click()
        time.sleep(2)

        checkoutButton = driver.find_element_by_xpath("//button[@class='btn btn-success']")
        checkoutButton.click()
        time.sleep(2)

        suggestions = driver.find_element_by_xpath("//input[@id='country']")
        suggestions.send_keys("Ind")
        time.sleep(7)

        autosuggests = driver.find_elements_by_xpath("//div[@class='suggestions']//a")
        for autosuggest in autosuggests:
            if autosuggest.text == "India":
                autosuggest.click()
                time.sleep(2)
                break

        checkbox = driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']")
        checkbox.click()
        time.sleep(2)

        purchase = driver.find_element_by_xpath("//input[@class='btn btn-success btn-lg']")
        purchase.click()
        time.sleep(2)

        successtext = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']")
        print(successtext.text)

        driver.get_screenshot_as_file("Screenshot.png")


o = window()
o.method()
