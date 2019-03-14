import BaibaoxiangMobile
import time
import femail
from PIL import Image
import pytesseract
import traceback

'''必改参数'''
url='https://test-plus.vdongchina.com/app/ewei_shopv2_api.php?i=1001&r=member&comefrom=wxapp&openid=sns_wa_o6mWA4noeUX5DRr-FaAajrjZ0e1o&mid=&merchid=&authkey=&timestamp=1539064803196'
shopname="请输入页面标题"
box = (53, 994, 560, 1047)


'''启动手机微信'''
M=BaibaoxiangMobile.MGO()

'''先获取该会员的金额'''
vip_jine_start=M.vip_jine(url)

'''拍个照片，记录手机状态'''
M.paizhao("打开微信")

'''判断微信是否正常打开了'''
dakai=M.panduan_dakai_wechat()
if dakai==1:
    '''拍照'''
    png_name=M.paizhao("已打开微信")
else:
    '''拍照'''
    png_name = M.paizhao("已打开微信")
    '''发邮件报错'''
    M.email("未成功打开微信","plain",png_name)

'''滑动屏幕'''
M.moblie_huadong()

'''拍照'''
pen_names =M.paizhao("下拉微信")

'''输出当前页面的标题'''
M.inputbt("微信", "下拉微信错误出现Bug", 0,"plain",pen_names)
M.biaoji_time()

'''进入小程序'''
M.biaoji_time()
time.sleep(5)
try:
    print(M.driver.find_element_by_id("com.tencent.mm:id/ge").text)
except:
    femail("无法打开小程序", "plain", pen_names)
M.Cid("com.tencent.mm:id/gd","管家plus小程序入口","进入管家plus小程序中","Bug--无法进入小程序")

print("点击小程序图标")
time.sleep(40)
'''拍照'''
pen_names = M.paizhao("进入小程序的商城首页")
'''开始判断是否进入了小程序，如果进入了就可以获取到小程序的标题，如果为进入就无法获取小程序的标题，此时发送报错邮件，并重复进行进入'''

gogo=1
ii=1
while gogo==1 and ii<=10:
    M.biaoji_time()
    try:
        biaoti_new=M.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
        print("成功进入小程序")
        print("当前标题是：",biaoti_new)
        gogo=2
    except:
        print("再次点击执行进入小程序操作")
        M.Cid("com.tencent.mm:id/gd", "管家plus小程序入口", "进入管家plus小程序中", "Bug--无法进入小程序")
        ii+=1
        time.sleep(5)
if ii==11:
    femail("进入小程序连续失败11次","plain",pen_names)
M.biaoji_time()

'''拍照'''
pen_names = M.paizhao("进入小程序的商城首页")

'''**************************************************************************************************************商城购买商品***********************************************************************'''


'''输出当前页面的标题'''
M.inputbt(shopname, "进入商城首页报错", 1, "plain", pen_names)
M.biaoji_time()

'''打开全部分类'''
shuxin = "//android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
M.Cxpath(shuxin, "底部导航全部分类", "进入全部分类", "Bug--无法进入全部分类")
time.sleep(10)
'''拍照'''
pen_names = M.paizhao("打开全部分类")
'''输出当前页面的标题'''
M.inputbt("全部分类", "进入全部分类报错", 1, "plain", pen_names)
M.biaoji_time()


'''打开所有商品'''
M.driver.tap([(65, 395), (175, 545)], 500)
time.sleep(10)
'''拍照'''
pen_names =M.paizhao("打开所有商品")
'''输出当前页面的标题'''
M.inputbt("商品列表", "进入全部商品列表报错", 1, "plain",pen_names)
M.biaoji_time()


'''点击一个商品'''
M.driver.tap([(40, 345), (277, 743)], 500)
time.sleep(10)
M.biaoji_time()

'''拍照'''
png_names = M.paizhao("进入商品详情页面")

'''输出当前页面的标题'''
bt_shangpin = M.inputbt("", "进入商品详情页报错", 0, "plain", png_names)
M.biaoji_time()

'''从图片解析商品价格'''
shoping_jiage=M.get_shoping_img_jiage(png_names,box)

'''获取会员折扣'''
vip_zhekou=M.vip_lv_zekou(url)

'''计算折扣之后的商品价格'''
try:
    print("该商品的原价格为：", shoping_jiage)
    print("该会员当前折扣为：", vip_zhekou)
    shangpingjiage=shoping_jiage*vip_zhekou
    print("折扣之后应付金额为：",shangpingjiage)
except Exception as e:
    ee=traceback.format_exc()
    print("报错信息")
    print(ee)
    print("报错结束")
    M.email("计算商品折扣后价格失败！！报错如下<br>%s"%ee,"html","")
M.biaoji_time()

