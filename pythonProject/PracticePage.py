from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class clickSendkey:

    def test(self):
        driver = webdriver.Chrome(executable_path='/Users/Jatin Singh/Downloads/chromedriver')
        driver.get('https://letskodeit.teachable.com/')
        driver.maximize_window()

        practice = driver.find_element_by_xpath("//a[@href='/pages/practice']")
        practice.click()
        time.sleep(4)

        radio = driver.find_element_by_xpath("//input[@id='benzradio']")
        radio.click()
        print('Benz is selected: ' + str(radio.is_selected()))
        time.sleep(2)

        checkbox = driver.find_element_by_xpath("//input[@id='benzcheck']")
        checkbox.click()
        time.sleep(2)

        checkbox1 = driver.find_element_by_id('bmwcheck')
        checkbox1.click()
        time.sleep(2)

        element = driver.find_element_by_id('carselect')
        sel = Select(element)

        sel.select_by_value('benz')
        time.sleep(2)

        sel.select_by_index('0')
        time.sleep(2)

        sel.select_by_visible_text('Honda')
        time.sleep(2)

        driver.find_element_by_id('hide-textbox').click()
        time.sleep(2)

        driver.find_element_by_id('show-textbox').click()
        time.sleep(2)
        webelement = driver.find_element_by_id('show-textbox')
        webstate = webelement.is_displayed()
        print('Textbox is displayed: ' + str(webstate))

        webt = driver.find_element_by_id('opentab')
        webtext = webt.text
        print('Text for webelement is: ' + webtext)

        attribut = driver.find_element_by_id('name')
        attribute = attribut.get_attribute('placeholder')
        print('Attribute of element is: ' + attribute)

        # loginlink = driver.find_element_by_xpath("//div[@id='navbar']//a[@href = '/sign_in']")
        # loginlink.click()
        # time.sleep(2)
        #
        # username = driver.find_element_by_id('user_email')
        # username.send_keys('JatinSsingh@gmail.com')
        # time.sleep(2)
        #
        # password = driver.find_element_by_id('user_password')
        # password.send_keys('Password')
        # time.sleep(2)
        #
        # submit = driver.find_element_by_xpath("//form[@id='new_user']//input[@type = 'submit']")
        # submit.click()
        # time.sleep(3)


o = clickSendkey()
o.test()
