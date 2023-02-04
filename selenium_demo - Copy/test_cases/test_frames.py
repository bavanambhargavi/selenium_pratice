from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 


def test_check_frame():
    driver = webdriver.Chrome("D:\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://w3schools.com/")
    time.sleep(3)
    driver.find_element(By.ID, "search2").send_keys("Html tutorial")
    time.sleep(4)
    driver.find_element(By.XPATH, "//input[@id='search2']").send_keys(Keys.ENTER)
    time.sleep(3)
    driver.switch_to.frame(0)
    driver.quit()




