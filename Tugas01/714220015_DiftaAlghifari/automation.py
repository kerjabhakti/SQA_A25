import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self): #Digunakan Untuk Setup Awal Sebelum test
        service = Service(ChromeDriverManager().install()) #Karena menggunakan chrome, maka kita gunakan chromedriver
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(5) #Waktu tunggu jika terjadi error/elemen g nemu

    def test_successful_login(self):
        driver = self.driver
        driver.get("https://pos-akuntan.github.io/login.html")

        driver.find_element(By.ID, "email").send_keys("yuniatadihba@gmail.com")
        driver.find_element(By.ID, "password").send_keys("1234567890")
        driver.find_element(By.ID, "login-btn").click()

        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert_text = alert.text
            self.assertIn("Login berhasil", alert_text)
            alert.accept()
        except:
            self.fail("Alert login berhasil tidak muncul.")

        WebDriverWait(driver, 10).until(EC.url_contains("adminpage"))
        self.assertIn("adminpage", driver.current_url)
        print("Login berhasil, Sudah diarahkan ke Dashboard")

    def test_invalid_login(self):
        driver = self.driver
        driver.get("https://pos-akuntan.github.io/login.html")

        driver.find_element(By.ID, "email").send_keys("salah@email.com")
        driver.find_element(By.ID, "password").send_keys("passwordsalah")
        driver.find_element(By.ID, "login-btn").click()

        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert_text = alert.text
            self.assertIn("Akun anda tidak aktif: undefined", alert_text)
            alert.accept()
        except:
            self.fail("Alert login gagal tidak muncul.")

    def tearDown(self):
        self.driver.quit()


# Jalankan test dengan laporan custom
if __name__ == "__main__":
    start_time = time.time()

    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    end_time = time.time()
    duration = end_time - start_time

    print("\n========= HASIL LAPORAN PENGUJIAN =========")
    print(f"Jumlah Test       : {result.testsRun}")
    print(f"Jumlah Gagal      : {len(result.failures)}")
    print(f"Jumlah Error      : {len(result.errors)}")
    print(f"Waktu Eksekusi    : {duration:.2f} detik")

    if result.wasSuccessful():
        print("✅ Semua test berhasil dijalankan.")
    else:
        print("❌ Ada test yang gagal atau error.")
