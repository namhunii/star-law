import os
import sys
import urllib.request
import pandas as pd
import json
from datetime import datetime, timedelta

target_dt = '20221130'
data=[]

for i in range(31):
    new_date = datetime.strptime(target_dt, '%Y%m%d') + timedelta(days = i + 1)
    data.append(new_date.strftime('%y-%m-%d'))
    
date=data

##################################

print("-----------통합검색 카테고리1~3 비교 -------------------- ")

client_id = input("id를 입력하세요 : ") 
client_secret = input("비밀번호를 입력하세요 : ")
url = "https://openapi.naver.com/v1/datalab/search"
body = "{\"startDate\":\"2022-12-01\",\"endDate\":\"2022-12-31\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"회생\",\"keywords\":[\"개인회생\",\"대구개인회생\",\"대구개인회생전문\",\"개인회생신청자격\",\"개인회생전문\"]},{\"groupName\":\"이혼\",\"keywords\":[\"대구이혼변호사\",\"대구이혼전문변호사\",\"대구이혼상담\",\"이혼전문변호사\",\"이혼변호사\"]},{\"groupName\":\"음주\",\"keywords\":[\"음주운전\",\"음주행정\",\"음주형사\",\"대구음주운전전문\",\"음주운전변호사\"]}]}";
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_data=response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
    
result = json.loads(response_data)

ratio_data1=[a['ratio'] for a in result['results'][0]['data']]
ratio_data2=[a['ratio'] for a in result['results'][1]['data']]
ratio_data3=[a['ratio'] for a in result['results'][2]['data']]

a= pd.DataFrame({'date':date,
        '회생':ratio_data1,
        '이혼':ratio_data2,
        '음주':ratio_data3})


###########################

print("-----------PC검색 카테고리1~3 비교 -------------------- ")

client_id = input("id를 입력하세요 : ") 
client_secret = input("비밀번호를 입력하세요 : ") 
url = "https://openapi.naver.com/v1/datalab/search"
body = "{\"startDate\":\"2022-12-01\",\"endDate\":\"2022-12-31\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"회생\",\"keywords\":[\"개인회생\",\"대구개인회생\",\"대구개인회생전문\",\"개인회생신청자격\",\"개인회생전문\"]},{\"groupName\":\"이혼\",\"keywords\":[\"대구이혼변호사\",\"대구이혼전문변호사\",\"대구이혼상담\",\"이혼전문변호사\",\"이혼변호사\"]},{\"groupName\":\"음주\",\"keywords\":[\"음주운전\",\"음주행정\",\"음주형사\",\"대구음주운전전문\",\"음주운전변호사\"]}],\"device\":\"pc\"}";
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_data=response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
    
result = json.loads(response_data)

ratio_data1=[a['ratio'] for a in result['results'][0]['data']]
ratio_data2=[a['ratio'] for a in result['results'][1]['data']]
ratio_data3=[a['ratio'] for a in result['results'][2]['data']]

a= pd.DataFrame({'date':date,
        '회생':ratio_data1,
        '이혼':ratio_data2,
        '음주':ratio_data3})


#########################

print("-----------Mobile검색 카테고리1~3 비교 -------------------- ")

client_id = input("id를 입력하세요 : ") 
client_secret = input("비밀번호를 입력하세요 : ") 
url = "https://openapi.naver.com/v1/datalab/search"
body = "{\"startDate\":\"2022-12-01\",\"endDate\":\"2022-12-31\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"회생\",\"keywords\":[\"개인회생\",\"대구개인회생\",\"대구개인회생전문\",\"개인회생신청자격\",\"개인회생전문\"]},{\"groupName\":\"이혼\",\"keywords\":[\"대구이혼변호사\",\"대구이혼전문변호사\",\"대구이혼상담\",\"이혼전문변호사\",\"이혼변호사\"]},{\"groupName\":\"음주\",\"keywords\":[\"음주운전\",\"음주행정\",\"음주형사\",\"대구음주운전전문\",\"음주운전변호사\"]}],\"device\":\"mo\"}";
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_data=response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
    
result = json.loads(response_data)

ratio_data1=[a['ratio'] for a in result['results'][0]['data']]
ratio_data2=[a['ratio'] for a in result['results'][1]['data']]
ratio_data3=[a['ratio'] for a in result['results'][2]['data']]

a= pd.DataFrame({'date':date,
        '회생':ratio_data1,
        '이혼':ratio_data2,
        '음주':ratio_data3})


#################################

print("-----------통합검색 회생 카테고리 비교 -------------------- ")

client_id = input("id를 입력하세요 : ") 
client_secret = input("비밀번호를 입력하세요 : ") 
url = "https://openapi.naver.com/v1/datalab/search"
body = "{\"startDate\":\"2022-12-01\",\"endDate\":\"2022-12-31\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"개인회생\",\"keywords\":[\"개인회생\"]},{\"groupName\":\"대구개인회생\",\"keywords\":[\"대구개인회생\"]},{\"groupName\":\"대구개인회생전문\",\"keywords\":[\"대구개인회생전문\"]},{\"groupName\":\"개인회생신청자격\",\"keywords\":[\"개인회생신청자격\"]},{\"groupName\":\"개인회생전문\",\"keywords\":[\"개인회생전문\"]}]}";
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_data=response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
    
