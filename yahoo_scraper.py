import requests
from bs4 import BeautifulSoup

response = requests.get('https://tw.stock.yahoo.com/class-quote?sectorId=46&exchange=TAI')
soup = BeautifulSoup(response.text,'lxml')

date = soup.find('time').get('datatime') #用BeatifulSoup模組的find方法找到time標籤定位，再用get方法將屬性datatime的值取回
#用find_all方法是因為有很多列資料
rows = soup.find_all('div',{'class':'Bgc(#fff) table-row D(f) H(48px) Ai(c) Bgc(#e7f3ff):h Fz(16px) Px(12px) Bxz(bb) Bdbs(s) Bdbw(1px) Bdbc($bd-primary-divider)'})

result = []  #定義一個空串列，要儲存之後抓取的資料
for row in rows:
    company = row.find('div',{'class':'Lh(20px) Fw(600) Fz(16px) Ell'}).getText() #股票名稱
    #第一種寫法
    price = row.find_all('div',{'class':'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(68px)'})[0].getText()
    #另一種寫法
    #price = row.find('div',{'class':'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(68px)'}).getText()

    #由於需要用trend-up、trend-down字串判斷漲跌，所以處理程序為:先將抓回來的資料儲存成status_element，
    #再由status_element的資料內抓取span標籤下class屬性資料儲存成status_class變數，
    #再命名一個status變數標記漲跌幅判斷的結果，
    #判斷C($c-trend-down)是否有在屬性值裡面，若有則加上標記+status_element的值(用getText方法)
    status_element = row.find_all('div',{'class':'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(74px)'})[0]

    status_class = status_element.find('span').get('class')

    status =''  #用來標記漲跌幅判斷的結果
    if 'C($c-trend-down)' in status_class:
        status = '▼' + status_element.getText()
    elif 'C($c-trend-up)' in status_class:
        status = '▲' + status_element.getText()
    else:
        status = status_element.getText()
    #以下是漲跌幅%的漲跌幅判斷，邏輯與上面漲跌幅程式碼相同
    percentage_element = row.find_all('div',{'class':'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(74px)'})[1]

    percentage_class = percentage_element.find('span').get('class')

    percentage = ''#用來標記漲跌幅判斷的結果
    if 'C($c-trend-down)' in percentage_class:
        percentage = '▼' + percentage_element.getText()
    elif 'C($c-trend-up)' in percentage_class:
        percentage = '▲' + percentage_element.getText()
    else:
        percentage_element.getText()
    result.append([date,company,price,status,percentage])    #將抓取的資料新增至空串列中，且每個欄位分儲不同串列
    
print(result)