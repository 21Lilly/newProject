#coding=utf8
# import random
# h = []
# while(len(h)<100):
#     h.append(random.randint(1000,10000))
#
# print(h)
# print(len(h))

import  requests

Host = 'http://127.0.0.1:80'
api_url = '{Host}/api/mgr/sq_mgr/'
header = {'Content-Type':'application/x-www-form-urlencoded'}

payload = {
    'action':'add_course',
    'data':"""{
            "name":"lily",
            "desc":"hellojhjdss",
            "display_idx":"2"    
            }"""
          }

reqs = requests.post(api_url,data=payload)
reqs.encoding = 'utf8' #设置响应编码--显示中文

print(reqs.request.headers)
print(reqs.request.body)
print(reqs.text)