import requests
import re

#from urllib import request
import json

url="http://xcx.9.cn/app/1"



r=requests.get(url)
k=r.text
print(k)
html = r.content.decode('utf-8')
print(html)

if html==k :
    print(111111111)
a='abca'
s="aba acd"
erweima = re.findall(r'<div class="detailLeft fl">.*?<div class="detaltext">.*?<img src="(.*?)".*?</div>',html,re.DOTALL)
print(erweima)
