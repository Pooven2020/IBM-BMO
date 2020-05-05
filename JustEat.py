import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:/Users/KiaanGeetesh/Downloads/chromedriver/chromedriver.exe')
driver.get('http://www.just-eat.co.uk');
time.sleep(10)
search_box = driver.find_element_by_class_name('Form_c-search-input_3ySg3')
search_box.send_keys('AR51 1AA')
search_box.submit()
time.sleep(15) 
driver.quit()
