import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '2b34c37f079d3908027968d4d2daed7b'
redirect_uri = 'https://www.naver.com'
authorize_code = 'gfCsI80nbWe9_4uMb2M0kBEMEnxmKyhiCFxxCCyRVUUMuwctP9aLnmdwMg_m4uEJwZ8uBgo9dGkAAAF-8agWfw'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json

with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)