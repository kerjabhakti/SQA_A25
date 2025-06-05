from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Buka browser
driver = webdriver.Chrome()
driver.get("https://proyek-tiga.github.io/login/")

# Isi email & password
driver.find_element(By.NAME, "email").send_keys("iiitest@example.com")
driver.find_element(By.NAME, "password").send_keys("rahasia123")

# Submit form
driver.find_element(By.TAG_NAME, "form").submit()
time.sleep(2)

# Coba deteksi alert
try:
    # Pertama: alert sukses login
    alert = driver.switch_to.alert
    print("🔔 Alert 1 muncul:", alert.text)
    alert.accept()
    time.sleep(1)

    # Kedua: alert redirect berhasil
    alert = driver.switch_to.alert
    print("🔔 Alert 2 muncul:", alert.text)
    alert.accept()
    print("✅ Alert ditutup.")
except:
    print("❌ Tidak ada alert atau login gagal.")

# Tunggu proses redirect
time.sleep(2)

# Cek URL setelah login
current_url = driver.current_url
print("📍 URL setelah login:", current_url)

if "FrontendPenyelenggara" in current_url:
    print("🎯 Berhasil login dan diarahkan ke halaman penyelenggara.")
else:
    print("⚠️ Login tidak diarahkan ke halaman penyelenggara.")

# Tutup browser
driver.quit()
