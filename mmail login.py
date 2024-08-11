from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
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

# Submit the form (adjust the form submission method if necessary)
password.send_keys(Keys.RETURN)

# Optionally, wait for the next page to load
driver.implicitly_wait(10)

# Do whatever you need to do after login, e.g., take a screenshot or interact with elements
driver.get('http://mmail.netcore.co.in/emmbin/manage_sudentials.pl#')
driver.implicitly_wait(10)
driver.get('http://mmail.netcore.co.in/emmbin/show_suspect_files_test.pl?pageno=1&showlinks=2&client_name=&fromdate=&enddate=&pagesize=150&search=0')
driver.implicitly_wait(10)
# Repeat the process as needed
for _ in range(5):  # Change the range value to the number of repetitions you need
    try:
        # Wait for the button to be clickable and click it
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'Clean Upload'))  # Replace with the actual ID or locator of the button
        )
        button.click()

        # Wait for the pop-up and handle it
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert.accept()  # Click "OK" on the pop-up

        # Refresh the page
        driver.refresh()

        # Optional: wait for a few seconds before repeating
        time.sleep(2)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        break

driver.refresh()
# Close the browser
driver.quit()