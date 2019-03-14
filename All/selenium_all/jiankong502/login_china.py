import baibaoxiang

url="http://sso.vdongchina.com"
go=baibaoxiang.geturl(url)
wchen_vdong={
    "username":"vdongshops",
    "pasword":"1234567890",
}

ho=wchen_vdong
go.Sid("inphoneinput","用户名",ho["username"],"输入用户名","无法输入用户名")
go.Sid("pasword","密码",ho["pasword"],"输入密码","无法输入密码")
go.CTag_name_zidingyi("button","text","登录","登录","登录成功","登录失败")
go.llq.maximize_window()
