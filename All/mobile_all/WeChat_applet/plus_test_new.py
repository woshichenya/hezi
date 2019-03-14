import BaibaoxiangMobile
import time
import femail
import traceback

'''必改参数'''
url='https://test-plus.vdongchina.com/app/ewei_shopv2_api.php?i=1001&r=member&comefrom=wxapp&openid=sns_wa_o6mWA4noeUX5DRr-FaAajrjZ0e1o&mid=&merchid=&authkey=&timestamp=1539064803196'
shopname="请输入页面标题"
box = (53, 994, 560, 1047)
vip_jifen_bianhao_data={
    "page":1,
    "status":0,
    "comefrom":"wxapp",
    "openid":"sns_wa_o6mWA4noeUX5DRr-FaAajrjZ0e1o"

}
vip_jifen_bianhao_url="https://test-plus.vdongchina.com/app/ewei_shopv2_api.php?i=1001&r=creditshop.log.getlist&timestamp=1539574021264"


'''启动手机微信'''
M=BaibaoxiangMobile.MGO()
M.biaoji_time()
time.sleep(20)

'''先获取该会员的金额'''
vip_jine_start=M.vip_jine(url)
M.biaoji_time()


'''拍个照片，记录手机状态'''
png_names =M.paizhao("打开微信")
M.biaoji_time()


'''判断微信是否正常打开了'''
dakai=M.panduan_dakai_wechat()
if dakai==1:
    '''拍照'''
    png_name=M.paizhao("已打开微信")
    M.biaoji_time()
else:
    '''拍照'''
    png_name = M.paizhao("已打开微信")
    '''发邮件报错'''
    M.email("未成功打开微信","plain",png_name)
    M.biaoji_time()

'''滑动屏幕'''
M.moblie_huadong()
M.biaoji_time()

'''拍照'''
pen_names =M.paizhao("下拉微信")
M.biaoji_time()
time.sleep(5)

'''输出当前页面的标题'''
M.inputbt("微信", "下拉微信错误出现Bug", 0,"plain",pen_names,"")
M.biaoji_time()

'''进入小程序'''
M.biaoji_time()
time.sleep(5)
try:
    print("小程序名称是：",M.driver.find_element_by_id("com.tencent.mm:id/ge").text)
except:
    femail("无法打开小程序", "plain", pen_names)
M.Cid("com.tencent.mm:id/gd","管家plus小程序入口","进入管家plus小程序中","Bug--无法进入小程序")
M.biaoji_time()

print("点击小程序图标")
time.sleep(50)
M.biaoji_time()
'''拍照'''
pen_names = M.paizhao("进入小程序的商城首页")

'''开始判断是否进入了小程序，如果进入了就可以获取到小程序的标题，如果为进入就无法获取小程序的标题，此时发送报错邮件，并重复进行进入'''
M.biaoji_time()

gogo=1
ii=1
while gogo==1 and ii<=10:
    M.biaoji_time()
    try:
        biaoti_new=M.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
        print("成功进入小程序")
        print("当前标题是：",biaoti_new)
        gogo=2
        M.biaoji_time()
    except:
        print("再次点击执行进入小程序操作")
        M.Cid("com.tencent.mm:id/gd", "管家plus小程序入口", "进入管家plus小程序中", "Bug--无法进入小程序")
        ii+=1
        time.sleep(5)
        M.biaoji_time()
if ii==11:
    femail("进入小程序连续失败11次","plain",pen_names)
M.biaoji_time()

'''拍照'''
pen_names = M.paizhao("进入小程序的商城首页")
M.biaoji_time()

'''**************************************************************************************************************商城购买商品***********************************************************************'''


'''输出当前页面的标题'''
M.inputbt(shopname, "进入商城首页报错", 1, "plain", pen_names,"")
M.biaoji_time()

'''打开全部分类'''
shuxin = "//android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
M.Cxpath(shuxin, "底部导航全部分类", "进入全部分类", "Bug--无法进入全部分类")
M.biaoji_time()
time.sleep(15)
'''拍照'''
pen_names = M.paizhao("打开全部分类")
M.biaoji_time()
'''输出当前页面的标题'''
M.inputbt("全部分类", "进入全部分类报错", 1, "plain", pen_names,"")
M.biaoji_time()


'''打开所有商品'''
M.dianji(65,395,175,545,500)
M.biaoji_time()
time.sleep(10)
M.biaoji_time()
'''拍照'''
pen_names =M.paizhao("打开所有商品")
M.biaoji_time()
'''输出当前页面的标题'''
M.inputbt("商品列表", "进入全部商品列表报错", 1, "plain",pen_names,"")
M.biaoji_time()


