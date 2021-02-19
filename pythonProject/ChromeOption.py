from selenium import webdriver


class attribute:

    def test(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--start-maximized")
        chrome_option.add_argument("--headless")
        chrome_option.add_argument("--ignore-certificate-errors")

        driver = webdriver.Chrome(executable_path='/Users/Jatin Singh/Downloads/chromedriver', options=chrome_option)
        driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')

        print(driver.title)


o = attribute()
o.test()
