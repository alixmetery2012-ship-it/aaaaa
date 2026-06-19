import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

DIRECT_LINK = "https://omg10.com/4/11173811"

def get_driver():
    ua = UserAgent()
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f'user-agent={ua.random}')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver

def visit_link():
    driver = get_driver()
    try:
        print("Link ziyaret ediliyor...")
        driver.get(DIRECT_LINK)
        time.sleep(random.uniform(8, 15))
        driver.quit()
        return True
    except Exception as e:
        print("Hata:", e)
        driver.quit()
        return False

if __name__ == "__main__":
    for i in range(1):
        visit_link()
        print("Test tamam.")
