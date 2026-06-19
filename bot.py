import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DIRECT_LINK = "https://omg10.com/4/11173811"

def get_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    return driver

def visit_link():
    driver = get_driver()
    try:
        print("Link ziyaret ediliyor...")
        driver.get(DIRECT_LINK)
        time.sleep(10)
        driver.quit()
        print("Ziyaret başarılı.")
        return True
    except Exception as e:
        print("Hata:", e)
        driver.quit()
        return False

if __name__ == "__main__":
    for i in range(1):
        visit_link()
        print("Test tamamlandı.")
