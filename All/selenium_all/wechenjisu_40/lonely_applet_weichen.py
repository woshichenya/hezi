import traceback
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
l='china'
l='test'
l='Test_ShopSplit'
if l=='test':
    print("进入：test")
    import selenium_all.wechenjisu_40.Test
    go = selenium_all.wechenjisu_40.Test.go
    Go = selenium_all.wechenjisu_40.Test.Go
    GO = selenium_all.wechenjisu_40.Test.GO
if l=='china':
    print("进入：china")
    import selenium_all.wechenjisu_40.china
    go= selenium_all.wechenjisu_40.china.go
    Go= selenium_all.wechenjisu_40.china.Go
    GO= selenium_all.wechenjisu_40.china.GO
if l=='Test_ShopSplit':
    print("进入：Test_ShopSplit")
    import selenium_all.wechenjisu_40.Test_ShopSplit
    print(11111)
    go = selenium_all.wechenjisu_40.Test_ShopSplit.go
    Go = selenium_all.wechenjisu_40.Test_ShopSplit.Go
    GO = selenium_all.wechenjisu_40.Test_ShopSplit.GO



def lonely_applet_new():
    go.CTag_name_zidingyi("p","text","创建小程序","创建小程序按钮","点击创建小程序","Bug--无法点击创建小程序")

    jb_sum=go.Jubing()
    if jb_sum>1:
        go.Qhjubing(2)
    go.Sname("name","小程序名称输入框","自动化虚拟独立小程序","输入名称","Bug--无法输入名称")
    go.STag_name_zidingyi("input","placeholder","版本描述","自动化测试数据","版本描述","输入版本描述","Bug--无法输入版本描述")
    go.Sname("original","原始ID","123","输入原始ID","Bug--无法输入原始ID")
    go.Sname("key","Appid","234","输入Appid","Bug--无法输入Appid")
    go.Sname("secret","AppSecret","455","输入AppSecret","Bug--无法输入AppSecret")
    go.Sname("version","版本号","1.0","输入版本号","Bug--无法输入版本号")

    go.CTag_name_zidingyi("li","ng-click","selectMore()","添加应用按钮","点击添加应用","Bug--无法点击添加应用")
    time.sleep(4)
    # go.Cxpath("/html/body/div[2]/div[2]/div/div/div/div/div/form/div/div[3]/div/div[1]/div/div[7]/div/div/div/div/div/div/div[2]/div/ul/li[6]/a")
    article = go.llq.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div/form/div/div[3]/div/div[1]/div/div[7]/div/div/div/div/div/div/div[2]/div/ul/li[1]/div")
    ActionChains(go.llq).move_to_element(article).perform()
    try:
        go.llq.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div/form/div/div[3]/div/div[1]/div/div[7]/div/div/div/div/div/div/div[2]/div/ul/li[1]/div").click()
        print(111111111111)
    except:
        go.error()
        try:
            go.llq.find_element_by_xpath(
                "/html/body/div[2]/div[2]/div/div/div/div/div/form/div/div[3]/div/div[1]/div/div[7]/div/div/div/div/div/div/div[2]/div/ul/li[1]/a/i").send_keys(Keys.ENTER)
            print(22222222222)
        except:
            go.error()
            go.llq.find_element_by_xpath(
                "/html/body/div[2]/div[2]/div/div/div/div/div/form/div/div[3]/div/div[1]/div/div[7]/div/div/div/div/div/div/div[2]/div/ul/li[1]/a/i").click()
            print(33333333333333333333)
    #go.CTag_name_zidingyi("p","text","同城小程序","同城小程序应用","选择同城小程序应用","Bug--无法选择同城小程序应用")

    go.Ctext("下一步","下一步按钮","下一步","Bug--无法点击下一步")
    go.Cid("btnIds","生成版本按钮","点击生成版本按钮","Bug--无法点击生成版本按钮")
    try:
        alert = go.llq.switch_to_alert()
        alert.accept()
    except:
        ee=traceback.format_exc()
        print(ee)









#lonely_applet_new()
# lonely_applet_input("独立商城小程序")
# lonely_applet_shop()
def public_App_home():
    go.CTag_name_zidingyi("p", "text", "切换公众号", 1, 2, 3)
def public_App_into(input):
    go.lonely_applet_input(input)
    go.Jubing_go(2,2)
    go.yingyong_shop("微动天下商城")
def public_app_menu_into(menu_name):
    name=menu_name+"菜单"
    go.CText_partial_s(menu_name,name,"进入%s"%name,"Bug--无法进入%s"%name)

#*********************************************************************公众号模块群
def fenxiaoshang():
    go.CTextS("应用", "应用超链接", "进入应用超链接", "Bug--无法进入应用超链接")
    go.CText_partial_s("分销系统", "分销系统超链接", "进入分销系统超链接", "Bug--无法进入分销系统超链接")

def quyudaili():
    go.CTextS("应用", "应用超链接", "进入应用超链接", "Bug--无法进入应用超链接")
    go.CText_partial_s("区域代理", "区域代理超链接", "进入区域代理超链接", "Bug--无法进入区域代理超链接")

def kanjiahuodong():
    go.CTextS("应用", "应用超链接", "进入应用超链接", "Bug--无法进入应用超链接")
    a_ok=1
    while a_ok<30:
        try:
            go.llq.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[2]/a[1]/div").send_keys(Keys.END)
            print('将滚动条拉到底端')
        except:
            print("重复第%d次"%a_ok)
            a_ok+=1
    go.CText_partial_s("砍价活动", "砍价活动超链接", "进入砍价活动超链接", "Bug--无法进入砍价活动超链接")


#*********************************************************************独立小程序模块群**************************
def lonely_applet_shop():
    d = go.llq.current_url
    print("当前页面的html是：", d)
    c=go.Jubing()
    if c>1:
        go.Qhjubing(2)
    d=go.llq.current_url
    print("当前页面的html是：",d)
    go.CText_partial_s("小程序商城","小程序商城超链接","进入小程序商城","Bug--无法进入小程序商城")
    go.CText("系统管理","系统管理菜单","进入系统管理","Bug--无法进入系统管理")
    go.Ctext("微信配置","微信配置页面","进入微信配置页面","Bug--无法进入微信配置页面")
    go.title_panduan("微信配置")
    go.CText("保存","保存按钮","保存小程序信息","Bug--无法保存小程序信息")
    go.C_class_text("确认按钮","button","btn btn-primary alert-confirm-btn","确认","确认保存","Bug--没有确认按钮")


#*********************************************************************执行群
def godoing():
    on_time=time.time()
    go.lonely_applet_input("商城独立小程序")
    lonely_applet_shop()
    public_App_into("产品研发中心5")
    kanjiahuodong()
    end_time=time.time()
    print("一共用了",end_time-on_time,"秒")












godoing()