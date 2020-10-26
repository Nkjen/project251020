from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
from selenium.webdriver.chrome.options import Options
time.sleep(3)


chrome_options = Options()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(options = chrome_options)

print('opening website')

# driver = webdriver.Chrome()
driver.get('https://api.encoding.com')

print('finding search selector and inputing "getStatus"')

search_box = driver.find_element(By. CLASS_NAME, 'searchbox')
search_box.click()
time.sleep(3)
selector_box = driver.find_element(By. CLASS_NAME, 'Input')
selector_box.send_keys('getStatus')
time.sleep(2)

print('following the link getStatus')
get_status = driver.find_elements(By. CSS_SELECTOR, 'a header')
get_status = get_status[1].click()
time.sleep(4)
print('checking the URL')
current_url = driver.current_url
url_2_check = "https://api.encoding.com/reference/responses-getstatus-extended"
print(current_url)

time.sleep(3)
assert url_2_check in current_url
if url_2_check == current_url:
    print('url checking done properly')
else:
    print("doesn't work")

print('clicking json button')
json_button = driver.find_elements(By. CSS_SELECTOR, 'div div button')
json_button = json_button[5].click()

print('setting json area')
json_block = driver.find_elements(By. CLASS_NAME, 'rdmd-code')
json_block = json_block[3]
json_text = json_block.text
json_loads = json.loads(json_text)

print('checking json Response')
json_responce = json_loads['response']['job'][0]['processor']
print(json_responce)

if "AMAZON" and 'RACKSPACE' in json_responce:
    print('checking json responce is ok')

json_format = json_loads['response']['job'][0]['format'][0]['status']
print(json_format)

if 'Status' in json_format:
    print('checking json format is ok')






