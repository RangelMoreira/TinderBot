import os

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv

load_dotenv()

login_facebook = os.getenv('FACEBOOK_LOGIN')
password_facebook = os.getenv('FACEBOOK_PASS')

# Keep Chrome browser open after program finisehs
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Option to keep Chrome open

driver = webdriver.Chrome(options=options)

url = "https://tinder.com/"
driver.get(url)

time.sleep(2)
try:
    login_button = driver.find_element(By.LINK_TEXT, value="Entrar")
    login_button.click()
    time.sleep(2)

    facebook_login_button = driver.find_element(By.XPATH,
                                                value="/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]")
    facebook_login_button.click()

    # Facebook Login
    base_window = driver.window_handles[0]
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)

    txt_login_facebook = driver.find_element(By.ID, value="email")
    txt_login_facebook.send_keys(login_facebook)

    txt_password_facebook = driver.find_element(By.ID, value="pass")
    txt_password_facebook.send_keys(password_facebook)

    access_button = driver.find_element(By.ID, value="loginbutton")
    access_button.click()

    input("Solve the captcha and press enter")

    # Switch to Tinder
    driver.switch_to.window(base_window)

    # Other Buttons
    accept_cookies = driver.find_element(By.XPATH,
                                         value='//*[@id="s408606152"]/div/div[2]/div/div/div[1]/div[2]/button')
    accept_cookies.click()

    allow_location = driver.find_element(By.XPATH, value='//*[@id="s408606152"]/div/div/div/div/div[3]/button[1]')
    allow_location.click()

    allow_notification_button = driver.find_element(By.XPATH,
                                                    value='//*[@id="s408606152"]/div/div/div/div/div[3]/button[1]')
    allow_notification_button.click()
except NoSuchElementException:
    raise NoSuchElementException
count = 0
while True:
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_RIGHT)
    count += 1
    time.sleep(5)
    if count >= 2:
        count = 0
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_LEFT)
    time.sleep(5)
