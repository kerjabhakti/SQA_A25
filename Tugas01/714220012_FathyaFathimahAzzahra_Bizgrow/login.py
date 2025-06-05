from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Fungsi untuk klik tombol peringatan DOM Cloud jika ada
def handle_domcloud_warning(driver):
    try:
        print("🔍 Mengecek apakah ada peringatan DOM Cloud...")
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'I understand')]"))
        ).click()
        print("✅ Tombol 'I understand' berhasil diklik.")
    except:
        print("✅ Tidak ada peringatan DOM Cloud, lanjut.")

# Inisialisasi browser
driver = webdriver.Chrome()
driver.get("https://bizgrow.sgp.dom.my.id/login")
driver.maximize_window()

# Tangani peringatan DOM Cloud
handle_domcloud_warning(driver)

# Tunggu sampai form login siap
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.NAME, "npm")))
print("📋 Form login ditemukan.")

# Isi form login
driver.find_element(By.NAME, "npm").send_keys("1234567890")
driver.find_element(By.NAME, "password").send_keys("Password123")

# Klik tombol "Sign in"
driver.find_element(By.XPATH, "//button[contains(text(),'Sign in')]").click()
print("🚀 Tombol Sign in diklik...")

# Tunggu sampai diarahkan ke dashboard
WebDriverWait(driver, 10).until(
    EC.url_contains("/dashboard")  # Bisa juga "/dashboard-seller"
)
print("✅ Login berhasil! Sekarang di halaman:", driver.current_url)

# Tutup browser
driver.quit()