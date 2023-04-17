import time

from selenium.webdriver.common.by import By
import random
from appium import webdriver

from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    InvalidElementStateException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def click_lets_go(driver):
    lg = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="Let\'s go"]')))
    lg.click()


def click_next(driver):
    lg = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="Next"]')))
    lg.click()


def type_email(driver, email):
    lg = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.XPATH, f'//android.widget.EditText[@resource-id="input_email"]')))
    lg.send_keys(email)


def type_password(driver):
    # keys = [39, 29, 49, 48, 56, 44, 43, 43, 48, 56, 54, 37, 42]
    # time.sleep(1)
    # for each in keys:
    #     driver.press_keycode(each)
    driver.set_clipboard_text('kaut.poot.zin')
    time.sleep(1)
    driver.press_keycode(279)
    time.sleep(1)
    driver.press_keycode(66)


def check_word(driver):
    try:
        WebDriverWait(driver, 12).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 f"//android.widget.TextView[@text='Welcome, Tsdt!']")))
        return True
    except (TimeoutException, NoSuchElementException):
        return False


def check_password_screen(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView")))
        return True
    except (TimeoutException, NoSuchElementException):
        return False