'''点击一个商品'''
M.dianji(40, 345,277,743,500)
M.biaoji_time()
time.sleep(10)
M.biaoji_time()

'''拍照'''
png_names = M.paizhao("进入商品详情页面")
M.biaoji_time()

'''输出当前页面的标题'''
bt_shangpin = M.inputbt("", "进入商品详情页报错", 0, "plain", png_names,"")
M.biaoji_time()

'''从图片解析商品价格'''
shoping_jiage=M.get_shoping_img_jiage(png_names,box)
M.biaoji_time()

'''获取会员折扣'''
vip_zhekou=M.vip_lv_zekou(url)
M.biaoji_time()

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
    M.biaoji_time()
except Exception as e:
    ee = traceback.format_exc()
    print("报错信息")
    print(ee)
    print("报错结束")
    M.email("计算购买商品折扣后会员余额失败！！报错如下<br>%s" % ee, "html", "")
    M.biaoji_time()
M.biaoji_time()

'''点击立刻购买商品'''
print("点击立刻购买商品")
M.dianji(532,1096,709,1114,500)
M.biaoji_time()
time.sleep(10)


'''拍照'''
png_names = M.paizhao("点击立刻购买")
M.biaoji_time()

'''输出当前页面的标题'''
M.inputbt(bt_shangpin, "购买商品报错", 1, "plain", png_names,"")
M.biaoji_time()


'''点击确认购买商品'''
print("点击确认购买商品")
M.dianji(197,1105,461,1172,500)
M.biaoji_time()
time.sleep(10)

'''拍照'''
png_names =M.paizhao("点击确认购买")
M.biaoji_time()

'''输出当前页面的标题'''
M.inputbt("确认订单", "确认购买时报错", 1, "plain",png_names,"")
M.biaoji_time()


'''点击立即支付按钮'''
print("点击立即支付按钮")
M.dianji(523,1141,675,1177,500)
M.biaoji_time()
time.sleep(10)


'''拍照'''
png_names =M.paizhao("点击支付按钮")

'''输出当前页面的标题'''
M.inputbt("收银台", "选择支付方式报错", 1, "plain",png_names,"")
M.biaoji_time()


'''点击余额支付按钮'''
print("点击余额支付按钮")
'''点击第一个支付选项'''
#M.dianji(106, 467,627, 549,500)

'''点击第二个支付选项'''
M.dianji(119, 366,585, 439,500)
M.biaoji_time()
time.sleep(10)

yue=1
i=1
while yue!=1 and i<=30:
    M.biaoji_time()
    '''点击余额支付按钮'''
    M.dianji(119, 366,585, 439,500)
    M.biaoji_time()
    time.sleep(10)
    print("点击余额支付按钮")


    try:

        bt=M.driver.find_element_by_id("com.tencent.mm:id/cd6").text
        if bt=="确认要支付吗?":
            yue=2
            break

        M.biaoji_time()

    except Exception as e:
        print("报错信息")

        print(e)
        print("报错结束")
        M.biaoji_time()

M.biaoji_time()

print()
'''拍照'''
png_names =M.paizhao("点击余额支付按钮")
M.biaoji_time()


'''输出当前页面的标题'''
M.inputbt("收银台", "支付报错", 1, "plain",png_names,"")
M.biaoji_time()


'''确认使用余额支付'''
M.Cid("com.tencent.mm:id/an3","确认余额支付按钮","确认使用余额支付中","Bug--无法确认使用余额支付")
time.sleep(10)
M.biaoji_time()


'''拍照'''
pen_names =M.paizhao("确认使用余额支付")
M.biaoji_time()


'''输出当前页面的标题'''
bt_name2 = M.inputbt("支付成功", "商品支付未成功", 3, "plain", pen_names,"")
M.biaoji_time()


oo=0
if bt_name2=="支付成功":
    print("商品购买完成")
    oo=1
M.biaoji_time()


'''获取消费后金额'''
vip_jine_end=M.vip_jine(url)
M.biaoji_time()


try:
    if vip_jine_end == vip_jine_new and oo == 1:
        jieguo1 = "**********************************************************************商品购买测试通过"
    if vip_jine_end != vip_jine_new and oo != 1:
        jieguo1 = "*************************************************商品购买测试不通过，请及时追查失败原因"
        M.email(jieguo1, "plain", pen_names)
    if vip_jine_end == vip_jine_new and oo != 1:
        jieguo1 = "***************************************************商品购买成功，但是，页面没有进行转跳"
    print(jieguo1)
    M.biaoji_time()
except Exception as e:
    print("报错信息")
    print(e)
    print("报错结束")
    M.biaoji_time()
M.biaoji_time()



