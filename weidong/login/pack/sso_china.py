from baibaoxiang import baibaoxiang
class login_go():
    def on(self,user,username,password):
        if user =="":
            whu={
                "username":username,
                "password":password
            }
        else:
            if user == "wchen_vdong":
                whu={
                    "username":"vdongshops",
                    "password":"1234567890",
                }
            if user == "wchen_plus":
                whu={
                    "username":"18000000356",
                    "password":"1234567a",
                }
            if user == "plus":
                whu={
                    "username":"18811020000",
                    "password":"12345678",
                }
            if user == "plus_boss":
                whu={
                    "username":"18100000000",
                    "password":"1234567a",
                }
            if user == "plus_shop":
                whu={
                    "username":"18000000355",
                    "password":"1234567a",
                }
            if user == "plus_admin":
                whu={
                    "username":"17400000000",
                    "password":"a12345678",
                }
            if user == "plus_test":
                whu={
                    "username":"18000000361",
                    "password":"1234567a",
                }
        url = "http://sso.vdongchina.com"
        go = baibaoxiang.geturl(url)
        go.Sid("inphoneinput","用户名",whu["username"],"输入用户名","无法输入用户名")
        go.Sid("pasword","密码",whu["password"],"输入密码","无法输入密码")
        go.CTag_name_zidingyi("button","text","登录","登录","登录成功","登录失败")
        go.llq.maximize_window()
        return go
