import time

from selenium import webdriver



options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# # options.add_argument('window-size=1200x600')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get('https://finance.yahoo.com/quote/BA?p=BA&.tsrc=fin-srch');

time.sleep(1) # Let the user actually see something!

# search_box = driver.find_element_by_name('q')

# search_box.send_keys('ChromeDriver')

# search_box.submit()


# 현재가 
# elem = driver.find_element_by_xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[1]/span')

elem = driver.find_element_by_xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]')


after_elem = driver.find_element_by_xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div[2]/fin-streamer[2]')




print(elem)
# src = elem.get_attribute('href')
currentPrice = elem.text
afterPrice = after_elem.text
print('currentPrice:',currentPrice)
print('afterPrice:',afterPrice)

# time.sleep(3) # Let the user actually see something!

driver.quit()