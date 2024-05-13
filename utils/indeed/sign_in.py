""" from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options """

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def enter_email(driver, info):
    """This function is used to enter your email in Indeed"""
    # Get email field
    email_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "ifl-InputFormField-ihl-useId-passport-webapp-1")
        )
    )

    # Write email in text box
    email_element.send_keys(info.email)
    print("Introducing your email.")

    # CLick Continue button
    time.sleep(2)
    button = driver.find_element(
        By.XPATH,
        "/html/body/div/div[2]/main/div/div/div[2]/div/form/button",
    ).click()

    # Sometime a captcha appear and you have to click de button again.
    try:
        time.sleep(2)
        flag_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div/div[2]/main/div/div/div[2]/div/form[1]/div[1]/div/label",
                )
            )
        )
        print("¡A Captcha has appear! Clicking button again.")

        time.sleep(2)

        # CLick Continue button
        button = driver.find_element(
            By.XPATH,
            "/html/body/div/div[2]/main/div/div/div[2]/div/form[1]/button",
        ).click()

    except:
        print(" ")


""" def email_captcha(driver):
    # Check if the page has navigated to the next page or encountered a CAPTCHA
    try:
        # Find a element in the same page, if there is, there is a Captcha!
        time.sleep(2)
        email_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div/div[2]/main/div/div/div[2]/div/form/div/label",
                )
            )
        )

        print("¡There is a CAPTCHA!")

        # CLick Continue button
        print("Click button again.")
        button = driver.find_element(
            By.XPATH,
            "/html/body/div/div[2]/main/div/div/div[2]/div/form/button",
        ).click()

    except:
        print("There is not CAPTCHA in email page.") """


def enter_password(driver, info):
    """This function is to enter tour password in Indeed"""
    # Check password page
    flag_element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "/html/body/div/div[2]/main/div/div/div[2]/div/form[1]/div[1]/div/label",
            )
        )
    )

    print("Introducing your password.")

    # Write password in text box
    password_element = driver.find_element(
        By.ID, "ifl-InputFormField-ihl-useId-passport-webapp-1"
    )
    password_element.send_keys(info.password)

    time.sleep(2)

    # CLick Continue button
    button = driver.find_element(
        By.XPATH,
        "/html/body/div/div[2]/main/div/div/div[2]/div/form[1]/button",
    ).click()

    # Sometime a captcha appear and you have to write the password again.
    try:
        time.sleep(2)
        flag_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div/div[2]/main/div/div/div[2]/div/form[1]/div[1]/div/label",
                )
            )
        )
        print("¡A Captcha has appear! Writing password again.")

        # Write password in text box
        password_element = driver.find_element(
            By.ID, "ifl-InputFormField-ihl-useId-passport-webapp-1"
        )
        password_element.send_keys(info.password)

        time.sleep(2)

        # CLick Continue button
        button = driver.find_element(
            By.XPATH,
            "/html/body/div/div[2]/main/div/div/div[2]/div/form[1]/button",
        ).click()

    except:
        print("¡Login successfully!")


def access_code(driver, info):
    """This function is used when indeed want you to login with a 6 digit acess code"""

    # Cheack acces code page
    flag_element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "/html/body/div/div[2]/main/div/div/div[2]/div/div[4]",
            )
        )
    )
    print("LOGIN WITH AN ACCESS CODE")
    print(f"A 6 digit code was send to {info.email}")

    # Introduce the code
    code = input("Introduce the 6 digit code: ")

    # Write the code in text box
    input_element = driver.find_element(By.ID, "passcode-input")
    input_element.send_keys(code + Keys.ENTER)


def verification(driver, info):
    """This function is used when Indeed want you to login with a 2 step verification"""

    # Check 2 step verification page
    try:
        flag_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div/div[2]/main/div/div/div[2]/div/form/div[1]/div/label",
                )
            )
        )
        print("2 STEP VERIFICATION")
        print(f"The verification code was send to {info.email}")

        # Enter the code
        code = input("Introduce the code: ")

        # Write the code in text box
        input_element = driver.find_element(By.ID, "verification_input")
        input_element.send_keys(code)

        # CLick Continue button
        button = driver.find_element(
            By.ID,
            "submit-code",
        ).click()

        # Sometime a captcha appear and you have to write the password again.
        try:
            time.sleep(2)
            # Check captacha with a flag element
            flag_element = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "/html/body/div/div[2]/main/div/div/div[2]/div/form/div[1]/div/label",
                    )
                )
            )
            print("¡A Captcha has appear! Writing code again.")

            # Write password in text box
            input_element = driver.find_element(By.ID, "verification_input")
            input_element.send_keys(code)

            time.sleep(1)

            # CLick Continue button
            button = driver.find_element(
                By.ID,
                "submit-code",
            ).click()

        except:
            print("¡Login successfully!")

    except:
        print("No verification needed.\n")
