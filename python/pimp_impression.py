from selenium import webdriver
from selenium.webdriver.chrome.service import Service     
from webdriver_manager.chrome import ChromeDriverManager  

import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for i in range(1000):
    time.sleep(1)
    driver.get(url)
    print(i, end="\r")
    
