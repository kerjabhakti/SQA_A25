#tess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://akt74.github.io/tech_alpha_login_perantara/")  # Ganti dengan path ke file login.html milikmu
    driver.maximize_window()

    time.sleep(1)  # Tunggu agar elemen dimuat

    # ✅ Ganti ke By.ID
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("admin")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("admin123")

    # Klik tombol login
    login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
    login_button.click()

    time.sleep(3)
    print("✅ Login selesai. Cek apakah berhasil redirect.")

except Exception as e:
    print(f"❌ Terjadi error: {e}")

finally:
    driver.quit()
