from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup WebDriver (gunakan path ChromeDriver Anda jika perlu)
driver = webdriver.Chrome()

# Buka halaman login
driver.get("https://proyek3-pos.github.io/laundrypos-fe/login.html")
driver.maximize_window()

# Tunggu beberapa detik untuk memastikan halaman termuat
time.sleep(2)

# Temukan input field dan isi username & password
username_field = driver.find_element(By.ID, "username")  # Asumsikan ID-nya 'username'
password_field = driver.find_element(By.ID, "password")  # Asumsikan ID-nya 'password'

username_field.send_keys("admin")
password_field.send_keys("admin")

# Tekan tombol login
login_button = driver.find_element(By.TAG_NAME, "button")  # Ambil tombol pertama
login_button.click()

# Tunggu untuk melihat hasil login
time.sleep(5)

# Validasi hasil login (misalnya: redirect ke dashboard, cek URL)
if "dashboard" in driver.current_url.lower() or "home" in driver.page_source.lower():
    print("✅ Login berhasil.")
else:
    print("❌ Login gagal.")

# Tutup browser
driver.quit()
