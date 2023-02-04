from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(
    "D:\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("http.//www.google.com/")
print(driver.title)
time.sleep(20)
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("getting started with python")
time.sleep(4)
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.close()
