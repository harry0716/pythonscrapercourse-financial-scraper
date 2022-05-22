import requests
import json

response = requests.get('https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&date=20220520&selectType=30&_=1653196653387')
print(response.json()['data'])