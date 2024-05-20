from indeed.info import *
from indeed.indeed import Indeed

with Indeed(teardown=False) as bot:
    # Go to login page
    bot.land_webpage()
    # Email
    bot.enter_email()

    try:
        # Password
        bot.enter_password()
        # 2 step verification
        bot.verification()
    except:
        # Access code
        bot.access_code()

    # Go to home page
    bot.homepage()
    # Serch job in browser
    bot.search_job()  # add job, place as inputs external of indeed\info.py
    # Extractjob information
    bot.click_job(folder=r"data")

    # extend to more pages
    # extract company info.
