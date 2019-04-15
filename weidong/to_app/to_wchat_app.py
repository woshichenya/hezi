import login.login
import time
from selenium.webdriver.common.keys import *
system="china"
login_go=login.login.Login()
go=login_go.on(system,"wchen_vdong","","")




k_1=1
while k_1==1:

    for autogo in range (1,5):
        try:
            go.llq.find_element_by_id("autogo")
            time.sleep(3)
            go.llq.find_element_by_id("autogo").click()
            # break
        except:
            time.sleep(1)

    i=1
    a=1
    for i in range (1,10):
        try:
            span_t=go.llq.find_elements_by_tag_name("span")
            for x in span_t:
                if  "选择公众号" in x.text :
                    a=2
                    break
        except Exception as e:
            print(e)

        if a==2:
            print("进入公众号列表页面")
            break
        elif a==1:
            print("没有进入公众号列表页面")
        time.sleep(1)
        if i % 3 == 0 and a == 1:
            go.CTag_name_zidingyi("p", "text", "切换公众号", "切换切换公众号超链接", "进入公众号列表", "Bug--无法切换至公众号列表")





#进入公众号
    # go.lonely_applet_input("测试专用-产品研发账号10")

    if system == "china":
        pulic_name = "测试专用-产品研发账号10"
        yingyong_name = "商城综合版"
    if system == "test":
        print("测试系统")
        pulic_name = "魔力游商城moli"
        yingyong_name = "微信墙"
    go.lonely_applet_input(pulic_name)
    # go.Jubing_go(2, 2)
    go.huadongpingmu_xiayige("/html/body")
    go.yingyong_shop(yingyong_name)


    k_1 += 1