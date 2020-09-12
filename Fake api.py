import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://toolbox.google.com/factcheck/explorer/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_id("search-input")
search_box.send_keys('Has California Passed A Legislation Decriminalizing Paedophilia')
search_box.send_keys(Keys.ENTER)
print(driver.find_element_by_xpath('/html/body/fact-check-tools/div/div[2]/search-results-page/div/div[6]/fc-results-list/ul[1]/mat-card/div[3]/div[3]/div').text)

time.sleep(5) # Let the user actually see something!
#driver.quit()

