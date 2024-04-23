from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import info


class IndeedBot:
    def __init__(self):
        # create a new Firefox session
        service = Service(executable_path=r"Browser\geckodriver.exe")
        self.driver = webdriver.Firefox(service=service)

        # open indeed
        self.driver.get("https://secure.indeed.com/account/login")

        # Create headless chrome
        # options = Options()
        # options.headless = True

        # EMAIL PAGE
        try:
            ## Get email field
            email_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.ID, "ifl-InputFormField-ihl-useId-passport-webapp-1")
                )
            )

            ## Write email in text box
            email_element.send_keys(info.email + Keys.ENTER)

            ## Check if the page has navigated to the next page or encountered a CAPTCHA
            try:
                # Check if you haven't successfully navigated to the next page
                time.sleep(3)

                same_page_element = WebDriverWait(self.driver, 4).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "/html/body/div/div[2]/main/div/div/div[2]/div/form/div/label",
                        )
                    )
                )
                print("Encountered CAPTCHA. Clicked the button again.")

                ## CLick Continue button
                button = self.driver.find_element(
                    By.XPATH,
                    "/html/body/div/div[2]/main/div/div/div[2]/div/form/button",
                ).click()

            except:
                print("Successfully navigated to password page.")
                # If next page element not found, it means a CAPTCHA may have appeared

        except:
            print("login page was not loaded")
            # self.driver.close()

        time.sleep(3)

        # PASSWORD PAGE "/html/body/div/div[2]/main/div/div/div[2]/div/form[1]/div[1]/div/label"
        # Captcha?
        # 6 digit verification "/html/body/div/div[2]/main/div/div/div[2]/div/div[2]/div/label"
        #   # Captcha?

        try:
            password_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "/html/body/div/div[2]/main/div/div/div[2]/div/form[1]/div[1]/div/label",
                    )
                )
            )
            print("You are in the password page")

        except:
            print("You are not in password page")


"""         try:
            ## Get password field
            password_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.ID, "ifl-InputFormField-ihl-useId-passport-webapp-1")
                )
            )
            ## Write password in text box
            password_element.send_keys(info.password)

            ## CLick Continue button
            button = self.driver.find_element(
                By.XPATH,
                "/html/body/div/div[2]/main/div/div/div[2]/div/form/button",
            ).click()

            ## Check if the page has navigated to the next page or encountered a CAPTCHA
            try:
                next_page_element = WebDriverWait(self.driver, 4).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "/html/body/div[2]/div/div/div[2]/main/div/div[1]/h1",
                        )
                    )
                )
                print("Successfully navigated to the user config page.")

            except:
                # If next page element not found, it means a CAPTCHA may have appeared
                print("Encountered CAPTCHA in password page.")

                ## Get password field
                password_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.ID, "ifl-InputFormField-ihl-useId-passport-webapp-1")
                    )
                )
                ## Write password in text box again
                password_element.send_keys(info.password + Keys.ENTER)

                ## CLick Continue button
                button = self.driver.find_element(
                    By.XPATH,
                    "/html/body/div/div[2]/main/div/div/div[2]/div/form/button",
                ).click()

                ## Check if the there is a two step varification
                try:
                    verification_element = WebDriverWait(self.driver, 4).until(
                        EC.presence_of_element_located(
                            (
                                By.XPATH,
                                '//*[@id="pageHeaderText"]',
                            )
                        )
                    )

                    verification_box = WebDriverWait(self.driver, 4).until(
                        EC.presence_of_element_located(
                            (
                                By.ID,
                                "verification_input",
                            )
                        )
                    )
                    print("There a two verification step\n")
                    verification_code = input(
                        "Check your email and enter the two step verification code: "
                    )
                    verification_box.send_keys(verification_code + Keys.ENTER)

                except:
                    time.sleep(3)

        except:
            print("A 6 digit code was sent to email...\n")

            verification_element = WebDriverWait(self.driver, 4).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="pageHeaderText"]',
                    )
                )
            )

            verification_box = WebDriverWait(self.driver, 4).until(
                EC.presence_of_element_located(
                    (
                        By.ID,
                        "verification_input",
                    )
                )
            )
            print("There a two verification step\n")
            verification_code = input(
                "Check your email and enter the verification code: "
            )
            verification_box.send_keys(verification_code + Keys.ENTER)

            input("Write the 6 digit code... ")

            # self.driver.close()

        # Go to main page
        home_button = (
            WebDriverWait(self.driver, 10)
            .until(EC.presence_of_element_located((By.XPATH, '//*[@id="FindJobs"]')))
            .click()
        )

        # VERIFICATION: /html/body/div/div[2]/main/div/div/div[2]/div/form/div[1]/div/label """


IndeedBot()
