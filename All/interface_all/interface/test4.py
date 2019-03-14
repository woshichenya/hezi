import requests
import json
payload = {
    "a":"login",
    "c":"user",
    "password":"12345678",
    "username":"bosst"

}
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
    "X-Requested-With":"XMLHttpRequest",
    "cookie":"__cfduid=d16a8d227328eb3853a6987e8187a14d21534832912;Hm_lvt_bd3bd79ac0fdbfdfece9009d7f93e160=1535682760,1536199949;_ga=GA1.2.614100209.1536199968;LiveWSPWT85081952=1536199975320640064425;NPWT85081952fistvisitetime=1536199975341;NPWT85081952lastvisitetime=1536199975342; NPWT85081952visitecounts=1; NPWT85081952visitepages=1; NPWT85081952IP=%7C121.69.81.74%7C;28cb___session=7f6crBdCa%2F6%2FzFtqufMulPJv21Hn3vsUI6fEKcPZyybdfNcLXk2LEDPByi505brrwTvJT0Uxxef35PfsWotfPg%2FO6xDXQKSkEYsWz%2BFhDWSgxOkNAqRn34pHvMVjG1vAX5lq7wPl%2F5taWjMAF2Au9%2BSXgOLD%2BgnpaYAUKD%2FxWZEJagE%2FBA; 28cb___lastvisit_344=%2Chttp%3A//test-plus.vdongchina.com/web/index.php%3Fc%3Daccount%26a%3Dminiapp_info%26moren%3D5;28cb___notice=1539004809;28cb___uniacid=1001;28cb___switch=ubt9U;28cb___uid=344;__lastvisit_344=1001%2Chttp%3A//test-plus.vdongchina.com/web/index.php%3Fc%3Dsite%26a%3Dentry%26m%3Dewei_shopv2%26do%3Dweb%26r%3Dorder; __notice=1539005470"

}
handles2={

    "cookie":"__cfduid=d16a8d227328eb3853a6987e8187a14d21534832912;Hm_lvt_bd3bd79ac0fdbfdfece9009d7f93e160=1535682760,1536199949;_ga=GA1.2.614100209.1536199968;LiveWSPWT85081952=1536199975320640064425;NPWT85081952fistvisitetime=1536199975341;NPWT85081952lastvisitetime=1536199975342; NPWT85081952visitecounts=1; NPWT85081952visitepages=1; NPWT85081952IP=%7C121.69.81.74%7C;28cb___session=7f6crBdCa%2F6%2FzFtqufMulPJv21Hn3vsUI6fEKcPZyybdfNcLXk2LEDPByi505brrwTvJT0Uxxef35PfsWotfPg%2FO6xDXQKSkEYsWz%2BFhDWSgxOkNAqRn34pHvMVjG1vAX5lq7wPl%2F5taWjMAF2Au9%2BSXgOLD%2BgnpaYAUKD%2FxWZEJagE%2FBA; 28cb___lastvisit_344=%2Chttp%3A//test-plus.vdongchina.com/web/index.php%3Fc%3Daccount%26a%3Dminiapp_info%26moren%3D5;28cb___notice=1539004809;28cb___uniacid=1001;28cb___switch=ubt9U;28cb___uid=344;__lastvisit_344=1001%2Chttp%3A//test-plus.vdongchina.com/web/index.php%3Fc%3Dsite%26a%3Dentry%26m%3Dewei_shopv2%26do%3Dweb%26r%3Dorder; __notice=1539005470"

}
handles3={

    "28cb___session":"2eb03HOLO8fBNXakIoHC5hXSbtx0NaoJeyMqqSCDhdzM2sbQsblkS6vBLVJzbSmCBTrsWCckfubFIGmFfgj0nIx7LMzaVLQPK4zpbF2eWPyiaPl2G15JUp%2BFQDQY0qV6ixT%2BGfDWHALUr43uEjy%2Bqn2LXYk9TWf25R%2BQxv56TtLhm2eBvg"

}
url='http://test-plus.vdongchina.com/web/index.php?c=site&a=entry&m=ewei_shopv2&do=web&r=order'
url2='http://test-plus.vdongchina.com/web/index.php?c=site&a=entry&m=ewei_shopv2&do=web&r=member.list.detail&id=67455'
url3='https://test-plus.vdongchina.com/app/ewei_shopv2_api.php?i=1001&r=member&comefrom=wxapp&openid=sns_wa_o6mWA4gAL1CoThVCxqqMF39bB_Bo&mid=&merchid=&authkey=&timestamp=1539064803196'
url4='https://test-plus.vdongchina.com/app/ewei_shopv2_api.php?i=1001&r=member&comefrom=wxapp&openid=sns_wa_o6mWA4noeUX5DRr-FaAajrjZ0e1o&mid=&merchid=&authkey=&timestamp=1539064803196'
url5='https://test-plus.vdongchina.com/app/ewei_shopv2_api.php?i=1001&r=creditshop.log.getlist&timestamp=1539266067120'
#r=urllib.request.Request(,payload)
print(handles)
r=requests.get(url5)

#r=requests.post(url,json=payload,headers=handles)
kkk=r.text
print("这里输出返回值text:",kkk)
print("返回值输出结束")
print("输出第一个字符",kkk[0])
print("输出第二个字符",kkk[1])


kk = json.loads(r.text)
print("这里输出返回值华为数组的text:",kk)
print("返回值输出结束")

print("输出金额",kk['error'])
#print("这里输出返回值json:",r.json())
#print("返回值输出结束")
json_txt=json.dumps(r.text)
print(json_txt)
print("输出第一个字符",json_txt[0])
print("输出第二个字符",json_txt[1])
#c=r.json()
#print("输出json",c)
#print("?",c['error'])
print(r.headers)
print(r.request)
print(r.status_code)
print(r.cookies)
kk = json.loads(r.text)
print("这里输出返回值华为数组的text:",kk)
print("返回值输出结束")
print("输出金额",kk['credit2'])
#credit1
print("输出积分",kk['credit1'])
jifen_float=float(kk['credit1'])
jine_float=float(kk['credit2'])
print("积分是：",jifen_float,"分，金额是：",jine_float,"元")
