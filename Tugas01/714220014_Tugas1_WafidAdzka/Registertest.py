from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup ChromeDriver
options = Options()
driver = webdriver.Chrome(options=options)

# Buka halaman
driver.get("https://proyek3webtokoemas.github.io/FEPROYEK1/loginregis.html")

# Klik tombol Register di atas (jika perlu)
register_tab = driver.find_element(By.XPATH, "//button[contains(text(),'Register')]")
register_tab.click()
time.sleep(1)  # Tunggu transisi (jika ada)

# Isi form register
driver.find_element(By.NAME, "name").send_keys("Kayy")
driver.find_element(By.NAME, "email").send_keys("kayy72128@gmail.com")
driver.find_element(By.NAME, "password").send_keys("kayy712")
driver.find_element(By.NAME, "confirmpassword").send_keys("kayy712")

# Klik tombol register
driver.find_element(By.XPATH, "//button[text()='Register']").click()

# Tunggu beberapa detik untuk melihat hasilnya
time.sleep(5)

# Tutup browser
driver.quit()
