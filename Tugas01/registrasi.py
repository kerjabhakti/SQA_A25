from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Inisialisasi browser dengan WebDriver otomatis
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # 1. Buka halaman registrasi
    driver.get("https://proyek3-e-commerce.github.io/tefae-commerce/registrasi.html")
    driver.maximize_window()
    time.sleep(2)

    # 2. Isi form registrasi
    driver.find_element(By.ID, "username").send_keys("ayutest123")  # Ubah sesuai kebutuhan
    driver.find_element(By.ID, "email").send_keys("ayutest123@example.com")  # Ubah sesuai kebutuhan
    driver.find_element(By.ID, "password").send_keys("12345678")

    # 3. Klik tombol Register
    driver.find_element(By.XPATH, '//button[text()="Register"]').click()

    # 4. Tunggu hasil redirect
    time.sleep(3)

    # 5. Verifikasi apakah registrasi berhasil
    current_url = driver.current_url
    page_text = driver.page_source.lower()

    if "login" in current_url or "login" in page_text:
        print("✅ Registrasi berhasil, diarahkan ke halaman login.")
    else:
        print(f"❌ Gagal registrasi. Sekarang ada di URL: {current_url}")

    time.sleep(5)

finally:
    driver.quit()
