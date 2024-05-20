import os
import time

# Selenium tools
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Modules
import indeed.info as info


class Indeed(webdriver.Firefox):
    def __init__(self, driver_path=info.BASE_URL, teardown=False):
        # Create a new Firefox session
        self.driver_path = driver_path
        self.teardown = teardown

        self.EMAIL = info.EMAIL
        self.PASSWORD = info.PASSWORD
        self.JOB = info.JOB
        self.PLACE = info.PLACE

        self.sleep = 5

        os.environ["PATH"] += self.driver_path

        # With the super() function, you dont have to write driver any time.
        # webdriver is the parent class and Indeed the child.
        super(Indeed, self).__init__()

        self.implicitly_wait(5)
        # self.maximize_window()

        # Create headless chrome
        # options = Options()
        # options.headless = True

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            time.sleep(5)
            self.quit()

    def land_webpage(self):
        self.get("https://secure.indeed.com/account/login")

    def enter_email(self):
        """This method enter the email in the input box"""

        # Check email page
        try:
            # Find email box element
            email_element = self.find_element(
                By.ID,
                "ifl-InputFormField-ihl-useId-passport-webapp-1",
            )
            print("Enter email".center(50, "-"))
            # write the email in box
            email_element.send_keys(self.EMAIL)

            # Click Continue button
            button = self.find_element(
                By.CSS_SELECTOR,
                'button[data-tn-element="auth-page-email-submit-button"]',
            ).click()

            time.sleep(self.sleep)

            # Sometime a captcha appear and you have to click de button again.
            print("Cheking for captcha:")
            try:
                # Check captcha with an element of the same page, if it exists, there is a captcha.
                flag_element = self.find_element(
                    By.CSS_SELECTOR,
                    'h1[data-tn-section="auth-page-header--enter-email"]',
                )
                print("flag text:", flag_element.text)
                print("¡A Captcha has appear!")

                time.sleep(self.sleep)

                # CLick Continue button
                print("Click button again")
                button = self.find_element(
                    By.CSS_SELECTOR,
                    'button[type="submit"]',
                ).click()

            except:
                print("No captcha has appeared")

        except:
            print("There is an error with email page")

    def enter_password(self):
        """This function is to enter tour password in Indeed"""

        # Check password page
        try:
            flag_element = self.find_element(
                By.CSS_SELECTOR,
                'h1[data-tn-section="auth-page-header--login"]',
            )
            print("\nflag text:", flag_element.text)
            print("Enter password".center(50, "-"))

            # Write password in text box
            password_element = self.find_element(
                By.ID,
                "ifl-InputFormField-ihl-useId-passport-webapp-1",
            )
            password_element.send_keys(self.PASSWORD)

            time.sleep(2)

            # CLick Continue button
            button = self.find_element(
                By.CSS_SELECTOR,
                'button[data-tn-element="auth-page-sign-in-password-form-submit-button"]',
            ).click()

            time.sleep(self.sleep)

            # Sometime a captcha appear and you have to write the password again.
            print("Checking for captcha...")
            try:
                # Check captcha with an element of the same page, if it exists, there is a captcha.
                flag_element = self.find_element(
                    By.CSS_SELECTOR,
                    'h1[data-tn-section="auth-page-header--login"]',
                )
                print("\tflag text:", flag_element.text)
                print("\t¡A Captcha has appear! Writing password again.")

                time.sleep(self.sleep)

                # Write password in text box
                password_element = self.find_element(
                    By.ID,
                    "ifl-InputFormField-ihl-useId-passport-webapp-1",
                )
                password_element.send_keys(self.PASSWORD)

                # CLick Continue button
                button = self.find_element(
                    By.CSS_SELECTOR,
                    'button[data-tn-element="auth-page-sign-in-password-form-submit-button"]',
                ).click()

            except:
                print("No captcha has appeared")

        except:
            # print("\tYou are not in password page")
            pass

    def verification(self):
        """This function is used when Indeed want you to login with a 2 step verification"""
        # Check 2 step verification page
        try:
            flag_element = self.find_element(
                By.ID,
                "pageHeaderText",
            )
            print("\nflag text:", flag_element.text)
            print("2 step verification".center(50, "-"))
            print(f"A 6 digit code was send to {self.EMAIL}")

            # Enter the code
            code = input("Introduce the code: ")

            # Write the code in text box
            input_element = self.find_element(
                By.ID,
                "verification_input",
            )
            input_element.send_keys(code)

            # Click Continue button
            button = self.find_element(
                By.ID,
                "submit-code",
            ).click()

            time.sleep(self.sleep)

            # Sometime a captcha appear and you have to write the password again.
            print("Checking for captcha...")
            try:
                # Check captcha with an element of the same page, if it exists, there is a captcha.
                flag_element = self.find_element(
                    By.ID,
                    "pageHeaderText",
                )
                print("flag text:", flag_element.text)
                print("¡A Captcha has appear! Writing password again.")

                # Write the code in text box
                input_element = self.find_element(
                    By.ID,
                    "verification_input",
                )
                input_element.send_keys(code)

                time.sleep(self.sleep)

                # CLick Continue button
                button = self.find_element(
                    By.ID,
                    "submit-code",
                ).click()

            except:
                print("No captcha has appeared")
        except:
            pass

    def access_code(self):
        """This function is used when indeed want you to login with a 6 digit acess code"""

        # Check acces code page
        try:
            flag_element = self.find_element(
                By.CSS_SELECTOR,
                'h1[data-testid="auth-page-otp-header"]',
            )
            print("Access code".center(50, "-"))
            print("flag_text:", flag_element.text)
            print(f"A 6 digit code was send to {self.EMAIL}")

            # Introduce the code
            code = input("Introduce the 6 digit code: ")

            # Write the code in text box
            input_element = self.find_element(
                By.ID,
                "passcode-input",
            )
            input_element.send_keys(code + Keys.ENTER)

            # CLick Continue button
            button = self.find_element(
                By.CSS_SELECTOR,
                'button[data-tn-element="otp-verify-login-submit-button"]',
            ).click()

        except:
            # print("No 6 digit verification")
            pass

    def homepage(self):
        """Go to home page"""
        # Check configuration web page
        try:
            flag_element = self.find_element(
                By.CSS_SELECTOR,
                'h1[data-testid="settings-Title"]',
            )
            print("flag text: ", flag_element.text)
            print("Homepage".center(50, "-"))

            home_button = self.find_element(
                By.ID,
                "FindJobs",
            ).click()

            print("You are in home page")

        except:
            pass

    def search_job(self):
        """Search your desirable job by place in Indeed browser"""
        # In the future add add action to select the first elemene tof the list.

        print("Searching your derireble job...")
        time.sleep(1)

        # Get job field
        job_element = self.find_element(By.ID, "text-input-what")
        # Write job in text box
        job_element.send_keys(self.JOB)

        time.sleep(1)

        # Get place field
        place_element = self.find_element(By.ID, "text-input-where")

        # Write place in text box
        place_element.send_keys(self.PLACE)

        home_button = self.find_element(
            By.CSS_SELECTOR,
            'button[type="submit"]',
        ).click()

    def click_job(self, folder=None):
        # Find job elements
        job_elements = self.find_elements(
            By.CSS_SELECTOR,
            'a[data-hide-spinner="true"]',
        )

        print("Job offers - page 1".center(50, "-"))
        for i, job in enumerate(job_elements):
            # Click in job
            job.click()
            # Wait description to load
            time.sleep(2)

            # Place
            place_element = self.find_element(
                By.CSS_SELECTOR,
                'div[data-testid="inlineHeader-companyLocation"]',
            )
            # Company
            company_element = self.find_element(
                By.CSS_SELECTOR, 'a[class="css-1ioi40n e19afand0"]'
            )
            # Job description
            job_description_element = self.find_element(By.ID, "jobDescriptionText")

            # extractat information
            title = job.text
            job_id = job.get_attribute("id")
            place = place_element.text
            company_name = company_element.text
            company_url = company_element.get_attribute("href")
            description = job_description_element.text

            # Save in text file or show in console
            if folder != None:
                # Define path
                file_path = os.path.join(folder, job_id + ".txt")

                # Write the scrapped information in text file
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write("Job title:\n" + title + "\n")
                    file.write("Job place:\n" + place + "\n")
                    file.write("Company_name:\n" + company_name + "\n")
                    file.write("Company_url:\n" + company_url + "\n")
                    file.write("Description:\n" + description + "\n")

            else:
                print(job_id.center(50, "-"))
                print("Job title: " + title)
                print("Job place: " + place)
                print("Company_name: " + company_name)
                print("Company_url: " + company_url)
