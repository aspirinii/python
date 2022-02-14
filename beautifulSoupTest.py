import requests
from bs4 import BeautifulSoup

ticker = 'TSLA'

# url = f'https://finance.yahoo.com/quote/TSLA?p=TSLA'
url = f'https://finance.yahoo.com/quote/{ticker}?p={ticker}'

# 몇번시도하니 이제 안준다 ??


response = requests.get(url)
response.raise_for_status()
html = response.text
soup = BeautifulSoup(html, 'lxml')

currentPrice = soup.find('fin-streamer', {'data-symbol':ticker,'data-field':'regularMarketPrice'})

PostPrice = soup.find('fin-streamer', {'data-symbol':ticker,'data-field':'postMarketPrice'})
pretty = soup.prettify()

with open(f"{ticker}Price.txt", "w+") as file:
    file.write(pretty)
file.close

#구글만 이상한페이지가 리턴된다

# print(soup)
print(currentPrice)
print(currentPrice.text)

print(PostPrice)
print(PostPrice.text)

