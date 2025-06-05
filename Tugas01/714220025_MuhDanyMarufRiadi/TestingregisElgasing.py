from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

# Fungsi buat generate string random
def random_string(length=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def random_email():
    return f"{random_string()}@example.com"

def random_phone():
    return ''.join(random.choice(string.digits) for _ in range(10))

def random_password(length=8):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

# Setup webdriver dengan ChromeDriverManager agar otomatis download driver terbaru
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://poshotelelgasing.github.io/HotelElGasing.github.io/login.html"

try:
    for i in range(10):
        driver.get(url)
        time.sleep(1)  # tunggu load halaman

        # Klik tombol "Daftar" agar form registrasi muncul
        btn_register = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "register"))
        )
        btn_register.click()

        # Tunggu sampai form registrasi benar-benar tampil
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".register-container form"))
        )

        # Tunggu input form bisa diisi
        reg_username = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "regUsername"))
        )
        reg_email = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "regEmail"))
        )
        reg_phone = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "regPhone"))
        )
        reg_password = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "regPassword"))
        )

        # Isi form registrasi
        reg_username.clear()
        reg_username.send_keys(f"user{random_string()}")

        reg_email.clear()
        reg_email.send_keys(random_email())

        reg_phone.clear()
        reg_phone.send_keys(random_phone())

        reg_password.clear()
        reg_password.send_keys(random_password())

        # Submit form registrasi
        driver.find_element(By.CSS_SELECTOR, ".register-container form button[type='submit']").click()

        # Tunggu alert muncul dan ambil teksnya
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print(f"Registrasi {i+1}: Alert text -> {alert.text}")
        alert.accept()

        # Jeda sebelum registrasi berikutnya
        time.sleep(1)

finally:
    driver.quit()
