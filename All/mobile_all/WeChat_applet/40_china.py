# coding: utf-8
from appium import webdriver
import time
import traceback
from beifen import baibaoxiang, femail

'''换系统需要修改的地方：
1.域名必须要改——url
2.检查登录按钮
3.修改用户名和密码——username/pasword
4.修改小程序的入口
5.修改会员的ID——userid
6.修改后台小程序管理入口
'''


'''必改参数'''
userid="3482"
url="https://xiao.vdongchina.com"
username="vdongshops"
pasword="1234567890"
name="陈雅小号"
shopname="微动商城"

'''web开始'''
GO= baibaoxiang.geturl
Go= baibaoxiang.geturl.llq
go= baibaoxiang.geturl(url)
Go.maximize_window()

'''邮件方法'''
email= femail.email


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
        png_name=a+Time+mingcheng+b
        driver.get_screenshot_as_file(png_name)
        return png_name

'''封装一个输出标题的方法'''
def inputbt(dbiaoti,em_neirong_text,shifouquan,geshi_plain_or_html_s,pen_all_name):
    gogo=2
    ii=1
    while gogo==2 and ii<=30:
        try:
            if dbiaoti!="微信" :
                bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
            elif dbiaoti=="微信":
                bt=driver.find_element_by_xpath("//android.widget.TextView[@resource-id='android:id/text1']").text
            gogo=1
        except Exception as e:
            print("标题获取中。。。")
            time.sleep(1)
    if shifouquan==1:
        if bt!=dbiaoti:
            email(em_neirong_text,geshi_plain_or_html_s,pen_all_name)
            print("标题不完全一样，已发送邮件")
        else:
            print("标题是：", bt, "标题验证通过")
    if shifouquan==0:
        if dbiaoti not in bt :
            email(em_neirong_text, geshi_plain_or_html_s,pen_all_name)
            print("标题不包含判断值,已发送邮件")
        else:
            print("标题是：", bt, "标题验证通过")
    if shifouquan==3:
            if dbiaoti not in bt :
                print("未转跳页面，标题不一致")
    return bt

'''封装一个mobile_id点击操作'''
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
                        i=1
                        driver.find_element_by_id(shuxing).click()
                        print(chenggong)
                        xxx=3
                    except:
                        print(shibai,"执行等待操作，当前执行",i,"次")
                        i+=1

            except:
                print(mingcheng,"不存在，执行等待操作，当前等待",i,"秒")
                i+=1
                time.sleep(1)

'''封装一个mobile_xpath点击操作'''
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


'''封装一个4.0web登录操作'''
def login_40():
    try:
        go.Sxpath("//input[@name='username']","用户名输入框",username,"成功输入用户名","输入用户名失败")
        go.Sxpath("//input[@name='password']","密码输入框",pasword,"成功输入密码","输入密码失败")
        go.Cxpath("//*[@id='submit']","登陆按钮","登录中","无法点击登陆")
        go.Cxpath("/html/body/div[2]/div[2]/div/div/div[1]/div/div/a[2]","进入公众号管理页面","进入公众号管理页面","Bug--无法公众号管理页面")
        go.Cxpath("/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/a/div[2]","魔力游商城转跳链接","进入公众号魔力游商城","Bug--无法进入公众号魔力游商城")
        go.Cxpath("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/ul/li[3]/a","微动天下商城转跳链接","进入微动天下商城","Bug--无法进入微动天下商城")
    except Exception as e:
        pen_names=go.paizhao_pc("登录报错图片")
        email("登录报错：<br>%s"%e,"html",pen_names)


'''封装获取会员积分的方法'''
def huiyuanjifen():
    try:
        go.Cxpath("/html/body/div[2]/ul/li[3]/a/span","会员列表","进入会员列表页面","Bug--无法进入会员列表页面")
        go.Sxpath("/html/body/div[6]/div[2]/form/div/div/input", "搜索框", userid, "成功输入会员编号", "Bug--无法输入会员编号")
        go.Cxpath("/html/body/div[6]/div[2]/form/div/div/span[5]/button[1]","会员搜索按钮","点击会员搜索按钮","Bug--无法点击会员搜索按钮")
        x=1
        i=1
        while x==1 and i<=30:
            try:
                huiyuanjifen=Go.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div/table/tbody/tr/td[5]/span[1]/span").text
                x=2
            except:
                i+=1
                time.sleep(1)
        return huiyuanjifen
    except Exception as e:
        pen_names=go.paizhao_pc("获取会员积分报错图片")
        email("获取会员积分报错：<br>%s"%e,"html",pen_names)

