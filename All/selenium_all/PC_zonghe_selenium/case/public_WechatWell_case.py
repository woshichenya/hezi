import PC_zonghe_selenium.into.into_public
import traceback
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

'''调用进入小程序管理页面的脚本'''
f=PC_zonghe_selenium.into.into_public
go=f.go
Go=f.Go
GO=f.GO
object_on=f.object_on
type_on=f.type_on

def huodong_home():
    go.Ctext("活动管理", "活动管理超链接", "进入活动管理页面", "Bug--无法进入活动管理页面")
    go.Cxpath("/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div/div[2]/ul/li[2]/a/i", "管理活动",
              "进入管理活动页面", "Bug--无法进入活动管理页面")
def user_new():
    go.Ctext("用户", "用户", "进入用户页面", "Bug--无法进入用户页面")
    i=101
    while i<1000:
        x="0"+str(i)

        go.Ctext("添加用户","添加用户","进入添加用户页面","Bug--无法进入添加用户页面")
        go.Sname("nick_name","昵称输入框",x,"输入昵称","Bug--无法输入昵称")
        go.Cname("submit","昵称输入框","输入昵称","Bug--无法输入昵称")
        i+=1
        time.sleep(2)

def jiabin_new():
    go.Ctext("嘉宾", "嘉宾", "进入嘉宾页面", "Bug--无法进入嘉宾页面")
    i = 12
    while i < 100:
        x = "0" + str(i)
        go.Ctext("添加嘉宾", "添加嘉宾", "进入添加嘉宾页面", "Bug--无法进入添加嘉宾页面")
        go.Sid("name","嘉宾名称",x,"输入名称","Bug--无法输入名称")
        go.Sid("displayid", "排序", x, "输入排序", "Bug--无法输入排序")
        go.Cname("submit", "昵称输入框", "输入昵称", "Bug--无法输入昵称")
        i += 1
        time.sleep(2)

def photo_new():
    go.Ctext("相册", "相册", "进入相册页面", "Bug--无法进入相册页面")
    i=21
    while i <= 80:
        i_sum=int(i%20)
        if i_sum==0:
            i_sum=20
        go.Ctext("添加相册", "添加相册", "进入添加相册页面", "Bug--无法进入添加相册页面")
        go.Sid("displayid", "排序", i, "输入排序", "Bug--无法输入排序")
        go.C_class_text("选择图片", "button", "btn btn-default", "选择图片", "打开选择图片插件", "Bug--无法打开选择图片插件")
        x="/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div["+str(i_sum)+"]"
        sum="第"+str(i)+"张图片"
        time.sleep(2)
        if i>20:
            i_sum_s=0
            while i_sum_s<int(i/20):
                go.Ctext("下一页»","下一页","翻页","Bug--无法翻页")
                time.sleep(2)
                i_sum_s+=1
        go.Cxpath(x,sum,"点击%s"%sum,"Bug--无法点击%s"%sum)
        time.sleep(2)
        go.CTag_name_zidingyi("button","text","确定","确定按钮","点击确定","Bug--无法点击确定")
        time.sleep(2)
        go.Cname("submit", "昵称输入框", "输入昵称", "Bug--无法输入昵称")
        i += 1
        time.sleep(2)




huodong_home()
photo_new()
# user_new()
# jiabin_new()