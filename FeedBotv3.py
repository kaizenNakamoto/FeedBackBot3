'''

Education purpose only

'''


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#Chrome Ver : 84    Update ur chromedriver.exe if necessary from here https://sites.google.com/a/chromium.org/chromedriver/downloads

U='xxxxxx' # USERNAME
P='xxxxxx' # PASSWORD
T=4          # Number of Teachers

driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.get('https://campus.bmsce.ac.in/student')
time.sleep(3)
usn=driver.find_element_by_name('usn')
pas=driver.find_element_by_name('password')
usn.send_keys(U)
pas.send_keys(P)
buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Sign In')]")
for b in buttons:
    b.click()
time.sleep(2)
driver.get('https://campus.bmsce.ac.in/student/feedbackFaculty/1')
for i in range(T):
    buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Give Feedback')]")
    buttons[0].click()
    time.sleep(2)
    buttons = driver.find_elements_by_xpath("//*[contains(@id, 'rating-5')]")
    for b in buttons:
        b.send_keys(webdriver.common.keys.Keys.SPACE)
    buttons = driver.find_element_by_id('submit_feedback')
    actions = ActionChains(driver)
    actions.move_to_element(buttons).click().perform()
    print(str((i+1)/T*100)+' DONE')