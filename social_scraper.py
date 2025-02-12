from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Set up Selenium WebDriver
chrome_driver_path = "chromedriver.exe"  # Change this if necessary
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# URL of the public post
post_url = "https://twitter.com/elonmusk/status/1760000000000000000"  # Replace with your post URL

# Open Twitter post
driver.get(post_url)
time.sleep(5)

# Scroll to load comments
for _ in range(5):  
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

# Extract comments
comments = driver.find_elements(By.CSS_SELECTOR, "div[lang]")  

data = []
for comment in comments:
    data.append(comment.text)

# Save to CSV
df = pd.DataFrame(data, columns=["Comments"])
df.to_csv("comments.csv", index=False)
print("✅ Comments saved successfully!")

# Close browser
driver.quit()
