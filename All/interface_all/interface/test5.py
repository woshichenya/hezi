import requests
import json
'''这里定义参数'''
payload = {
    "a":"login",
    "c":"user",
    "password":"12345678",
    "username":"bosst"

}
'''这里定义消息头，可增加cookie'''
handles={
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Connection":"keep-alive",
    "Content-Length":"32",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Host":"test-plus.vdongchina.com",
    "Referer":"http://test-plus.vdongchina.com/web/index.php?c=user&a=login&",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
    "X-Requested-With":"XMLHttpRequest"

}
url='http://test-plus.vdongchina.com/web/index.php?c=user&a=login&'
#r=urllib.request.Request(,payload)
print(handles)
r=requests.post(url,data=payload,headers=handles)
#r=requests.post(url,json=payload,headers=handles)
print("这里输出返回值text:",r.text)
print("返回值输出结束")

print("这里输出返回值json:",r.json())
print("返回值输出结束")
json_txt=json.dumps(r.text)
print(json_txt)
print("输出第一个字符",json_txt[0])
print("输出第二个字符",json_txt[1])
c=r.json()
print("输出json",c)
#print("?",c['error'])
print(r.headers)
print(r.request)
print(r.status_code)
print(r.cookies)
