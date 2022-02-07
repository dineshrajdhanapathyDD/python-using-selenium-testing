from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href*='shop']").click()

products = driver.find_element_by_xpath("//div[@class='card h-100]")

#//div[@class='card h-100']/div/h4/a
#products =//div[@class = 'card h-100']
for product in products:
    print(product.find_element_by_xpath("div/h4/a").text)