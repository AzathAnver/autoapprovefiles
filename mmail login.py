import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the login page
driver.get('http://mmail.netcore.co.in/emmbin/superlogin.pl')

# Find the fields and input the credentials
account_name = driver.find_element(By.NAME, 'user')
account_name.send_keys('support')

username = driver.find_element(By.NAME, 'pass')
username.send_keys('EM$@ReP0r!$^')

password = driver.find_element(By.NAME, 'mobile')
password.send_keys('9994617344')

# Submit the form
password.send_keys(Keys.RETURN)

# Wait for the page to load after login
driver.implicitly_wait(10)

# Navigate to the desired page
driver.get('http://mmail.netcore.co.in/emmbin/show_suspect_files_test.pl?pageno=1&showlinks=2&client_name=&fromdate=&enddate=&pagesize=150&search=0')
driver.implicitly_wait(10)

# Function to click and handle each "Clean Upload" button sequentially
def click_clean_upload_buttons():
    clean_upload_buttons = driver.find_elements(By.XPATH, "//input[@value='Clean Upload' and contains(@onclick, 'cleanUpload')]")
    
    for button in clean_upload_buttons:
        try:
            # Click the current "Clean Upload" button
            button.click()
            print("Clicked the 'Clean Upload' button.")
            
            # Wait for the pop-up to appear and accept it
            WebDriverWait(driver, 15).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()
            print("Pop-up was accepted.")
            
            # Optionally, wait for the page to stabilize after the interaction
            time.sleep(2)
        except Exception as e:
            print(f"An error occurred: {e}")

# Main loop to continuously check for new buttons
while True:
    click_clean_upload_buttons()
    print("Waiting for 5 minutes before checking again...")
    time.sleep(30)  # Wait for 5 minutes (300 seconds) before checking again

# Note: The script will keep running indefinitely. Manually terminate the script when needed.