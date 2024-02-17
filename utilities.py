import os
from bs4 import BeautifulSoup
import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
load_dotenv(override=True)

def initialise_driver():
    return webdriver.Chrome()

def navigate_to_root(driver):
    driver.get(os.getenv('ROOT_URL'))
    try:
        element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, config.CSS_selectors['START']))
        )
    except:
        print("Timed out before 'START' button loaded")
    
def click_by_id(driver, name):
    try:
        element_id = config.CSS_selectors[name]
        element = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.ID, element_id))
        )
        element.click()
        return True
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return False

def get_number_of_cards_on_page(driver):
    try:
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'card__overlay'))
        )
        case_cards = driver.find_elements(By.CLASS_NAME, 'card__overlay')
        return len(case_cards)
    except:
        return 0

def get_score_text_on_page(driver):
    try:
        element = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.ID, config.CSS_selectors['SCORE']))
        )
        return element.text
    except:
        return None

def click_on_case(driver, case):
    try:
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'card__overlay'))
        )
        case_cards = driver.find_elements(By.CLASS_NAME, 'card__overlay')
        case_cards[case - 1].click()
    except Exception as e:
        pass
    
def click_div_with_text(driver, text):
    try:
        element = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{text}')]"))
        )
        element.click()
        return True
    except Exception as e:
        return False

def text_is_visible(driver, text):
    try:
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{text}')]"))
        )
        return True
    except:
        return False

