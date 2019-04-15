from baibaoxiang import baibaoxiang

class login_go():
    def on(self,user,username,password):
        if user =="":
            whu={
                "username":username,
                "password":password
            }
        else:
            if user =="wchen_vdong":
                whu={
                    "username":"vdongshopplus",
                    "password":"1234567890",
                }
            if user == "wchen_admin":
                whu={
                    "username":"maxstone",
                    "password":"vdongchina2019",
                }
            if user == "wchen_vdong2":
                whu={
                    "username":"18871551774",
                    "password":"123456789",
                }
            if user == "wchen_vdong3":
                whu={
                    "username":"18710262651",
                    "password":"123456789",
                }
            if user == "wchen_plus":
                #管家plus方新门店
                whu={
                    "username":"18871551666",
                    "password":"1234567a",
                }
            if user == "plus_boss":
                whu={
                    "username":"18871551001",
                    "password":"1234567a",
                }
            if user == "plus_shop":
                whu={
                    "username":"18871551665",
                    "password":"1234567a",
                }
            if user == "plus_admin":
                whu={
                    "username":"17400000000",
                    "password":"12345678",
                }
        url = "http://test-sso.vdongchina.com"
        go = baibaoxiang.geturl(url)

        go.Sid("inphoneinput","用户名",whu["username"],"输入用户名","无法输入用户名")
        go.Sid("pasword","密码",whu["password"],"输入密码","无法输入密码")
        go.CTag_name_zidingyi("button","text","登录","登录","登录成功","登录失败")
        go.llq.maximize_window()
        return go