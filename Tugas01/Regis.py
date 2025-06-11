from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import random
import time

def generate_test_email():
    """Generate a unique test email address"""
    return f"testuser{random.randint(1000,9999)}@example.com"

def register_user():
    # Initialize WebDriver with options
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    try:
        driver = webdriver.Chrome(options=options)
        
        # Navigate to registration page
        driver.get("https://floristry-app.netlify.app/")
        
        try:
            # Click sign up link (modify if needed)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Sign up"))
            ).click()
        except TimeoutException:
            print("Sign up link not found, proceeding directly to registration")
        
        # Wait for registration form
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Please sign up')]"))
        )
        
        # Generate test credentials
        email = generate_test_email()
        password = "SecurePass123!"
        
        # Fill registration form
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='email']"))
        )
        email_field.send_keys(email)
        
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']"))
        )
        password_field.send_keys(password)
        
        # Submit registration
        register_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Register')]"))
        )
        register_btn.click()
        
        # Verify successful registration
        try:
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'success') or contains(text(), 'Welcome')]"))
            )
            print(f"Registration successful! Email: {email}")
            driver.save_screenshot("registration_success.png")
        except TimeoutException:
            print("Registration verification failed")
            driver.save_screenshot("registration_failure.png")
            
    except Exception as e:
        print(f"Error during registration: {str(e)}")
        if 'driver' in locals():
            driver.save_screenshot("registration_error.png")
    finally:
        if 'driver' in locals():
            time.sleep(2)  # Keep browser open briefly
            driver.quit()

if __name__ == "__main__":
    register_user()