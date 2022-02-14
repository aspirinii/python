import time
from tokenize import Double
from selenium import webdriver
import requests
import json



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



with open("kakao_code.json","r") as fp:
    tokens = json.load(fp)

url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

# kapi.kakao.com/v2/api/talk/memo/default/send 

headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}
ticker = "BA"
criticalLevel = 200
messege_text = f"over{criticalLevel}. {ticker} current Price{currentPrice}"

data={
    "template_object": json.dumps({
        "object_type": "text",
        "text": messege_text,
        "link": {
            "web_url" : "헤헤. text와 link 객체는 필수로 넣어야 하는 거구나? button_title과 buttons는 안 넣어도 상관 없지만 말이야!",
            "mobile_web_url" : "헤헤. text와 link 객체는 필수로 넣어야 하는 거구나? button_title과 buttons는 안 넣어도 상관 없지만 말이야!",
        },
        "button_title" : "Saturday News"
    })
}



if float(currentPrice) > criticalLevel :
    response = requests.post(url, headers=headers, data=data)
    response.status_code
    print(f'sent message over{criticalLevel}. {ticker} current Price{currentPrice}')
else :
    print('not over',criticalLevel)

# working  Feb 12 2022