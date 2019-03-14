import selenium_all.wechenjisu_40.login.login_china
import time

go = selenium_all.wechenjisu_40.login.login_china.go
#确认是否进入首页
ss= 0
while ss < 100 :
    try:
        go.llq.find_element_by_partial_link_text("退出")
        break
    except:
        print("暂未进入页面，等待两秒")
        time.sleep(2)

#切换至公众号页面
go.CTag_name_zidingyi("p","text","切换公众号","切换公众号按钮","切换至公众号列表页面","Bug--无法切换至公众号列表页面")
#进入公众号
go.lonely_applet_input("测试专用-产品研发账号10")
#进入智云物业
go.yingyong_shop("智云物业")

go.CTag_name_zidingyi("dt","text","运营策略","运营策略下拉框","展开运营策略","无法展开运营策略")
go.CTag_name_zidingyi("a","data-title","快递驿站","快递驿站菜单","进入快递驿站","无法进入快递驿站")
#快件管理
go.CTag_name_zidingyi("button","text","快件管理","快件管理菜单","进入快件管理","无法进入快件管理")

go.Ctext("新增寄件","新增取件菜单","新增取件菜单ok","新增取件菜单no ok ")

