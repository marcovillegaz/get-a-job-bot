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
    # bot.search_job()
