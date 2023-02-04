from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome("D:\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("http://www.jqueryui.com/drop/droppable")
time.sleep(3)
source = driver.find_element(By.XPATH, "//div[@id='draggable']")
target = driver.find_element(By.ID, "droppable")

action = ActionChains(driver)
action.drag_and_drop(source, target)
action.perform()

driver.quit()


