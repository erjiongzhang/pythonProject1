#coding=utf-8
import requests
r= requests.get(url="https://www.baidu.com/")
print(r.status_code)
print (r.url)
print (r.text)