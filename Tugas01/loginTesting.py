from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Inisialisasi Chrome driver
driver = webdriver.Chrome()

# Fungsi mengecek apakah register berhasil lewat SweetAlert
def is_register_successful():
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "swal2-popup"))
        )
        title = driver.find_element(By.CLASS_NAME, "swal2-title").text
        content = driver.find_element(By.CLASS_NAME, "swal2-html-container").text
        print(f"[SweetAlert] {title}: {content}")

        ok_button = driver.find_element(By.CLASS_NAME, "swal2-confirm")
        ok_button.click()

        return "berhasil" in title.lower()
    except:
        return False

# Base data
base_email = "teslogiccoffee"
base_phone = "081234567"
counter = 1
success = False
password_used = "rahasia123"
name_used = "Pengguna Tes"

# Loop sampai sukses daftar
while not success:
    driver.get("https://logiccoffee.id.biz.id/register/")
    time.sleep(2)

    # Generate email & phone unik
    email = f"{base_email}{random.randint(1000,9999)}@mail.com"
    phone = f"{base_phone}{random.randint(100,999)}"

    try:
        # Cari dan isi input
        driver.find_element(By.NAME, "Name").clear()
        driver.find_element(By.NAME, "Name").send_keys(name_used)

        driver.find_element(By.NAME, "PhoneNumber").clear()
        driver.find_element(By.NAME, "PhoneNumber").send_keys(phone)

        driver.find_element(By.NAME, "Email").clear()
        driver.find_element(By.NAME, "Email").send_keys(email)

        driver.find_element(By.NAME, "Password").clear()
        driver.find_element(By.NAME, "Password").send_keys(password_used)

        # Klik tombol "Daftar"
        driver.find_element(By.ID, "register-button").click()

        # Cek apakah berhasil
        if is_register_successful():
            print(f"✅ Registrasi berhasil dengan Email: {email} dan No HP: {phone}")
            success = True
        else:
            print(f"❌ Gagal daftar dengan Email: {email}, coba ulang...")
            counter += 1
            time.sleep(2)

    except Exception as e:
        print("❌ Terjadi kesalahan saat proses:", e)
        break

# Tutup browser
driver.quit()
