from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
import sys

def initialize_driver():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=options)
        return driver
    except WebDriverException as e:
        print(f"Failed to initialize WebDriver: {str(e)}")
        print("Please ensure:")
        print("1. Chrome is installed")
        print("2. chromedriver is in PATH or matches your Chrome version")
        sys.exit(1)

def login_to_floristry(driver):
    try:
        # Navigate to login page
        driver.get("https://floristry-app.netlify.app/")
        
        # Handle login button
        try:
            login_btn = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Log In"))
            )
            login_btn.click()
        except TimeoutException:
            print("Login button not found, proceeding directly to login form")
        
        # Fill login form
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.NAME, "email"))
        ).send_keys("ewi@example.com")
        
        driver.find_element(By.NAME, "password").send_keys("12345678")
        
        # Submit form
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Log In')]"))
        ).click()
        
        # Verify successful login
        WebDriverWait(driver, 15).until(
            lambda d: "dashboard" in d.current_url.lower() or 
            any(text in d.page_source.lower() for text in ["welcome", "dashboard"])
        )
        print("Login successful!")
        return True
        
    except TimeoutException as e:
        print(f"Timeout occurred: {str(e)}")
        current_url = driver.current_url
        print(f"Current URL: {current_url}")
        if "login" in current_url.lower():
            print("Possible login failure - check credentials")
        return False
    except Exception as e:
        print(f"Unexpected error during login: {str(e)}")
        return False

def main():
    driver = initialize_driver()
    try:
        if login_to_floristry(driver):
            # Add post-login actions here
            pass
        else:
            print("Login process failed")
    finally:
        # Cleanup with assurance
        try:
            driver.save_screenshot("final_state.png")
            print("Saved screenshot to final_state.png")
        except:
            pass
        driver.quit()

if __name__ == "__main__":
    main()