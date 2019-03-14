from appium import webdriver
import BaibaoxiangMobile
import time

'''换系统需要修改的地方：
1.域名必须要改——url
2.检查登录按钮
3.修改用户名和密码——username/pasword
4.修改小程序的入口
5.修改会员的ID——userid
6.修改后台小程序管理入口
'''


'''必改参数'''
url4='https://test-plus.vdongchina.com/app/ewei_shopv2_api.php?i=1001&r=member&comefrom=wxapp&openid=sns_wa_o6mWA4noeUX5DRr-FaAajrjZ0e1o&mid=&merchid=&authkey=&timestamp=1539064803196'

'''启动手机微信'''
M=BaibaoxiangMobile.MGO

'''先获取该会员的金额'''
vip_jine_start=M.vip_jifen()


'''开始启动程序'''
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
print("启动手机程序打开微信")
driver.implicitly_wait(5)
print("已经打开微信程序")
driver.implicitly_wait(5)
print("等待五秒")


'''拍照'''
paizhao("打开微信")


'''判断微信是否正常打开了'''
xxx=1
while xxx==1:
    try:
        driver.find_element_by_id("com.tencent.mm:id/b0w")
        #driver.find_element_by_id("com.tencent.mm:id/chn")
        xxx=2
    except:
        print("微信未完全打开，等待中...")

'''拍照'''
paizhao("已打开微信")

'''输出当前页面的标题'''
bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='android:id/text1']").text
print("标题是：", bt)




'''获取频幕分辨率，并进行输出'''
sss=1
ii=1
while sss==1:
    try:
        #driver.get_window_size()['width']
        x = driver.get_window_size()['width']
        y=driver.get_window_size()['height']
        print("横坐标最大值",x)
        print("纵坐标最大值",y)
        '''尝试滑动频幕'''
        x1 = x*0.5
        y1 = y*0.15
        y2 = y*0.75
        time.sleep(3)
        print("滑动前")
        driver.swipe(x1,y1,x1,y2)
        driver.implicitly_wait(5)
        print("滑动后")
        sss=2
    except:
        print("获取分辨率失败，再来一次，当前第",ii,"次")
        ii+=1
        time.sleep(1)

'''拍照'''
paizhao("下拉微信")

'''输出当前页面的标题'''
bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='android:id/text1']").text
print("标题是：", bt)


'''进入小程序'''
time.sleep(5)
print(driver.find_element_by_id("com.tencent.mm:id/ge").text)
Cid("com.tencent.mm:id/gd","飞龙小程序入口","进入飞龙小程序中","Bug--无法进入小程序")

#Cid("com.tencent.mm:id/t9","飞龙小程序入口","进入飞龙小程序中","Bug--无法进入小程序")
print("点击小程序图标")
time.sleep(40)

'''拍照'''
paizhao("进入小程序的商城首页")

'''输出当前页面的标题'''
bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
print("标题是：", bt)

'''打开全部分类'''
Cxpath(
    "//android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]",
    "底部导航全部分类", "进入全部分类", "Bug--无法进入全部分类")
time.sleep(10)
'''拍照'''
paizhao("打开全部分类")
'''输出当前页面的标题'''
bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
print("标题是：", bt)

'''打开所有商品'''
driver.tap([(65, 395), (175, 545)], 500)
time.sleep(10)
'''拍照'''
paizhao("打开所有商品")
'''输出当前页面的标题'''
bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
print("标题是：", bt)

'''点击一个商品'''
driver.tap([(40, 345), (277, 743)], 500)
time.sleep(10)

'''拍照'''
paizhao("进入商品详情页面")

'''输出当前页面的标题'''
bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
print("标题是：", bt)

'''获取商品价格'''
b = shangpinjiage(bt)
b = float(b)
print("商品价格为：", b)

'''计算消费后金额'''
c = a - b
print("会员剩余金额应为：",c)


'''点击购买商品'''
print("点击购买商品")
driver.tap([(532,1096), (709,1114)],  500)
time.sleep(10)


'''拍照'''
paizhao("点击购买")

'''输出当前页面的标题'''
bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
print("标题是：", bt)


'''点击确认购买商品'''
print("点击确认购买商品")
driver.tap([(197,1105), (461,1172)],  500)
time.sleep(10)


'''拍照'''
paizhao("点击确认购买")

'''输出当前页面的标题'''
bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
print("标题是：", bt)



'''点击支付按钮'''
print("点击支付按钮")
driver.tap([(495,1096), (505,1172)],  500)
time.sleep(10)


'''拍照'''
paizhao("点击支付按钮")

'''输出当前页面的标题'''
bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
print("标题是：", bt)


'''点击余额支付按钮'''
print("点击余额支付按钮")
driver.tap([(409,364), (642,439)],  500)
time.sleep(10)


'''拍照'''
paizhao("点击余额支付按钮")

'''输出当前页面的标题'''
bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
print("标题是：", bt)



'''确认使用余额支付'''
Cid("com.tencent.mm:id/an3","确认余额支付按钮","确认使用余额支付中","Bug--无法确认使用余额支付")
time.sleep(10)


'''拍照'''
paizhao("确认使用余额支付")

'''输出当前页面的标题'''
bt=driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
print("标题是：",bt)

if bt=="支付成功":
    print("商品购买完成")
    oo=1


'''获取该会员消费后剩余的金额'''
d = huiyuanjine()
d = float(d)
print("会员实际剩余金额为：", d)

if d==c and oo==1:
    print("商品购买测试通过")
if d!=c or oo!=1:
    print("商品购买测试不通过，请及时查看失败原因")




time.sleep(100)