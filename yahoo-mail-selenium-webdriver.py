from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
x=input("Enter username :\t")
x=x.strip()
y=input("Enter password :\t")
browser = webdriver.Firefox()
browser.get('http://mail.yahoo.com')
action = webdriver.ActionChains(browser)
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys(x)
nextButton = browser.find_element_by_id('login-signin')
nextButton.click()
time.sleep(1)
passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys(y)
signinButton = browser.find_element_by_id('login-signin')
signinButton.click()
