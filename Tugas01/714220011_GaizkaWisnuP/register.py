from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Path ChromeDriver kamu
service = Service(r'C:\Users\INFINIX\Downloads\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Buka halaman register
driver.get("https://proyek3-pos.github.io/laundrypos-fe/register.html")
driver.maximize_window()
time.sleep(2)

# Isi form dengan data unik
driver.find_element(By.ID, "name").send_keys("Tes Staff")
unique_username = f"staff{random.randint(1000, 9999)}"
print("🔄 Menggunakan username:", unique_username)
driver.find_element(By.ID, "username").send_keys(unique_username)
driver.find_element(By.ID, "password").send_keys("tes12345")

# Submit form
driver.find_element(By.ID, "registerForm").submit()

try:
    # Tunggu SweetAlert muncul maksimal 10 detik
    alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "swal2-popup"))
    )

    # Ambil isi SweetAlert
    alert_title = driver.find_element(By.CLASS_NAME, "swal2-title").text
    alert_content = driver.find_element(By.CLASS_NAME, "swal2-html-container").text
    print("🟢 SweetAlert muncul:")
    print("   Judul :", alert_title)
    print("   Pesan :", alert_content)

    # Klik tombol OK pada SweetAlert
    driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
    time.sleep(2)

    # Cek redirect ke login
    if "login" in driver.current_url:
        print("✅ Registrasi berhasil! Dialihkan ke halaman login.")
    else:
        print("⚠️ Tidak redirect ke login. URL saat ini:", driver.current_url)

except Exception as e:
    print("❌ SweetAlert gagal ditampilkan atau error:", str(e))

# Tutup browser
time.sleep(2)
driver.quit()
