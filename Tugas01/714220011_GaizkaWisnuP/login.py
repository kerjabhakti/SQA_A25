from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 🔧 Ganti path ini sesuai lokasi ChromeDriver milikmu
service = Service(r'C:\Users\INFINIX\Downloads\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# 🔗 Buka halaman login
driver.get("https://proyek3-pos.github.io/laundrypos-fe/login.html")
driver.maximize_window()

# 📝 Isi form login
username = "staff5874"   # Ganti dengan username yang valid
password = "tes12345"    # Ganti dengan password yang sesuai

driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)

# 🚀 Submit form
driver.find_element(By.ID, "loginForm").submit()

try:
    # ⏳ Tunggu SweetAlert muncul (maks 10 detik)
    alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "swal2-popup"))
    )

    # 📖 Ambil isi SweetAlert
    alert_title = driver.find_element(By.CLASS_NAME, "swal2-title").text
    alert_text = driver.find_element(By.CLASS_NAME, "swal2-html-container").text
    print("🟢 SweetAlert muncul:")
    print("   Judul:", alert_title)
    print("   Pesan:", alert_text)

    # Tunggu redirect otomatis (karena pakai `.then(() => redirect)` di JS)
    time.sleep(3)

    # ✅ Validasi URL redirect
    current_url = driver.current_url
    if "dashboard" in current_url:
        print("✅ Login berhasil: Role admin (dashboard.html)")
    elif "customer-staff" in current_url:
        print("✅ Login berhasil: Role staff (customer-staff.html)")
    else:
        print("⚠️ Login berhasil tapi URL tidak dikenali:", current_url)

except Exception as e:
    print("❌ Login gagal atau SweetAlert tidak muncul:", str(e))

# 🔚 Tutup browser
time.sleep(2)
driver.quit()
