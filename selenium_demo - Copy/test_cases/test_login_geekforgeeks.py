from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("D:\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
# driver.implicitly_wait(10)

driver.get("http://www.google.com/")
time.sleep(4)
driver.find_element(By.NAME, "q").send_keys("geeksforgeeks")
driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").send_keys(Keys.ENTER)
time.sleep(3)
driver.close()


