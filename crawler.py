from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from  argparse import ArgumentParser
from time import sleep

class webCrawler:
    def __init__(self, username=None, password=None):
        self.driver = self.startup()
        self.username = username
        self.password = password

    def startup(self):
        chromeOptions = Options()
        chromeOptions.headless=True
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
        clockin_div = self.driver.find_elements_by_id('clockin')[0]
        attendance = self.checkUserAttendance()
        self.mouseMoveAndClick(clockin_div, attendance)

    def clockout(self):
        clockout_div = self.driver.find_elements_by_id('clockout')[0]
        attendance = self.checkUserAttendance()
        self.mouseMoveAndClick(clockout_div, attendance)
        
    def mouseMoveAndClick(self, element, attendance):
        clockType = element.text.split()[0]
        if attendance == True:
            sleep(1)
            action = webdriver.ActionChains(self.driver)
            action.move_to_element(element).click(element).perform()
            print(f'已打卡{clockType}')
        else:
            print(f'無需打卡{clockType}')        

    def checkUserAttendance(self):
        reminders = self.driver.find_elements_by_id('collapseOne')[0].text     
        selfName = self.driver.find_elements_by_id('user-dropdown')[0].text.split()[0]
        if selfName not in reminders:
            return True
        else:
            return False

def argument_parse():
    parser = ArgumentParser()
    parser.add_argument('--username')
    parser.add_argument('--password')
    parser.add_argument('--action', default='clockin')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    options = argument_parse()
    crawler = webCrawler(options.username, options.password)
    crawler.login()

    if options.action == 'clockin':
        crawler.clockin()

    elif options.action == 'clockout':
        crawler.clockout()


