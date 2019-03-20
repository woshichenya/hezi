from appium import webdriver
from beifen import baibaoxiang
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
userid="4525"
url="https://test-xiao.vdongtx.com/"
username="vdongshopplus"
pasword="1234567890"
name="陈雅小号"

'''web开始'''
GO= baibaoxiang.geturl
Go= baibaoxiang.geturl.llq
go= baibaoxiang.geturl(url)
Go.maximize_window()

desired_caps = {}

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.1.1',
    'deviceName': 'emulator-5554',
    #'deviceName': 'freeme-4g-868607020470921',
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

'''封装一个4.0web登录操作'''
def login_40():
    go.Sxpath("//input[@name='username']","用户名输入框",username,"成功输入用户名","输入用户名失败")
    go.Sxpath("//input[@name='password']","密码输入框",pasword,"成功输入密码","输入密码失败")
    go.Cxpath("//*[@id='submit']","登陆按钮","登录中","无法点击登陆")
    go.Cxpath("/html/body/div[2]/div[2]/div/div/div[1]/div/div/a[2]","进入公众号管理页面","进入公众号管理页面","Bug--无法公众号管理页面")
    go.Cxpath("/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/a/div[2]","魔力游商城转跳链接","进入公众号魔力游商城","Bug--无法进入公众号魔力游商城")
    go.Cxpath("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/ul/li[1]/a","微动天下商城转跳链接","进入微动天下商城","Bug--无法进入微动天下商城")

'''封装获取会员积分的方法'''
def huiyuanjifen():
    go.Cxpath("/html/body/div[2]/ul/li[3]/a/span","会员列表","进入会员列表页面","Bug--无法进入会员列表页面")
    go.Sxpath("/html/body/div[6]/div[2]/form/div/div/input", "搜索框", userid, "成功输入会员编号", "Bug--无法输入会员编号")
    go.Cxpath("/html/body/div[6]/div[2]/form/div/div/span[5]/button[1]","会员搜索按钮","点击会员搜索按钮","Bug--无法点击会员搜索按钮")
    huiyuanjifen=Go.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div/table/tbody/tr/td[5]/span[1]/span").text
    huiyuanjifen = float(huiyuanjifen)
    return huiyuanjifen

'''封装一个获取粉丝最新订单编号的方法'''
def jifendingdan():
    go.Cxpath("/html/body/div[2]/ul/li[9]/a/span","应用按钮","进入小程序应用页面","Bug--无法进入小程序应用页面")
    go.Cxpath("/html/body/div[5]/div[2]/div/div[2]/a[2]/div/span/span", "积分商城按钮", "进入积分商城页面", "Bug--无法进入积分商城页面")
    go.Cxpath("/html/body/div[3]/div/div[2]", "参与记录按钮", "展开参与记录下拉框", "Bug--无法展开参与记录下拉框")
    go.Cxpath("/html/body/div[3]/div/ul[4]/li/a", "兑换记录按钮", "打开兑换记录页面", "Bug--无法打开兑换记录页面")
    go.Sxpath("/html/body/div[6]/div[2]/form/div/div[2]/div/input", "搜索框", name, "成功输入粉丝姓名", "Bug--无法输入粉丝姓名")
    go.Cxpath("/html/body/div[6]/div[2]/form/div/div[2]/div/span/button[1]", "兑换记录搜索按钮", "点击会员搜索按钮", "Bug--无法点击会员搜索按钮")
    dingdanbianhao=Go.find_element_by_xpath("/html/body/div[6]/div[2]/table/tbody/tr[2]/td").text
    dingdanbianhao=dingdanbianhao[2:16]
    dingdanbianhao=int(dingdanbianhao)
    return dingdanbianhao

'''调用login_40()'''
login_40()
'''web端切换到准备页面'''
handles_all=Go.window_handles
while len(handles_all)<2:
    handles_all = Go.window_handles
Go.switch_to.window(handles_all[1])




driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
print("启动手机程序打开微信")
driver.implicitly_wait(5)
print("已经打开微信程序")
driver.implicitly_wait(5)
print("等待五秒")


xxx=1
while xxx==1:
    try:
        driver.find_element_by_id("com.tencent.mm:id/b0w")
        xxx=2
    except:
        print("微信未完全打开，等待中...")
        time.sleep(5)

