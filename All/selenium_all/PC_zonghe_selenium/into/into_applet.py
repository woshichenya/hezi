import time
import PC_zonghe_selenium.go.on_all
from selenium.webdriver.common.keys import *
from selenium.webdriver.common.action_chains import ActionChains


f=PC_zonghe_selenium.go.on_all
go=f.from_def.go
Go=f.from_def.Go
GO=f.from_def.GO
object_on=f.object_on
type_on=f.type_on

def into_shop():
    sum_c=1
    sum_c_a=0
    while sum_c<30 and sum_c_a==0:
        try:
            go.llq.find_elements_by_link_text("创建小程序")
            print("当前是小程序页面")
            sum_c_a=1
        except:
            go.error()
            sum_c+=1
        if sum_c_a==1:
            go.CTag_name_zidingyi("p", "text", "切换小程序", "切换小程序超链接", "进入小程序列表", "Bug--无法切换至小程序列表")



into_shop()



