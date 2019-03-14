import requests
import json
import re



data2={
    "password":"123456789",
    "rember":"",
    "username":"18871551774",
}


url1="https://test-sso.vdongchina.com/index/logincheck"
url_index="https://test-sso-xiao.vdongchina.com/web/index.php?c=index&a=account&"

l=requests.post(url1,data=data2)
print(l.text)
print("登录的cookies",l.cookies)
print("cookie的个数：",len(l.cookies))
for i in l.cookies:
    print("cookies是：",i)
c=l.cookies.get_dict()
k=json.dumps(c)
# print("登录的json cookies",k)
# print("登录的消息头",l.headers)
# print("当前链接：",l.url)
# print(l.request.headers)
ccc=re.findall(r'Cookie (.*?) for',str(l.cookies),)
j_2=";".join(ccc)
print("正则表达式之后再将cookies转化成为字符串：",j_2)
headers_index={
     "cookie":j_2
}
l2=requests.get(url_index,headers=headers_index)
print(l2.text)

