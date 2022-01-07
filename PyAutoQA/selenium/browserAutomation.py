import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# EXAMPLE
#browser = webdriver.Chrome('C:\\Users\\josia\\OneDrive\\Desktop\\vsCode\\Python\\Automation')
browser.get('https://twitter.com/home')
elem = browser.find_element_by_class_name('errorContainer')
elem
elem.tag_name
elem.get_attribute('onclick')
elem.text
elem.location
elem = broswer.find_element_by_css_selector(".downloadBox")
elem.tag_name
elem = browser/find_element_by_link_text('many browsers')
elem.get_attribute('href')
elem.click()
elem.back()
elem.forward()
elem.refresh()
elem.back()
elem.quit()

browser.get('https://www.facebook.com/')
email = browser.find_element_by_id('email')
email.send_keys('josiahjamison7@gmail.com')
password = browser.find_element_by_id('pass')
password.send_keys('123asd')
password.send_keys(Keys.ENTER)