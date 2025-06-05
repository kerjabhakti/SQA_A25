from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup ChromeDriver
options = Options()
driver = webdriver.Chrome(options=options)

# Buka halaman login
driver.get("https://proyek3webtokoemas.github.io/FEPROYEK1/loginregis.html")

# Klik tombol "Login"
login_tab = driver.find_element(By.XPATH, "//button[contains(text(),'Login')]")
login_tab.click()
time.sleep(1)

# Isi form login
driver.find_element(By.NAME, "email").send_keys("fathir080604@gmail.com")
driver.find_element(By.NAME, "password").send_keys("123456")

# Klik tombol Login
driver.find_element(By.XPATH, "//button[text()='Login']").click()

# Tunggu beberapa detik untuk melihat hasil (bisa diganti cek status login berhasil/gagal)
time.sleep(5)

# Tutup browser
driver.quit()
