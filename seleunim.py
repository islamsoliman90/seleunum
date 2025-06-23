from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website="https://egy.almaviva-visa.it/"
import os
import sys

# Get ChromeDriver path from command-line argument, environment variable, or use default
if len(sys.argv) > 1:
	path = sys.argv[1]
else:
	path = os.environ.get("CHROMEDRIVER_PATH", "./chromedriver-win64/chromedriver.exe")

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
Ser=Service(executable_path=path)

driver=webdriver.Chrome(options=option, service=Ser)

driver.get(website)
# Example using a CSS selector (update the selector to match your target element)
registerpage = driver.find_element(by="css selector", value="app-user-menu button")
registerpage.click()
print("done")

#email=driver.find_element(by="xpath", value="//*[@id=\"password\"]").send_keys("islam@gmail")
element_enter=driver.find_element(by="css selector", value="pf-c-form-control")
element_enter.send_keys("your_barcode_value")

