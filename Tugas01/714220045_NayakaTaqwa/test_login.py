from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login_test(username, password):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    # Isi form login
    username_input = driver.find_element(By.NAME, "user-name")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys(username)
    password_input.send_keys(password)

    # Klik tombol login
    login_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    login_button.click()

    time.sleep(2)

    # Cek hasil login
    if "inventory" in driver.current_url:
        print(f"[✅] Login berhasil dengan username: '{username}' dan password: '{password}'")
    else:
        # Coba cari pesan error (jika ada)
        try:
            error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
            print(f"[❌] Login gagal - Pesan error: {error_message}")
        except:
            print(f"[❌] Login gagal tanpa pesan error - Username: '{username}'")

    driver.quit()

# 🔎 Jalankan test:

# 1. Test login berhasil
login_test("standard_user", "secret_sauce")

login_test("problem_user", "secret_sauce")

# 2. Test login gagal - username salah
login_test("salah_user", "secret_sauce")

# 3. Test login gagal - password salah
login_test("standard_user", "salah_password")

# 4. Test login gagal - keduanya salah
login_test("user_x", "pass_x")
