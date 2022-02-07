from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href*='shop']").click() #webpage shop click

products = driver.find_elements_by_xpath("//div[@class='card h-100']") #choose specific product

#//div[@class='card h-100']/div/h4/a
#products =//div[@class = 'card h-100']
for product in products:
    #print(product.find_element_by_xpath("div/h4/a").text  #all product print in name
    productName = product.find_element_by_xpath("div/h4/a").text  #which product choose its shows
    if productName == "Blackberry":  #check blackberry product
        #add the cart
        product.find_element_by_xpath("div/button").click()   #click the add button
driver.find_element_by_css_selector("a[class*='btn-primary']").click() #add product checkout click
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()  #verify checkout click
driver.find_element_by_id("country").send_keys("ind")  #enter the country name
wait = WebDriverWait(driver, 7) # time of whole process
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click() #enter country and click
driver.find_element_by_xpath("//div[@class = 'checkbox checkbox-primary']").click() #agree box click
driver.find_element_by_css_selector("[type='submit']").click()  #purchase button click
#print(driver.find_element_by_class_name("alert-success").text)  #delievry message shown in display
sucessText = driver.find_element_by_class_name("alert-success").text
assert "Success! Thank you!" in sucessText
driver.get_screenshot_as_file("screen.png")