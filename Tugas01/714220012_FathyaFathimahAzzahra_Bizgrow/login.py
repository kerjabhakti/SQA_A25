from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Konfigurasi akun
npm = "1234567890"
password = "Password123"

# Fungsi untuk klik tombol peringatan DOM Cloud jika ada
def handle_domcloud_warning(driver):
    try:
        print("🔍 Mengecek apakah ada peringatan DOM Cloud...")
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'I understand, I trust this site')]"))
        ).click()
        print("✅ Tombol 'I understand' berhasil diklik.")
    except:
        print("✅ Tidak ada peringatan DOM Cloud, lanjut.")

# Inisialisasi browser
driver = webdriver.Chrome()
driver.get("https://bizgrow.sgp.dom.my.id/login")
driver.maximize_window()

# Tangani peringatan jika ada
handle_domcloud_warning(driver)

# Tunggu sampai form login muncul
wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.NAME, "npm")))
print("📋 Form login ditemukan.")

# Isi form login
driver.find_element(By.NAME, "npm").send_keys(npm)
driver.find_element(By.NAME, "password").send_keys(password)

# Klik tombol login
driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
print("🔐 Tombol Login diklik...")

# Tunggu redirect ke dashboard
try:
    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
    current_url = driver.current_url
    print(f"✅ Berhasil login! Dialihkan ke: {current_url}")
except:
    print("❌ Gagal login atau tidak dialihkan ke dashboard.")

# Cetak judul halaman saat ini
print("📄 Title halaman:", driver.title)

# Tutup browser
time.sleep(2)
driver.quit()