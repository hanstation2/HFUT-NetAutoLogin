from selenium import webdriver
import time, json, sys, os
from selenium.webdriver.common.by import By


idnum = json.load(open('./idnum.json'))
s_id = idnum['id']
password = idnum['password']
print(s_id,password)
time.sleep(3)
options = webdriver.EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Edge(options=options)

driver.get(r'http://172.18.3.3/0.htm')
'''driver = webdriver.Chrome()
driver.get("http://172.18.3.3/0.htm")'''
element = driver.find_element(By.XPATH, "//*[@id='username']")
element.click()
time.sleep(0.5)
element.send_keys(s_id)

element = driver.find_element(By.XPATH, "//*[@id='password']")
element.click()
time.sleep(0.5)
element.send_keys(password)
time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='submit']").click()
print('successfully logged in')
time.sleep(1)
os.system("taskkill /F /IM msedge.exe")
os.system("taskkill /F /IM WindowsTerminal.exe")


