from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
import time
import config
from playsound import playsound

driver = webdriver.Chrome('chromedriver')
driver.get('https://fp.trafikverket.se/boka/#/licence')
driver.implicitly_wait(config.wait_time/10) ## seconds



## Incorrect config handling
try:
    print('Read README.md and configure config.py before running script')
    ### social security
    if len(config.social_security) != 12:
        print('social_security may be configured incorrectly')
        print('social_security:', config.social_security)
    ### license_type 
    if not config.license_type[0].isupper():
        print('license_type may be configured incorrectly')
        print('license_type:', config.license_type)
    if ('Körprov' not in config.exam and 'Kunskapsprov' not in config.exam) or config.exam[-1] != config.license_type:
        print('exam or license_type may be configured incorrectly')
        print('exam:', config.exam)
        print('license_type:', config.license_type)
    if config.rent_option and config.language_option:
        print('rent_option or rent_option may be configured incorrectly')
        print('you should probably remove one')
        print('rent_option:', config.rent_option)
        print('language_option:', config.language_option)
    if (len(config.dates) % 2) != 0 or not isinstance(type(config.dates), list):
        print('dates may be configured incorrectly')
        print('dates:', config.dates)
    if not isinstance(type(config.locations), list):
        print('locations may be configured incorrectly')
        print('locations:', config.locations)
except:
    pass



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
def step_three(option_type=None, option_value=None):
    try:
        if option_type == "rent":
            rent_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//select[@id='vehicle-select']/option[text()='{option_value}']"))
            )
            rent_element.click()
        if option_type == "language":
            language_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//select[@id='language-select']/option[text()='{option_value}']"))
            )
            language_element.click()
    except:
        pass


## Selects location
def select_location(loc):
    try:
        location_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "id-control-searchText-1-1"))
        )
        location_element.clear()
        location_element.send_keys(loc, Keys.ENTER)
    except:
        pass

## Finds and selects available time based on arguments
def book_time(first_date, last_date):
    try:
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//*[text()='Lediga provtider']"))
        )
        first_date = datetime.strptime(first_date, '%Y-%m-%d').date()
        last_date = datetime.strptime(last_date, '%Y-%m-%d').date()
        while first_date < last_date:
            try:
                find_date = driver.find_element_by_xpath(f"//*[contains(text(), '{str(first_date)}')]")
                if find_date:
                    find_date_button = find_date.find_element_by_xpath(f"//*[text()='Välj']")
                    find_date_button.click()
                    return False
            except:
                pass
            finally:
                if first_date <= last_date:
                    first_date = first_date + timedelta(days=1)
    except:
        pass
    return True


## continue regardless of strings existance

step_three_conf = False;
try:
    if config.rent_option:
        step_three_conf_type = "rent"
        step_three_conf_value = config.rent_option
        step_three_conf = config.rent_option
        step_three_conf = True
    if config.language_option:
        step_three_conf_type = "language"
        step_three_conf_value = config.language_option
        step_three_conf = True
except:
    pass

## puts it together
## initial pages etc
step_one(config.social_security, config.license_type)
time.sleep(config.wait_time)
step_two(config.exam)
time.sleep(config.wait_time)
## final page
def final_page():
    continue_running = True
    while continue_running:
        for i in config.locations:
            try:
                if continue_running:
                    if step_three_conf_type and step_three_conf_value:
                        step_three(step_three_conf_type, step_three_conf_value)
                    select_location(i)
                    time.sleep(config.wait_time/2)
                    ## for handling multiple timespans
                    for j in range(0, len(config.dates), 2):
                        continue_running = book_time(config.dates[j], config.dates[j+1])
                        time.sleep(config.wait_time/4)
                        if not continue_running:
                            timestamp = datetime.now() + timedelta(minutes=15)
                            while datetime.now() < timestamp:
                                playsound('sounds/alert.mp3')
                            break
                    driver.refresh()
            except:
                pass


if __name__ == '__main__':
    final_page()

driver.quit()