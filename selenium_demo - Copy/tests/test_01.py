import time
from selenium import webdriver

def test_sam():
    p = webdriver.Chrome('D:\\Downloads\\chromedriver_win32\\chromedriver.exe')
    p.get("https://www.google.com/")
    time.sleep(10)
    