result = json.loads(response_data)

date1=[a['period'] for a in result['results'][0]['data']]
date2=[a['period'] for a in result['results'][1]['data']]
date3=[a['period'] for a in result['results'][2]['data']]
date4=[a['period'] for a in result['results'][3]['data']]
date5=[a['period'] for a in result['results'][4]['data']]


ratio_data1=[a['ratio'] for a in result['results'][0]['data']]
ratio_data2=[a['ratio'] for a in result['results'][1]['data']]
ratio_data3=[a['ratio'] for a in result['results'][2]['data']]
ratio_data4=[a['ratio'] for a in result['results'][3]['data']]
ratio_data5=[a['ratio'] for a in result['results'][4]['data']]

a=pd.DataFrame({'date':date1,
               '개인회생':ratio_data1})

b=pd.DataFrame({'date':date2,
               '대구개인회생':ratio_data2})

c=pd.DataFrame({'date':date3,
               '대구개인회생전문':ratio_data3})

d=pd.DataFrame({'date':date4,
               '개인회생신청자격':ratio_data4})

e=pd.DataFrame({'date':date5,
               '개인회생전문':ratio_data5})


merge_outer1=pd.merge(a,b, how='outer', on='date')
merge_outer2=pd.merge(c,d, how='outer', on='date')
merge_outer3=pd.merge(merge_outer1,merge_outer2, how='outer', on='date')
total=pd.merge(merge_outer3,e, how='outer', on='date')


################################

print("-----------통합검색 이혼 카테고리 비교 -------------------- ")

client_id = input("id를 입력하세요 : ") 
client_secret = input("비밀번호를 입력하세요 : ") 
url = "https://openapi.naver.com/v1/datalab/search"
body = "{\"startDate\":\"2022-12-01\",\"endDate\":\"2022-12-31\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"대구이혼변호사\",\"keywords\":[\"대구이혼변호사\"]},{\"groupName\":\"대구이혼전문변호사\",\"keywords\":[\"대구이혼전문변호사\"]},{\"groupName\":\"대구이혼상담\",\"keywords\":[\"대구이혼상담\"]},{\"groupName\":\"이혼전문변호사\",\"keywords\":[\"이혼전문변호사\"]},{\"groupName\":\"이혼변호사\",\"keywords\":[\"이혼변호사\"]}]}";
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_data=response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
    
result = json.loads(response_data)

date6=[a['period'] for a in result['results'][0]['data']]
date7=[a['period'] for a in result['results'][1]['data']]
date8=[a['period'] for a in result['results'][2]['data']]
date9=[a['period'] for a in result['results'][3]['data']]
date10=[a['period'] for a in result['results'][4]['data']]


ratio_data6=[a['ratio'] for a in result['results'][0]['data']]
ratio_data7=[a['ratio'] for a in result['results'][1]['data']]
ratio_data8=[a['ratio'] for a in result['results'][2]['data']]
ratio_data9=[a['ratio'] for a in result['results'][3]['data']]
ratio_data10=[a['ratio'] for a in result['results'][4]['data']]

a1=pd.DataFrame({'date':date6,
               '대구이혼변호사':ratio_data6})

b1=pd.DataFrame({'date':date7,
               '대구이혼전문변호사':ratio_data7})

c1=pd.DataFrame({'date':date8,
               '대구이혼상담':ratio_data8})

d1=pd.DataFrame({'date':date9,
               '이혼전문변호사':ratio_data9})

e1=pd.DataFrame({'date':date10,
               '이혼변호사':ratio_data10})

merge_outer11=pd.merge(a1,b1, how='outer', on='date')
merge_outer22=pd.merge(c1,d1, how='outer', on='date')
merge_outer33=pd.merge(merge_outer11,merge_outer22, how='outer', on='date')
total1=pd.merge(merge_outer33,e1, how='outer', on='date')


###############################


print("-----------통합검색 음주 카테고리 비교 -------------------- ")

client_id = input("id를 입력하세요 : ") 
client_secret = input("비밀번호를 입력하세요 : ") 
url = "https://openapi.naver.com/v1/datalab/search"
body = "{\"startDate\":\"2022-12-01\",\"endDate\":\"2022-12-31\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"음주운전\",\"keywords\":[\"음주운전\"]},{\"groupName\":\"음주행정\",\"keywords\":[\"음주행정\"]},{\"groupName\":\"음주형사\",\"keywords\":[\"음주형사\"]},{\"groupName\":\"대구음주운전전문\",\"keywords\":[\"대구음주운전전문\"]},{\"groupName\":\"음주운전변호사\",\"keywords\":[\"음주운전변호사\"]}]}";
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_data=response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
    
result = json.loads(response_data)

