import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome('.\chromedriver', options=chrome_options)

driver.maximize_window()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

message = driver.find_element_by_id('user-message')
user_input_message = 'hello'
message.send_keys(user_input_message)

btns = driver.find_elements_by_class_name('btn-default')
btns[0].click()

output_message = driver.find_element_by_id('display')

assert user_input_message in output_message.text

time.sleep(5)

number1 = driver.find_element_by_id('sum1')
number1.send_keys('5')
number2 = driver.find_element_by_id('sum2')
number2.send_keys('10')

btns[1].click()

time.sleep(1000)
driver.quit()
