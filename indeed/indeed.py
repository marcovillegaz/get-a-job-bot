# Selenium tools
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Modules
from utils.indeed import sign_in
from utils.indeed import search


class Indeed(webdriver.Firefox):
    def __init__(self, driver_path="Browser\geckodriver.exe"):
        # create a new Firefox session
        # service = Service(executable_path=r"Browser\geckodriver.exe")
        self.driver_path = driver_path
        super(Indeed, self).__init__()

        # self.driver = webdriver.Firefox(service=service)

        # self.info = info
        # open indeed
        # self.driver.get("https://secure.indeed.com/account/login")
        # self.driver.implicitly_wait(5)

        # Create headless chrome
        # options = Options()
        # options.headless = True

    """ def login(self):
        print("Logging in Indeed".center(80, "-"))
        try:
            # Email
            sign_in.enter_email(self.driver, self.info)

            try:
                # Password
                sign_in.enter_password(self.driver, self.info)
                sign_in.verification(self.driver, self.info)
            except:
                # Access code
                sign_in.access_code(self.driver, self.info)

            # Go to main page
            home_button = (
                WebDriverWait(self.driver, 10)
                .until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="FindJobs"]'))
                )
                .click()
            )
            print("Now you are in home page")

        except:
            print("There was an error during login process")

    def find_job(self):
        print(f"Searching a job of '{self.info.job}' in '{self.info.place}'")
        search.enter_job(self.driver, self.info)
        search.enter_place(self.driver, self.info)

        time.sleep(2)
        button = self.driver.find_element(
            By.XPATH,
            "/html/body/div/div[1]/div/span/div[4]/div[1]/div/div/div/div/form/div/div[2]/button",
        ).click()

        search.extract_results(self.driver) """
