# test_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Buka halaman login
driver.get("https://yayasann-sipatir08s-projects.vercel.app/login")
time.sleep(2)

# Data login (isi sesuai hasil register)
email = "user1234@mail.com"
password = "test1234"

# Isi form login
driver.find_element(By.ID, "email").send_keys(email)
driver.find_element(By.ID, "password").send_keys(password)

# Klik tombol login
driver.find_element(By.CLASS_NAME, "login-btn").click()

# Tunggu redirect atau respon
time.sleep(5)

# Cek keberhasilan login berdasarkan URL atau elemen tertentu
if "dashboard" in driver.current_url or "home" in driver.page_source.lower():
    print("✅ Login berhasil.")
else:
    print("❌ Login gagal.")

# Tutup browser
driver.quit()