date11=[a['period'] for a in result['results'][0]['data']]
date22=[a['period'] for a in result['results'][1]['data']]
date33=[a['period'] for a in result['results'][2]['data']]
date44=[a['period'] for a in result['results'][3]['data']]
date55=[a['period'] for a in result['results'][4]['data']]


ratio_data11=[a['ratio'] for a in result['results'][0]['data']]
ratio_data22=[a['ratio'] for a in result['results'][1]['data']]
ratio_data33=[a['ratio'] for a in result['results'][2]['data']]
ratio_data44=[a['ratio'] for a in result['results'][3]['data']]
ratio_data55=[a['ratio'] for a in result['results'][4]['data']]

a2=pd.DataFrame({'date':date11,
               '음주운전':ratio_data11})

b2=pd.DataFrame({'date':date22,
               '음주행정':ratio_data22})

c2=pd.DataFrame({'date':date33,
               '음주형사':ratio_data33})

d2=pd.DataFrame({'date':date44,
               '대구음주운전전문':ratio_data44})

e2=pd.DataFrame({'date':date55,
               '음주운전변호사':ratio_data55})

merge_outer111=pd.merge(a2,b2, how='outer', on='date')
merge_outer222=pd.merge(c2,d2, how='outer', on='date')
merge_outer333=pd.merge(merge_outer111,merge_outer222, how='outer', on='date')
total2=pd.merge(merge_outer333,e2, how='outer', on='date')

##############################

merge_01=pd.merge(total,total1, how='outer', on='date')
total012=pd.merge(merge_01,total2, how='outer', on='date')


print("---------------통합검색 모든 카테고리 안에서 각 키워드가 차지하는 비율------------------")
total012=total012.fillna(0)
total012['합계']=total012['개인회생']+total012['대구개인회생']+total012['대구개인회생전문']+total012['개인회생신청자격']+total012['개인회생전문']+total012['대구이혼변호사']+total012['대구이혼전문변호사']+total012['대구이혼상담']+total012['이혼전문변호사']+total012['이혼변호사']+total012['음주운전']+total012['음주행정']+total012['음주형사']+total012['대구음주운전전문']+total012['음주운전변호사']

### 회생 비율 구하기
total012['개인회생비율']=(total012['개인회생']/total012['합계'])*100
total012['대구개인회생비율']=(total012['대구개인회생']/total012['합계'])*100
total012['대구개인회생전문비율']=(total012['대구개인회생전문']/total012['합계'])*100
total012['개인회생신청자격비율']=(total012['개인회생신청자격']/total012['합계'])*100
total012['개인회생전문비율']=(total012['개인회생전문']/total012['합계'])*100

#### 이혼 비율 구하기
total012['대구이혼변호사비율']=(total012['대구이혼변호사']/total012['합계'])*100
total012['대구이혼전문변호사비율']=(total012['대구이혼전문변호사']/total012['합계'])*100
total012['대구이혼상담비율']=(total012['대구이혼상담']/total012['합계'])*100
total012['이혼전문변호사비율']=(total012['이혼전문변호사']/total012['합계'])*100
total012['이혼변호사비율']=(total012['이혼변호사']/total012['합계'])*100

#### 음주 비율 구하기
total012['음주운전비율']=(total012['음주운전']/total012['합계'])*100
total012['음주행정비율']=(total012['음주행정']/total012['합계'])*100
total012['음주형사비율']=(total012['음주형사']/total012['합계'])*100
total012['대구음주운전전문비율']=(total012['대구음주운전전문']/total012['합계'])*100
total012['음주운전변호사비율']=(total012['음주운전변호사']/total012['합계'])*100

######################

print("---------------통합검색 회생 카테고리 안에서 각 키워드가 차지하는 비율------------------")
total=total.fillna(0)
total['합계']=total['개인회생']+total['대구개인회생']+total['대구개인회생전문']+total['개인회생신청자격']+total['개인회생전문']
total['개인회생비율']=(total['개인회생']/total['합계'])*100
total['대구개인회생비율']=(total['대구개인회생']/total['합계'])*100
total['대구개인회생전문비율']=(total['대구개인회생전문']/total['합계'])*100
total['개인회생신청자격비율']=(total['개인회생신청자격']/total['합계'])*100
total['개인회생전문비율']=(total['개인회생전문']/total['합계'])*100

#######################

print("---------------통합검색 이혼 카테고리 안에서 각 키워드가 차지하는 비율------------------")
total1=total1.fillna(0)
total1['합계']=total1['대구이혼변호사']+total1['대구이혼전문변호사']+total1['대구이혼상담']+total1['이혼전문변호사']+total1['이혼변호사']
total1['대구이혼변호사비율']=(total1['대구이혼변호사']/total1['합계'])*100
total1['대구이혼전문변호사비율']=(total1['대구이혼전문변호사']/total1['합계'])*100
total1['대구이혼상담비율']=(total1['대구이혼상담']/total1['합계'])*100
total1['이혼전문변호사비율']=(total1['이혼전문변호사']/total1['합계'])*100
total1['이혼변호사비율']=(total1['이혼변호사']/total1['합계'])*100

########################

