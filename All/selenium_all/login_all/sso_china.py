from beifen import baibaoxiang

url="http://sso.vdongchina.com"
go= baibaoxiang.geturl(url)
plus={
    "username":"18811020000",
    "paswored":"12345678",
}
plus_shop={
    "username":"18811021000",
    "paswored":"12345678",
}
wchen={
    "username":"vdongshops",
    "pasword":"1234567890",
}
go.Sid("inphoneinput","用户名",plus["username"],"输入用户名","无法输入用户名")
go.Sid("pasword","密码",plus["paswored"],"输入密码","无法输入密码")
go.Cxpath("/html/body/div[1]/div[1]/div[1]/div[6]/button","登录","登录成功","登录失败")
go.llq.maximize_window()