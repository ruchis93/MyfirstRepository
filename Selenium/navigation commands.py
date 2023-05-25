'''import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://w3schools.com")
print(driver.title)
driver.maximize_window()
time.sleep(2)

driver.get("https://www.google.com")
print(driver.title)
driver.maximize_window()
time.sleep(2)

driver.back()
print(driver.title)
driver.maximize_window()
time.sleep(2)



driver.forward()
print(driver.title)
driver.maximize_window()
time.sleep(2)

driver.quit()






from selenium.webdriver.chrome.service import Service
import time

serve = Service("chromedriver.exe")
driver = webdriver.Chrome(service=serve)
driver.get("http://www.google.com")
time.sleep(2)
print(driver.title)
print(driver.current_url)

# driver = webdriver.Chrome(service=serve)
driver.get("http://www.facebook.com")
time.sleep(5)
print(driver.title)


driver.back()
time.sleep(3)
print(driver.title)

driver.forward()
time.sleep(2)
print(driver.title)

driver.quit()'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\\Users\\singl\\OneDrive\\Documents\\Ruchi\\Selenium\\chromedriver.exe")
driver.get("http://www.python.org")

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

time.sleep(8)

driver.close()


