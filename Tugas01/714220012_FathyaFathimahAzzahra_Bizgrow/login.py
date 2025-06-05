from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inisialisasi browser
driver = webdriver.Chrome()
driver.get("https://bizgrow.sgp.dom.my.id/login")
driver.maximize_window()

# Tunggu hingga elemen form muncul
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.NAME, "npm")))

# Isi form login
driver.find_element(By.NAME, "npm").send_keys("1234567890")
driver.find_element(By.NAME, "password").send_keys("Password123")

# Klik tombol Login
driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()

# Tunggu hingga halaman berikutnya dimuat atau pesan sukses muncul
time.sleep(3)  # Disarankan mengganti dengan WebDriverWait untuk kondisi spesifik

# Cetak judul halaman setelah login
print("Title setelah login:", driver.title)

# Tutup browser
driver.quit()
