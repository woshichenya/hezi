import time
import PC_zonghe_selenium.go.on_all


f=PC_zonghe_selenium.go.on_all
go=f.from_def.go
Go=f.from_def.Go
GO=f.from_def.GO
object_on=f.object_on
type_on=f.type_on

def into_shop():
    if object_on=="plus":
        '''进入小程序管理页面'''
        go.Cxpath("(.//*[normalize-space(text()) and normalize-space(.)='架构图'])[1]/following::h4[1]", "小程序下拉框", "展开小程序下拉框",
                  "Bug无法展开小程序下拉框")
        go.Cxpath("(.//*[normalize-space(text()) and normalize-space(.)='小程序'])[1]/following::li[1]", "小程序下拉框", "展开小程序下拉框",
                  "Bug无法展开小程序下拉框")
        go.Ctext(u"小程序管理", "第一个叫小程序管理的超链接", "进入第一个小程序", "Bug无法进入第一个小程序")

        x = 1
        i = 1
        while x == 1:
            time.sleep(1)
            print("获取句柄第", i, "次")
            i += 1
            s = GO.Jubing(0)
            if s >= 2:
                x = 2
                Title = Go.title
                print(Title)
                print(Go.current_url)
                handles = Go.window_handles
                Go.switch_to_window(handles[1])
                print(Go.current_url)

    if object_on == "wchen":
        go.CTag_name_zidingyi("p", "text", "切换公众号", "切换公众号超链接", "进入公众号列表", "当前已处于公众号列表")
        if type_on=="china":
            print("正式系统")
            pulic_name="测试专用-产品研发账号10"
            yingyong_name="商城综合版"
        if type_on=="test":
            print("测试系统")
            pulic_name = "魔力游商城moli"
            yingyong_name = "微信墙"
        go.lonely_applet_input(pulic_name)
        go.Jubing_go(2,2)
        go.yingyong_shop(yingyong_name)



into_shop()



