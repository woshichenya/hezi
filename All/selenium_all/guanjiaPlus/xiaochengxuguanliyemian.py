from selenium.webdriver.support.select import Select

import traceback
import time
from selenium.webdriver.common.keys import Keys
diaoyong="test"
diaoyong="china"
if diaoyong=="test":
    import guanjiaPlus.Test
    '''调用测试系统的登录脚本'''
    go=guanjiaPlus.Test.go
    Go=guanjiaPlus.Test.Go
    GO=guanjiaPlus.Test.GO
if diaoyong=="china":
    import guanjiaPlus.China
    '''调用正式系统的登录脚本'''
    go=guanjiaPlus.China.go
    Go=guanjiaPlus.China.Go
    GO=guanjiaPlus.China.GO

'''进入小程序管理页面'''
#Go.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='架构图'])[1]/following::h4[1]").click()
#Go.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='小程序'])[1]/following::li[1]").click()
go.Cxpath("(.//*[normalize-space(text()) and normalize-space(.)='架构图'])[1]/following::h4[1]","小程序下拉框","展开小程序下拉框","Bug无法展开小程序下拉框")
go.Cxpath("(.//*[normalize-space(text()) and normalize-space(.)='小程序'])[1]/following::li[1]","小程序下拉框","展开小程序下拉框","Bug无法展开小程序下拉框")
go.Ctext(u"小程序管理","第一个叫小程序管理的超链接","进入第一个小程序","Bug无法进入第一个小程序")


# ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
x=1
i=1
while x==1:
    time.sleep(1)
    print("获取句柄第",i,"次")
    i+=1
    s=GO.Jubing(0)
    if s >=2:
        x=2
        Title=Go.title
        print(Title)
        print(Go.current_url)
        handles=Go.window_handles
        Go.switch_to_window(handles[1])
        print(Go.current_url)