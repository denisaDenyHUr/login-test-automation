
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

#1. Google Chrome opening automatically 
chrome.get('https://www.google.com/')
sleep(2)

#2. Click on "Agree" cookies button
chrome.find_element(By.CSS_SELECTOR, value='#L2AGLb > div').click()
sleep(3)

#3. Click on "Sign in" button 
chrome.find_element(By.XPATH, '//*[@id="gb"]/div/div[2]/a').click()
sleep(3)

#4. Type the email in the  "email" field 
chrome.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys('softwaretestingaut01@gmail.com')
sleep(3)

#5. Click on "next" button 
chrome.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
sleep(3)

#6. Type the password in the "password" field
chrome.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('FortechTest01')
sleep(3)

#7. Click on "next" button
chrome.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
sleep(8)

#8. The browser closes automatically.