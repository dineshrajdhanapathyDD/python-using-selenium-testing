from selenium import webdriver
#driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

s = Service('C:/chromedriver.exe')
driver = webdriver.Chrome(service=s)
#iframe, frameset, frame
driver.get("https://the-internet.herokuapp.com/iframe")
#frameid or frame name or index value

driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.CSS_SELECTOR,"#tinymce").clear()
#driver.find_element_by_css_selector("tinymce").clear()
driver.find_element(By.CSS_SELECTOR,"#tinymce").send_keys("i am able to automate")
#driver.find_element_by_css_selector("tinymce").send_keys('i am able to automate')
driver.switch_to.default_content()

print(driver.find_element(By.TAG_NAME,"h3").text)
