import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# driver = webdriver.Chrome(executable_path="chromedriver.exe")
from selenium.webdriver.chrome.service import Service

serve = Service("chromedriver.exe")
driver = webdriver.Chrome(service=serve)

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='RESULT_TextField-1']").send_keys("Ruchi")
print(driver.find_element(By.XPATH,"//*[@id='RESULT_TextField-1']").get_attribute("value"))






'''driver.find_element(By.ID,"RESULT_TextField-2").send_keys("Singla")
driver.find_element(By.ID,"RESULT_TextField-3").send_keys("3245657890")
driver.find_element(By.ID,"RESULT_TextField-4").send_keys("India")
driver.find_element(By.ID,"RESULT_TextField-5").send_keys("Shimla")
driver.find_element(By.ID,"RESULT_TextField-6").send_keys("singlaruchi66@gmail.com")
driver.find_element(By.XPATH,"//*[@id='q26']/table/tbody/tr[2]/td").click()
driver.find_element(By.XPATH,"//*[@id='q15']//table//tbody//tr[2]//td").click()
driver.find_element(By.XPATH,"//*[@id='q15']/table/tbody/tr[6]/td").click()
element = driver.find_element(By.ID,"RESULT_RadioButton-9")
drp = Select(element)
drp.select_by_index(1)
time.sleep(5)
driver.find_element(By.ID,"FSsubmit").click()'''
driver.close()
