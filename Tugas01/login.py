from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # 1. Buka halaman login
    driver.get("https://proyek3-e-commerce.github.io/tefae-commerce/login.html")
    driver.maximize_window()
    time.sleep(2)

    # 2. Isi username dan password
    driver.find_element(By.ID, "username").send_keys("ayu@example.com")
    driver.find_element(By.ID, "password").send_keys("12345678")

    # 3. Klik tombol login
    driver.find_element(By.XPATH, '//button[text()="Login"]').click()

    # 4. Tunggu login selesai
    time.sleep(2)

    # 5. Redirect ke index.html (beranda Glowing)
    driver.get("https://proyek3-e-commerce.github.io/tefae-commerce/index.html")
    time.sleep(2)

    # 6. Verifikasi apakah berhasil masuk ke beranda
    current_url = driver.current_url
    page_text = driver.page_source.lower()

    if "index.html" in current_url or "glowing" in page_text:
        print("✅ Berhasil masuk ke halaman utama Glowing.")
    else:
        print(f"❌ Gagal redirect. Sekarang ada di: {current_url}")

    time.sleep(5)

finally:
    driver.quit()
