from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import baibaoxiang
import time
from selenium.webdriver.common.keys import Keys


'''web开始'''
GO=baibaoxiang.geturl
Go= baibaoxiang.geturl.llq
url="http://test-plus.vdongchina.com"
go= baibaoxiang.geturl(url)
Go.maximize_window()


'''封装wechat方法'''
desired_caps = {}

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.1.1',
    #'platformVersion': '7.0',
    #'deviceName': 'emulator-5554',
    'deviceName': 'freeme-4g-868607020470921',
    #'deviceName': 'mi_5s-66680442',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,
    'appPackage': 'com.tencent.mm',
    'appActivity': 'com.tencent.mm.ui.LauncherUI',
    'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
}
'''封装一个拍照方法'''
def paizhao(mingcheng):
        a="D:\\img\\"
        b=".png"
        Time=time.strftime("%Y-%m-%d--%H^%M^%S", time.localtime())
        driver.get_screenshot_as_file(a+Time+mingcheng+b)


'''封装一个id点击操作'''
def Cid(shuxing,mingcheng,chenggong,shibai):
        xxx=1
        i=1
        while xxx==1 and i<=30:
            try:
                driver.find_element_by_id(shuxing)
                print(mingcheng,"存在，执行下一步")
                xxx=2
                i=1
                while xxx==2 and i<=30:
                    try:
                        driver.find_element_by_id(shuxing).click()
                        print(chenggong)
                        xxx=3
                    except:
                        print(shibai,"执行等待操作，当前等待",i,"秒")
                        i+=1
                        time.sleep(1)
            except:

                print(mingcheng,"不存在，执行等待操作，当前等待",i,"秒")
                i+=1
                time.sleep(1)

'''封装一个xpath点击操作'''
def Cxpath(shuxing,mingcheng,chenggong,shibai):
        xxx=1
        i=1
        while xxx==1 and i<=30:
            try:
                driver.find_element_by_xpath(shuxing)
                print(mingcheng,"存在，执行下一步")
                xxx=2
                i=1
                while xxx==2 and i<=30:
                    try:
                        driver.find_element_by_xpath(shuxing).click()
                        print(chenggong)
                        xxx=3
                    except:
                        print(shibai,"执行等待操作，当前等待",i,"秒")
                        i+=1
                        time.sleep(1)
            except:

                print(mingcheng,"不存在，执行等待操作，当前等待",i,"秒")
                i+=1
                time.sleep(1)


'''执行web登录操作'''
go.Cxpath("/html/body/div/div[1]/div[2]/div/a","转跳登录页按钮","转跳登录页中","Bug--无法转跳到登录页")
go.Sxpath("//input[@name='username']","用户名输入框","boss1808","已经输入用户名","Bug--无法输入用户名")
go.Sxpath("//input[@name='password']","密码输入框","123456789","已经输入密码","Bug--无法输入密码")
go.Cxpath("//input[@id='submit']","登录按钮","登录中，等待页面转跳","Bug--登录失败")
go.Cxpath("/html/body/div[2]/div[2]/div/div[1]/ul/li[4]/div[1]/h4","小程序列表","展开首页小程序列表","Bug--无法展开首页小程序列表")
go.Cxpath("/html/body/div[2]/div[2]/div/div[1]/ul/li[4]/div[2]/ul/li[1]","小程序概况列表","进入首页小程序概况列表","Bug--无法进入首页小程序概况列表")
go.Cxpath("/html/body/div[2]/div[2]/div/div[2]/div/div/div[4]/div/table/tbody/tr[1]/td[7]/a","小程序管理按钮","进入小程序管理页面","Bug--无法进入小程序管理页面")
handles_all=Go.window_handles
while len(handles_all)<2:
    time.sleep(1)
    handles_all = Go.window_handles
if len(handles_all)==2:
    time.sleep(5)
    Go.switch_to.window(handles_all[1])



'''封装获取会员金额的方法'''
def huiyuanjine():
    go.Cxpath("/html/body/div[2]/ul/li[3]/a/span","会员列表","进入会员列表页面","Bug--无法进入会员列表页面")
    go.Sxpath("/html/body/div[6]/div[2]/form/div/div/input","搜索框","26378","成功输入会员编号","Bug--输入会员编号")
    go.Cxpath("/html/body/div[6]/div[2]/form/div/div/span[5]/button[1]","会员搜索按钮","点击会员搜索按钮","Bug--无法点击会员搜索按钮")
    huiyuanjines=Go.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div/table/tbody/tr/td[5]/span[2]/span").text
    return huiyuanjines


'''封装获取商品价格的方法'''
def shangpinjiage(names):
    go.Cxpath("/html/body/div[2]/ul/li[2]/a/span","商品超链接","进入商品页面","Bug--无法进入商品页面")
    go.Sxpath("/html/body/div[6]/div[2]/form/div/div/input","搜索框",names,"成功输入商品名称","Bug--输入商品名称")
    go.Cxpath("/html/body/div[6]/div[2]/form/div/div/span[3]/button","商品搜索按钮","点击商品搜索按钮","Bug--无法点击商品搜索按钮")
    shangpinjiages=Go.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div/table/tbody/tr/td[5]/a").text
    return shangpinjiages



cci=1
while cci==1:
    '''先获取该会员的金额'''
    a = huiyuanjine()
    a = float(a)
    print("会员余额：",a)


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
    Cxpath("//android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]","底部导航全部分类","进入全部分类","Bug--无法进入全部分类")
    time.sleep(10)
    '''拍照'''
    paizhao("打开全部分类")
    '''输出当前页面的标题'''
    bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
    print("标题是：", bt)

    '''打开所有商品'''
    driver.tap([(65,395),(175,545)],500)
    time.sleep(10)
    '''拍照'''
    paizhao("打开所有商品")
    '''输出当前页面的标题'''
    bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
    print("标题是：", bt)

    '''点击一个商品'''
    driver.tap([(40,345),(277,743)],500)
    time.sleep(10)

    '''拍照'''
    paizhao("进入商品详情页面")

    '''输出当前页面的标题'''
    bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
    print("标题是：", bt)


    '''获取商品价格'''
    b = shangpinjiage(bt)
    b = float(b)
    print("商品价格为：",b)

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