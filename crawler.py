# https://sites.google.com/a/chromium.org/chromedriver/home
# Get same version as your chrome

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
import time

social_security = ''
license_type = 'B'
exam = 'Körprov B'
rent_option = 'Ja, automat'
first_date = '2020-07-16'
second_first_date = '2020-08-04'
last_date = '2020-07-26'
second_last_date = '2020-08-31'
loc = ['Sollentuna', 'Järfälla']

driver = webdriver.Chrome("C:\chromedriver")
driver.get('https://fp.trafikverket.se/boka/#/licence')


## Inputs SS and license type
def step_one(social_security, license_type):
    social_security_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "social-security-number-input"))
    )
    social_security_element.send_keys(social_security)
    driver.find_element_by_xpath(f'//*[@title="{license_type}"]').click()


## Selects Exam
def step_two(exam):
    exam_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//*[text()='{exam}']"))
    )
    exam_element_parent = exam_element.find_element_by_xpath('..')
    exam_element_parent.click()


## Selects rent option
def step_three(rent_option=None):
    if rent_option:
        rent_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//select[@id='vehicle-select']/option[text()='{rent_option}']"))
        )
        rent_element.click()


# Page 3
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
        except:
            pass
        finally:
            if first_date <= last_date:
                first_date = first_date + timedelta(days=1)



## puts it together
step_one(social_security, license_type)
step_two(exam)
while True:
    for i in loc:
        step_three(rent_option)
        time.sleep(3)
        select_location(i)
        time.sleep(3)
        book_time(first_date, last_date)
        book_time(second_first_date, second_last_date)
        time.sleep(3)
    driver.refresh()
    time.sleep(3)