print("---------------통합검색 음주 카테고리 안에서 각 키워드가 차지하는 비율------------------")
total2=total2.fillna(0)
total2['합계']=total2['음주운전']+total2['음주행정']+total2['음주형사']+total2['대구음주운전전문']+total2['음주운전변호사']
total2['음주운전비율']=(total2['음주운전']/total2['합계'])*100
total2['음주행정비율']=(total2['음주행정']/total2['합계'])*100
total2['음주형사비율']=(total2['음주형사']/total2['합계'])*100
total2['대구음주운전전문비율']=(total2['대구음주운전전문']/total2['합계'])*100
total2['음주운전변호사비율']=(total2['음주운전변호사']/total2['합계'])*100

############################

print("---------- PC 검색 회생 카테고리 비교 -------------------- ")

client_id = input("id를 입력하세요 : ") 
client_secret = input("비밀번호를 입력하세요 : ") 
url = "https://openapi.naver.com/v1/datalab/search"
body = "{\"startDate\":\"2022-12-01\",\"endDate\":\"2022-12-31\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"개인회생\",\"keywords\":[\"개인회생\"]},{\"groupName\":\"대구개인회생\",\"keywords\":[\"대구개인회생\"]},{\"groupName\":\"대구개인회생전문\",\"keywords\":[\"대구개인회생전문\"]},{\"groupName\":\"개인회생신청자격\",\"keywords\":[\"개인회생신청자격\"]},{\"groupName\":\"개인회생전문\",\"keywords\":[\"개인회생전문\"]}],\"device\":\"pc\"}";
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_data=response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
    
result = json.loads(response_data)

date1p=[a['period'] for a in result['results'][0]['data']]
date2p=[a['period'] for a in result['results'][1]['data']]
date3p=[a['period'] for a in result['results'][2]['data']]
date4p=[a['period'] for a in result['results'][3]['data']]
date5p=[a['period'] for a in result['results'][4]['data']]

ratio_data1p=[a['ratio'] for a in result['results'][0]['data']]
ratio_data2p=[a['ratio'] for a in result['results'][1]['data']]
ratio_data3p=[a['ratio'] for a in result['results'][2]['data']]
ratio_data4p=[a['ratio'] for a in result['results'][3]['data']]
ratio_data5p=[a['ratio'] for a in result['results'][4]['data']]


ap=pd.DataFrame({'date':date1p,
               '개인회생':ratio_data1p})

bp=pd.DataFrame({'date':date2p,
               '대구개인회생':ratio_data2p})

cp=pd.DataFrame({'date':date3p,
               '대구개인회생전문':ratio_data3p})

dp=pd.DataFrame({'date':date4p,
               '개인회생신청자격':ratio_data4p})

ep=pd.DataFrame({'date':date5p,
               '개인회생전문':ratio_data5p})


merge_outer1p=pd.merge(ap,bp, how='outer', on='date')
merge_outer2p=pd.merge(cp,dp, how='outer', on='date')
merge_outer3p=pd.merge(merge_outer1p,merge_outer2p, how='outer', on='date')
totalp=pd.merge(merge_outer3p,ep, how='outer', on='date')

##############################

print("-----------PC검색 이혼 카테고리 비교 -------------------- ")

client_id = input("id를 입력하세요 : ") 
client_secret = input("비밀번호를 입력하세요 : ") 
url = "https://openapi.naver.com/v1/datalab/search"
body = "{\"startDate\":\"2022-12-01\",\"endDate\":\"2022-12-31\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"대구이혼변호사\",\"keywords\":[\"대구이혼변호사\"]},{\"groupName\":\"대구이혼전문변호사\",\"keywords\":[\"대구이혼전문변호사\"]},{\"groupName\":\"대구이혼상담\",\"keywords\":[\"대구이혼상담\"]},{\"groupName\":\"이혼전문변호사\",\"keywords\":[\"이혼전문변호사\"]},{\"groupName\":\"이혼변호사\",\"keywords\":[\"이혼변호사\"]}],\"device\":\"pc\"}";
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_data=response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
    
result = json.loads(response_data)

date11p=[a['period'] for a in result['results'][0]['data']]
date22p=[a['period'] for a in result['results'][1]['data']]
date33p=[a['period'] for a in result['results'][2]['data']]
date44p=[a['period'] for a in result['results'][3]['data']]
date55p=[a['period'] for a in result['results'][4]['data']]


ratio_data11p=[a['ratio'] for a in result['results'][0]['data']]
ratio_data22p=[a['ratio'] for a in result['results'][1]['data']]
ratio_data33p=[a['ratio'] for a in result['results'][2]['data']]
ratio_data44p=[a['ratio'] for a in result['results'][3]['data']]
ratio_data55p=[a['ratio'] for a in result['results'][4]['data']]

ap1=pd.DataFrame({'date':date11p,
               '대구이혼변호사':ratio_data11p})

bp1=pd.DataFrame({'date':date22p,
               '대구이혼전문변호사':ratio_data22p})

cp1=pd.DataFrame({'date':date33p,
               '대구이혼상담':ratio_data33p})

