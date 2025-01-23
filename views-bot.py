from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time

url = input("Enter url: ")
duration = input("Enter duration: ")
amount = input("Enter amout of loops: ")
yourMail = input("Enter your mail: ")
yourPassword = input("Enter password: ")

for i in range(int(amount)):
    driver = uc.Chrome()
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    searchbox = driver.find_element(By.XPATH, '//*[@id="topbar"]/div[2]/div[2]/ytd-button-renderer/yt-button-shape/a')
    searchbox.click()
    time.sleep(2)
    searchbox = driver.find_element(By.XPATH, '//*[@id="identifierId"]').click()
    driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys('yourMail')
    time.sleep(2)
    searchbox = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()
    time.sleep(5)
    searchbox = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').click()
    driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(yourPassword)
    time.sleep(2)
    searchbox = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button').click()
    time.sleep(int(duration))
    driver.close()



    