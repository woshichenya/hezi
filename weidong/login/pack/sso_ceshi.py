from baibaoxiang import baibaoxiang
class login_go():
    def on(self,user,username,password):
        if user =="":
            whu={
                "username":username,
                "password":password
            }
        else:
            if user == "wchen_shoptest":
                whu={
                    "username":"shoptester",
                    "password":"shoptester",
                }
            if user == "wchen_admin":
                whu={
                    "username":"maxstone",
                    "password":"vdongchina2019",
                }

        url="http://ceshi-sso.vdongchina.com"
        go= baibaoxiang.geturl(url)
        go.Sid("inphoneinput","用户名",whu["username"],"输入用户名","无法输入用户名")
        go.Sid("pasword","密码",whu["password"],"输入密码","无法输入密码")
        go.CTag_name_zidingyi("button","text","登录","登录","登录成功","登录失败")
        go.llq.maximize_window()
        return go