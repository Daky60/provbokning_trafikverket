from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
import time
import config
from playsound import playsound

driver = webdriver.Chrome(config.chromedriver_location)
driver.get('https://fp.trafikverket.se/boka/#/licence')



## Inputs SS and license type
def step_one(social_security, license_type):
    social_security_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "social-security-number-input"))
    )
    social_security_element.send_keys(social_security)
    driver.find_element_by_xpath(f'//*[@title="{license_type}"]').click()


## Selects exam
def step_two(exam):
    exam_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//*[text()='{exam}']"))
    )
    exam_element_parent = exam_element.find_element_by_xpath('..')
    exam_element_parent.click()


## Selects rent or language option
def step_three(rent_option=None, language_option=None):
    if rent_option:
        rent_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//select[@id='vehicle-select']/option[text()='{rent_option}']"))
        )
        rent_element.click()
    if language_option:
        language_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//select[@id='language-select']/option[text()='{rent_option}']"))
        )
        language_element.click()


## Selects location
def select_location(loc):
    location_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id-control-searchText"))
    )
    location_element.clear()
    location_element.send_keys(loc, Keys.ENTER)


## Finds and selects available time based on arguments
def book_time(first_date, last_date):
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, f"//*[text()='Lediga provtider']"))
    )
    first_date = datetime.strptime(first_date, '%Y-%m-%d').date()
    last_date = datetime.strptime(last_date, '%Y-%m-%d').date()
    while first_date < last_date:
        try:
            t = driver.find_element_by_xpath(f"//*[contains(text(), '{str(first_date)}')]")
            if t:
                button = t.find_element_by_xpath(f"//*[text()='Välj']")
                button.click()
                playsound('alert.mp3')
                return False
        except:
            pass
        finally:
            if first_date <= last_date:
                first_date = first_date + timedelta(days=1)
    return True


## continue regardless of strings existance
try:
    if config.rent_option:
        step_three_conf = config.rent_option
    else:
        step_three_conf = config.language_option
except:
    step_three_conf = False



## puts it together
continue_running = True
step_one(config.social_security, config.license_type)
step_two(config.exam)
while continue_running:
    for i in config.locations:
        if step_three_conf:
            step_three(step_three_conf)
        time.sleep(3)
        select_location(i)
        time.sleep(3)
        continue_running = book_time(config.dates[0], config.dates[1])
        time.sleep(3)
    driver.refresh()
    time.sleep(3)