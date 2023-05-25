import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

serve = Service("chromedriver.exe")
driver = webdriver.Chrome(service=serve)
driver.get("https://www.sastasafar.com/")

'''element = driver.find_element(By.XPATH, "//input[@name='origin']").send_keys("BOM")

elem = driver.find_element(By.XPATH,"//*[@id='eac-container-origin']")

cities_departure = driver.find_elements(By.XPATH,"//div[@class='eac-item']")    
for city in cities_departure:
    if "BOM" in city.text:
        city.click()'''

driver.implicitly_wait(10)
driver.find_element(By.XPATH,("//input[@id='dateNew']")).click()
time.sleep(2)

alldates = driver.find_elements(By.XPATH,("//table[@id='dateNew_table']"))
for date_element in alldates:
        date = date_element.text
        print(date)










