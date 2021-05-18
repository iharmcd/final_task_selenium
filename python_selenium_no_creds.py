# to run, please provide: 
# 1. path to webdriver - used for EDGE browser from https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# 2. epam account login
# 3. epam account password 
# to variables PATH_DRIVER, login, password accordingly

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH_DRIVER = # your path 

url_site_test = r'https://projectby.trainings.dlabanalytics.com/imakayed/notebooks/final_task.ipynb' 

login = # your epam account login

password = # your epam account password

driver = webdriver.Edge(PATH_DRIVER)

driver.get(url_site_test)

try:
	log_in = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((BY.ID, "zocial-epam-idp"))


		)
except:
	pass

log_in = driver.find_element_by_id("zocial-epam-idp")
log_in.click()

try:
	log_in_lg = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((BY.ID, "userNameInput"))

		)
except:
	pass

log_in_lg = driver.find_element_by_id("userNameInput")
log_in_lg.clear()
log_in_lg.send_keys(login)

log_in_psw = driver.find_element_by_id("passwordInput")
log_in_psw.clear()
log_in_psw.send_keys(password)

submit_button = driver.find_element_by_id("submitButton") 
submit_button.click()

try:
	log_in_lg = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, "button[title = 'run cell, select below'"))

		)

except:
	pass


jupyter_run = driver.find_element_by_css_selector("button[title='run cell, select below']")

jupyter_run.click()



