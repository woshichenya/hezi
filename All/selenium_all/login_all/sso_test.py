from beifen import baibaoxiang

url="http://test-sso.vdongchina.com"
go= baibaoxiang.geturl(url)
wchen_vdong={
    "username":"vdongshopplus",
    "password":"1234567890",
}
wchen_max_admin={
    "username":"maxstone",
    "password":"vdongchina2019",
}
plus_test={
    "shoujihao":"18871551001",
    "password":"1234567a",
}
go.Sid("inphoneinput","用户名",wchen_vdong["username"],"输入用户名","无法输入用户名")
go.Sid("pasword","密码",wchen_vdong["password"],"输入密码","无法输入密码")
go.Cxpath("/html/body/div[1]/div[1]/div[1]/div[6]/button","登录","登录成功","登录失败")
go.llq.maximize_window()