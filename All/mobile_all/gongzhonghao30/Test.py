from beifen import baibaoxiang

go= baibaoxiang.geturl("http://test-mp.vdongtx.com/web/index.php?c=user&a=login&")
Go= baibaoxiang.geturl

def denglu():
    go.Sxpath("//input[@name='username']","用户名输入框","admin","输入用户名","Bug--无法输入用户名")
    go.Sxpath("//input[@name='password']", "密码输入框", "11111111", "输入密码", "Bug--无法输入密码")
    go.Cxpath("//input[@id='submit']", "登录按钮", "登录中", "Bug--无法进行登录")

denglu()
'''
"","","","",""
password
'''