from Functions import *

desired_cap_Audi = {
    "deviceName": "emulator-5554",
    "platformName": "Android",
    "appPackage": "de.myaudi.mobile.assistant",
    "noReset": 'true',
    "appActivity": "de.audi.onetouch.MainActivity",
    "automationName": "UiAutomator2",
    "fullReset": 'false',
    "newCommandTimeout": "50000",
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap_Audi)

email = "light.bell0356@fastmail.com"
passowrd = "kaut.poot.zin"


click_lets_go(driver)
type_email(driver, email)
click_next(driver)
if check_password_screen(driver):
    type_password(driver)
    if print(check_word(driver)):
        pass
else:
    print("NO SCREEN FOR PASSWORD")