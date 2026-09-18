import time
import os
import gspread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Google Sheets API setup (Modern & Clean method)
client = gspread.service_account(filename='credentials.json')
sheet = client.open("Aviator Data").sheet1

# Headless Chrome Browser setup
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

url = "https://example.com/aviator"  # Target website URL
driver.get(url)

print("Bot runs successfully...")

while True:
    try:
        multiplier_element = driver.find_element(By.XPATH, '//div[@class="payouts"]')
        latest_value = multiplier_element.text
        if latest_value:
            sheet.append_row([time.strftime("%Y-%m-%d %H:%M:%S"), latest_value])
            print(f"Data saved: {latest_value}")
        time.sleep(10)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
