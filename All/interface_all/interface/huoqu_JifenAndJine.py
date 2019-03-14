import requests
import json
url3='https://test-plus.vdongchina.com/app/ewei_shopv2_api.php?i=1001&r=member&comefrom=wxapp&openid=sns_wa_o6mWA4gAL1CoThVCxqqMF39bB_Bo&mid=&merchid=&authkey=&timestamp=1539064803196'
url4='https://test-plus.vdongchina.com/app/ewei_shopv2_api.php?i=1001&r=member&comefrom=wxapp&openid=sns_wa_o6mWA4noeUX5DRr-FaAajrjZ0e1o&mid=&merchid=&authkey=&timestamp=1539064803196'
huiyuan_zehou={
    "普通会员":1,
    "钻石会员":0.77,
    "白银会员":1,
    "黄金会员":1
}
def jifen():
    r=requests.get(url4)
    kk = json.loads(r.text)
    jifen_float=float(kk['credit1'])
    print("积分是：",jifen_float)
    return jifen_float
def jine():
    r = requests.get(url4)
    kk = json.loads(r.text)
    jine_float = float(kk['credit2'])
    print( "金额是：", jine_float, "元")
    return jine_float
#levelname
def Vip_lv_zekou():
    r = requests.get(url4)
    kk = json.loads(r.text)
    vip_lv = kk['levelname']
    print( "等级是：", vip_lv)
    vip_zekou=huiyuan_zehou[vip_lv]
    print("会员折扣为：", vip_zekou)
    return vip_zekou


jifens=jifen()
jines=jine()
vipZhekou=Vip_lv_zekou()
print(jines*vipZhekou)
