from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()  # Pastikan chromedriver terinstall

driver.get("https://proyek-tiga.github.io/login/")

time.sleep(2)

email_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "password")

email_input.send_keys("Farhan1654@gmail.com")
password_input.send_keys("12345678")
password_input.send_keys(Keys.ENTER)

time.sleep(5)

print("Current URL after login:", driver.current_url)

driver.quit()
