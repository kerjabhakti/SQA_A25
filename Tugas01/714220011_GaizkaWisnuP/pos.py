from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

service = Service(r'C:\Users\INFINIX\Downloads\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://proyek3-pos.github.io/laundrypos-fe/login.html")

    # Login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys("staff5874")
    driver.find_element(By.ID, "password").send_keys("tes12345")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Tunggu redirect ke halaman staff
    WebDriverWait(driver, 15).until(EC.url_contains("customer-staff.html"))

    # Klik tombol laundry-btn
    laundry_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-sm.btn-primary.laundry-btn"))
    )
    laundry_btn.click()
    print("Tombol laundry-btn berhasil diklik.")

    # Tunggu redirect ke halaman pos.html
    WebDriverWait(driver, 10).until(EC.url_contains("pos.html"))

    # Tunggu dropdown serviceType dan opsi muncul
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "serviceType")))

    def dropdown_has_options(driver):
        select = Select(driver.find_element(By.ID, "serviceType"))
        return len(select.options) > 1

    WebDriverWait(driver, 15).until(dropdown_has_options)

    # Pilih layanan laundry dari dropdown
    service_dropdown = Select(driver.find_element(By.ID, "serviceType"))
    service_dropdown.select_by_index(1)

    # Tangani SweetAlert otomatis jika muncul setelah memilih layanan
    try:
        alert = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "swal2-popup"))
        )
        confirm_button = alert.find_element(By.CLASS_NAME, "swal2-confirm")
        confirm_button.click()
        print("SweetAlert terdeteksi dan dikonfirmasi otomatis.")
    except TimeoutException:
        print("SweetAlert tidak muncul, lanjut proses.")

    # Masukkan berat cucian
    weight_input = driver.find_element(By.ID, "weight")
    weight_input.clear()
    weight_input.send_keys("3")

    time.sleep(1)  # tunggu harga update jika ada

    # Klik tombol order untuk buat transaksi
    driver.find_element(By.ID, "orderButton").click()

    # Tunggu redirect ke halaman payment.html
    WebDriverWait(driver, 10).until(EC.url_contains("payment.html"))

    # Tunggu form payment siap
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "payment-form")))

    # Tunggu sampai semua input form pembayaran terisi otomatis (nilai tidak kosong)
    WebDriverWait(driver, 20).until(lambda d: all([
        d.find_element(By.ID, "customerName").get_attribute("value").strip() != "",
        d.find_element(By.ID, "email").get_attribute("value").strip() != "",
        d.find_element(By.ID, "phone").get_attribute("value").strip() != "",
        d.find_element(By.ID, "service").get_attribute("value").strip() != "",
        d.find_element(By.ID, "weight").get_attribute("value").strip() != "",
        d.find_element(By.ID, "gross_amount").get_attribute("value").strip() != "",
        d.find_element(By.ID, "transactionId").get_attribute("value").strip() != ""
    ]))

    print("Form pembayaran sudah terisi otomatis, klik tombol bayar...")

    # Klik tombol bayar submit form
    driver.find_element(By.ID, "pay-button").click()

    # Tunggu popup Midtrans (modal snap) muncul, tunggu beberapa detik, dan ambil screenshot
    time.sleep(10)
    driver.save_screenshot("hasil_pembayaran.png")

except TimeoutException:
    print("Timeout menunggu elemen atau halaman.")
finally:
    driver.quit()
