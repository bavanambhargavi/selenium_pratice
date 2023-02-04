# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.page_load_strategy = "none"
# driver = webdriver.Chrome(options=options)
# driver.get("http://www.google.com")
# driver.quit()

#from selenium import webdriver
#from selenium.webdriver.common.by import By


# def test_eight_components():
#     driver = webdriver.Chrome()

#     driver.get("https://www.selenium.dev/selenium/web/web-form.html")

#     title = driver.title
#     assert title == "Web form"

#     #driver.implicitly_wait(8)
#     driver.implictly_wait(5)

#     text_box = driver.find_element(by=By.NAME, value="my-text")
#     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

#     text_box.send_keys("Selenium")
#     submit_button.click()

#     message = driver.find_element(by=By.ID, value="message")
#     value = message.text
#     assert value == "Received!"

#     driver.quit()

# from selenium import webdriver

# firefox_options = webdriver.FirefoxOptions()
# driver = webdriver.Remote(
#     command_executor='http://geekforgeeks.com',
#     options=firefox_options
# )
# driver.get("http://www.google.com")
# driver.quit() 
  
# from selenium.webdriver.support.wait import WebDriverWait
# driver = webdriver.chrome()
# driver.navigate("file:///race_condition.html")
# el = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.TAG_NAME,"p"))
# assert el.text == "Hello from JavaScript!"
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
def document_initialised(driver):
    return driver.execute_script("return initialised")
driver = webdriver.Chrome()
driver.get("http://www.google.com")
time.sleep(2)
driver.navigate().to("http://www.python.com")
WebDriverWait(driver, timeout=10).until(document_initialised)
el = driver.find_element(By.NAME, "p")
assert el.text == "Hello from python"
  