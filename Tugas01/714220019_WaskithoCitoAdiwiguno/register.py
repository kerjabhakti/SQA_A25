from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inisialisasi browser
driver = webdriver.Chrome()

# Fungsi untuk cek apakah registrasi berhasil berdasarkan isi SweetAlert
def is_register_successful():
    try:
        # Tunggu hingga SweetAlert muncul
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "swal2-popup"))
        )

        # Ambil teks dari SweetAlert
        title = driver.find_element(By.CLASS_NAME, "swal2-title").text
        content = driver.find_element(By.CLASS_NAME, "swal2-html-container").text

        # Klik tombol OK (confirm)
        ok_button = driver.find_element(By.CLASS_NAME, "swal2-confirm")
        ok_button.click()

        if "Registrasi Berhasil" in title:
            return True
        else:
            return False
    except:
        return False

# --------------------
# Bagian REGISTRASI
# --------------------
base_username = "waskitho"
counter = 1
success = False
registered_username = ""
password_used = "12345"

while not success:
    driver.get("https://proyek3-pos.github.io/laundrypos-fe/register.html")
    time.sleep(2)

    # Ambil input field: name, username, password
    inputs = driver.find_elements(By.TAG_NAME, "input")
    if len(inputs) < 3:
        print("❌ Gagal menemukan input field.")
        break

    name_input = inputs[0]
    username_input = inputs[1]
    password_input = inputs[2]

    name_input.clear()
    username_input.clear()
    password_input.clear()

    registered_username = f"{base_username}{counter}"
    name_input.send_keys("Waskitho")
    username_input.send_keys(registered_username)
    password_input.send_keys(password_used)

    # Klik tombol Sign Up
    sign_up_btn = driver.find_element(By.XPATH, "//button[text()='Sign Up']")
    sign_up_btn.click()

    # Tunggu popup muncul & evaluasi hasil registrasi
    if is_register_successful():
        print(f"✅ Registrasi berhasil dengan username: {registered_username}")
        success = True
    else:
        print(f"❌ Username '{registered_username}' sudah digunakan, coba lagi...")
        counter += 1

# --------------------
# Bagian LOGIN
# --------------------
if success:
    # Tunggu redirect ke halaman login (bisa delay beberapa detik)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )

    try:
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")

        username_field.send_keys(registered_username)
        password_field.send_keys(password_used)

        # Klik tombol login (tombol pertama)
        login_button = driver.find_element(By.TAG_NAME, "button")
        login_button.click()

        time.sleep(5)

        # Validasi berhasil login
        if "dashboard" in driver.current_url.lower() or "home" in driver.page_source.lower():
            print("✅ Login berhasil.")
        else:
            print("❌ Login gagal.")
    except:
        print("❌ Gagal menemukan elemen login.")
else:
    print("❌ Tidak bisa lanjut ke login karena registrasi gagal.")

# Tutup browser
driver.quit()
