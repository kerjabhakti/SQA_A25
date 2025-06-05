# test_register.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

driver = webdriver.Chrome()

# Buka halaman register
driver.get("https://yayasann-sipatir08s-projects.vercel.app/register")
time.sleep(2)

# Data unik
rand_num = random.randint(1000, 9999)
email = f"user{rand_num}@mail.com"
name = "Tester Selenium"
password = "test1234"

# Isi form
driver.find_element(By.ID, "email").send_keys(email)
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "password").send_keys(password)

# Klik tombol daftar
driver.find_element(By.XPATH, "//button[text()='Daftar']").click()

# Tunggu selesai (ubah sesuai redirect atau notifikasi)
time.sleep(5)

print(f"✅ Berhasil submit form register dengan email: {email}")

# Tutup browser
driver.quit()
