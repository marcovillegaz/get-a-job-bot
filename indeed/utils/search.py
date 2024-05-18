"""In this script are function usefull to use the job browser and extract information"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def enter_job(driver, info):
    time.sleep(1)
    # Get job field
    job_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "text-input-what"))
    )

    # Write job in text box
    job_element.send_keys(info.job)


def enter_place(driver, info):
    time.sleep(1)
    # Get place field
    place_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "text-input-where"))
    )

    # Write place in text box
    place_element.send_keys(info.place)


def extract_results(driver):
    time.sleep(1)
    # Get job elements
    results_elements = driver.find_elements(
        By.CLASS_NAME, "jobTitle css-198pbd eu4oa1w0"
    )
    print(results_elements)


# Box with jobs: class = css-5lfssm eu4oa1w0
# Next page button XPATH: /html/body/main/div/div[2]/div/div[5]/div/div[1]/nav/ul/li[6]/a


# Right panel ID: jobsearch-ViewjobPaneWrapper
#
#
# //*[@id="job_80ee56190eca614a"]
