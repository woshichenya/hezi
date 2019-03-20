#http://plus.vdongchina.com/
from beifen import baibaoxiang
import time
url="http://aplus.vdongchina.com/"
go= baibaoxiang.geturl(url)


bosstao={
    "username":"vdong",
    "pasword":"vdongchina2018"
}

ho = bosstao
go.Ctext("立即登录","立即登录按钮","进入登录页面","无法点击立即登录按钮")
time.sleep(5)
go.Jubing_go(2,2)
go.Sid("inputAccount","用户名",ho["username"],"输入用户名","无法输入用户名")
go.Sid("inputPassword", "密码", ho["pasword"], "输入密码", "无法输入密码")
go.CTag_name_zidingyi("input","value","登录","登录","登录成功","登录失败")
# go.Cxpath("/html/body/div[1]/div[1]/div[1]/div[6]/button","登录","登录成功","登录失败")
go.llq.maximize_window()