from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    # === 1. Buka halaman login ===
    driver.get("https://proyek3-e-commerce.github.io/tefae-commerce/login.html")

    # === 2. Isi email dan password, lalu klik Login ===
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys("testuser@example.com")
    driver.find_element(By.ID, "password").send_keys("12345678")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # === 3. Tunggu halaman index.html terbuka ===
    WebDriverWait(driver, 10).until(EC.url_contains("index.html"))
    current_url = driver.current_url
    print("Halaman saat ini setelah login:", current_url)

    if "index.html" in current_url:
        print("✅ Landingpage berhasil dibuka setelah login.")
    else:
        print("❌ Gagal membuka landingpage setelah login.")

    # === 4. Klik ikon user untuk buka menu logout ===
    auth_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "auth-icon"))
    )
    auth_icon.click()

    # === 5. Setelah menu terbuka, klik tombol Logout ===
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout-btn"))
    )
    logout_button.click()

    # === 6. Tunggu kembali ke halaman login ===
    WebDriverWait(driver, 10).until(EC.url_contains("login.html"))
    current_url_after_logout = driver.current_url
    print("Halaman setelah logout:", current_url_after_logout)

    if "login.html" in current_url_after_logout:
        print("✅ Logout berhasil dan diarahkan ke halaman login.")
    else:
        print("❌ Logout gagal atau tidak diarahkan ke halaman login.")

except Exception as e:
    print("❌ Terjadi error:", e)

finally:
    driver.quit()