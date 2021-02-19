from selenium import webdriver
import time

class Practice():

    def test(self):

        driver = webdriver.Chrome(executable_path='/Users/Jatin Singh/Downloads/chromedriver')
        driver.get('https://letskodeit.teachable.com/')
        time.sleep(2)
        driver.refresh()
        print('1st time refresh the page')
        time.sleep(2)
        driver.get(driver.current_url)
        print('2nd time refresh the page')
        driver.maximize_window()
        time.sleep(2)
        title = driver.title
        print('Title is :'+ title)
        currenturl = driver.current_url
        print('Current_URL is :' + currenturl)
        driver.get('https://outlook.office365.com/mail/inbox/')
        time.sleep(3)
        currenturl = driver.current_url
        print('Current_URL is :' + currenturl)
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(3)
        pagesource = driver.page_source
        print(pagesource)
        #driver.close()
        driver.quit()

c = Practice()
c.test()
