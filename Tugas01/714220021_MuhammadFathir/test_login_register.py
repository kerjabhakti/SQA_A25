from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inisialisasi browser
driver = webdriver.Chrome()

try:
    # === 1. Buka halaman Registrasi ===
    driver.get("https://proyek3-e-commerce.github.io/tefae-commerce/registrasi.html")
    driver.maximize_window()
    time.sleep(2)

    print("📝 Mengisi form registrasi...")

    # Isi form registrasi
    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "email").send_keys("testuser@example.com")
    driver.find_element(By.ID, "password").send_keys("12345678")

    # Klik tombol Register
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    print("✅ Submit form registrasi selesai.")
    time.sleep(3)  # Tunggu respon redirect / popup

    # === 2. Buka halaman Login ===
    driver.get("https://proyek3-e-commerce.github.io/tefae-commerce/login.html")
    time.sleep(2)

    print("🔐 Mengisi form login...")

    # Isi form login
    driver.find_element(By.ID, "email").send_keys("testuser@example.com")
    driver.find_element(By.ID, "password").send_keys("12345678")

    # Klik tombol Login
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    print("✅ Submit form login selesai.")
    time.sleep(3)  # Tunggu hasil login

except Exception as e:
    print("❌ Terjadi error:", e)

finally:
    driver.quit()