dp1=pd.DataFrame({'date':date44p,
               '이혼전문변호사':ratio_data44p})

ep1=pd.DataFrame({'date':date55p,
               '이혼변호사':ratio_data55p})

merge_outer11p=pd.merge(ap1,bp1, how='outer', on='date')
merge_outer22p=pd.merge(cp1,dp1, how='outer', on='date')
merge_outer33p=pd.merge(merge_outer11p,merge_outer22p, how='outer', on='date')
totalp1=pd.merge(merge_outer33p,ep1, how='outer', on='date')

###########################

print("-----------PC 검색 음주 카테고리 비교 -------------------- ")

client_id = input("id를 입력하세요 : ") 
client_secret = input("비밀번호를 입력하세요 : ") 
url = "https://openapi.naver.com/v1/datalab/search"
body = "{\"startDate\":\"2022-12-01\",\"endDate\":\"2022-12-31\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"음주운전\",\"keywords\":[\"음주운전\"]},{\"groupName\":\"음주행정\",\"keywords\":[\"음주행정\"]},{\"groupName\":\"음주형사\",\"keywords\":[\"음주형사\"]},{\"groupName\":\"대구음주운전전문\",\"keywords\":[\"대구음주운전전문\"]},{\"groupName\":\"음주운전변호사\",\"keywords\":[\"음주운전변호사\"]}],\"device\":\"pc\"}";
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_data=response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
    
result = json.loads(response_data)

date111p=[a['period'] for a in result['results'][0]['data']]
date222p=[a['period'] for a in result['results'][1]['data']]
date333p=[a['period'] for a in result['results'][2]['data']]
date444p=[a['period'] for a in result['results'][3]['data']]
date555p=[a['period'] for a in result['results'][4]['data']]


ratio_data111p=[a['ratio'] for a in result['results'][0]['data']]
ratio_data222p=[a['ratio'] for a in result['results'][1]['data']]
ratio_data333p=[a['ratio'] for a in result['results'][2]['data']]
ratio_data444p=[a['ratio'] for a in result['results'][3]['data']]
ratio_data555p=[a['ratio'] for a in result['results'][4]['data']]

ap2=pd.DataFrame({'date':date111p,
               '음주운전':ratio_data111p})

bp2=pd.DataFrame({'date':date222p,
               '음주행정':ratio_data222p})

cp2=pd.DataFrame({'date':date333p,
               '음주형사':ratio_data333p})

dp2=pd.DataFrame({'date':date444p,
               '대구음주운전전문':ratio_data444p})

ep2=pd.DataFrame({'date':date555p,
               '음주운전변호사':ratio_data555p})

merge_outer111p=pd.merge(ap2,bp2, how='outer', on='date')
merge_outer222p=pd.merge(cp2,dp2, how='outer', on='date')
merge_outer333p=pd.merge(merge_outer111p,merge_outer222p, how='outer', on='date')
totalp2=pd.merge(merge_outer333p,ep2, how='outer', on='date')

#############################

merge_01p=pd.merge(totalp,totalp1, how='outer', on='date')
total012p=pd.merge(merge_01p,totalp2, how='outer', on='date')

print("---------------PC검색 모든 카테고리 안에서 각 키워드가 차지하는 비율------------------")
total012p=total012p.fillna(0)
total012p['합계']=total012p['개인회생']+total012p['대구개인회생']+total012p['대구개인회생전문']+total012p['개인회생신청자격']+total012p['개인회생전문']+total012p['대구이혼변호사']+total012p['대구이혼전문변호사']+total012p['대구이혼상담']+total012p['이혼전문변호사']+total012p['이혼변호사']+total012p['음주운전']+total012p['음주행정']+total012p['음주형사']+total012p['대구음주운전전문']+total012p['음주운전변호사']

### 회생 비율 구하기
total012p['개인회생비율']=(total012p['개인회생']/total012p['합계'])*100
total012p['대구개인회생비율']=(total012p['대구개인회생']/total012p['합계'])*100
total012p['대구개인회생전문비율']=(total012p['대구개인회생전문']/total012p['합계'])*100
total012p['개인회생신청자격비율']=(total012p['개인회생신청자격']/total012p['합계'])*100
total012p['개인회생전문비율']=(total012p['개인회생전문']/total012p['합계'])*100

#### 이혼 비율 구하기
total012p['대구이혼변호사비율']=(total012p['대구이혼변호사']/total012p['합계'])*100
total012p['대구이혼전문변호사비율']=(total012p['대구이혼전문변호사']/total012p['합계'])*100
total012p['대구이혼상담비율']=(total012p['대구이혼상담']/total012p['합계'])*100
total012p['이혼전문변호사비율']=(total012p['이혼전문변호사']/total012p['합계'])*100
total012p['이혼변호사비율']=(total012p['이혼변호사']/total012p['합계'])*100

