from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
s = Service('C:/chromedriver.exe')
driver = webdriver.Chrome(service=s)

#driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")  #if use this warning shown

#s = Service('C:/Users/.../chromedriver.exe')
#driver = webdriver.Chrome(service=s)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
childwindow = driver.window_handles[1]
driver.switch_to.window(childwindow)
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
#print(driver.find_element_by_tag_name("h3").text)  #check assert

assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text