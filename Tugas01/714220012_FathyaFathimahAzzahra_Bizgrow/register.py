from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

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
driver.get("https://bizgrow.sgp.dom.my.id/register")
driver.maximize_window()

# Coba klik tombol "I understand" jika muncul
handle_domcloud_warning(driver)

# Tunggu sampai form muncul
wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.NAME, "name")))
print("📋 Form pendaftaran ditemukan.")

# Isi form
driver.find_element(By.NAME, "name").send_keys("Test User")
driver.find_element(By.NAME, "email").send_keys("testuser123@example.com")
driver.find_element(By.NAME, "npm").send_keys("1234567890")
driver.find_element(By.NAME, "phone_number").send_keys("081234567890")
driver.find_element(By.NAME, "password").send_keys("Password123")
driver.find_element(By.NAME, "password_confirmation").send_keys("Password123")

# Pilih peran (role)
select_role = Select(driver.find_element(By.NAME, "role"))
select_role.select_by_visible_text("Pembeli")  # atau "Penjual"

# Klik tombol "Sign up"
driver.find_element(By.XPATH, "//button[contains(text(),'Sign up')]").click()
print("🚀 Tombol Sign up diklik...")

# Tunggu hasil atau redireksi
time.sleep(3)
print("📄 Title halaman setelah register:", driver.title)

# Tutup browser
driver.quit()