from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Inisialisasi browser
driver = webdriver.Chrome()

# Buka halaman register
driver.get("https://proyek-tiga.github.io/login/register.html")
time.sleep(2)

# Isi form input
driver.find_element(By.ID, "name").send_keys("imam Test")
driver.find_element(By.ID, "email").send_keys("itest@example.com")
driver.find_element(By.ID, "password").send_keys("rahasia123")

# Pilih peran dari dropdown
dropdown = Select(driver.find_element(By.TAG_NAME, "select"))
dropdown.select_by_visible_text("Penyelenggara")  # atau "Pembeli"

# Klik tombol daftar
driver.find_element(By.XPATH, "//button[text()='Daftar']").click()
time.sleep(2)

# Tangani alert (jika muncul)
try:
    alert = driver.switch_to.alert
    print("🔔 Alert muncul:", alert.text)
    alert.accept()
    print("✅ Alert ditutup.")
except:
    print("❌ Tidak ada alert setelah registrasi.")

# Tunggu proses redirect
time.sleep(2)

# Cek apakah diarahkan ke halaman login
current_url = driver.current_url
print("📍 URL setelah submit:", current_url)

if "login" in current_url:
    print("🎯 Registrasi berhasil dan diarahkan ke halaman login.")
else:
    print("⚠️ Tidak diarahkan ke halaman login setelah registrasi.")

# Tutup browser
driver.quit()