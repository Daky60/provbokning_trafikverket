from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
import time
import config
from playsound import playsound

class SeleniumDriver():
    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver', options=chrome_options)
        self.driver.get('https://fp.trafikverket.se/boka/#/')
        self.driver.implicitly_wait(0.1)
        self.continue_running = True
    def login(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//*[text()='Boka prov']"))
            ).click()
        except TimeoutException:
            print("Took too long to load")
        except NoSuchElementException:
            print("Could not find element. Check config or report on Github")
        except Exception:
            print("Something went wrong")
    def enter_social_security(self):
        try:
            social_security_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "social-security-number-input"))
                )
            time.sleep(5)
            social_security_element.send_keys(config.social_security)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//*[text()='Fortsätt']"))
            ).click()
        except TimeoutException:
            print("Took too long to load")
        except NoSuchElementException:
            print("Could not find element. Check config or report on Github")
        except Exception:
            print("Something went wrong")
    def select_exam(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//*[@title='{config.license_type}']"))
            ).click()
            return True
        except TimeoutException:
            print("Took too long to load")
        except NoSuchElementException:
            print("Could not find element. Check config or report on Github")
        except Exception:
            print("Something went wrong. Check config or report on Github")
    def select_exam_type(self):
        try:
            exam_type_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//*[text()='{(config.exam)}']"))
            )
            exam_type_element.find_element(By.XPATH, '..').click()
        except NoSuchElementException:
            print("Could not find element. Check config or report on Github")
        except:
            pass
    def select_rent_or_language(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//select[@id='vehicle-select']/option[text()='{config.rent_or_language}']"))
            ).click()
        except NoSuchElementException:
            print("Could not find element. Check config or report on Github")
        except:
            pass
    def select_location(self, location):
        self.location = location
        try:
            location_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "id-control-searchText-1-1"))
            )
            location_element.clear()
            location_element.send_keys(self.location, Keys.ENTER)
        except NoSuchElementException:
            print("Could not find element. Check config or report on Github")
        except:
            pass
    def select_time(self, first_date, last_date):
        self.first_date = first_date
        self.last_date = last_date
        try:
            WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//*[text()='Lediga provtider']"))
            )
            self.first_date = datetime.strptime(self.first_date, '%Y-%m-%d').date()
            self.last_date = datetime.strptime(self.last_date, '%Y-%m-%d').date()
            while self.first_date < self.last_date:
                try:
                    find_date = self.driver.find_element(By.XPATH, f"//*[contains(text(), '{str(self.first_date)}')]")
                    if find_date:
                        find_date_button = find_date.find_element(By.XPATH,f"//*[text()='Välj']")
                        find_date_button.click()
                        return False
                except:
                    pass
                finally:
                    if self.first_date <= self.last_date:
                        self.first_date = self.first_date + timedelta(days=1)
        except:
            pass
        return True
    def book_exam(self):
        time.sleep(5)
        try:
            exam_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//button[@class='btn btn-lg btn-primary col-xs-12']"))
            )
            self.driver.execute_script("arguments[0].click();", exam_element)
        except TimeoutException:
            print("Took too long to load")
        except NoSuchElementException:
            print("Could not find element. Check config or report on Github")
        except: 
            pass
    def confirm_booking(self):
        try:
            exam_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//*[text()='Betala senare']"))
            )
            exam_element.find_element(By.XPATH, '..').click()
        except TimeoutException:
            print("Took too long to load")
        except NoSuchElementException:
            print("Could not find element. Check config or report on Github")
        except: 
            pass
    def confirm_phone_number(self):
        try:
            phone_number_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "input-phone"))
                ).get_attribute("value")
            phone_number_element2 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "input-second-phone"))
                )
            phone_number_element2.send_keys(phone_number_element)
        except TimeoutException:
            print("Took too long to load")
        except NoSuchElementException:
            print("Could not find element. Check config or report on Github")
        except: 
            pass
    def confirm_last(self):
        try:
            exam_type_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//button[@class='btn btn-primary btn-lg btn-block']"))
            )
            exam_type_element.find_element(By.XPATH, '..').click()
        except TimeoutException:
            print("Took too long to load")
        except NoSuchElementException:
            print("Could not find element. Check config or report on Github")
        except: 
            pass
    def refresh_page(self):
        return self.driver.refresh()

def find_exam(driver):
    driver.login()
    time.sleep(5)
    driver.enter_social_security()
    time.sleep(5)
    driver.select_exam()
    time.sleep(5)
    while driver.continue_running:
        for i in config.locations:
            try:
                driver.select_exam_type()
                time.sleep(0.3)
                driver.select_rent_or_language()
                time.sleep(0.3)
                if driver.continue_running:
                    driver.select_location(i)
                    time.sleep(0.1)
                    for j in range(0, len(config.dates), 2):
                        driver.continue_running = driver.select_time(config.dates[j], config.dates[j+1])
                        time.sleep(0.1)
                        if not driver.continue_running:
                            time.sleep(5)
                            driver.book_exam()
                            time.sleep(5)
                            driver.confirm_booking()
                            time.sleep(5)
                            driver.confirm_phone_number()
                            time.sleep(5)
                            driver.confirm_last()
                            playsound('sounds/alert.mp3')
            except:
                pass
        driver.refresh_page()
        time.sleep(1)
if __name__ == '__main__':
    find_exam(SeleniumDriver())
