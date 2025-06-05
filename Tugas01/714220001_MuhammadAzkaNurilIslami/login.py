import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Ganti dengan Firefox() jika pakai Firefox
        self.driver.get("https://proyek-3-proyek.github.io/login/")  # Ganti dengan URL login yang sebenarnya

    def test_login_success(self):
        driver = self.driver
        driver.find_element(By.ID, "email").send_keys("playerskost@gmail.com")
        driver.find_element(By.ID, "username").send_keys("KostsPlayer")
        driver.find_element(By.ID, "password").send_keys("12!@qaZX")
        driver.find_element(By.ID, "loginButton").click()

        time.sleep(2)  # Tunggu sebentar untuk load

        # Cek apakah redirect berhasil atau halaman berubah
        self.assertIn("dashboard", driver.current_url)  # Sesuaikan dengan URL setelah login sukses

    def test_login_failed(self):
        driver = self.driver
        driver.find_element(By.ID, "email").send_keys("admingg@gmail.com")
        driver.find_element(By.ID, "username").send_keys("AdminGG")
        driver.find_element(By.ID, "password").send_keys("adminGG123")
        driver.find_element(By.ID, "loginButton").click()

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
