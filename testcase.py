from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.action_chains import ActionChains

# Start the WebDriver and open the HTML page
service = Service(executable_path='/usr/local/bin/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=service, options=options)

# Open the WordPress login page
driver.get("http://65.0.18.145/wp-login.php")

# Find the username field and enter the username
username = driver.find_element(By.ID, "user_login")
username.send_keys("user")

# Find the password field and enter the password
password = driver.find_element(By.ID, "user_pass")
password.send_keys("SyXXCMCWZe4Bo&ar1SafP$cU")

# Find the login button and click it
login_button = driver.find_element(By.ID, "wp-submit")
login_button.click()

driver.get("http://65.0.18.145/activity")

commentBox = driver.find_element(By.ID, "whats-new")
textToCheck = "Hello, this is the workshop by Xebia!"
commentBox.send_keys(textToCheck)

postUpdateButton = driver.find_element(By.ID, "aw-whats-new-submit")
postUpdateButton.click()

time.sleep(5)

found_content = driver.find_element(
    By.CSS_SELECTOR, '#activity-stream .activity-content .activity-inner > p').text

assert found_content == textToCheck

commentButton = driver.find_element(
    By.CSS_SELECTOR, '#activity-stream .activity-content .acomment-reply')
commentButton.click()

actions = ActionChains(driver)

# Simulate typing wherever the cursor is
actions.send_keys("Your text to be typed")

# Perform the actions
actions.perform()

commentPostButton = driver.find_element(
    By.CSS_SELECTOR, '#activity-stream [type=submit]')
commentPostButton.click()

time.sleep(20)
# Close the browser window
driver.quit()