'''点击返回首页按钮'''
print("点击返回首页按钮")
M.dianji(430, 609,632, 662,500)
M.biaoji_time()
time.sleep(10)

'''拍照'''
png_names = M.paizhao("点击返回首页按钮")
M.inputbt(shopname, "购买商品后，返回首页报错", 3, "plain", png_names,"")
M.biaoji_time()

'''返回，直到首页'''
try:
    bt = M.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
    while bt != shopname:
        M.Cid("com.tencent.mm:id/kq", "返回", "返回上一页", "Bug--无法点击返回")
        time.sleep(10)
        bt = M.driver.find_element_by_id("com.tencent.mm:id/kt").text
        M.biaoji_time()

    M.Cid("com.tencent.mm:id/cp", "底部菜单-首页", "已转跳至首页", "Bug--无法点击底部菜单-首页")
except:
    1 == 1
M.biaoji_time()

time.sleep(20)


'''**********************************积分商城***********************************************************'''

M.dianji(398,349,493,449,500)
print("点击积分商城按钮")
M.biaoji_time()
time.sleep(10)

'''拍照'''
png_names=M.paizhao("点击积分商城")
M.biaoji_time()
M.inputbt("积分商城首页","进入积分商城错误",1,"plain",png_names,"")
M.biaoji_time()


'''点击第一个积分分类'''
M.dianji(51, 795, 126, 865, 500)
print("点击第一个积分分类")
M.biaoji_time()
time.sleep(10)
png_names =M.paizhao("进入第一个积分商品分类")
M.inputbt("商品列表","进入积分商城第一个商品分类错误",1,"plain",png_names,"")
M.biaoji_time()

'''点击第一个积分商品'''
print("点击第一个积分商品")
M.dianji(31, 268, 303, 615, 500)
M.biaoji_time()
time.sleep(10)
png_names =M.paizhao("进入第一个积分商品")
M.inputbt("商品详情","进入积分商城第一个商品错误",1,"plain",png_names,"")
M.biaoji_time()


'''点击立即兑换'''
print("点击立即兑换")
M.dianji(247, 1098, 467, 1164, 500)
M.biaoji_time()
time.sleep(10)
png_names =M.paizhao("点击立即兑换")
M.inputbt("确认订单","点击立即兑换错误",1,"plain",png_names,"")
M.biaoji_time()

'''点击立即支付'''
print("点击立即支付")
M.dianji(522, 1101, 690, 1171, 500)
M.biaoji_time()
time.sleep(10)
png_names =M.paizhao("点击立即支付")
M.inputbt("确认订单","点击立即支付错误",1,"plain",png_names,"")
M.biaoji_time()



'''点击余额支付'''
print("点击余额支付")
M.dianji(277, 1028, 490, 1074, 500)
M.biaoji_time()
time.sleep(10)
png_names =M.paizhao("点击余额支付")
M.inputbt("确认订单","点击余额支付错误",1,"plain",png_names,"")
M.biaoji_time()

time_New = time.strftime("%Y%m%d%H%M%S", time.localtime())
time_New = int(time_New)
print("准备点击确认余额支付的时间",time_New)

'''点击确定支付按钮'''
print("点击确定支付按钮")
M.dianji(429, 684, 568, 733, 500)
time_New = time.strftime("%Y%m%d%H%M%S", time.localtime())
time_New = int(time_New)
M.biaoji_time()
time.sleep(10)
png_names =M.paizhao("点击确定支付")
M.inputbt("确认订单","点击确定支付错误",1,"plain",png_names,"")
M.biaoji_time()






'''点击确定按钮'''
print("点击确定按钮")
M.dianji(219, 647, 500, 700, 500)
M.biaoji_time()
time.sleep(10)
png_names =M.paizhao("点击确定按钮")
M.inputbt("订单详情","点击确定错误",1,"plain",png_names,"")
M.biaoji_time()




'''***********************************************'''

try:
    jifendingdan_time = M.vip_jifen_dingdan(vip_jifen_bianhao_url,vip_jifen_bianhao_data)
    print("记录时间为：",time_New)
    print("订单时间为：",jifendingdan_time)
    print("时间差异：", jifendingdan_time - time_New)
except Exception as e:
    print("报错信息")
    print(e)
    print("报错结束")
try:
    if jifendingdan_time - time_New < 5 and jifendingdan_time - time_New > -5:
        jieguo2 = "*****************************************************************积分商品兑换测试通过"
        print(jieguo2)
    else:
        jieguo2 = "**********************************************积分商品兑换测试不通过,请及时追查失败原因"
        print(jieguo2)
except Exception as e:
    print("报错信息")
    print(e)
    print("报错结束")
M.biaoji_time()















