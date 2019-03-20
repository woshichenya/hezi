from baibaoxiang import baibaoxiang
from baibaoxiang import femail
import requests
from selenium import webdriver

email=femail.email
webdriver.Chrome()
url="http://sso.vdongchina.com"
go = baibaoxiang.geturl(url)
import time

wchen_vdong={
    "username":"vdongshops",
    "pasword":"1234567890",
}

ho=wchen_vdong
go.Sid("inphoneinput","用户名",ho["username"],"输入用户名","无法输入用户名")
go.Sid("pasword","密码",ho["pasword"],"输入密码","无法输入密码")
go.CTag_name_zidingyi("button","text","登录","登录","登录成功","登录失败")
go.llq.maximize_window()

while 1==1:
    try:
        i=1
        a=1
        for i in range (1,10):
            try:
                span_t=go.llq.find_elements_by_tag_name("span")
                for x in span_t:
                    if  "选择小程序" in x.text :
                        a=2
                        break
            except Exception as e:
                print(e)

            if a==2:
                print("进入小程序页面")
                break
            elif a==1:
                print("没有进入小程序页面")
            time.sleep(1)

        autogo =1
        for autogo in range (1,5):
            try:
                go.llq.find_element_by_id("autogo")
                time.sleep(3)
                go.Cid("autogo", "关闭按钮", "关闭提示框", "没有关闭框")
                break
            except:
                time.sleep(1)



        go.lonely_applet_input("独立商城")

        go.Jubing_go(2,2)

        url_yes="https://xiao.vdongchina.com/addons/zjhj_mall/core/web/index.php?"
        url_1=1
        for url_1 in range (1,5):
            url_new=go.llq.current_url
            if url_yes in url_new:
                print("已进入独立商城首页")
                break

        go.CTag_name_zidingyi("div","class","btn-group float-left","独立商城下拉框","展开独立商城下拉框","无法展开独立商城下拉框")
        go.Ctext("返回系统","返回系统按钮","点击返回系统","无法点击返回系统")
        go.Jubing_go(2,1)
        go.llq.close()
        go.Jubing_go(1,1)
    # print(go.llq.window_handles)
    # print(go.llq.current_window_handle)
    except:
        try:
            re=requests.get("https://xiao.vdongchina.com/addons/zjhj_mall/core/web/index.php?r=mch/store/index&sign=1")

            if 502 in re.status_code:
                res=["mengwenhao@vdongchina.com","baidebin@vdongchina.com"]
                email("502啦快看看","html","",res)
        except:
            print("有个其他错误")