'''计算消费后金额'''
try:
    vip_jine_new = vip_jine_start - shangpingjiage
    print("会员剩余金额应为：", vip_jine_new)
except Exception as e:
    ee = traceback.format_exc()
    print("报错信息")
    print(ee)
    print("报错结束")
    M.email("计算购买商品折扣后会员余额失败！！报错如下<br>%s" % ee, "html", "")
M.biaoji_time()

'''点击立刻购买商品'''
print("点击立刻购买商品")
M.driver.tap([(532,1096), (709,1114)],  500)
time.sleep(10)
M.biaoji_time()

'''拍照'''
png_names = M.paizhao("点击立刻购买")

'''输出当前页面的标题'''
M.inputbt(bt_shangpin, "购买商品报错", 1, "plain", png_names)
M.biaoji_time()


'''点击确认购买商品'''
print("点击确认购买商品")
M.driver.tap([(197,1105), (461,1172)],  500)
time.sleep(10)
M.biaoji_time()
'''拍照'''
png_names =M.paizhao("点击确认购买")

'''输出当前页面的标题'''
M.inputbt("确认订单", "确认购买时报错", 1, "plain",png_names)


'''点击立即支付按钮'''
print("点击立即支付按钮")
M.driver.tap([(523,1141), (675,1177)],  500)
time.sleep(10)

M.biaoji_time()

'''拍照'''
png_names =M.paizhao("点击支付按钮")

'''输出当前页面的标题'''
M.inputbt("收银台", "选择支付方式报错", 1, "plain",png_names)

'''点击余额支付按钮'''
print("点击余额支付按钮")
'''点击第一个支付选项'''
#driver.tap([(106, 467), (627, 549)], 500)
'''点击第二个支付选项'''
M.driver.tap([(119, 366), (585, 439)], 500)
time.sleep(10)
M.biaoji_time()

yue=1
i=1
while yue!=1 and i<=30:
    M.biaoji_time()
    '''点击余额支付按钮'''

    M.driver.tap([(119, 366), (585, 439)], 500)
    print("点击余额支付按钮")
    time.sleep(10)
    try:
        print(11111111111111)
        bt=M.driver.find_element_by_id("com.tencent.mm:id/cd6").text
        if bt=="确认要支付吗?":
            yue=2
            break
            print(22222)
    except Exception as e:
        print("报错信息")
        print(33333333333)
        print(e)
        print("报错结束")
M.biaoji_time()

print()
'''拍照'''
png_names =M.paizhao("点击余额支付按钮")

'''输出当前页面的标题'''
M.inputbt("收银台", "支付报错", 1, "plain",png_names)
M.biaoji_time()


'''确认使用余额支付'''
M.Cid("com.tencent.mm:id/an3","确认余额支付按钮","确认使用余额支付中","Bug--无法确认使用余额支付")
time.sleep(10)
M.biaoji_time()


'''拍照'''
pen_names =M.paizhao("确认使用余额支付")

'''输出当前页面的标题'''
bt_name2 = M.inputbt("支付成功", "商品支付未成功", 3, "plain", pen_names)

oo=0
if bt_name2=="支付成功":
    print("商品购买完成")
    oo=1
M.biaoji_time()


'''获取消费后金额'''
vip_jine_end=M.vip_jine(url)

try:
    if vip_jine_end == vip_jine_new and oo == 1:
        jieguo1 = "商品购买测试通过"
    if vip_jine_end != vip_jine_new and oo != 1:
        jieguo1 = "商品购买测试不通过，请及时追查失败原因"
        M.email(jieguo1, "plain", pen_names)
    if vip_jine_end == vip_jine_new and oo != 1:
        jieguo1 = "商品购买成功，但是，页面没有进行转跳"
    print(jieguo1)
except Exception as e:
    print("报错信息")
    print(e)
    print("报错结束")
M.biaoji_time()



'''点击返回首页按钮'''
print("点击返回首页按钮")
M.driver.tap([(430, 609), (632, 662)], 500)
time.sleep(10)
M.biaoji_time()
'''拍照'''
png_names = M.paizhao("点击返回首页按钮")
M.inputbt(shopname, "购买商品后，返回首页报错", 3, "plain", png_names)
M.biaoji_time()

'''返回，直到首页'''
try:
    bt = M.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
    while bt != shopname:
        M.Cid("com.tencent.mm:id/kq", "返回", "返回上一页", "Bug--无法点击返回")
        time.sleep(10)
        bt = M.driver.find_element_by_id("com.tencent.mm:id/kt").text
    M.Cid("com.tencent.mm:id/cp", "底部菜单-首页", "已转跳至首页", "Bug--无法点击底部菜单-首页")
except:
    1 == 1
M.biaoji_time()





time.sleep(80)

