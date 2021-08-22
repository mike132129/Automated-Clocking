from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep

class webCrawler:
    def __init__(self, username, password):
        self.driver = self.startup()
        self.username = username
        self.password = password

    def startup(self):
        chromeOptions = Options()
        chromeOptions.add_argument("--window-size=1920,1080")
        prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False}
        chromeOptions.add_experimental_option("prefs", prefs)
        chromeOptions.add_experimental_option("excludeSwitches", ["enable-automation"])
        chromeOptions.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(chrome_options=chromeOptions)
        driver.get('https://cloud.nueip.com/')
        return driver

    def login(self):
        dept_input = self.driver.find_element_by_id('dept_input')
        dept_input.send_keys('lawsnote')

        username_input = self.driver.find_element_by_id('username_input')
        username_input.send_keys(self.username)

        password_input = self.driver.find_element_by_id('password-input')
        password_input.send_keys(self.password)

        sleep(1)

        login_button = self.driver.find_element_by_id('login-button')
        login_button.click()

        sleep(5)

    def clockin(self):
        clockin_button = self.driver.find_element_by_xpath('//div[@class="clock_btn margin-right-5 padding-all-20 Link ctrl-clockin" and @id="clockin"]')
        clockin_button.click()
        print('clockin finish')

    def clockout(self):
        clockout_button = self.driver.find_element_by_xpath('//div[@class="clock_btn margin-right-5 padding-all-20 Link ctrl-clockin" and @id="clockout"]')
        clockout_button.click()
        print('clockout finish')

if __name__ == '__main__':
    crawler = webCrawler("LN0041", "mike980340")
    crawler.login()
    crawler.clockout()