'''封装获取会员金额的方法'''
def huiyuanjine():
    try:
        go.Cxpath("/html/body/div[2]/ul/li[3]/a/span","会员列表","进入会员列表页面","Bug--无法进入会员列表页面")
        go.Sxpath("/html/body/div[6]/div[2]/form/div/div/input", "搜索框", userid, "成功输入会员编号", "Bug--无法输入会员编号")
        go.Cxpath("/html/body/div[6]/div[2]/form/div/div/span[5]/button[1]","会员搜索按钮","点击会员搜索按钮","Bug--无法点击会员搜索按钮")
        x = 1
        i = 1
        while x == 1 and i <= 30:
            try:
                huiyuanjines = Go.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div/table/tbody/tr/td[5]/span[2]/span").text
                x = 2
            except:
                i += 1
                time.sleep(1)

        return huiyuanjines
    except Exception as e:
        pen_names=go.paizhao_pc("获取会员金额报错图片")
        email("获取会员金额报错：<br>%s"%e,"html",pen_names)

'''保存运行时间'''
def biaoji_time():
    t=time.time()
    t=int(t)
    ft=open('D:\\text.txt','w')
    ft.write(str(t))
    ft.close()

'''封装获取商品价格的方法'''
def shangpinjiage(shopname):
    try:
        go.Cxpath("/html/body/div[2]/ul/li[2]/a/span","商品超链接","进入商品页面","Bug--无法进入商品页面")
        go.Sxpath("/html/body/div[6]/div[2]/form/div/div/input","搜索框",shopname,"成功输入商品名称","Bug--输入商品名称")
        go.Cxpath("/html/body/div[6]/div[2]/form/div/div/span[3]/button","商品搜索按钮","点击商品搜索按钮","Bug--无法点击商品搜索按钮")
        x = 1
        i = 1
        while x == 1 and i <= 30:
            try:
                shangpinjiages = Go.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div/table/tbody/tr/td[5]/a").text
                x = 2
            except:
                i += 1
                time.sleep(1)

        return shangpinjiages
    except Exception as e:
        pen_names=go.paizhao_pc("获取商品价格报错图片")
        email("获取商品价格报错：<br>%s"%e,"html",pen_names)

'''封装一个获取会员折扣的方法'''
def huiyuanzekou():
    try:
        go.Cxpath("/html/body/div[2]/ul/li[3]/a/span", "会员列表", "进入会员列表页面", "Bug--无法进入会员列表页面")
        go.Sxpath("/html/body/div[6]/div[2]/form/div/div/input", "搜索框", userid, "成功输入会员编号", "Bug--无法输入会员编号")
        go.Cxpath("/html/body/div[6]/div[2]/form/div/div/span[5]/button[1]", "会员搜索按钮", "点击会员搜索按钮", "Bug--无法点击会员搜索按钮")
        huiyuandengjis = Go.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div/table/tbody/tr/td[3]").text
        go.Cxpath("/html/body/div[3]/div/ul[2]/li/a", "会员等级按钮", "进入会员等级页面", "Bug--无法进入会员等级页面")
        if huiyuandengjis == "普通会员":
            huiyuanzekou_all = 1
        elif huiyuandengjis != "普通会员":
            go.Sxpath("/html/body/div[6]/div[2]/form[1]/div/div[2]/div/input", "搜索框", huiyuandengjis, "成功输入会员等级","Bug--无法输入会员等级")
            go.Cxpath("/html/body/div[6]/div[2]/form[1]/div/div[2]/div/span/button", "会员等级搜索按钮", "点击会员等级搜索按钮","Bug--无法点击会员等级搜索按钮")
            huiyuanzekou_all = Go.find_element_by_xpath("/html/body/div[6]/div[2]/form[2]/table/tbody/tr/td[4]").text
            huiyuanzekou_all = float(huiyuanzekou_all)
            huiyuanzekou_all = huiyuanzekou_all * 0.1
        return huiyuanzekou_all
    except Exception as e:
        pen_names=go.paizhao_pc("获取会员折扣报错图片")
        email("获取会员折扣报错：<br>%s"%e,"html",pen_names)

