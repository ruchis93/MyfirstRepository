import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://w3schools.com")
print(driver.title)
driver.maximize_window()
time.sleep(2)
driver.quit()






'''import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

serve = Service("chromedriver.exe")
driver = webdriver.Chrome(service=serve)
driver.get("http://www.google.com")
time.sleep(2)
print(driver.title)
print(driver.current_url)

driver.quit()'''
