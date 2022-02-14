# from urllib.parse import quote_plus,unquote_plus  
# 한글 텍스트를 퍼센트 인코딩으로 변환
# import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally

import os
import time

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# # options.add_argument('window-size=1200x600')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome(options=options)

def scrolling():

    SCROLL_PAUSE_TIME = 0.7
    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        print('scrolling')
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            time.sleep(SCROLL_PAUSE_TIME)
            try:
                # status = browser.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').size()
                # print("click more image"+str(status))
                browser.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
            except:
                # status = browser.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').isDisplayed()
                # print(status)
                print('byebye')
                break
        else:
            last_height = new_height



def download(searchName):
    browser.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")
    elem = browser.find_element_by_name("q")
    # _input = input('What do you want to download ?')
    # searchName = _input
    print(f'{searchName} download start')
    print(elem)
    elem.send_keys(searchName) 
    elem.send_keys(Keys.RETURN)
    # html = browser.find_element_by_tag_name('html')
    # html.send_keys(Keys.END)

    # scrolling()


    images = browser.find_elements_by_css_selector('img.rg_i.Q4LuWd')
    
    print('number of images : ' + str(len(images)))

    try:
        # Create target Directory
        os.mkdir(searchName)
        print("Directory " , searchName ,  " Created ") 
    except FileExistsError:
        print("Directory " , searchName ,  " already exists")

    i = 1 #개수 카운터 
    for img in images:
        try:
            img.click()
            # imgadd = browser.find_elements_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img')
            imgadd = browser.find_elements_by_class_name('n3VNCb')
            print(imgadd)
            print(len(imgadd))
            src = imgadd[0].get_attribute('src')
            jsname = imgadd[0].get_attribute('jsname')
            print(jsname)
            print(src)
            alt = imgadd[0].get_attribute('alt')
            print(alt)

            ## Set up the image URL and filename
            filename = f'{searchName}/{i:03}.png'

            # Open the url image, set stream to True, this will return the stream content.
            r = requests.get(src, stream = True)
            # print(r.status_code)

            # Check if the image was retrieved successfully
            if r.status_code == 200:
                # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
                r.raw.decode_content = True
                # Open a local file with wb ( write binary ) permission.
                with open(filename,'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                print('Image sucessfully Downloaded: ',filename)
                i += 1
                if i == 5 : break
            else:
                print('Image Couldn\'t be retreived')

        except:
            print('download exception!')
            break
            pass

izonelist = ['아이즈원 김민주','아이즈원 권은비','아이즈원 사쿠라', '아이즈원 강혜원', '아이즈원 최예나', '아이즈원 이채연', '아이즈원 김채원', '아이즈원 나코', '아이즈원 히토미', '아이즈원 조유리', '아이즈원 안유진', '아이즈원 장원영']
rvlist =['레드벨벳 슬기', '레드벨벳 아이린', '레드벨벳 웬디', '레드벨벳 조이', '레드벨벳 예리']
itzylist=['있지 예지', '있지 리아', '있지 류진', '있지 유나']
bplist=['블랙핑크 지수', '블랙핑크 로제','블랙핑크 리사', '블랙핑크 제니'] 

for name in ["아이린"]:
    download(name)

browser.close()
