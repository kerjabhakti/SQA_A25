from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

# Inisialisasi browser
driver = webdriver.Chrome()
driver.get("https://bizgrow.sgp.dom.my.id/register")
driver.maximize_window()

# Tunggu hingga elemen form muncul
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.NAME, "fullname")))

# Isi form register
driver.find_element(By.NAME, "fullname").send_keys("Test User")
driver.find_element(By.NAME, "email").send_keys("testuser789@example.com")
driver.find_element(By.NAME, "npm").send_keys("1023456789")
driver.find_element(By.NAME, "phone").send_keys("081234567890")
driver.find_element(By.NAME, "password").send_keys("Password123")
driver.find_element(By.NAME, "password_confirmation").send_keys("Password123")

# Pilih role
select_role = Select(driver.find_element(By.NAME, "role"))
select_role.select_by_visible_text("Pembeli")  # atau "Penjual"

# Klik tombol Register
driver.find_element(By.XPATH, "//button[contains(text(),'Register')]").click()

# Tunggu hingga halaman berikutnya dimuat atau pesan sukses muncul
time.sleep(3)  # Disarankan mengganti dengan WebDriverWait untuk kondisi spesifik

# Cetak judul halaman setelah register
print("Title setelah register:", driver.title)

# Tutup browser
driver.quit()
