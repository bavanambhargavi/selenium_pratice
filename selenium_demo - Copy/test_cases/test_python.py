from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('/chromedriver')
driver.maximize_window()
driver.get("https://www.python.org")
time.sleep(4)
driver.find_element(By.XPATH, "//li[@id='downloads']//a[normalize-space()='Downloads']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='row download-list-widget']//li[1]").click()
time.sleep(4)
print(driver.get_screenshot_as_file("python_org.png"))
driver.close()
