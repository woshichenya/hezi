from beifen import baibaoxiang

url="http://sso.vdongchina.com"
go= baibaoxiang.geturl(url)
shoujihao="18000000043"
go.Sid("inphoneinput","用户名",shoujihao,"输入用户名","无法输入用户名")
go.Sid("pasword","密码","123456789","输入密码","无法输入密码")
go.Cxpath("/html/body/div[1]/div[1]/div[1]/div[6]/button","登录","登录成功","登录失败")
go.llq.maximize_window()