from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website="https://egy.almaviva-visa.it/"
path="./chromedriver-win64/chromedriver.exe"
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
Ser=Service(executable_path=path)

driver=webdriver.Chrome(options=option, service=Ser)

driver.get(website)
registerpage=driver.find_element(by="xpath",value="/html/body/app-root/app-header/div/mat-toolbar/div[3]/app-user-menu/div/button")
registerpage.click()
print("done")