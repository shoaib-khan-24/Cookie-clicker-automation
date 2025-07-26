
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def money_str_to_integer(money_in_str):
    new_money_in_list = money_in_str.split(',')
    new_money_in_str = "".join(new_money_in_list)
    return int(new_money_in_str)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#langSelect-EN").click()
time.sleep(2)
try:
    driver.find_element(By.CSS_SELECTOR, ".cc_banner a").click()
except Exception:
    print("pop-up not found!")

my_cookies = 0
upgrade_time = 5.0
time_back = time.time()
time_end = time.time() + 5*60       #running for 5 minutes




while time.time() < time_end:
    driver.find_element(By.ID, "bigCookie").click()
    my_cookies = money_str_to_integer(driver.find_element(By.CSS_SELECTOR, "#cookies").text.split()[0])
    if time.time() - time_back >= upgrade_time:
        upgrade_time += 0.2
        all_products = driver.find_elements(By.CSS_SELECTOR, "#products .unlocked")

        for product in all_products[::-1]:
            if my_cookies >= money_str_to_integer(product.find_element(By.CLASS_NAME, "price").text):
                product.click()
                break

        time_back = time.time()


print(f"Cookies {driver.find_element(By.XPATH, '//*[@id="cookiesPerSecond"]').get_attribute("innerHTML")}")
print("\nExiting...")
driver.quit()