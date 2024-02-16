from selenium import webdriver
import os
from dotenv import load_dotenv
load_dotenv(override=True)

def initialise_driver():
    return webdriver.Chrome()

def navigate_to_root(driver):
    driver.get(os.getenv('ROOT_URL'))