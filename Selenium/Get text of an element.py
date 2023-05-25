from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(0.5)
driver.get("https://www.google.com/")
#identify element
l= driver.find_element(By.NAME,"q")
l.send_keys("Selenium new")

#get_attribute() to get value of input box
print(l.get_attribute('value'))
driver.close()