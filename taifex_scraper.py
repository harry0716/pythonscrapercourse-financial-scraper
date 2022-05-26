import requests
import json

url = 'https://mis.taifex.com.tw/futures/api/getQuoteList' #要抓取資料的網頁URL

#因為使用的是POST方法，所以必須回到"開發者模式"的Payload下的 view source將參數複製
payload = {
    "MarketType":"0",
    "SymbolType":"F",
    "KindID":"1",
    "CID":"TXF",
    "ExpireMonth":"",
    "RowSize":"全部",
    "PageNo":"",
    "SortColumn":"",
    "AscDesc":"A"
}

headers = {
    'content-type':'application/json',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
}

response =  requests.post(url,data = json.dumps(payload),headers = headers)
#json模組的dumps方法，來把json格式參數序列化
print(response.json()['RtData']['QuoteList'][1])