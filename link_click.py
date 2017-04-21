from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.packtpub.com/index')

elm = browser.find_element_by_class_name('login-popup')
elm.click()