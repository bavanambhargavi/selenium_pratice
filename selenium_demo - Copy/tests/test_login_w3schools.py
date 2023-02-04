from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.()
driver.get("http://www.w3schools.com")
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='search2']")
time.sleep(3)
driver.close()
















