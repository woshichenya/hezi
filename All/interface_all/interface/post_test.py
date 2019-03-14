import json
import requests
import time


data={
    "page":1,
    "status":0,
    "comefrom":"wxapp",
    "openid":"sns_wa_o6mWA4gAL1CoThVCxqqMF39bB_Bo"

}
url="https://test-plus.vdongchina.com/app/ewei_shopv2_api.php?i=1001&r=creditshop.log.getlist&timestamp=1539574021264"
time_New = time.strftime("%Y%m%d%H%M%S", time.localtime())
time_New = int(time_New)
print(time_New)
r=requests.post(url,data=data)
print(r.text)
kk=json.loads(r.text)
    #load(r.text)
print("数组话之后：",kk)
print(kk['list'])
kkk=kk['list']
#kkk=json.loads(kk['list'])
print(kkk)
kkkk=str(kkk)
print(kkkk)
kkkkk=kkkk[26:46]
print(kkkkk)
print(kkkkk[1])
kkkkkk=json.loads(kkkkk)
dingdan_bianhao=str(kk['list'])[26:46]
dingdan_bianhao = str(json.loads(r.text)['list'])[26:46]
dingdan_bianhao=int(dingdan_bianhao[0:14])
print("显示：",dingdan_bianhao)


def vip_jifen_dingdan(self):
    r = requests.post(url, data=data)
    dingdan_bianhao = str(json.loads(r.text)['list'])[26:46]
    dingdan_bianhao = float(dingdan_bianhao[0:16])
    print("最新订单编号为：",dingdan_bianhao)
Time = time.strftime("%Y%m%d%H%M%S", time.localtime())
Time = int(Time)
print(Time)
print(dingdan_bianhao)


time_New = time.strftime("%Y%m%d%H%M%S", time.localtime())
time_New = int(time_New)
print(time_New)