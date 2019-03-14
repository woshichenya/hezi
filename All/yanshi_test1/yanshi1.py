import BaibaoxiangMobile
import time


'''必改参数'''
url='https://test-plus.vdongchina.com/app/ewei_shopv2_api.php?i=1001&r=member&comefrom=wxapp&openid=sns_wa_o6mWA4noeUX5DRr-FaAajrjZ0e1o&mid=&merchid=&authkey=&timestamp=1539064803196'
shopname="请输入页面标题"
box = (53, 994, 560, 1047)


M=BaibaoxiangMobile.MGO()
M.moblie_huadong()

time.sleep(10)
M.dianji(153,764,481,862,500)
print("点击腾讯新闻")
time .sleep(10)
M.paizhao("点击新闻")


vip_jifen_new=M.vip_jifen(url)

print("积分是:",vip_jifen_new)
M.Cid("stabtn","登录按钮","点击登录按钮","没法点击")