#### 음주 비율 구하기
total012p['음주운전비율']=(total012p['음주운전']/total012p['합계'])*100
total012p['음주행정비율']=(total012p['음주행정']/total012p['합계'])*100
total012p['음주형사비율']=(total012p['음주형사']/total012p['합계'])*100
total012p['대구음주운전전문비율']=(total012p['대구음주운전전문']/total012p['합계'])*100
total012p['음주운전변호사비율']=(total012p['음주운전변호사']/total012p['합계'])*100


##########################

print("---------------PC검색 회생 카테고리 안에서 각 키워드가 차지하는 비율------------------")
totalp=totalp.fillna(0)
totalp['합계']=totalp['개인회생']+totalp['대구개인회생']+totalp['대구개인회생전문']+totalp['개인회생신청자격']+totalp['개인회생전문']
totalp['개인회생비율']=(totalp['개인회생']/totalp['합계'])*100
totalp['대구개인회생비율']=(totalp['대구개인회생']/totalp['합계'])*100
totalp['대구개인회생전문비율']=(totalp['대구개인회생전문']/totalp['합계'])*100
totalp['개인회생신청자격비율']=(totalp['개인회생신청자격']/totalp['합계'])*100
totalp['개인회생전문비율']=(totalp['개인회생전문']/totalp['합계'])*100


##########################

print("---------------PC검색 이혼 카테고리 안에서 각 키워드가 차지하는 비율------------------")
totalp1=totalp1.fillna(0)
totalp1['합계']=totalp1['대구이혼변호사']+totalp1['대구이혼전문변호사']+totalp1['대구이혼상담']+totalp1['이혼전문변호사']+total1['이혼변호사']
totalp1['대구이혼변호사비율']=(totalp1['대구이혼변호사']/totalp1['합계'])*100
totalp1['대구이혼전문변호사비율']=(totalp1['대구이혼전문변호사']/totalp1['합계'])*100
totalp1['대구이혼상담비율']=(totalp1['대구이혼상담']/totalp1['합계'])*100
totalp1['이혼전문변호사비율']=(totalp1['이혼전문변호사']/totalp1['합계'])*100
totalp1['이혼변호사비율']=(totalp1['이혼변호사']/totalp1['합계'])*100


##############################

print("---------------PC검색 음주 카테고리 안에서 각 키워드가 차지하는 비율------------------")
totalp2=totalp2.fillna(0)
totalp2['합계']=totalp2['음주운전']+totalp2['음주행정']+totalp2['음주형사']+totalp2['대구음주운전전문']+totalp2['음주운전변호사']
totalp2['음주운전비율']=(totalp2['음주운전']/totalp2['합계'])*100
totalp2['음주행정비율']=(totalp2['음주행정']/totalp2['합계'])*100
totalp2['음주형사비율']=(totalp2['음주형사']/totalp2['합계'])*100
totalp2['대구음주운전전문비율']=(totalp2['대구음주운전전문']/totalp2['합계'])*100
totalp2['음주운전변호사비율']=(totalp2['음주운전변호사']/totalp2['합계'])*100


##########################################


print("-----------Mobile 검색 회생 카테고리 비교 -------------------- ")

client_id = input("id를 입력하세요 : ") 
client_secret = input("비밀번호를 입력하세요 : ") 
url = "https://openapi.naver.com/v1/datalab/search"
body = "{\"startDate\":\"2022-12-01\",\"endDate\":\"2022-12-31\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"개인회생\",\"keywords\":[\"개인회생\"]},{\"groupName\":\"대구개인회생\",\"keywords\":[\"대구개인회생\"]},{\"groupName\":\"대구개인회생전문\",\"keywords\":[\"대구개인회생전문\"]},{\"groupName\":\"개인회생신청자격\",\"keywords\":[\"개인회생신청자격\"]},{\"groupName\":\"개인회생전문\",\"keywords\":[\"개인회생전문\"]}],\"device\":\"mo\"}";
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_data=response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
    
result = json.loads(response_data)

date1m=[a['period'] for a in result['results'][0]['data']]
date2m=[a['period'] for a in result['results'][1]['data']]
date3m=[a['period'] for a in result['results'][2]['data']]
date4m=[a['period'] for a in result['results'][3]['data']]
date5m=[a['period'] for a in result['results'][4]['data']]


ratio_data1m=[a['ratio'] for a in result['results'][0]['data']]
ratio_data2m=[a['ratio'] for a in result['results'][1]['data']]
ratio_data3m=[a['ratio'] for a in result['results'][2]['data']]
ratio_data4m=[a['ratio'] for a in result['results'][3]['data']]
ratio_data5m=[a['ratio'] for a in result['results'][4]['data']]

am=pd.DataFrame({'date':date1m,
               '개인회생':ratio_data1m})

bm=pd.DataFrame({'date':date2m,
               '대구개인회생':ratio_data2m})

cm=pd.DataFrame({'date':date3m,
               '대구개인회생전문':ratio_data3m})

dm=pd.DataFrame({'date':date4m,
               '개인회생신청자격':ratio_data4m})

em=pd.DataFrame({'date':date5m,
               '개인회생전문':ratio_data5m})