'''封装一个点击操作'''
def Cid(shuxing,mingcheng,chenggong,shibai):
    xxx=1
    i=1
    while xxx==1 and i<=20:
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

'''获取频幕分辨率，并进行输出'''
sss=1
ii=1
while sss==1:
    try:
        driver.get_window_size()['width']
        x = driver.get_window_size()['width']
        y=driver.get_window_size()['height']
        print("横坐标最大值",x)
        print("纵坐标最大值",y)
        '''尝试滑动频幕'''
        x1 = x*0.5
        y1 = y*0.25
        y2 = y*0.9
        time.sleep(3)
        print("滑动前")
        driver.swipe(148,146,148,530)
        driver.implicitly_wait(5)
        print("滑动后")
        sss=2
    except:
        print("获取分辨率失败，再来一次，当前第",ii,"次")
        ii+=1
        time.sleep(1)


'''进入小程序'''
time.sleep(5)
print(driver.find_element_by_id("com.tencent.mm:id/ge").text)
Cid("com.tencent.mm:id/gd","魔力游商城小程序","进入魔力游商城小程序中","Bug--无法进入魔力游商城小程序")

print("点击小程序图标")
time.sleep(20)
bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
print("标题是：", bt)

'''获取积分'''
huiyuanjifen=huiyuanjifen()
print("会员积分：",huiyuanjifen)

'''**************************************************************************************************************积分商城***********************************************************************'''
'''拍照'''
paizhao("准备点击积分商城按钮")

'''点击积分商城按钮'''
print("点击积分商城按钮")
driver.tap([(390, 876), (500, 990)], 500)
time.sleep(10)
bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
if bt!="积分商城首页":
    print("标题是：", bt)
while bt!="积分商城首页":
    '''点击积分商城按钮'''
    print("点击积分商城按钮")
    driver.tap([(390, 876), (500, 990)], 500)
    time.sleep(10)
    '''获取标题'''
    bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
    if bt != "积分商城首页":
        print("标题是：", bt)

'''拍照'''
paizhao("点击积分商城按钮")

'''点击第一个积分分类'''
print("点击第一个积分分类")
driver.tap([(51, 749), (126, 875)], 500)
time.sleep(10)
bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
print("标题是：", bt)
'''拍照'''
paizhao("点击第一个积分分类")

'''点击第一个积分商品'''
print("点击第一个积分商品")
driver.tap([(31, 268), (303, 615)], 500)
time.sleep(10)
bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
print("标题是：", bt)
'''拍照'''
paizhao("点击第一个积分商品")


'''点击立即兑换'''
print("点击立即兑换")
driver.tap([(247, 1098), (467, 1164)], 500)
time.sleep(10)
bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
print("标题是：", bt)
'''拍照'''
paizhao("点击立即兑换")


'''点击立即支付'''
print("点击立即支付")
driver.tap([(522, 1101), (690, 1171)], 500)
time.sleep(10)
bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
print("标题是：", bt)
'''拍照'''
paizhao("点击立即支付")

'''点击余额支付'''
print("点击余额支付")
driver.tap([(277, 1028), (490, 1074)], 500)
time.sleep(10)
bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
print("标题是：", bt)
'''拍照'''
paizhao("点击余额支付")


'''点击确定支付按钮'''
print("点击确定支付按钮")
driver.tap([(429, 684), (568, 733)], 500)
Time=time.strftime("%Y%m%d%H%M%S", time.localtime())
Time=int(Time)
time.sleep(10)
bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
print("标题是：", bt)
'''拍照'''
paizhao("点击确定支付按钮")


'''点击确定按钮'''
print("点击确定按钮")
driver.tap([(233, 647), (422, 697)], 500)
time.sleep(10)
bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
print("标题是：", bt)
'''拍照'''
paizhao("点击确定按钮")


jifendingdantime=jifendingdan()
print(Time)
print(jifendingdantime)
print("时间差异：",jifendingdantime-Time)
if jifendingdantime-Time<100 and jifendingdantime-Time>-100:
    print("积分商品兑换成功")
else:
    print("积分商品兑换失败")



