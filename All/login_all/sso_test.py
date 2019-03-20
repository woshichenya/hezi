from beifen import baibaoxiang

url="http://test-sso.vdongchina.com"
go= baibaoxiang.geturl(url)
wchen_vdong={
    "username":"vdongshopplus",
    "password":"1234567890",
}
wchen_admin={
    "username":"maxstone",
    "password":"vdongchina2019",
}
wchen_vdong2={
    "username":"18871551774",
    "password":"123456789",
}
wchen_vdong3={
    "username":"18710262651",
    "password":"123456789",
}
#管家plus方新门店
wchen_vdong4={
    "username":"18871551666",
    "password":"1234567a",
}
plus_test={
    "username":"18871551001",
    "password":"1234567a",
}
plus_test2={
    "username":"18871551665",
    "password":"1234567a",
}
plus_admin={
    "username":"17400000000",
    "password":"12345678",
}
plus_test={
    "username":"18000000354",
    "password":"1234567a",
}
ho=plus_test2
go.Sid("inphoneinput","用户名",ho["username"],"输入用户名","无法输入用户名")
go.Sid("pasword","密码",ho["password"],"输入密码","无法输入密码")
# go.Cxpath("/html/body/div[1]/div[1]/div[1]/div[6]/button","登录","登录成功","登录失败")
go.CTag_name_zidingyi("button","text","登录","登录","登录成功","登录失败")
go.llq.maximize_window()