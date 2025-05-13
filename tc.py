from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://translate.google.com/")
    wait = WebDriverWait(driver, 10)

    settings_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Settings']")))
    settings_button.click()

    lang_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Change language']")))
    lang_option.click()

    vietnamese_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Tiếng Việt']")))
    vietnamese_option.click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Cài đặt']")))
    print("✅ Test Passed: Giao diện đã chuyển sang tiếng Việt!")

except Exception as e:
    print(" Test Failed:", str(e))

finally:
    driver.quit()