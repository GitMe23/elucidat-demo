import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import config
from dotenv import load_dotenv
load_dotenv(override=True)
import time

def initialise_driver():
    return webdriver.Chrome()

def navigate_to_root(driver):
    driver.get(os.getenv('ROOT_URL'))
    try:
        # Wait until 'START' is visible to the user
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, config.CSS_selectors['START']))
        )
        time.sleep(1)    
    except:
        print("Timed out before 'START' button loaded")
    
def clickById(driver, name):
    element_id = config.CSS_selectors[name]
    driver.find_element(By.ID, element_id).click()
    time.sleep(1)   