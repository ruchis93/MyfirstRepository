import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_forms.asp")
driver.maximize_window()
driver.find_element(By.ID,"css").send_keys(Keys.ENTER)
driver.find_element(By.ID,"vehicle3").send_keys(Keys.ENTER)
time.sleep(10)
driver.close()
