import selenium.webdriver.safari.webdriver
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pandas as pd
from bs4 import BeautifulSoup

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from config.credentials import *
from helpers.utils import batch_generator
from helpers.parsing import get_course, get_class_name, get_section_capacity

options = webdriver.ChromeOptions()
options.add_argument("start-maximized") #open Browser in maximized mode
options.add_argument("disable-infobars") # disabling infobars
options.add_argument("--disable-extensions") # disabling extensions
options.add_argument("--disable-gpu") # applicable to windows os only
options.add_argument("--disable-dev-shm-usage") # overcome limited resource problems
options.add_argument("--no-sandbox") # // Bypass OS security model
options.add_argument('--headless')

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)

login_url = "https://ais92hbprd.ais.uchicago.edu/psc/hbprd/EMPLOYEE/EMPL/s/WEBLIB_REDIRECT.ISCRIPT2.FieldFormula.IScript_redirect"
driver.get(login_url)

driver.maximize_window()
time.sleep(5)

# username:
driver.find_element(By.ID, "okta-signin-username").send_keys(USERNAME)
print('Sending Username')

# password:
driver.find_element(By.ID, "okta-signin-password").send_keys(PASSWORD)
print('Sending Password')

time.sleep(10)
# <input class="button button-primary" type="submit" value="Sign In" id="okta-signin-submit" data-type="save">
driver.find_element(By.ID, "okta-signin-submit").submit()
print('Submitting the credentials')

time.sleep(60)
#### START ####
# Authentication layer / DUO Push

#### END ####

button_to_click = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="quicklinks-module"]/a[2]')
    )
)
button_to_click.click()
print("My Classes Clicked.")

select = Select(driver.find_element(By.ID, 'UC_CLSRCH_WRK2_SUBJECT'))

# select by visible text
select.select_by_value('MSCA')
print("Department is selected as MSCA.")

driver.find_element(By.ID, 'UC_CLSRCH_WRK2_SEARCH_BTN').click()
print("Page is refreshed.")

time.sleep(5)

html = driver.page_source

soup = BeautifulSoup(html, 'html5lib')  # If this line causes an error, run 'pip install html5lib' or install html5lib

table = soup.find('div', attrs={'id': 'win0divUC_RSLT_NAV_WRK_PTPG_ROWS_GRID'})

number_of_courses = int(table.text.split('results')[0].strip())
batches = batch_generator(number_of_courses)
batches = [(start, end) for start, end in batches]
batches = [(start, end) if start == 0 else (0, end - start) for start, end in batches]

data_list = []
for start, end in batches:
    time.sleep(15)
    html = driver.page_source
    soup = BeautifulSoup(html,
                         'html5lib')

    course_numbers = list(range(start, end))
    for course_no in course_numbers:
        class_name = get_class_name(soup, course_no)
        section_code, section_condition, section_type = get_course(soup, course_no)
        total_capacity, current_capacity = get_section_capacity(soup, course_no)
        data_list.append(
            [class_name, section_code, section_condition, section_type, total_capacity, current_capacity])

    time.sleep(5)

    try:
        next_button = driver.find_element(By.XPATH, '//*[@id="UC_RSLT_NAV_WRK_SEARCH_CONDITION2"]', )
        if next_button:
            next_button.click()
    except Exception as e:
        print(e)

columns = ["class_name", "section_code", "section_condition", "section_type", "total_capacity", "current_capacity"]
data = pd.DataFrame(data=data_list, columns=columns)
print(data)