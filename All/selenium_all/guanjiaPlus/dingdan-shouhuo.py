from selenium.webdriver.support.select import Select
import time
import traceback
import guanjiaPlus.xiaochengxuguanliyemian

'''调用进入小程序管理页面的脚本'''
go=guanjiaPlus.xiaochengxuguanliyemian.go
Go=guanjiaPlus.xiaochengxuguanliyemian.Go
GO=guanjiaPlus.xiaochengxuguanliyemian.GO

cishu=1
while cishu<=200:
    '''进入订单待收货页面'''
    go.Cxpath(u"(.//*[normalize-space(text()) and normalize-space(.)='订单管理'])[2]/following::a[2]","待收货按钮","转跳待收货页面","按钮不存在")


    '''选择关键字类型为会员信息'''
    cishu_a = 1
    while cishu < 200 and cishu_a == 1:
        try:
            Go.find_element_by_name("searchfield").click()
            Select(Go.find_element_by_name("searchfield")).select_by_visible_text(u"会员信息")
            cishu_a = 2
        except Exception as e:
            ee = traceback.format_exc()
            print("报错开始")
            print(ee)
            print("报错结束")
            time.sleep(1)


    '''搜索陈雅小号的订单'''
    time.sleep(5)
    Go.find_elements_by_id("keyword").clear()
    go.Sxpath("// *[ @ id = 'keyword']", "搜索条件", u"陈", "成功输入姓名", "Bug无法正常输入")
    #Go.find_element_by_id("keyword").send_keys(u"陈雅小号")

    '''点击搜索按钮'''
    # /html/body/div[6]/div[2]/form/div/div/span[5]/button[1]
    go.Cxpath("/html/body/div[6]/div[2]/form/div/div/span[5]/button[1]", "搜索按钮", "点击搜索", "Bug无法点击搜索")

    '''进行收货操作'''

    go.Ctext(u"确认收货","确认收货按钮","点击确认收货按钮","Bug无法点击确认收货按钮")
    go.Cxpath("/html/body/div[9]/div[2]/div/div/div/div/div[4]/button[1]","提示框的确认按钮","已确认提示框内容","Bug无法点击提示框的确认按钮")
    cishu+=1