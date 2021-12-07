#coding=utf-8、
from selenium import webdriver
from time import sleep
import requests
d=webdriver.Chrome()
d.get("https://eoms-test.wywk.cn/dashbord")
d.find_element_by_id("username").send_keys("117100")
d.find_element_by_id("password").send_keys("jiahui0819....")
d.find_element_by_id("login-submit").click()
sleep(8)
d.get("https://eoms-test.wywk.cn/pms-management/hotel")
sleep(2)
import pytest
a=9461
b=2047
c=6734
d=1250
e=18100
f=0
print(a+b+c+d+e+f)