merge_outer1m=pd.merge(am,bm, how='outer', on='date')
merge_outer2m=pd.merge(cm,dm, how='outer', on='date')
merge_outer3m=pd.merge(merge_outer1m,merge_outer2m, how='outer', on='date')
totalm=pd.merge(merge_outer3m,em, how='outer', on='date')



####################################

print("-----------Mobile 검색 이혼 카테고리 비교 -------------------- ")

client_id = input("id를 입력하세요 : ") 
client_secret = input("비밀번호를 입력하세요 : ") 
url = "https://openapi.naver.com/v1/datalab/search"
body = "{\"startDate\":\"2022-12-01\",\"endDate\":\"2022-12-31\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"대구이혼변호사\",\"keywords\":[\"대구이혼변호사\"]},{\"groupName\":\"대구이혼전문변호사\",\"keywords\":[\"대구이혼전문변호사\"]},{\"groupName\":\"대구이혼상담\",\"keywords\":[\"대구이혼상담\"]},{\"groupName\":\"이혼전문변호사\",\"keywords\":[\"이혼전문변호사\"]},{\"groupName\":\"이혼변호사\",\"keywords\":[\"이혼변호사\"]}],\"device\":\"mo\"}";
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_data=response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
    
result = json.loads(response_data)


date11m=[a['period'] for a in result['results'][0]['data']]
date22m=[a['period'] for a in result['results'][1]['data']]
date33m=[a['period'] for a in result['results'][2]['data']]
date44m=[a['period'] for a in result['results'][3]['data']]
date55m=[a['period'] for a in result['results'][4]['data']]


ratio_data11m=[a['ratio'] for a in result['results'][0]['data']]
ratio_data22m=[a['ratio'] for a in result['results'][1]['data']]
ratio_data33m=[a['ratio'] for a in result['results'][2]['data']]
ratio_data44m=[a['ratio'] for a in result['results'][3]['data']]
ratio_data55m=[a['ratio'] for a in result['results'][4]['data']]

am1=pd.DataFrame({'date':date11m,
               '대구이혼변호사':ratio_data11m})

bm1=pd.DataFrame({'date':date22m,
               '대구이혼전문변호사':ratio_data22m})

cm1=pd.DataFrame({'date':date33m,
               '대구이혼상담':ratio_data33m})

dm1=pd.DataFrame({'date':date44m,
               '이혼전문변호사':ratio_data44m})

em1=pd.DataFrame({'date':date55m,
               '이혼변호사':ratio_data55m})

merge_outer11m=pd.merge(am1,bm1, how='outer', on='date')
merge_outer22m=pd.merge(cm1,dm1, how='outer', on='date')
merge_outer33m=pd.merge(merge_outer11m,merge_outer22m, how='outer', on='date')
totalm1=pd.merge(merge_outer33m,em1, how='outer', on='date')


####################################


print("-----------Mobile 검색 음주 카테고리 비교 -------------------- ")

client_id = input("id를 입력하세요 : ")
client_secret = input("비밀번호를 입력하세요 : ")
url = "https://openapi.naver.com/v1/datalab/search"
body = "{\"startDate\":\"2022-12-01\",\"endDate\":\"2022-12-31\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"음주운전\",\"keywords\":[\"음주운전\"]},{\"groupName\":\"음주행정\",\"keywords\":[\"음주행정\"]},{\"groupName\":\"음주형사\",\"keywords\":[\"음주형사\"]},{\"groupName\":\"대구음주운전전문\",\"keywords\":[\"대구음주운전전문\"]},{\"groupName\":\"음주운전변호사\",\"keywords\":[\"음주운전변호사\"]}],\"device\":\"mo\"}";
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_data=response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
    
result = json.loads(response_data)


date111m=[a['period'] for a in result['results'][0]['data']]
date222m=[a['period'] for a in result['results'][1]['data']]
date333m=[a['period'] for a in result['results'][2]['data']]
date444m=[a['period'] for a in result['results'][3]['data']]
date555m=[a['period'] for a in result['results'][4]['data']]


ratio_data111m=[a['ratio'] for a in result['results'][0]['data']]
ratio_data222m=[a['ratio'] for a in result['results'][1]['data']]
ratio_data333m=[a['ratio'] for a in result['results'][2]['data']]
ratio_data444m=[a['ratio'] for a in result['results'][3]['data']]
ratio_data555m=[a['ratio'] for a in result['results'][4]['data']]

am2=pd.DataFrame({'date':date111m,
               '음주운전':ratio_data111m})

bm2=pd.DataFrame({'date':date222m,
               '음주행정':ratio_data222m})

cm2=pd.DataFrame({'date':date333m,
               '음주형사':ratio_data333m})

dm2=pd.DataFrame({'date':date444m,
               '대구음주운전전문':ratio_data444m})

em2=pd.DataFrame({'date':date555m,
               '음주운전변호사':ratio_data555m})

merge_outer111m=pd.merge(am2,bm2, how='outer', on='date')
merge_outer222m=pd.merge(cm2,dm2, how='outer', on='date')
merge_outer333m=pd.merge(merge_outer111m,merge_outer222m, how='outer', on='date')
totalm2=pd.merge(merge_outer333m,em2, how='outer', on='date')