'''封装一个获取粉丝最新订单编号的方法'''
def jifendingdan():
    try:
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
    except Exception as e:
        pen_names=go.paizhao_pc("获取最新订单编号报错图片")
        email("获取最新订单编号报错信息：<br>%s"%e,"html",pen_names)

'''调用login_40()'''
login_40()
'''web端切换到准备页面'''
handles_all = Go.window_handles
handles_all_shuzi = 1
while len(handles_all) < 2 and handles_all_shuzi <= 30:
    handles_all = Go.window_handles
    handles_all_shuzi += 1
try:
    Go.switch_to.window(handles_all[1])
except Exception as e:
    print("报错信息")
    print(e)
    print("报错结束")


try:
    cci=1
    while cci==1:
        cci+=1
        '''先获取该会员的金额'''
        huiyuanyue = huiyuanjine()
        huiyuanyue = float(huiyuanyue)
        print("会员余额：",huiyuanyue)
        biaoji_time()

        kwx=1
        while kwx==1:
            try:
                '''开始启动程序'''
                driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
                #driver = webdriver.Remote('http://10.11.41.116:4723/wd/hub', desired_caps)
                print("启动手机程序打开微信")
                driver.implicitly_wait(5)
                print("已经打开微信程序")
                driver.implicitly_wait(5)
                print("等待五秒")
                kwx=2
                biaoji_time()
            except Exception as e:
                biaoji_time()
                ee=traceback.format_exc()
                print("e报错开始")
                print(e)
                print("e报错结束")
                print("ee报错开始")
                print(ee)
                print("ee报错结束")

            biaoji_time()


        '''拍照'''
        pen_names=paizhao("打开微信")
        biaoji_time()


        '''判断微信是否正常打开了'''
        xxx=1
        while xxx==1:
            try:
                driver.find_element_by_id("com.tencent.mm:id/b0w")
                xxx=2
            except:
                biaoji_time()
                print("微信未完全打开，等待中...")
                time.sleep(3)
        biaoji_time()

        '''拍照'''
        pen_names =paizhao("已打开微信")
        biaoji_time()

        '''输出当前页面的标题'''
        inputbt("微信", "打开微信错误出现Bug", 0,"plain",pen_names)
        biaoji_time()




        '''获取频幕分辨率，并进行输出'''
        sss=1
        ii=1
        while sss==1:
            biaoji_time()
            '''**************************************************************************************************************进入小程序***********************************************************************'''
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
                ee=1
            except Exception as e:
                ee=traceback.format_exc()
                print("获取分辨率失败，再来一次，当前第",ii,"次")
                ii+=1
                time.sleep(1)
            if ee!=1:
                email("获取手机分辨率报错：<br>%s"%ee,"plain","")
        biaoji_time()



        '''拍照'''
        pen_names =paizhao("下拉微信")

        '''输出当前页面的标题'''
        inputbt("微信", "下拉微信错误出现Bug", 0,"plain",pen_names)
        biaoji_time()


        '''进入小程序'''
        biaoji_time()
        time.sleep(5)
        try:
            print(driver.find_element_by_id("com.tencent.mm:id/ge").text)
        except:
            email("无法打开小程序","plain",pen_names)
        Cid("com.tencent.mm:id/gd","微动研发演示账号7小程序","进入微动研发演示账号7小程序中","Bug--无法进入微动研发演示账号7小程序")
        #Cid("com.tencent.mm:id/t9","飞龙小程序入口","进入飞龙小程序中","Bug--无法进入小程序")
        print("点击小程序图标")
        time.sleep(40)
        '''拍照'''
        pen_names = paizhao("进入小程序的商城首页")
        gogo=1
        ii=1
        while gogo==1 and ii<=10:
            biaoji_time()
            try:
                biaoti_new=driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
                print("成功进入小程序")
                print("当前标题是：",biaoti_new)
                gogo=2
            except:
                print("再次点击执行进入小程序操作")
                Cid("com.tencent.mm:id/gd", "微动研发演示账号7小程序", "进入微动研发演示账号7小程序中", "Bug--无法进入微动研发演示账号7小程序")
                ii+=1
                time.sleep(5)
        if ii==11:
            email("进入小程序连续失败11次","plain",pen_names)
        biaoji_time()

        '''拍照'''
        pen_names =paizhao("进入小程序的商城首页")

        '''**************************************************************************************************************商城购买商品***********************************************************************'''
        '''输出当前页面的标题'''
        inputbt(shopname,"进入商城首页报错",1,"plain",pen_names)
        biaoji_time()

        '''打开全部分类'''
        shuxin="//android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
        Cxpath(shuxin,"底部导航全部分类", "进入全部分类", "Bug--无法进入全部分类")
        time.sleep(10)
        '''拍照'''
        pen_names =paizhao("打开全部分类")
        '''输出当前页面的标题'''
        inputbt("全部分类","进入全部分类报错",1,"plain",pen_names)
        biaoji_time()

        '''打开所有商品'''
        driver.tap([(65, 395), (175, 545)], 500)
        time.sleep(10)
        '''拍照'''
        pen_names =paizhao("打开所有商品")
        '''输出当前页面的标题'''
        inputbt("商品列表", "进入全部商品列表报错", 1, "plain",pen_names)
        biaoji_time()

        '''点击一个商品'''
        driver.tap([(40, 345), (277, 743)], 500)
        time.sleep(10)
        biaoji_time()

        '''拍照'''
        pen_names =paizhao("进入商品详情页面")

        '''输出当前页面的标题'''
        bt_shangpin=inputbt("","进入商品详情页报错",0,"plain",pen_names)
        biaoji_time()

        '''获取商品价格'''
        try:
            shangpingjiage = shangpinjiage(bt_shangpin)
            shangpingjiage = float(shangpingjiage)
            print("商品价格为：", shangpingjiage)
        except Exception as e:
            print("报错信息")
            print(e)
            print("报错结束")
        biaoji_time()

        '''获取会员折扣'''
        go.Cxpath("/html/body/div[2]/ul/li[3]/a/span", "会员列表", "进入会员列表页面", "Bug--无法进入会员列表页面")
        go.Sxpath("/html/body/div[6]/div[2]/form/div/div/input", "搜索框", userid, "成功输入会员编号", "Bug--无法输入会员编号")
        go.Cxpath("/html/body/div[6]/div[2]/form/div/div/span[5]/button[1]", "会员搜索按钮", "点击会员搜索按钮", "Bug--无法点击会员搜索按钮")
        biaoji_time()
        try:
            huiyuandengjis = Go.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div/table/tbody/tr/td[3]").text
        except Exception as e:
            ee=traceback.format_exc()
            pen_names=go.paizhao_pc("获取会员等级")
            email("抓取会员折扣失败，报错内容:<br>"%e,"html",pen_names)
            huiyuandengjis="普通会员"
        go.Cxpath("/html/body/div[3]/div/ul[2]/li/a", "会员等级按钮", "进入会员等级页面", "Bug--无法进入会员等级页面")
        if huiyuandengjis == "普通会员":
            huiyuanzekou_all = 1
        elif huiyuandengjis != "普通会员":
            go.Sxpath("/html/body/div[6]/div[2]/form[1]/div/div[2]/div/input", "搜索框", huiyuandengjis, "成功输入会员等级","Bug--无法输入会员等级")
            go.Cxpath("/html/body/div[6]/div[2]/form[1]/div/div[2]/div/span/button", "会员等级搜索按钮", "点击会员等级搜索按钮","Bug--无法点击会员等级搜索按钮")
            try:
                huiyuanzekou_all = Go.find_element_by_xpath("/html/body/div[6]/div[2]/form[2]/table/tbody/tr/td[4]").text
            except Exception as e:
                ee = traceback.format_exc()
                pen_names=go.paizhao_pc("会员折扣")
                email("抓取会员等级折扣失败，报错内容:<br>" % e, "html",pen_names)
            huiyuanzekou_all = float(huiyuanzekou_all)
            huiyuanzekou_all = huiyuanzekou_all * 0.1
        biaoji_time()

        '''计算折扣之后的商品价格'''
        try:
            shangpingjiage=shangpingjiage*huiyuanzekou_all
            print("该会员当前折扣为：",huiyuanzekou_all)
            print("折扣之后应付金额为：",shangpingjiage)
        except Exception as e:
            print("报错信息")
            print(e)
            print("报错结束")
        biaoji_time()

        '''计算消费后金额'''
        try:
            c = huiyuanyue - shangpingjiage
            print("会员剩余金额应为：",c)
        except Exception as e:
            print("报错信息")
            print(e)
            print("报错结束")
        biaoji_time()


        '''点击立刻购买商品'''
        print("点击立刻购买商品")
        driver.tap([(532,1096), (709,1114)],  500)
        time.sleep(10)
        biaoji_time()


        '''拍照'''
        pen_names =paizhao("点击购买")

        '''输出当前页面的标题'''
        inputbt(bt_shangpin,"购买商品报错",1,"plain",pen_names)
        biaoji_time()


        '''点击确认购买商品'''
        print("点击确认购买商品")
        driver.tap([(197,1105), (461,1172)],  500)
        time.sleep(10)
        biaoji_time()

        '''拍照'''
        pen_names =paizhao("点击确认购买")

        '''输出当前页面的标题'''
        inputbt("确认订单", "确认购买时报错", 1, "plain",pen_names)



        '''点击立即支付按钮'''
        print("点击立即支付按钮")
        driver.tap([(523,1141), (675,1177)],  500)
        time.sleep(10)

        biaoji_time()

        '''拍照'''
        pen_names =paizhao("点击支付按钮")

        '''输出当前页面的标题'''
        inputbt("收银台", "选择支付方式报错", 1, "plain",pen_names)

        '''点击余额支付按钮'''
        print("点击余额支付按钮")
        '''点击第一个支付选项'''
        #driver.tap([(106, 467), (627, 549)], 500)
        '''点击第二个支付选项'''
        driver.tap([(119, 366), (585, 439)], 500)
        time.sleep(10)
        biaoji_time()

        yue=1
        i=1
        while yue!=1 and i<=30:
            biaoji_time()
            '''点击余额支付按钮'''

            driver.tap([(119, 366), (585, 439)], 500)
            print("点击余额支付按钮")
            time.sleep(10)
            try:
                print(11111111111111)
                bt=driver.find_element_by_id("com.tencent.mm:id/cd6").text
                if bt=="确认要支付吗?":
                    yue=2
                    break
                    print(22222)
            except Exception as e:
                print("报错信息")
                print(33333333333)
                print(e)
                print("报错结束")
        biaoji_time()

        print()
        '''拍照'''
        pen_names =paizhao("点击余额支付按钮")

        '''输出当前页面的标题'''
        inputbt("收银台", "支付报错", 1, "plain",pen_names)
        biaoji_time()


        '''确认使用余额支付'''
        Cid("com.tencent.mm:id/an3","确认余额支付按钮","确认使用余额支付中","Bug--无法确认使用余额支付")
        time.sleep(10)
        biaoji_time()


        '''拍照'''
        pen_names =paizhao("确认使用余额支付")

        '''输出当前页面的标题'''
        bt_name2 = inputbt("支付成功", "商品支付未成功", 3, "plain", pen_names)

        oo=0
        if bt_name2=="支付成功":
            print("商品购买完成")
            oo=1
        biaoji_time()

    ##############################################################################
        '''获取该会员消费后剩余的金额'''
        try:
            d = huiyuanjine()
            d = float(d)
            print("会员实际剩余金额为：", d)
        except Exception as e:
            print("报错信息")
            print(e)
            print("报错结束")
        biaoji_time()

        try:
            if d==c and oo==1:
                jieguo1="商品购买测试通过"
                print(jieguo1)
            if d!=c and oo!=1:
                jieguo1="商品购买测试不通过，请及时追查失败原因"
                email(jieguo1,"plain",pen_names)
                print(jieguo1)
            if d==c and oo!=1:
                jieguo1="商品购买成功，但是，页面没有进行转跳"
                print(jieguo1)
        except Exception as e:
            print("报错信息")
            print(e)
            print("报错结束")
        biaoji_time()



        '''点击返回首页按钮'''
        print("点击返回首页按钮")
        driver.tap([(430, 609), (632, 662)], 500)
        time.sleep(10)
        biaoji_time()

        '''拍照'''
        pen_names =paizhao("点击返回首页按钮")

        inputbt(shopname, "购买商品后，返回首页报错", 3, "plain",pen_names)
        biaoji_time()

        '''返回，直到首页'''
        try:
            bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text

            while bt!="全部分类":
                Cid("com.tencent.mm:id/kq", "返回", "返回上一页", "Bug--无法点击返回")
                time.sleep(10)
                bt = driver.find_element_by_id("com.tencent.mm:id/kt").text
            Cid("com.tencent.mm:id/cp","底部菜单-首页","转跳首页中","Bug--无法点击底部菜单-首页")
        except:
            1==1
        biaoji_time()

        '''**************************************************************************************************************积分商城***********************************************************************'''
        '''拍照'''
        pen_names =paizhao("准备点击积分商城按钮")

        '''点击积分商城按钮'''
        print("点击积分商城按钮")
        driver.tap([(537, 740), (677, 781)], 500)
        time.sleep(10)
        '''获取标题'''
        bt_name=inputbt("积分商城首页", "打开积分商城首页报错", 1, "plain",pen_names)
        biaoji_time()

        while bt_name != "积分商城首页":
            biaoji_time()
            '''点击积分商城按钮'''
            print("点击积分商城按钮")
            driver.tap([(390, 876), (500, 990)], 500)
            time.sleep(10)
            '''获取标题'''
            try:
                bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
                if bt != "积分商城首页":
                    print("标题是：", bt)
            except Exception as e:
                print("报错信息")
                print(e)
                print("报错结束")
        biaoji_time()

        '''拍照'''
        pen_names =paizhao("点击积分商城按钮")

        '''点击第一个积分分类'''
        print("点击第一个积分分类")
        driver.tap([(51, 749), (126, 875)], 500)
        time.sleep(10)
        try:
            bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
            print("标题是：", bt)
        except Exception as e:
            print("报错信息")
            print(e)
            print("报错结束")
        '''拍照'''
        pen_names =paizhao("点击第一个积分分类")
        biaoji_time()

        '''点击第一个积分商品'''
        print("点击第一个积分商品")
        driver.tap([(31, 268), (303, 615)], 500)
        time.sleep(10)
        try:
            bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
            print("标题是：", bt)
        except Exception as e:
            print("报错信息")
            print(e)
            print("报错结束")
        '''拍照'''
        pen_names =paizhao("点击第一个积分商品")
        biaoji_time()

        '''点击立即兑换'''
        print("点击立即兑换")
        driver.tap([(247, 1098), (467, 1164)], 500)
        time.sleep(10)
        try:
            bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
            print("标题是：", bt)
        except Exception as e:
            print("报错信息")
            print(e)
            print("报错结束")
        '''拍照'''
        pen_names =paizhao("点击立即兑换")
        biaoji_time()

        '''点击立即支付'''
        print("点击立即支付")
        driver.tap([(522, 1101), (690, 1171)], 500)
        time.sleep(10)
        try:
            bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
            print("标题是：", bt)
        except Exception as e:
            print("点击立即支付报错：", e)
        '''拍照'''
        pen_names =paizhao("点击立即支付")
        biaoji_time()

        '''点击余额支付'''
        print("点击余额支付")
        driver.tap([(277, 1028), (490, 1074)], 500)
        time.sleep(10)
        try:
            bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
            print("标题是：", bt)
        except Exception as e:
            print("报错信息")
            print(e)
            print("报错结束")
        '''拍照'''
        pen_names =paizhao("点击余额支付")
        biaoji_time()

        '''点击确定支付按钮'''
        print("点击确定支付按钮")
        driver.tap([(429, 684), (568, 733)], 500)
        Time = time.strftime("%Y%m%d%H%M%S", time.localtime())
        Time = int(Time)
        time.sleep(10)
        try:
            bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
            print("标题是：", bt)
        except Exception as e:
            print("报错信息")
            print(e)
            print("报错结束")
        '''拍照'''
        pen_names =paizhao("点击确定支付按钮")
        biaoji_time()

        '''点击确定按钮'''
        print("点击确定按钮")
        driver.tap([(207, 551), (487, 608)], 500)
        time.sleep(10)
        try:
            bt = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
            print("标题是：", bt)
        except Exception as e:
            print("报错信息")
            print(e)
            print("报错结束")
        '''拍照'''
        pen_names =paizhao("点击确定按钮")
        biaoji_time()

        try:
            jifendingdantime = jifendingdan()
            print(Time)
            print(jifendingdantime)
            print("时间差异：", jifendingdantime - Time)
        except Exception as e:
            print("报错信息")
            print(e)
            print("报错结束")
        try:
            if jifendingdantime - Time < 50 and jifendingdantime - Time > -50:
                jieguo2="积分商品兑换测试通过"
                print(jieguo2)
            else:
                jieguo2 = "积分商品兑换测试不通过,请及时追查失败原因"
                print(jieguo2)
        except Exception as e:
            print("报错信息")
            print(e)
            print("报错结束")
        biaoji_time()

        try:
            print(jieguo1,jieguo2)
        except:
            print("结果无法输出")
        biaoji_time()

        Go.quit()

        time.sleep(60)

        biaoji_time()
except:
    Go.quit()


