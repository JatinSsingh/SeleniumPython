from selenium import webdriver
import time


class attribute:

    def test(self):

        driver = webdriver.Chrome(executable_path='/Users/Jatin Singh/Downloads/chromedriver')
        driver.get("https://rahulshettyacademy.com/seleniumPractise/")
        driver.maximize_window()
        driver.implicitly_wait(10)

        List = []
        List1 = []

        text = driver.find_element_by_css_selector('input.search-keyword')
        text.send_keys('Cu')
        time.sleep(1)

        add_cart = driver.find_elements_by_xpath("//div[@class='product-action']/button")
        for button in add_cart:
            List.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
            button.click()
        print(List)

        cart_icon = driver.find_element_by_xpath("//img[@alt='Cart']")
        cart_icon.click()

        proceed = driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']")
        proceed.click()
        time.sleep(2)

        veg_list = driver.find_elements_by_css_selector("p.product-name")
        for veg in veg_list:
            List1.append(veg.text)
        print(List1)
        time.sleep(2)

        price = driver.find_elements_by_xpath("//tr/td[5]/p")
        sum1 = 0
        for amount in price:
            sum1 = sum1 + int(amount.text)
        print(sum1)

        Amt = driver.find_elements_by_xpath("//td[5]/p")
        add = 0
        for totalAmt in Amt:
            add = add + int(totalAmt.text)
        print(add)

        OriginalAmt = driver.find_element_by_css_selector(".discountAmt").text
        print(OriginalAmt)
        assert int(add) == int(OriginalAmt)

        code = driver.find_element_by_xpath("//input[@class='promoCode']")
        code.send_keys('rahulshettyacademy')
        apply = driver.find_element_by_xpath("//button[@class='promoBtn']")
        apply.click()

        applied_text = driver.find_element_by_css_selector("span.promoInfo")
        print(applied_text.text)
        time.sleep(2)

        DiscountedAmt = driver.find_element_by_css_selector(".discountAmt").text
        print(DiscountedAmt)
        assert float(DiscountedAmt) < int(OriginalAmt)

        placeOrder = driver.find_element_by_xpath("//button[text()='Place Order']")
        placeOrder.click()
        time.sleep(2)

        # dropDown = driver.find_element_by_xpath("//div[@xpath='1']//option")
        # sel = Select(dropDown)
        #
        # sel.select_by_value('India')
        # time.sleep(2)


o = attribute()
o.test()
