import urllib.request
import urllib.parse
from urllib import parse
from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import time


now = datetime.datetime.now()
nowDate = now.strftime('%Y년 %m월 %d일 %H시 %M분 %S초')

###############################

data=[]
print('--------------파워링크 크롤링 -----------------------')

keyword = input("검색어를 입력하세요 : ")
keywordchange = parse.quote(keyword)
page = urllib.request.urlopen('https://m.search.naver.com/search.naver?sm=msv_hty&where=m&ie=utf8&query='+keywordchange)
soup = BeautifulSoup(page, 'html.parser')

items = soup.select(".tit_area")
for e, item in enumerate(items,1):
    data.append([nowDate,keyword, e, item.text])


result = pd.DataFrame(data, columns=["time","keyword","rank","title"])
ans = result.loc[result.title.str.contains('스타 법무법인')|result.title.str.contains('리본회생파산')|result.title.str.contains('리본이혼')]


######################################

data1=[]
print('------------------------------1페이지 크롤링-----------------------------------------')

keyword = input("검색어를 입력하세요 : ")
keywordchange = parse.quote(keyword)

count=1

tema='power link'
url = f'https://m.search.naver.com/search.naver?sm=msv_hty&where=m&ie=utf8&query='+keywordchange
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
items = soup.select(".tit_area")
for e, item in enumerate(items,1):
    data1.append([keyword,tema,count, e, item.text])

tema='view'
url = f'https://m.search.naver.com/search.naver?sm=msv_hty&where=m&ie=utf8&query='+keywordchange
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
items = soup.find_all(class_="api_txt_lines total_tit _cross_trigger")
for e, item in enumerate(items,1):
    data1.append([keyword,tema,count, e, item.text])
    
tema='place'
url = f'https://m.search.naver.com/search.naver?sm=msv_hty&where=m&ie=utf8&query='+keywordchange
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
items = soup.find_all(class_="place_bluelink YwYLL")
for e, item in enumerate(items,1):
    data1.append([keyword,tema,count, e, item.text])
    
tema='지식in'
url = f'https://m.search.naver.com/search.naver?sm=msv_hty&where=m&ie=utf8&query='+keywordchange
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
items = soup.find_all(class_="api_txt_lines question_text")
for e, item in enumerate(items,1):
    data1.append([keyword,tema,count, e, item.text])
    
tema='news'
url = f'https://m.search.naver.com/search.naver?sm=msv_hty&where=m&ie=utf8&query='+keywordchange
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
items = soup.find_all(class_="link_tit")
for e, item in enumerate(items,1):
    data1.append([keyword,tema,count, e, item.text])


result1 = pd.DataFrame(data1, columns=["keyword","tema","page","순위","title"])
ans1 = result1.loc[result1.title.str.contains('스타 법무법인')|result1.title.str.contains('리본회생파산')|result1.title.str.contains('리본이혼')]

#########################################

data2=[]

print('----------------------------2~10페이지 크롤링 결과입니다-------------------------------------')

keyword = input("검색어를 입력하세요 : ")
keywordchange = parse.quote(keyword)
pageNum=2
count=2
for i in range(1,130,15): 
    url =f'https://m.search.naver.com/search.naver?page={pageNum}&query={keywordchange}&sm=mtb_pge&start={i}&where=m_web'
    
    html = urllib.request.urlopen(url).read()
    soup= BeautifulSoup(html, 'html.parser')
    
    title = soup.find_all(class_='link_tit')
    
    print(f'-----{count}페이지 결과입니다.----')
    for e, i in enumerate(title,1):
        print(f"{e} : {i.text}")
        print(i.attrs['href'])
        data2.append([keyword,count,e,i.text,i.attrs['href']])
    print()    
    pageNum = pageNum+1
    count = count+1


result2 = pd.DataFrame(data2, columns=["keyword","page","rank","title","link"])
ans2 = result2.loc[result2.title.str.contains('스타 법무법인')|result2.title.str.contains('리본회생파산')|result2.title.str.contains('리본이혼')]