import json
import requests

with open("kakao_code.json", "r") as fp:
    tokens = json.load(fp)

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '2b34c37f079d3908027968d4d2daed7b'
redirect_uri = 'https://www.naver.com'
authorize_code = 'gfCsI80nbWe9_4uMb2M0kBEMEnxmKyhiCFxxCCyRVUUMuwctP9aLnmdwMg_m4uEJwZ8uBgo9dGkAAAF-8agWfw'

data = {
    'grant_type':'refresh_token',
    'client_id':rest_api_key,
    'refresh_token':tokens['refresh_token']
    }

response = requests.post(url, data=data)
response.status_code



tokens['access_token'] = response.json()['access_token']
tokens['rest_api_key'] = rest_api_key


with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)
