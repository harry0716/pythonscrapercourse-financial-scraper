import requests
import json

#以下用requests套件的get方法，請求要爬取的網址資料
response = requests.get(  
    'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&date=20220520&selectType=30&_=1653196653387')

#呼叫.json方法來進行資料解析
#print(response.json())會出現未經排版的資料。通常我們會回到開發者模式去檢視json的資料結構
print(response.json()['data']) 
