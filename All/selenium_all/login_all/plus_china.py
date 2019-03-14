#http://plus.vdongchina.com/
import baibaoxiang
import time
url="http://aplus.vdongchina.com/"
go=baibaoxiang.geturl(url)
username="18811021000"
pasword="12345678"
go.Ctext("立即登录","立即登录按钮","进入登录页面","无法点击立即登录按钮")
time.sleep(5)
go.Jubing_go(2,2)
go.Sid("inphoneinput","用户名",username,"输入用户名","无法输入用户名")
go.Sid("pasword", "密码", pasword, "输入密码", "无法输入密码")
go.Cxpath("/html/body/div[1]/div[1]/div[1]/div[6]/button","登录","登录成功","登录失败")
go.llq.maximize_window()