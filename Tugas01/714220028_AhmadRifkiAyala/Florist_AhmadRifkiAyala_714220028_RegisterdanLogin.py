from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. Buat 20 akun dummy manual
dummy_accounts = [
    (f"cekUser{i}@example.com", f"Password{i:02d}!") for i in range(1, 5)
]

# 2. Setup WebDriver
options = Options()
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get("https://floristry-app.netlify.app/")

# 3. Helper Functions
def open_login_modal():
    login_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'bKMMW')]/a"))
    )
    login_icon.click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'sign in')]"))
    )

def click_signup():
    signup_button = driver.find_element(By.XPATH, "//button[contains(text(),'Sign up')]")
    signup_button.click()

    # Tunggu <h2>Please sign up</h2> dengan class yang tepat
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Please sign up') and contains(@class, 'sc-iCKXBC')]"))
    )
    
    time.sleep(1)  # beri waktu animasi modal selesai


def fill_register_form(email, password):
    # Tunggu field tersedia dan bisa diklik
    email_field = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='email' and contains(@class,'sc-jMbVJB')]"))
    )
    password_field = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='password' and contains(@class,'sc-jMbVJB')]"))
    )

    time.sleep(0.5)  # tunggu tambahan supaya animasi selesai

    # Ganti .clear() dengan JS
    driver.execute_script("arguments[0].value = '';", email_field)
    email_field.send_keys(email)

    driver.execute_script("arguments[0].value = '';", password_field)
    password_field.send_keys(password)

def fill_login_form(email, password):
    # Tunggu field tersedia dan bisa diklik
    email_field = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='email' and contains(@class,'sc-jgraLO')]"))
    )
    password_field = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='password' and contains(@class,'sc-jgraLO')]"))
    )

    time.sleep(0.5)  # tunggu tambahan supaya animasi selesai

    # Ganti .clear() dengan JS
    driver.execute_script("arguments[0].value = '';", email_field)
    email_field.send_keys(email)

    driver.execute_script("arguments[0].value = '';", password_field)
    password_field.send_keys(password)



def click_register():
    register_button = driver.find_element(By.XPATH, "//button[text()='Register']")
    register_button.click()
    time.sleep(2)


def click_login():
    login_button = driver.find_element(By.XPATH, "//button[text()='Log In']")
    login_button.click()
    time.sleep(2)

# def click_submit():
#     btn = driver.find_element(By.XPATH, "//button[contains(text(),'Sign up') or contains(text(),'Log In')]")
#     btn.click()
#     time.sleep(2)

# 4. Proses Register Semua Akun
for index, (email, password) in enumerate(dummy_accounts):
    print(f"🟢 Register akun ke-{index+1}: {email}")
    driver.get("https://floristry-app.netlify.app/")
    open_login_modal()
    click_signup()
    fill_register_form(email, password)
    click_register()

print("✅ Semua akun berhasil didaftarkan.\n🔁 Mulai proses login satu per satu...")

# 5. Proses Login Semua Akun
for index, (email, password) in enumerate(dummy_accounts):
    print(f"🔐 Login akun ke-{index+1}: {email}")
    driver.get("https://floristry-app.netlify.app/")
    open_login_modal()
    fill_login_form(email, password)
    click_login()

print("✅ Semua akun berhasil login.")
driver.quit()
print("🛑 Browser ditutup.")
