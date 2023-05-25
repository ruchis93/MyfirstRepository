import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serve = Service("chromedriver.exe")
driver = webdriver.Chrome(service=serve)
driver.get("https://fs2.formsite.com/ukneqas/form39/index.html")
driver.maximize_window()
# driver.find_element(By.ID,"input_2").send_keys("Ruchi Singla")

element_1 = driver.find_element(By.ID,"RESULT_RadioButton-2")
drp = Select(element_1)
drp.select_by_visible_text("Neuropathology")

element_2 = driver.find_element(By.ID,"RESULT_RadioButton-3")
drp = Select(element_2)
drp.select_by_index(6)


time.sleep(10)


