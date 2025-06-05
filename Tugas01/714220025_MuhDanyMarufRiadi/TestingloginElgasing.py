from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup WebDriver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://poshotelelgasing.github.io/HotelElGasing.github.io/login.html"
valid_email = "test1@gmail.com"
valid_password = "test130903"

login_success = False

try:
    driver.get(url)
    time.sleep(1)

    # Isi email & password
    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "loginEmail"))
    )
    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "loginPassword"))
    )

    email_input.clear()
    email_input.send_keys(valid_email)
    password_input.clear()
    password_input.send_keys(valid_password)

    # Klik tombol login
    login_button = driver.find_element(By.CSS_SELECTOR, ".login-container form button[type='submit']")
    login_button.click()

    # Tunggu alert "Login berhasil!" muncul
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print(f"📢 Alert muncul: {alert.text}")
    alert.accept()  # Klik OK pada alert

    # Tunggu redirect ke employee.html
    WebDriverWait(driver, 10).until(EC.url_contains("employee.html"))
    print("✅ Login berhasil, dialihkan ke halaman dashboard!")
    login_success = True

finally:
    if not login_success:
        driver.quit()
    else:
        print("🔓 Browser dibiarkan terbuka. Kamu sudah masuk ke dashboard.")
