from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("D:\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()
driver.get("http://www.google.com")
time.sleep(2)
driver.find_element(By.NAME,'q').send_keys('Flipkart')
driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(By.XPATH,"//h3[normalize-space()='Flipkart']").click()
driver.find_element(By.XPATH, "//a[@class='_1_3w1N']").click()
time.sleep(2)
#driver.implicitly_wait(10)
#driver.find_element(By.XPATH,"//input[@class='_2IX_2- VJZDxU']").clear()
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input').send_keys("9515996096")
#driver.implicitly_wait(10)
time.sleep(2)
#driver.find_element(By.XPATH,"").send_keys("bhargavi44")
#ime.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button").click()
time.sleep(3)
print(driver.get_screenshot_as_file("flipkart_org.png"))
driver.close()