###############################

merge_01m=pd.merge(totalm,totalm1, how='outer', on='date')
total012m=pd.merge(merge_01m,totalm2, how='outer', on='date')

print("---------------Mobile검색 모든 카테고리 안에서 각 키워드가 차지하는 비율------------------")
total012m=total012m.fillna(0)
total012m['합계']=total012m['개인회생']+total012m['대구개인회생']+total012m['대구개인회생전문']+total012m['개인회생신청자격']+total012m['개인회생전문']+total012m['대구이혼변호사']+total012m['대구이혼전문변호사']+total012m['대구이혼상담']+total012m['이혼전문변호사']+total012m['이혼변호사']+total012m['음주운전']+total012m['음주행정']+total012m['음주형사']+total012m['대구음주운전전문']+total012m['음주운전변호사']

### 회생 비율 구하기
total012m['개인회생비율']=(total012m['개인회생']/total012m['합계'])*100
total012m['대구개인회생비율']=(total012m['대구개인회생']/total012m['합계'])*100
total012m['대구개인회생전문비율']=(total012m['대구개인회생전문']/total012m['합계'])*100
total012m['개인회생신청자격비율']=(total012m['개인회생신청자격']/total012m['합계'])*100
total012m['개인회생전문비율']=(total012m['개인회생전문']/total012m['합계'])*100

#### 이혼 비율 구하기
total012m['대구이혼변호사비율']=(total012m['대구이혼변호사']/total012m['합계'])*100
total012m['대구이혼전문변호사비율']=(total012m['대구이혼전문변호사']/total012m['합계'])*100
total012m['대구이혼상담비율']=(total012m['대구이혼상담']/total012m['합계'])*100
total012m['이혼전문변호사비율']=(total012m['이혼전문변호사']/total012m['합계'])*100
total012m['이혼변호사비율']=(total012m['이혼변호사']/total012m['합계'])*100

#### 음주 비율 구하기
total012m['음주운전비율']=(total012m['음주운전']/total012m['합계'])*100
total012m['음주행정비율']=(total012m['음주행정']/total012m['합계'])*100
total012m['음주형사비율']=(total012m['음주형사']/total012m['합계'])*100
total012m['대구음주운전전문비율']=(total012m['대구음주운전전문']/total012m['합계'])*100
total012m['음주운전변호사비율']=(total012m['음주운전변호사']/total012m['합계'])*100


#################################

print("---------------Mobile검색 회생 카테고리 안에서 각 키워드가 차지하는 비율------------------")
totalm=totalm.fillna(0)
totalm['합계']=totalm['개인회생']+totalm['대구개인회생']+totalm['대구개인회생전문']+totalm['개인회생신청자격']+totalm['개인회생전문']
totalm['개인회생비율']=(totalm['개인회생']/totalm['합계'])*100
totalm['대구개인회생비율']=(totalm['대구개인회생']/totalm['합계'])*100
totalm['대구개인회생전문비율']=(totalm['대구개인회생전문']/totalm['합계'])*100
totalm['개인회생신청자격비율']=(totalm['개인회생신청자격']/totalm['합계'])*100
totalm['개인회생전문비율']=(totalm['개인회생전문']/totalm['합계'])*100


##########################################

print("---------------Mobile검색 이혼 카테고리 안에서 각 키워드가 차지하는 비율------------------")
totalm1=totalm1.fillna(0)
totalm1['합계']=totalm1['대구이혼변호사']+totalm1['대구이혼전문변호사']+totalm1['대구이혼상담']+totalm1['이혼전문변호사']+total1['이혼변호사']
totalm1['대구이혼변호사비율']=(totalm1['대구이혼변호사']/totalm1['합계'])*100
totalm1['대구이혼전문변호사비율']=(totalm1['대구이혼전문변호사']/totalm1['합계'])*100
totalm1['대구이혼상담비율']=(totalm1['대구이혼상담']/totalm1['합계'])*100
totalm1['이혼전문변호사비율']=(totalm1['이혼전문변호사']/totalm1['합계'])*100
totalm1['이혼변호사비율']=(totalm1['이혼변호사']/totalm1['합계'])*100


#####################################

print("---------------Mobile검색 음주 카테고리 안에서 각 키워드가 차지하는 비율------------------")
totalm2=totalm2.fillna(0)
totalm2['합계']=totalm2['음주운전']+totalm2['음주행정']+totalm2['음주형사']+totalm2['대구음주운전전문']+totalm2['음주운전변호사']
totalm2['음주운전비율']=(totalm2['음주운전']/totalm2['합계'])*100
totalm2['음주행정비율']=(totalm2['음주행정']/totalm2['합계'])*100
totalm2['음주형사비율']=(totalm2['음주형사']/totalm2['합계'])*100
totalm2['대구음주운전전문비율']=(totalm2['대구음주운전전문']/totalm2['합계'])*100
totalm2['음주운전변호사비율']=(totalm2['음주운전변호사']/totalm2['합계'])*100
