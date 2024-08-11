from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the login page
driver.get('https://login.netcoresmartech.com/')

# Find the fields and input the credentials
account_name = driver.find_element(By.NAME, 'accname')
account_name.send_keys('kaushiksmartech')

username = driver.find_element(By.NAME, 'login')
username.send_keys('admin')

password = driver.find_element(By.NAME, 'password')
password.send_keys('August@2024')

# Submit the form (adjust the form submission method if necessary)
password.send_keys(Keys.RETURN)

# Optionally, wait for the next page to load
driver.implicitly_wait(10)

# Do whatever you need to do after login, e.g., take a screenshot or interact with elements

# Close the browser
driver.quit()