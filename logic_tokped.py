from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from info_tokped import DataTokopedia

URL = "https://www.tokopedia.com/"
time.sleep(5)
SHOPPING = "discount"

class Tokopedia:
    """Intialization for Tokopedia"""
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login_tokopedia(self):
        """Login with username and password has already existed. Please input verified code manually"""
        self.driver.get(url=URL)
        time.sleep(2)
        login = self.driver.find_element_by_class_name("css-2hev56")
        login.click()
        time.sleep(2)
        username = self.driver.find_element_by_id("email-phone")
        username.send_keys(data.username)
        username.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element_by_id("password-input")
        password.send_keys(data.pass_word)
        try:
            login_tokped = self.driver.find_element_by_xpath('//*[@id="zeus-header"]/div[3]/div[2]/form/button/span/span')
            login_tokped.click()
            time.sleep(2)
        except NoSuchElementException:
            print("Please provide the correct Username or Password")
            time.sleep(1)
            self.driver.quit()
        else:
            # For SMS from tokopedia, must be input manually
            SMS = self.driver.find_element_by_xpath('//*[@id="zeus-header"]/div[3]/div/div/div[3]/div')
            SMS.click()

    def find_item(self):
        """Finding Item in all discount item or Finding item in search"""
        time.sleep(20)
        if data.shop == "discount":
            time.sleep(2)
            try:
                discount_item = self.driver.find_element_by_xpath('//*[@id="zeus-root"]/div/main/section[2]/div[1]/section/div[3]/a/div/img')
                discount_item.click()
                time.sleep(2)
                window_after = self.driver.window_handles[1]
                self.driver.switch_to(window_after)
            except NoSuchElementException:
                print("Something Wrong")
                self.driver.quit()
            else:
                time.sleep(3)
                all_product = self.driver.find_element_by_xpath('//*[@id="divComp#76043"]/div/div/div[7]/div/div/div/div/div[1]/div')
                all_product.click()
        else:
            name_of_item = input("What item do you need ? ")
            manually_search = self.driver.find_element_by_xpath('//*[@id="search-container"]/form/div/div/div/input')
            time.sleep(2)
            manually_search.send_keys(name_of_item)
            manually_search.send_keys(Keys.ENTER)

data = DataTokopedia()
data.user_pass()