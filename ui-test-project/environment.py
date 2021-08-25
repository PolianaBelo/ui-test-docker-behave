from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    context.url = context.config.userdata["url"]
    context.credentials = {
        "invalid-user-credentials":
            {
                "email": context.config.userdata["email"],
                "password": context.config.userdata["password"]
            }
    }
    context.login_error_message = context.config.userdata["login_error_message"]

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-translate')
    chrome_options.add_argument('headless')
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)


def after_all(context):
    context.driver.quit()
