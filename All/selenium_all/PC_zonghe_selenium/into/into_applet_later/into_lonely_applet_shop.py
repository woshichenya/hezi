import PC_zonghe_selenium.into.into_applet
import time
from selenium.webdriver.common.keys import *
from selenium.webdriver.common.action_chains import ActionChains


f=PC_zonghe_selenium.into.into_applet
go=f.go
Go=f.Go
GO=f.GO
object_on=f.object_on
type_on=f.type_on


if object_on == "wchen":
    if type_on == "china":
        pulic_name = "测试专用-产品研发账号10"
        yingyong_name = "商城综合版"
    if type_on == "test":
        pulic_name = "魔力游商城"
        yingyong_name = "微动天下商城"
    if type_on == "split_test":
        go.CTag_name_zidingyi("p", "text", "创建小程序", "创建小程序按钮", "点击创建小程序", "Bug--无法点击创建小程序")

go.lonely_applet_input(pulic_name)
go.Jubing_go(2, 2)
go.yingyong_shop(yingyong_name)