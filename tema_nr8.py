import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(ChromeDriverManager().install())

chrome.get('https://formy-project.herokuapp.com/form')

first_name_field = chrome.find_element(By.ID,"first-name")
first_name_field.send_keys("Alina")

components = chrome.find_element(By.LINK_TEXT,"Components")
components.click()

enable_disable = chrome.find_element(By.PARTIAL_LINK_TEXT,"Drop")
enable_disable.click()

chrome.get("https://www.techlistic.com/p/selenium-practice-form.html?utm_content=cmp-true")
username_field = chrome.find_element(By.NAME,"firstname")
username_field.send_keys("Alina")

time.sleep(3)




